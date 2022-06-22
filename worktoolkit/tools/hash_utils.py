import os
import os.path as osp
import traceback
from pathlib import Path
from typing import List

import typer
from loguru import logger

app = typer.Typer()

@app.command(name="hash", help="calculate the hash of given file")
def hash(input_path:str, algorithm: str):
    raise NotImplementedError


@app.command(name="compare", help="compare two files whether they are same")
def compare(input_path1: str, input_path2: str, algorithm: str):
    raise NotImplementedError


if __name__ == "__main__":
    app()
