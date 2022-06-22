import os
import os.path as osp
import traceback
from pathlib import Path
from typing import List
import qrcode

import typer
app = typer.Typer()

@app.command(name='encode', help="generate qrcode with given data")
def encode(data: str, output_path: str):
    raise NotImplementedError


@app.command(name='decode', help="extract data from qrcode")
def decode(input_path: str):
    raise NotImplementedError


if __name__ == "__main__":
    app()
