from typing import Dict
from pathlib import Path
import yaml
from jinja2 import Template, Undefined


class NullUndefined(Undefined):
    def __getattr__(self, key):
        return ''


class NTEUEngineBuilderConfig:
    @staticmethod
    def load(file: Path) -> Dict:
        with file.open() as f:
            t = Template(f.read(), undefined=NullUndefined)
            c = yaml.safe_load(t.render())
            return yaml.safe_load(t.render(c))