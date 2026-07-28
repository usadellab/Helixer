"""Strict, criterion-agnostic FASTA sequence-selection manifests."""

from __future__ import annotations

import csv
import hashlib
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FastaRecord:
    seqid: str
    sequence: str


@dataclass(frozen=True)
class SelectionDecision:
    seqid: str
    include: bool
    reason: str


def read_fasta(path: str) -> list[FastaRecord]:
    records: list[FastaRecord] = []
    seqid: str | None = None
    sequence: list[str] = []
    with open(path, encoding='utf-8') as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.rstrip('\n\r')
            if line.startswith('>'):
                if seqid is not None:
                    records.append(FastaRecord(seqid, ''.join(sequence)))
                seqid = line[1:].split(None, 1)[0]
                if not seqid:
                    raise ValueError(f'empty FASTA identifier at line {line_no}')
                sequence = []
            elif seqid is None:
                if line.strip():
                    raise ValueError(f'FASTA sequence before first header at line {line_no}')
            else:
                sequence.append(line.strip())
    if seqid is not None:
        records.append(FastaRecord(seqid, ''.join(sequence)))
    if not records:
        raise ValueError(f'FASTA input {path!r} contains no records')
    ids = [record.seqid for record in records]
    duplicate = next((item for item, count in Counter(ids).items() if count > 1), None)
    if duplicate:
        raise ValueError(f"duplicate FASTA seqid {duplicate!r}")
    return records


def parse_manifest(path: str, records: list[FastaRecord]) -> list[SelectionDecision]:
    manifest_bytes = Path(path).read_bytes()
    try:
        rows = list(csv.DictReader(manifest_bytes.decode('utf-8').splitlines(), delimiter='\t'))
    except UnicodeDecodeError as error:
        raise ValueError(f'selection manifest is not UTF-8: {error}') from error
    if not rows or rows[0] is None:
        raise ValueError('selection manifest has no decisions')
    required = {'seqid', 'include'}
    fieldnames = set(rows[0])
    if not required.issubset(fieldnames) or not fieldnames.issubset({'seqid', 'include', 'reason'}):
        raise ValueError('selection manifest columns must be seqid, include, and optional reason')
    decisions: dict[str, SelectionDecision] = {}
    fasta_ids = {record.seqid for record in records}
    for row_no, row in enumerate(rows, 2):
        seqid = (row.get('seqid') or '').strip()
        value = (row.get('include') or '').strip().lower()
        if not seqid:
            raise ValueError(f'empty seqid in selection manifest row {row_no}')
        if seqid in decisions:
            raise ValueError(f'duplicate manifest seqid {seqid!r}')
        if seqid not in fasta_ids:
            raise ValueError(f'manifest seqid {seqid!r} is absent from FASTA')
        if value not in {'true', 'false'}:
            raise ValueError(f"invalid include value {value!r} for {seqid!r}; use true or false")
        decisions[seqid] = SelectionDecision(seqid, value == 'true', (row.get('reason') or '').strip())
    missing = fasta_ids - set(decisions)
    if missing:
        raise ValueError(f'manifest has no decision for FASTA seqid {sorted(missing)[0]!r}')
    ordered = [decisions[record.seqid] for record in records]
    if not any(item.include for item in ordered):
        raise ValueError('selection manifest excludes every FASTA record')
    return ordered


def manifest_checksum(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_selected_fasta(path: str, records: list[FastaRecord], decisions: list[SelectionDecision]) -> None:
    with open(path, 'w', encoding='utf-8') as handle:
        for record, decision in zip(records, decisions):
            if decision.include:
                handle.write(f'>{record.seqid}\n{record.sequence}\n')


def write_report(path: str, records: list[FastaRecord], decisions: list[SelectionDecision], chunk_size: int,
                 manifest_path: str) -> None:
    reason_counts = Counter(item.reason for item in decisions if item.reason)
    with open(path, 'w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle, delimiter='\t')
        writer.writerow(['metric', 'value'])
        for label, subset in [('full', list(zip(records, decisions))), ('selected', [(r, d) for r, d in zip(records, decisions) if d.include])]:
            bp = sum(len(record.sequence) for record, _ in subset)
            rows = sum(2 * ((len(record.sequence) + chunk_size - 1) // chunk_size) for record, _ in subset)
            writer.writerow([f'{label}_records', len(subset)])
            writer.writerow([f'{label}_bp', bp])
            writer.writerow([f'{label}_two_strand_fixed_window_rows', rows])
            writer.writerow([f'{label}_padded_positions', rows * chunk_size])
        writer.writerow(['manifest_sha256', manifest_checksum(manifest_path)])
        for reason, count in sorted(reason_counts.items()):
            writer.writerow([f'reason_count:{reason}', count])
