from jinja2 import Template
from pathlib import Path
from typing import Dict
import logging
import shutil
from nteu_engine_builder.nteu_engine_builder_config import NTEUEngineBuilderConfig


class NTEUEngineBuilder:
    @staticmethod
    def create_assets(asset_dir: str = 'assets'):
        # Create old dir
        asset_dir = Path(asset_dir)
        try:
            shutil.copytree('nteu_engine_builder/assets', asset_dir)
            logging.info(f'`{asset_dir}` created')
        except FileExistsError:
            logging.info(f'`{asset_dir}` directory already exists')

    @staticmethod
    def build_dockerfile(asset_dir='assets'):
        asset_dir = Path(asset_dir)
        config: Dict = NTEUEngineBuilderConfig.load(asset_dir.joinpath('config.yaml'))

        # Create supervisord config
        with asset_dir.joinpath('supervisord.conf').open('w', encoding='utf-8') as f1:
            with asset_dir.joinpath('private/supervisord.conf').open() as f2:
                template_content = f2.read()
                template = Template(template_content)
                content = template.render(config=config)
            f1.write(content)
        logging.info(f'`{asset_dir.name}/supervisord.conf` created')

        with asset_dir.joinpath('gateway_launcher.py').open('w', encoding='utf-8') as f1:
            with asset_dir.joinpath('private/gateway_launcher.py').open() as f2:
                template_content = f2.read()
                template = Template(template_content)
                content = template.render(config=config)
            f1.write(content)
        logging.info(f'`{asset_dir.name}/gateway_launcher.py` created')

        # Create Dockerfile
        with asset_dir.joinpath('Dockerfile').open('w', encoding='utf-8') as f1:
            with asset_dir.joinpath('private/Dockerfile').open() as f2:
                template_content = f2.read()
                template = Template(template_content)
                content = template.render(config=config)
            f1.write(content)
        logging.info(f'`{asset_dir.name}/dockerfile` created')


