import traceback
import csv
import typer
from loguru import logger
import os
import os.path as osp
from pathlib import Path

app = typer.Typer()

@app.command(name="merge", help="merge multiple csv files in the specified directory")
def merge(
    dir: str,
    output_path: str = typer.Option(None, "--output-path", "-o", help="output path"),
):
    """ merge multiple csv files in the specified directory

    Args:
        dir (str): _description_
        output_path (str): _description_
    """
    if output_path is None:
        output_path = osp.join(os.getcwd(), f"merged.csv")
    raise NotImplementedError

@app.command(name="convert", help="convert csv file to other format")
def convert(
    input_path: str = typer.Argument(...),
    target_format: str = typer.Option("json", "--format", "-f", help="target format"),
    output_path: str = typer.Option(None, "--output-path", "-o", help="output path"),
):
    """ convert csv file to other format

    Args:
        input_path (str, optional): _description_. Defaults to typer.Argument(...).
        target_format (str, optional): _description_. Defaults to typer.Option("json", "--format", "-f", help="target format").
        output_path (str, optional): _description_. Defaults to typer.Option(None, "--output-path", "-o", help="output path").
    """
    raise NotImplementedError


if __name__ == "__main__":
    app()