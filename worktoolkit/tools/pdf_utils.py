import os
import os.path as osp
import traceback
from pathlib import Path
from typing import List

import typer
from loguru import logger
from pdfrw import PdfReader, PdfWriter

app = typer.Typer()

@app.command(name="subset", help="截取pdf文件部分页面")
def subset(
    input_path: str = typer.Argument(...),
    start_page: int = typer.Option(1, "--start-page", "-s", help="start page number"),
    end_page: int = typer.Option(-1, "--end-page", "-e", help="end page number"),
    output_path: str = typer.Option(None, "--output-path", "-o", help="output path"),
):
    """截取pdf文件部分页面

    Args:
        input_path (str): 输入pdf文件路径
        start_page (int, optional): 起始页码. Defaults to 1.
        end_page (int, optional): 终止页码. Defaults to -1.
        output_path (str, optional): 输出pdf保存路径. Defaults to None.
    """
    try:
        reader = PdfReader(input_path)
        num_pages = len(reader.pages)
        if end_page == -1:
            end_page = num_pages

        writer = PdfWriter()

        for page in range(start_page-1, end_page):
            writer.addpage(reader.pages[page])
        if output_path is None:
            p = Path(input_path)
            output_path = osp.join(os.getcwd(), f"{p.stem}-{start_page}-{end_page}.pdf")
        writer.write(output_path)
    except:
        logger.error("截取页面时发生错误！")
        traceback.print_exc()

@app.command(name="merge", help="拼接指定的pdf文件路径列表")
def merge(
    input_paths: List[str] = typer.Argument(...),
    output_path: str = typer.Option(None, "--output-path", "-o", help="output path"),
):
    """依次拼接指定的pdf文件路径列表

    Args:
        input_paths (List[str]): 需要拼接的pdf路径列表
        output_path (str, optional): 输出pdf保存路径
    """
    writer = PdfWriter()

    for path in input_paths:
        reader = PdfReader(path)
        writer.addpages(reader.pages)
    if output_path is None:
        output_path = osp.join(os.getcwd(), "merged.pdf")
    writer.write(output_path)

@app.command(name="rotate", help="旋转指定pdf文件页面")
def rotate(
    input_path: str = typer.Argument(...),
    start_page: int = typer.Option(1, "--start-page", "-s", help="start page number"),
    end_page: int = typer.Option(-1, "--end-page", "-e", help="end page number"),
    angle: int = typer.Option(90, "--angle", "-a", help="angle to rotate"), 
    output_path: str = typer.Option(None, "--output-path", "-o", help="output path"),
):
    """旋转指定pdf文件页面

    Args:
        input_path (str): pdf文件路径
        start_page (int, optional): 起始页码. 默认值为0.
        end_page (int, optional): 终止页码. 默认值为-1.
        angle (int, optional): 旋转角度. 90表示顺时针旋转90度，-90表示逆时针旋转90度， 默认值为90.
        output_path (str, optional): 结果pdf保存路径. 默认值为None.
    """
    try:
        assert angle % 90 ==0, "旋转度数必须是90倍数"
        reader = PdfReader(input_path)
        num_pages = len(reader.pages)
        if end_page == -1:
            end_page = num_pages
        assert start_page >= 1 and end_page <= num_pages, "页码范围不合法！"
        writer = PdfWriter()
        for i in range(num_pages):
            current_page = reader.pages[i]
            if i in range(start_page-1, end_page):
                current_page.Rotate = angle
            writer.addpage(current_page)
        if output_path is None:
            p = Path(input_path)
            output_path = osp.join(os.getcwd(), f"{p.stem}-rotated.pdf")
        writer.write(output_path)
    except:
        logger.error("旋转页面时发生错误！")
        traceback.print_exc()


if __name__ == "__main__":
    app()
