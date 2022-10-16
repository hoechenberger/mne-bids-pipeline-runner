# A runner for the MNE BIDS Pipeline

⚠️ This functionality has now moved into the MNE-BIDS-Pipeline itself. This project & repository will be archived. ⚠️

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

The easiest way to get started is by simply running

```shell
mne-bids-pipeline
```

from your project directory (i.e. the one that contains e.g. your analysis code
and / or data) in the terminal. An interactive menu will appear, allowing you
to access all functionality.

You may also skip some of the menu selection process by passing certain
command line arguments, as demonstrated below.

### Install the MNE BIDS Pipeline

```shell
mne-bids-pipeline install
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
