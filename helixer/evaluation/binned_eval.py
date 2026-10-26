#! /usr/bin/env python3
"""Evaluates predictions per bin of base position within the subsequence and per bin of gene length.

Writes position_bins.csv and gene_length_bins.csv to the output directory. Each row holds one bin: the
half-open range [bin_start, bin_end) in bp, the number of evaluated bases, the total accuracy, the
precision, recall and F1 of every class and composite score of ConfusionMatrixGenic and the confusion
matrix counts ({reference class}_ref_{predicted class}_pred). The classes are ig (intergenic), utr, cds and
intron; ConfusionMatrixGenic names the CDS class exon. Bases with a sample weight of 0 are skipped.

Position bins divide the subsequence into equally sized parts. Gene length bins group the bases by
data/gene_lengths, the length of the longest pre-mRNA overlapping a base (0 for intergenic bases).
--gene-length-edges sets the lower ends of the bins. Bin 0, [0, 1), always holds the intergenic bases and
the last bin is open-ended (empty bin_end).

Caveat of the gene length bins: genic predictions on intergenic reference bases (additional or too long
genes) have a gene length of 0 and are counted in bin 0 only. The other bins contain only genic reference
bases, so their recall is complete, but their precision and F1 lack these false positives and are too
high. In bin 0, the ig_ref_utr_pred, ig_ref_cds_pred and ig_ref_intron_pred counts are the intergenic
bases predicted as genic. docs/binned_evaluation.ipynb plots the CSV files.
"""

import argparse
import csv
import itertools
import logging
import os

import h5py
import numpy as np

from helixer.prediction.Metrics import ConfusionMatrixGenic

logger = logging.getLogger('HelixerLogger')

