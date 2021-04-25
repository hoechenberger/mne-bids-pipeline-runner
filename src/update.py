from typing import Optional
from pathlib import Path
import subprocess


def update_pipeline(
    parent_dir: Path
) -> None:
    pipeline_dir = parent_dir / 'mne-bids-pipeline'
    pipeline_dir = pipeline_dir.absolute()

    if not pipeline_dir.exists():
        raise FileNotFoundError(f'Could not find MNE BIDS Pipeline at '
                                f'location: {pipeline_dir}. Please run '
                                f'"mne-bids-pipeline download"')

    command = f'git -C {pipeline_dir} pull --rebase --autostash origin main'
    subprocess.run(command.split(' '))
