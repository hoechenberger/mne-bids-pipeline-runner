from typing import Literal, Optional, Union
from pathlib import Path
from fire import Fire
import questionary

from . import download_pipeline, update_pipeline, run_pipeline

def cli(
    command: Optional[Literal['download', 'update', 'run']] = None,
    project_dir: Optional[Union[Path, str]] = None,
    config: Optional[Union[Path, str]] = None
) -> None:
    if command is None:
        command = questionary.select(
            message='What would you like to do?',
            choices=['download', 'update', 'run']).ask()

    if project_dir is None:
        project_dir = questionary.path(
            message='Path of your analysis project',
            default='.'
        ).ask()

    if command != 'download' and config is None:
        config = questionary.path(
            message='Path of the config file',
            default=str(project_dir)
        ).ask()

    if config is not None:
        config = Path(config)

    if project_dir is None:
        project_dir = Path('.')
    else:
        project_dir = Path(project_dir)

    if command == 'download':
        download_pipeline()
    elif command == 'update':
        update_pipeline(parent_dir=project_dir)
    elif command == 'run':
        run_pipeline(config=config, parent_dir=project_dir)
    else:
        raise ValueError(f'Supported commands: download, update, run; '
                         f'got: {command}')


def main():
    Fire(cli)
