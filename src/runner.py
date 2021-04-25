from typing import Optional
from pathlib import Path
import subprocess
import sys


def run_pipeline(
    parent_dir: Path,
    config: Optional[Path] = None
) -> None:
    pipeline_dir = parent_dir / 'mne-bids-pipeline'
    pipeline_dir = pipeline_dir.absolute()

    if not pipeline_dir.exists():
        raise FileNotFoundError(f'Could not find MNE BIDS Pipeline at '
                                f'location: {pipeline_dir}. Please run '
                                f'"mne-bids-pipeline download"')

    python_exe_path = sys.executable
    pipeline_run_py_path = pipeline_dir / 'run.py'
    command = f'{python_exe_path} {pipeline_run_py_path}'

    # Rely on run.py to handle unspecified `--config` parameter
    if config is not None:
        command += f' --config={config}'

    subprocess.run(command.split(' '),
                   cwd=pipeline_run_py_path.parent)
