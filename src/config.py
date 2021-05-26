from pathlib import Path
import shutil


def configure_pipeline(
    project_dir: Path,
    config_path: Path
) -> None:
    pipeline_dir = project_dir / 'mne-bids-pipeline'
    assert pipeline_dir.exists()

    if config_path.exists():
        raise FileExistsError(
            f'😱 Oh no! The specified configuration path, {config_path}, '
            f'already exists! Please either remove this file or specify a '
            f'different name.'
        )

    config_source = pipeline_dir / 'config.py'
    config_target = config_path

    shutil.copy(config_source, config_target)

    print(f'\n✅ Successfully created configuration file {config_target}\n\n'
          f'Please open the file in an editor of your choice and make the '
          f'desired adjustments.')