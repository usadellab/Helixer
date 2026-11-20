# Helixer options
The most important scripts and their options are listed.
1. [Helixer.py](#1-helixerpy-options)
2. [fasta2h5.py](#2-fasta2h5py-options)
3. [HybridModel.py](#3-hybridmodelpy-options)
4. [HelixerPost](#4-helixerpost-options) (the same as the [post-processing parameters](#post-processing-parameters) for Helixer.py, plus further tuning options)
5. [import2geenuff.py](#5-import2geenuffpy-options)
6. [geenuff2h5.py](#6-geenuff2h5py-options)

## 1. Helixer.py options
Helixer.py always searches for the configuration file ``config/helixer_config.yaml`` in the current
working directory. If that file isn't provided, the parameters are expected to be given via the
command line.

### General parameters
| Parameter               | Default                                                                   | Explanation                                                                                                                                                                                                                                                                  |
|:------------------------|:--------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --fasta-path            | /                                                                         | FASTA input file                                                                                                                                                                                                                                                             |
| --gff-output-path       | /                                                                         | Output GFF3 file path                                                                                                                                                                                                                                                        |
| --species               | /                                                                         | Species name. Will be added to the GFF3 file.                                                                                                                                                                                                                                |
| --temporary-dir         | system default                                                            | Use supplied (instead of system default) for temporary directory (place where temporary h5 files from fasta to h5 conversion and Helixer's raw base-wise predictions get saved)                                                                                              |
| --subsequence-length    | vertebrate: 213840, land_plant: 64152, fungi: 21384, invertebrate: 213840 | How to slice the genomic sequence. Set moderately longer than length of typical genic loci. Tested up to 213840. Must be evenly divisible by the timestep width of the used model, which is typically 9. (Lineage dependent defaults)                                        |
| --write-by              | 20_000_000                                                                | Convert genomic sequence in super-chunks to numerical matrices with this many base pairs, which will be rounded to be divisible by subsequence-length; needs to be equal to or larger than subsequence length; for lower memory consumption, consider setting a lower number |
| --lineage               | /                                                                         | What model to use for the annotation. Options are: vertebrate, land_plant, fungi or invertebrate.                                                                                                                                                                            |
| --model-filepath        | /                                                                         | Set this to override the default model for any given lineage and instead take a specific model                                                                                                                                                                               |
| --downloaded-model-path | /                                                                         | Set to override the default download directory (<users_home_directory>/.local/share/Helixer/models) Helixer is checking to see if you use the newest model; only works with --lineage                                                                                        |

### Prediction parameters
| Parameter             | Default                                                                                                     | Explanation                                                                                                                                                                                                                                                                                                                                                                                 |
|:----------------------|:------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --batch-size          | 32                                                                                                          | The batch size for the raw predictions in TensorFlow. Should be as large as possible on your GPU to save prediction time.                                                                                                                                                                                                                                                                   |
| --deterministic       | False                                                                                                       | Enable deterministic GPU operations; reproducible across runs on GPUs that are not deterministic by default (e.g. NVIDIA L40S); may be slower on some GPU architectures.                                                                                                                                                                                                                    |
| --no-overlap          | False                                                                                                       | Switches off the overlapping after predictions are made. Overlap will improve prediction quality at subsequence ends by creating and overlapping sliding-window predictions. Predictions without overlapping will be faster, but will have lower quality towards the start and end of each subsequence. With this parameter --overlap-offset and --overlap-core-length will have no effect. |
| --overlap-offset      | vertebrate: 106920, land_plant: 32076, fungi: 10692, invertebrate: 106920 (i.e. subsequence_length / 2)     | Distance to 'step' between predicting subsequences when overlapping. Smaller values may lead to better predictions but will take longer. The subsequence_length should be evenly divisible by this value.                                                                                                                                                                                   |
| --overlap-core-length | vertebrate: 160380, land_plant: 48114, fungi: 16038, invertebrate: 160380 (i.e. subsequence_length * 3 / 4) | Predicted sequences will be cut to this length to increase prediction quality if overlapping is enabled. Smaller values may lead to better predictions but will take longer. Has to be smaller than subsequence_length.                                                                                                                                                                     |
| --compression-threads | 4                                                                                                           | Number of CPU threads compressing the predictions while the GPU predicts the next batches (only with --compression gzip, i.e. the default compression method); 0 compresses in the main thread after each batch.                                                                                                                                                                            |

### Post-processing parameters
| Parameter                | Default | Explanation                                                                                                                                                                                                                                  |
|:-------------------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --window-size            | 100     | Width of the sliding window that is assessed for intergenic vs genic (UTR/Coding Sequence/Intron) content                                                                                                                                    |
| --edge-threshold         | 0.1     | Threshold specifies the genic score which defines the start/end boundaries of each candidate region within the sliding window                                                                                                                |
| --peak-threshold         | 0.8     | Threshold specifies the minimum peak genic score required to accept the candidate region; the candidate region is accepted if it contains at least one window with a genic score above this threshold                                        |
| --min-coding-length      | 60      | Output is filtered to remove genes with a total coding length shorter than this value                                                                                                                                                        |
| --min-intron-length      | 50      | Minimum intron length in bp for U2-type introns (GT-AG and GC-AG; also covers U12-type GT-AG introns). Values below 2 act as 2                                                                                                               |
| --min-intron-length-u12  | 30      | Minimum intron length in bp for U12-type AT-AC introns. Values below 2 act as 2                                                                                                                                                              |
| --post-config-path       | /       | YAML config file for helixer_post_bin with further post-processing parameters, see [HelixerPost options](#4-helixerpost-options)                                                                                                             |
| --post-threads           | 4       | Number of CPU threads for post-processing; 0 uses all available cores, as does a number larger than the available cores                                                                                                                      |
| --post-max-in-flight-mbp | 4       | Cap on the total length in Mbp of the candidate regions queued or being decoded at a time; bounds the peak memory on genomes with many long candidate regions (e.g. human) and does not change the output. Lower it if memory is very short. |

For each post-processing parameter, the first of these sources that sets it is used:
1. Helixer.py command line
2. Helixer.py config file (`config/helixer_config.yaml` or `--config-path`)
3. The `--post-config-path` file
4. The defaults in the table above

The defaults for the two minimum intron lengths suit most species. They only need to be lowered for
species with introns shorter than 50 bp. In that case, setting both to the same lower value
(e.g. `--min-intron-length 30 --min-intron-length-u12 30`) is sufficient; it is not necessary to
find out which spliceosome (U2 or U12) splices the short introns of the species.

Values below 20 bp are not recommended, and Helixer.py logs a warning for them: transcripts with
introns shorter than 20 bp are masked in the training data (GeenuFF's `too_short_intron` check),
so the Helixer models never learned such introns.

## 2. fasta2h5.py options
fasta2h5.py always searches for the configuration file ``config/fasta2h5_config.yaml`` in the current
working directory. If that file isn't provided, the parameters are expected to be given via the
command line.

| Parameter            | Default   | Explanation                                                                                                                                                                                                                     |
|:---------------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --fasta-path         | /         | **Required**; FASTA input file                                                                                                                                                                                                  |
| --h5-output-path     | /         | **Required**; HDF5 output file for the encoded data. Must end with ".h5".                                                                                                                                                       |
| --species            | /         | **Required**; Species name. Will be added to the .h5 file.                                                                                                                                                                      |
| --subsequence-length | 21384     | Size of the chunks each genomic sequence gets cut into.                                                                                                                                                                         |
| --write-by           | 5_346_000 | Write in super-chunks with this many base pairs, which will be rounded to be divisible by subsequence-length; needs to be equal to or larger than subsequence length; peak memory grows with it, not with the chromosome length |
## 3. HybridModel.py options
(for training and evaluation)
### General parameters
| Parameter            | Default         | Explanation                                                                                                                                                                                                                                                                                                         |
|:---------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -d/--data-dir        | /               | Directory containing training and validation data (.h5 files). The naming convention for the training and validation files is "training_data[...].h5" and "validation_data[...].h5" respectively.                                                                                                                   |
| -s/--save-model-path | ./best_model.h5 | Path to save the best model (model with the best validation genic F1 (the F1 for the classes CDS, UTR and Intron)) to. If --save-every-check is used, the folder to save the best model to is also used to save interim models (these have a predefined naming convention: model_e<epoch_number>_<batch_number>.h5) |

### Model parameters
| Parameter      | Default | Explanation                                                                                           |
|:---------------|:--------|:------------------------------------------------------------------------------------------------------|
| --cnn-layers   | 1       | Number of convolutional layers                                                                        |
| --lstm-layers  | 1       | Number of bidirectional LSTM layers                                                                   |
| --units        | 32      | Number of LSTM units per bLSTM layer                                                                  |
| --filter-depth | 32      | Filter depth for convolutional layers                                                                 |
| --kernel-size  | 26      | Kernel size for convolutional layers                                                                  |
| --pool-size    | 9       | Best set to a multiple of 3 (codon/nucleotide triplet size)                                           |
| --dropout1     | 0.0     | If > 0, will add dropout layer with given dropout probability after the CNN. (range: 0.0-1.0)         |
| --dropout2     | 0.0     | If > 0, will add dropout layer with given dropout probability after the bLSTM block. (range: 0.0-1.0) |


### Training parameters
| Parameter               | Default   | Explanation                                                                                                                                                    |
|:------------------------|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -e/--epochs             | 10,000    | Number of training runs                                                                                                                                        |
| -b/--batch-size         | 8         | Batch size for training data; for multi-GPU training please multiply by the number of GPUs                                                                     |
| --val-test-batch-size   | 32        | Batch size for validation/test data; for multi-GPU training please multiply by the number of GPUs                                                              |
| --loss                  | /         | Loss function specification                                                                                                                                    |
| --patience              | 3         | Allowed epochs without the validation genic F1 improving before stopping training                                                                              |
| --check-every-nth-batch | 1,000,000 | Check validation genic F1 every nth batch, on default this check gets executed once every epoch regardless of the number of batches                            |
| --log-interval-fraction | 0.05      | Progress log fraction during training/validation batches e.g. 0.05 logs every 5 % of batches (default: 0.05)                                                   |
| --optimizer             | adamw     | Optimizer algorithm; options: adam or adamw                                                                                                                    |
| --clip-norm             | 3.0       | The gradient of each weight is individually clipped so that its norm is no higher than this value                                                              |
| --learning-rate         | 3e-4      | Learning rate for training                                                                                                                                     |
| --weight-decay          | 3.5e-5    | Weight decay for training; penalizes complexity and prevents overfitting                                                                                       |
| --class-weights         | /         | Weighting of the 4 classes [intergenic, UTR, CDS, Intron] (Helixer predictions)                                                                                |
| --transition-weights    | /         | Weighting of the 6 transition categories [transcription start site, start codon, donor splice site, transcription stop site, stop codon, acceptor splice site] |
| --resume-training       | False     | Add this to resume training (pretrained model checkpoint necessary)                                                                                            |

### Testing/Predicting parameters
| Parameter                   | Default                    | Explanation                                                                                                                                                                                                             |
|:----------------------------|:---------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -l/--load-model-path        | /                          | Path to a trained/pretrained model checkpoint. (HDF5 format)                                                                                                                                                            |
| -t/--test-data              | /                          | Path to one test HDF5 file.                                                                                                                                                                                             |
| -p/--prediction-output-path | predictions.h5             | Output path of the HDF5 prediction file. (Helixer base-wise predictions)                                                                                                                                                |
| --compression               | gzip                       | compression used for datasets in predictions h5 file ("lzf" or "gzip").                                                                                                                                                 |
| --compression-threads       | 4                          | CPU threads compressing the predictions with gzip (i.e. the default compression method) while the GPU predicts the next batches; 0 compresses in the main thread after each batch (no effect with lzf).                 |
| --eval                      | False                      | Add to run test/validation run instead of predicting.                                                                                                                                                                   |
| --overlap                   | False                      | Add to improve prediction quality at subsequence ends by creating and overlapping sliding-window predictions (with proportional increase in time usage).                                                                |
| --overlap-offset            | subsequence_length / 2     | Distance to 'step' between predicting subsequences when overlapping. Smaller values may lead to better predictions but will take longer. The subsequence_length should be evenly divisible by this value.               |
| --core-length               | subsequence_length * 3 / 4 | Predicted sequences will be cut to this length to increase prediction quality if overlapping is enabled. Smaller values may lead to better predictions but will take longer. Has to be smaller than subsequence_length. |

### Resources parameters
| Parameter         | Default                   | Explanation                                                                                                                             |
|:------------------|:--------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| --float-precision | float32                   | Precision of model weights and biases                                                                                                   |
| --gpu-id          | -1 (use all visible GPUs) | Sets GPU index, use if you want to train on one GPU on a multi-GPU machine without a job scheduler system                               |
| --deterministic   | False                     | Enable deterministic GPU ops; reproducible but potentially slower; use on GPUs that are not deterministic by default (e.g. NVIDIA L40S) |
| --workers         | 1                         | Number of threads used to fetch input data for training. Consider setting to match the number of GPUs                                   |

### Miscellaneous parameters
| Parameter          | Default | Explanation                                                                                                                                                                                                                                                                                                                      |
|:-------------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --save-every-check | False   | Add to save a model checkpoint every validation genic F1 check (see --check-every-nth-batch in [training parameters](#training-parameters) The folder to save the best model to (--save-model-path) is also used to save the interim models (these have a predefined naming convention: model_e<epoch_number>_<batch_number>.h5) |
| -v/--verbose       | False   | Add to run HybridModel.py in verbosity mode (additional information will be printed)                                                                                                                                                                                                                                             |
| --debug            | False   | Add to run in debug mode; truncates input data to small example (for training: just runs a few epochs)                                                                                                                                                                                                                           |

### Fine tuning parameters
| Parameter                    | Default | Explanation                                                                                                                             |
|:-----------------------------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------|
| --fine-tune                  | False   | Add/Use with --resume-training to replace and fine tune just the very last layer                                                        |
| --fine-tune-resume           | False   | Add/Use with --resume-training to resume your fine tuning of the very last layer                                                        |
| --pretrained-model-path      | /       | Required when predicting with a model fine tuned with coverage                                                                          |
| --input-coverage             | False   | Add to use "evaluation/rnaseq_(spliced_)coverage" from HDF5 training/validation files as additional input for a late layer of the model |
| --coverage-norm              | None    | None, linear or log (recommended); how coverage will be normalized before inputting                                                     |
| --post-coverage-hidden-layer | False   | Adds extra dense layer between concatenating coverage and final output layer                                                            |

## 4. HelixerPost options
The options for HelixerPost are either chosen when directly using Helixer.py (see 
[post-processing parameters](#post-processing-parameters)) or by using HelixerPost directly after
HybridModel.py, with the same parameter names and defaults. The three file paths are positional.
This requires HelixerPost 0.4.0 or newer; older versions only accept positional parameters.
```bash
helixer_post_bin [OPTIONS] <genome.h5> <predictions.h5> <output.gff3>
# e.g.
helixer_post_bin --peak-threshold 0.9 --min-intron-length 30 --min-intron-length-u12 30 \
  genome.h5 predictions.h5 output.gff3
```
Besides the post-processing parameters of Helixer.py (same names and defaults, except for the
Helixer.py-only `--post-*` options), `helixer_post_bin` has the following options:

| Parameter              | Default             | Explanation                                                                                                                                                                                                                                                               |
|:-----------------------|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -c/--config            | /                   | YAML config file with all post-processing parameters, including those without a command line option (minimum intron length per intron class, splice-flag booleans, per-donor fixed penalties); command line options override its values. Helixer.py: `--post-config-path` |
| --print-default-config | False               | Writes all defaults as a YAML config file template to stdout and exits                                                                                                                                                                                                    |
| -j/--threads           | 4                   | Number of threads for the hidden Markov model decoding; 0 uses all available cores, as does a number larger than the available cores. Helixer.py: `--post-threads` (default 4)                                                                                            |
| --max-in-flight-mbp    | 4                   | Cap on the total length in Mbp of the candidate regions queued or being decoded at a time; does not change the output. Helixer.py: `--post-max-in-flight-mbp`                                                                                                             |
| --rating               | /                   | Per-base rating output file (reference vs. prediction for each base and strand); only written when given; very large, roughly 230 bytes per bp                                                                                                                            |
| -v/--verbose           | False               | Prints per-sequence and per-strand ratings, one line per sequence and candidate region and the decoded hidden Markov model regions                                                                                                                                        |
| --hmm-prob-floor       | 1e-9                | Floor applied to the predicted probabilities before the negative-log conversion                                                                                                                                                                                           |
| --hmm-phase-retain     | 0.2                 | Weight given to the predicted phase signal (0 ignores it, 1 trusts it fully)                                                                                                                                                                                              |
| --hmm-start-weight     | 1000                | Multiplicative weight on the start codon base-match penalty                                                                                                                                                                                                               |
| --hmm-stop-weight      | 1000                | Multiplicative weight on the stop codon base-match penalty                                                                                                                                                                                                                |
| --hmm-donor-weight     | 2                   | Multiplicative weight on the splice donor base-match penalty                                                                                                                                                                                                              |
| --hmm-acceptor-weight  | 2                   | Multiplicative weight on the splice acceptor base-match penalty                                                                                                                                                                                                           |

`helixer_post_bin --print-default-config > helixer_post_config.yml` writes all defaults as a config
file template; after editing, it can be passed to Helixer.py with `--post-config-path`. The
[HelixerPost README](https://github.com/usadellab/HelixerPost#parameters) describes the config
options in more detail.
The detailed `--verbose` output is only available in the
[3-step workflow](../README.md#3-step-inference), which keeps the genome and predictions h5 files, so the post-processing can be
rerun without a new prediction.

## 5. import2geenuff.py options
(see [GeenuFF repository](https://github.com/usadellab/GeenuFF/tree/main))
### Configuration parameters
| Parameter     | Default           | Explanation                                                                                                                                                                                                  |
|:--------------|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --basedir     | /                 | Organized output (& input) directory. If this is not set, --gff3, --fasta and --db-path must be set.                                                                                                         |
| --config-file | config/import.yml | YAML file setting `min_intron_length` (default 20) and `min_cds_length` (default 60), the intron and spliced CDS lengths in bp below which a transcript is masked; the defaults apply without the file       |

### Override default with custom parameters
--gff3, --fasta and --db-path are **required** if ``--basedir`` is not set.

| Parameter  | Default                                                                                 | Explanation                                                                    |
|:-----------|:----------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| --gff3     | /                                                                                       | GFF3 formatted file to parse / standardize                                     |
| --fasta    | /                                                                                       | Fasta file to parse standardize (has to be the same assembly as the GFF3 file) |
| --db-path  | basedir/output/\<species\>.sqlite3 (when ``--basedir`` is set)                          | Output path of the GeenuFF database; must end in .sqlite3                      |
| --log-file | beside the database, named after it (e.g. genome.sqlite3 -> genome_geenuff_import.log)  | Output path for import2geenuff log file; it ends with the import summary       |

### Possible genome attribute parameters
| Parameter       | Default | Explanation                                    |
|:----------------|:--------|:-----------------------------------------------|
| --species       | /       | **Required**; (Scientific) name of the species |
| --accession     | /       | Genome assembly accession                      |
| --version       | /       | Genome assembly version                        |
| --acquired-from | /       | Genome source (example: NCBI_RefSeq)           |

### Miscellaneous parameter
| Parameter    | Default | Explanation                                                                                              |
|:-------------|:--------|:---------------------------------------------------------------------------------------------------------|
| --replace-db | /       | Whether to override a GeenuFF database file found at the default location/at the location of --db_path   |
| --verbose    | /       | Log every individual error as it is found, instead of only the summary at the end (can be a lot of text) |

## 6. geenuff2h5.py options
geenuff2h5.py always searches for the configuration file ``config/fasta2h5_config.yaml`` in the current
working directory. If that file isn't provided, the parameters are expected to be given via the
command line.

| Parameter            | Default   | Explanation                                                                                                                                                                                                                                                                                                                                                             |
|:---------------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --input-db-path      | /         | **Required**; Path to the GeenuFF SQLite input file/database (has to contain only one genome)                                                                                                                                                                                                                                                                           |
| --h5-output-path     | /         | **Required**; HDF5 output file for the encoded data. Must end with ".h5"                                                                                                                                                                                                                                                                                                |
| --add-additional     | /         | Outputs the datasets under alternatives/{add-additional}/ (and checks sort order against existing "data" datasets). Use to add e.g. additional annotations from Augustus                                                                                                                                                                                                |
| --subsequence-length | 21384     | Length of the subsequences that the model will use at once.                                                                                                                                                                                                                                                                                                             |
| --modes              | all       | Either "all" (default), or a comma separated list with desired members of the following {X, y, anno_meta, transitions} that should be exported. This can be useful, for instance when skipping transitions (to reduce size/mem) or skipping X because you are adding an additional annotation set to an existing file (i.e. y,anno_meta,transitions <- no whitespaces!) |
| --write-by           | 5,346,000 | Write in super-chunks with this many base pairs, which will be rounded to be divisible by subsequence-length; needs to be equal to or larger than subsequence length; peak memory grows with it, not with the chromosome length                                                                                                                                         |
