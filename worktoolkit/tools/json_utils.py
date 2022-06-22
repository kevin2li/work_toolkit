import traceback
import csv
import typer
from loguru import logger
import os
import os.path as osp
from pathlib import Path
import json
import glob
from tqdm import tqdm
app = typer.Typer()

@app.command(name="merge", help="merge multiple json files in the specified directory")
def merge(
    dir: str,
    output_path: str = typer.Option(None, "--output-path", "-o", help="output path"),
):
    """merge multiple json files in the specified directory

    Args:
        dir (str): directory containing json files
        output_path (str): result save path
    """
    result = []
    path_list = glob.glob(os.path.join(dir, "*.json"))
    assert len(path_list) > 0, "Directory does not contain json files"
    for path in tqdm(path_list):
        with open(path, 'r') as f:
            obj = json.load(f)
            result.append(obj)
    if output_path is None:
        output_path = osp.join(os.getcwd(), f"merged.json")
    with open(output_path, 'w') as f:
        json.load(result, f)

@app.command(name="convert", help="convert json file to other format")
def convert(
    input_path: str = typer.Argument(...),
    target_format: str = typer.Option("csv", "--format", "-f", help="target format"),
    output_path: str = typer.Option(None, "--output-path", "-o", help="output path"),
):
    """ convert json file to other format

    Args:
        input_path (str, optional): _description_. Defaults to typer.Argument(...).
        target_format (str, optional): _description_. Defaults to typer.Option("csv", "--format", "-f", help="target format").
        output_path (str, optional): _description_. Defaults to typer.Option(None, "--output-path", "-o", help="output path").
    """
    raise NotImplementedError


if __name__ == "__main__":
    app()