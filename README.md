# A runner for the MNE BIDS Pipeline

## Features

- Download the latest MNE BIDS Pipeline
- Update your local copy of the MNE BIDS Pipeline
- Run the MNE BIDS Pipeline
- Use separate versions of the MNE BIDS Pipeline for each of your projects

## Installation

```shell
pip install -e .
```

## Usage

### Download the MNE BIDS Pipeline

```shell
mne-bids-pipeline download
```

This downloads the latest version of the pipeline.

### Update the MNE BIDS Pipeline

```shell
mne-bids-pipeline update
```

This updates your MNE BIDS Pipeline to the latest version.

### Run the MNE BIDS Pipeline

```shell
mne-bids-pipeline run
```

This runs the MNE BIDS Pipeline. Please note that additional command line
arguments need to be passed, otherwise you will only get usage instructions.

Working example:

```shell
mne-bids-pipeline run --config=./my_custom_config.py
```
