from typing import Optional
from pathlib import Path
import subprocess

from .constants import GIT_REPO_URI


def install_pipeline(
    parent_dir: Optional[Path] = None
) -> None:
    if parent_dir is None:
        parent_dir = Path('.')

    target_dir = parent_dir / 'mne-bids-pipeline'
    if target_dir.exists():
        raise FileExistsError(f'The designated download directory, '
                              f'{target_dir}, already exists. You may wish to '
                              f'consider updating an existing MNE BIDS '
                              f'Pipeline via "mne-bids-pipeline update"')

    command = (f'git clone --single-branch --branch=main '
               f'{GIT_REPO_URI} {target_dir}')
    subprocess.run(command.split(' '))
    print('\n🚀 Successfully installed the MNE BIDS Pipeline!\n\n'
          'Next, run "mne-bids-pipeline" again to create a basic '
          'configuration.\n')