N_CLASSES = 4
METRICS = ('precision', 'recall', 'f1')
BASES_PER_BATCH = 2 * 10 ** 6
DEFAULT_GENE_LENGTH_EDGES = [500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
# ConfusionMatrixGenic name -> CSV column name
OUTPUT_NAMES = {'exon': 'cds'}


def binned_confusion_matrices(true_cls: np.ndarray, pred_cls: np.ndarray, bin_idx: np.ndarray,
                              n_bins: int) -> np.ndarray:
    """Counts one confusion matrix per bin in a single pass.

    Args:
        true_cls: Reference class index of every evaluated base, 1D.
        pred_cls: Predicted class index of every evaluated base, 1D.
        bin_idx: Bin index of every evaluated base, 1D.
        n_bins: Number of bins.

    Returns:
        Counts of shape (n_bins, 4, 4) with the reference class in dim 1 and the predicted class in dim 2.
    """
    flat_idx = (bin_idx * N_CLASSES + true_cls) * N_CLASSES + pred_cls
    counts = np.bincount(flat_idx, minlength=n_bins * N_CLASSES ** 2)
    return counts.reshape((n_bins, N_CLASSES, N_CLASSES))


def score_rows(cms: np.ndarray, bin_bounds: list[tuple[int, int | None]]) -> list[dict[str, float | int | None]]:
    """Scores each confusion matrix with ConfusionMatrixGenic.

    Args:
        cms: Counts of shape (n_bins, 4, 4) as returned by binned_confusion_matrices.
        bin_bounds: (start, end) of each bin; end is None for an open-ended bin.

    Returns:
        One row per bin with bin_start, bin_end, n_bases, accuracy, {score}_{metric} and
        {reference class}_ref_{predicted class}_pred columns. Accuracy and scores are NaN for bins without bases.
    """
    rows = []
    for counts, (start, end) in zip(cms, bin_bounds):
        cm = ConfusionMatrixGenic()
        cm.cm = counts.astype(np.uint64)
        n_bases = int(counts.sum())
        row = {'bin_start': start, 'bin_end': end, 'n_bases': n_bases,
               'accuracy': cm._total_accuracy() if n_bases else np.nan}
        for name, scores in cm._get_scores().items():
            for metric in METRICS:
                row[f'{OUTPUT_NAMES.get(name, name)}_{metric}'] = scores[metric] if n_bases else np.nan
        class_names = [OUTPUT_NAMES.get(name, name) for name in cm.col_names.values()]
        for (i, ref), (j, pred) in itertools.product(enumerate(class_names), repeat=2):
            row[f'{ref}_ref_{pred}_pred'] = int(counts[i, j])
        rows.append(row)
    return rows


def evaluate(h5_data_path: str, h5_pred_path: str, n_position_bins: int,
             gene_length_edges: list[int]) -> tuple[list[dict], list[dict]]:
    """Evaluates predictions per position bin and per gene length bin.

    Args:
        h5_data_path: h5 data file with data/y, data/sample_weights and data/gene_lengths.
        h5_pred_path: h5 predictions file with predictions matching the data file.
        n_position_bins: Number of equally sized bins the subsequence length is divided into.
        gene_length_edges: Ascending lower edges of the gene length bins after the first one, all > 1.

    Returns:
        Rows of the position bins and rows of the gene length bins, see score_rows.

    Raises:
        ValueError: If the shapes of labels and predictions differ or there are more position bins than bases
            per subsequence.
    """
    # bin 0 (gene length < 1) holds the intergenic bases
    edges = np.array([1] + gene_length_edges)
    n_length_bins = len(edges) + 1
    with h5py.File(h5_data_path, 'r') as h5_data, h5py.File(h5_pred_path, 'r') as h5_pred:
        y_true = h5_data['data/y']
        y_pred = h5_pred['predictions']
        sw = h5_data['data/sample_weights']
        gene_lengths = h5_data['data/gene_lengths']
        if y_true.shape != y_pred.shape:
            raise ValueError(f'shape of data/y {y_true.shape} and predictions {y_pred.shape} differ')
        n_seqs, seq_len = sw.shape
        if n_position_bins > seq_len:
            raise ValueError(f'{n_position_bins} position bins exceed the subsequence length of {seq_len}')

        position_idx = np.arange(seq_len) * n_position_bins // seq_len
        position_cms = np.zeros((n_position_bins, N_CLASSES, N_CLASSES), dtype=np.int64)
        length_cms = np.zeros((n_length_bins, N_CLASSES, N_CLASSES), dtype=np.int64)
        # constant memory footprint independent of the subsequence length
        batch_size = max(1, BASES_PER_BATCH // seq_len)
        for start in range(0, n_seqs, batch_size):
            logger.info(f'Evaluating subsequences {start} to {min(start + batch_size, n_seqs)} of {n_seqs}')
            batch = slice(start, start + batch_size)
            mask = sw[batch].astype(bool)
            true_cls = np.argmax(y_true[batch], axis=-1)[mask]
            pred_cls = np.argmax(y_pred[batch], axis=-1)[mask]
            position_cms += binned_confusion_matrices(true_cls, pred_cls,
                                                      np.broadcast_to(position_idx, mask.shape)[mask],
                                                      n_position_bins)
            length_cms += binned_confusion_matrices(true_cls, pred_cls,
                                                    np.digitize(gene_lengths[batch][mask], edges),
                                                    n_length_bins)

    position_starts = np.searchsorted(position_idx, np.arange(n_position_bins)).tolist()
    position_bounds = list(zip(position_starts, position_starts[1:] + [seq_len]))
    length_bounds = [(0, 1)] + list(zip(edges[:-1].tolist(), edges[1:].tolist())) + [(int(edges[-1]), None)]
    return score_rows(position_cms, position_bounds), score_rows(length_cms, length_bounds)


def write_csv(rows: list[dict], path: str) -> None:
    """Writes rows with identical keys to a CSV file with a header line."""
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--h5-data', type=str, required=True,
                        help='h5 data file with data/y, data/sample_weights and data/gene_lengths')
    parser.add_argument('-p', '--h5-predictions', type=str, required=True,
                        help='h5 predictions file made for --h5-data')
    parser.add_argument('-o', '--output-dir', type=str, required=True,
                        help='existing directory for position_bins.csv and gene_length_bins.csv')
    parser.add_argument('--position-bins', type=int, default=100,
                        help='number of equally sized bins the subsequence length is divided into (default: 100)')
    parser.add_argument('--gene-length-edges', type=int, nargs='+', default=DEFAULT_GENE_LENGTH_EDGES,
                        help='ascending lower edges (bp, all > 1) of the gene length bins after the first one; '
                             'the bins below are [0, 1) for intergenic bases and [1, first edge) '
                             f'(default: {" ".join(map(str, DEFAULT_GENE_LENGTH_EDGES))})')
    args = parser.parse_args()

    if args.position_bins < 1:
        parser.error('--position-bins must be at least 1')
    if np.any(np.diff([1] + args.gene_length_edges) <= 0):
        parser.error('--gene-length-edges must be strictly ascending and greater than 1')
    if not os.path.isdir(args.output_dir):
        parser.error(f'--output-dir {args.output_dir} does not exist')

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    position_rows, length_rows = evaluate(args.h5_data, args.h5_predictions, args.position_bins,
                                          args.gene_length_edges)
    for rows, name in ((position_rows, 'position_bins'), (length_rows, 'gene_length_bins')):
        path = os.path.join(args.output_dir, f'{name}.csv')
        write_csv(rows, path)
        logger.info(f'{path} written')


if __name__ == '__main__':
    main()
