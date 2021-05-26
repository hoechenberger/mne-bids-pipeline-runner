from typing import Literal, Optional, Union
from pathlib import Path
from fire import Fire
import questionary

from . import (install_pipeline, update_pipeline, configure_pipeline,
               run_pipeline)

def cli(
    command: Optional[Literal['install', 'update', 'configure', 'run']] = None,
    project_dir: Optional[Union[Path, str]] = None,
    config: Optional[Union[Path, str]] = None
) -> None:
    if command is None:
        command = questionary.select(
            message='What would you like to do?',
            choices=['install', 'update', 'configure', 'run']
        ).ask()

        if command is None:
            return

    if project_dir is None and command == 'install':
        project_dir = questionary.path(
            message='Path of your analysis project '
                    '("." for current directory)',
            default='.'
        ).ask()

        if project_dir is None:
            return
    elif project_dir is None:
        project_dir = '.'

    project_dir = Path(project_dir)

    if command in ['configure', 'run'] and config is None:
        if command == 'configure':
            message = 'Where to create the config file?'
        else:
            message = 'Path of existing config file'
    
        config = questionary.path(
            message=message,
            default=str(project_dir / 'config.py')
        ).ask()

        if config is None:
            return
        config = Path(config)

    if command == 'install':
        install_pipeline(parent_dir=project_dir)
    elif command == 'update':
        update_pipeline(parent_dir=project_dir)
    elif command == 'configure':
        configure_pipeline(project_dir=project_dir, config_path=config)
    elif command == 'run':
        run_pipeline(config=config, parent_dir=project_dir)
    else:
        raise ValueError(f'Supported commands: download, update, run; '
                         f'got: {command}')


def main():
    Fire(cli)
