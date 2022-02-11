from json import load
from os import getcwd, chdir, path
from pathlib import Path


class Config():
    def __init__(self):
        chdir(path.dirname(__file__))
        with open(f'{Path(getcwd()).parent}/config.json') as f:
            self.config = load(f)

    def __getattr__(self, arg):
        return self.config[arg]
