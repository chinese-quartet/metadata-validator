## Metadata Validator

<!-- ![https://img.shields.io/pypi/v/metadata_validator.svg](https://pypi.python.org/pypi/metadata_validator)
![https://img.shields.io/travis/yjcyxky/metadata_validator.svg](https://travis-ci.com/yjcyxky/metadata_validator)
![https://readthedocs.org/projects/metadata-validator/badge/?version=latest](https://metadata-validator.readthedocs.io/en/latest/?version=latest) -->

### Installation

```bash
pip install metadata_validator
```

or 

```bash
git clone https://github.com/chinese-quartet/metadata-validator.git
cd metadata-validator
python setup.py install
```

### Usage

```bash
Usage: metadata_validator [OPTIONS]

  Console script for metadata_validator.

Options:
  -i, --input FILE                Input file path, only support xlsx file.
                                  [required]
  -o, --output TEXT               Output error and warning messages as a file.
                                  [required]
  -t, --template-type [DNAseq|RNAseq|Proteomics|Metabolomics]
                                  It support the following metadata tables:
                                  'DNAseq', 'RNAseq', 'Proteomics,
                                  'Metabolomics'  [required]
  --help                          Show this message and exit.
```

### Example

Validate your metadata file of DNAseq template with the following command:

```bash
metadata_validator -i your_metadata_file.xlsx -o output.log -t DNAseq
```

### Metada

* Free software: MIT license
* Documentation: https://metadata-validator.readthedocs.io.


### Features

### TODO

### Credits
This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage) project template.