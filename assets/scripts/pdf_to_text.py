#!/usr/bin/env python3
"""
PDF 转纯文本工具
用法：
    python pdf_to_text.py input.pdf [output.txt]
    python pdf_to_text.py input.pdf > output.txt
"""

import sys
import argparse
import logging
from pathlib import Path

from logger import setup_logger

try:
    import pdfplumber
except ImportError:
    print("错误：未安装 pdfplumber，请运行：pip install pdfplumber", file=sys.stderr)
    sys.exit(1)

def convert_pdf_to_text(pdf_path: str, output_path: str = None) -> str:
    """
    将 PDF 文件转换为纯文本。

    参数：
        pdf_path: 输入 PDF 文件路径
        output_path: 可选的输出文本文件路径。若为 None，则返回文本字符串。

    返回：
        若 output_path 为 None，返回提取的文本字符串；否则返回空字符串。

    异常：
        FileNotFoundError: PDF 文件不存在时抛出。
        Exception: 其他 PDF 处理错误。
    """
    pdf_file = Path(pdf_path)
    if not pdf_file.is_file():
        raise FileNotFoundError(f"PDF 文件未找到：{pdf_path}")

    full_text = []

    logger = logging.getLogger(__name__)

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        logger.info(f"正在处理 {pdf_path}，共 {total_pages} 页")

        for i, page in enumerate(pdf.pages, start=1):
            if i % 5 == 0 or i == total_pages:
                logger.debug(f"第 {i} / {total_pages} 页")
            # 从页面提取文本
            text = page.extract_text()
            if text:
                full_text.append(text)
            else:
                logger.warning(f"第 {i} 页未找到文本")

    result_text = "\n\n".join(full_text)  # 用双换行保留页面分隔

    if output_path:
        output_file = Path(output_path)
        output_file.write_text(result_text, encoding="utf-8")
        logger.info(f"文本已保存至 {output_file.resolve()}")
        return ""
    else:
        return result_text


def main(input_path=None, output_path=None, verbose=False):
    if input_path is None:
        parser = argparse.ArgumentParser(
            description="使用 pdfplumber 将 PDF 文件转换为纯文本"
        )
        parser.add_argument("input", help="输入 PDF 文件路径")
        parser.add_argument("output", nargs="?", help="可选的输出文本文件路径（若省略则输出到标准输出）")
        parser.add_argument("-v", "--verbose", action="store_true", help="启用详细日志")
        args = parser.parse_args()
        _verbose = args.verbose
        _input = args.input
        _output = args.output
    else:
        _verbose = verbose
        _input = input_path
        _output = output_path

    level = logging.DEBUG if _verbose else logging.INFO
    logger = setup_logger(__name__, level)

    try:
        text = convert_pdf_to_text(_input, _output)
        if not _output and text:
            # 输出到标准输出
            sys.stdout.write(text)
    except FileNotFoundError as e:
        logger.error(e)
        sys.exit(1)
    except Exception as e:
        logger.error(f"PDF 转换失败：{e}")
        sys.exit(1)

if __name__ == "__main__":
    input_path = "assets\\temp\\Claude Haiku 4.5 System Card.pdf"
    output_path = input_path.replace(' ', '_').replace('.pdf', '.txt')
    main(input_path, output_path, True)
