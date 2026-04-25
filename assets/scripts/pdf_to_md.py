#!/usr/bin/env python3
"""
PDF 转 Markdown 工具
用法：
    python pdf_to_md.py input.pdf [output.md]
"""

import sys
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Optional, Tuple

from logger import setup_logger

try:
    import pdfplumber
except ImportError:
    print("错误：未安装 pdfplumber，请运行：pip install pdfplumber", file=sys.stderr)
    sys.exit(1)


def is_bold(fontname: str) -> bool:
    """启发式判断字体是否为粗体。"""
    if not fontname:
        return False
    lower = fontname.lower()
    return 'bold' in lower or 'black' in lower or 'heavy' in lower

def classify_line(line_text: str, font_size: float, is_bold_flag: bool, prev_font_size: float) -> Tuple[str, str]:
    """
    根据字号比例和粗体属性判断 Markdown 标题级别。
    返回 (Markdown前缀, 清理后的文本)。
    """
    cleaned = line_text.strip()
    if not cleaned:
        return '', ''

    # 启发式规则：大字号 + 粗体 -> 可能是标题
    if font_size > prev_font_size * 1.2 and is_bold_flag:
        # 超大字号：H1、H2
        if font_size > 20:
            return '# ', cleaned
        elif font_size > 16:
            return '## ', cleaned
        else:
            return '### ', cleaned
    elif is_bold_flag and font_size > 14:
        return '### ', cleaned
    elif is_bold_flag:
        return '#### ', cleaned
    else:
        return '', cleaned  # 普通段落

def parse_table_to_markdown(table: List[List[str]]) -> str:
    """将行列表（字符串列表）转换为 Markdown 表格。"""
    if not table or len(table) < 2:
        return ''

    # 确定列数
    num_cols = max(len(row) for row in table)
    # 将每行列数统一，并将 None 替换为空字符串
    normalized = []
    for row in table:
        norm_row = [(cell if cell is not None else '') for cell in row] + [''] * (num_cols - len(row))
        normalized.append(norm_row)

    # 构建 Markdown 表格
    lines = []
    # 表头行
    header = normalized[0]
    lines.append('| ' + ' | '.join(header) + ' |')
    # 分隔行
    sep = '|' + '|'.join([' --- ' for _ in range(num_cols)]) + '|'
    lines.append(sep)
    # 数据行
    for row in normalized[1:]:
        lines.append('| ' + ' | '.join(row) + ' |')
    return '\n'.join(lines)

def convert_pdf_to_markdown(pdf_path: str, output_path: Optional[str] = None) -> str:
    """
    将 PDF 转换为 Markdown，尽可能保留文档结构。

    参数：
        pdf_path: 输入 PDF 文件路径
        output_path: 可选的输出 Markdown 文件路径。若为 None，则返回 Markdown 字符串。

    返回：
        若 output_path 为 None，返回提取的 Markdown 字符串；否则返回空字符串。

    异常：
        FileNotFoundError: PDF 文件不存在时抛出。
        Exception: 其他 PDF 处理错误。
    """
    pdf_file = Path(pdf_path)
    if not pdf_file.is_file():
        raise FileNotFoundError(f"PDF 文件未找到：{pdf_path}")

    md_lines = []

    logger = logging.getLogger(__name__)

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        logger.info(f"正在处理 {pdf_path}，共 {total_pages} 页")

        for page_num, page in enumerate(pdf.pages, 1):
            if page_num % 5 == 0 or page_num == total_pages:
                logger.debug(f"第 {page_num} / {total_pages} 页")

            # 先提取表格及其位置信息（用于与文本交错排列）
            found_tables = page.find_tables()
            table_bboxes = [(table.bbox, table.extract()) for table in found_tables]

            # 提取字符级详细文本
            chars = page.chars if page.chars else []

            # 按 y 坐标将字符分组为行，用整数取整容差避免同一行被拆分
            lines_map: Dict[int, List[Dict]] = {}
            for char in chars:
                y = round(char['y0'])  # 取整容差，避免微小偏差拆行
                lines_map.setdefault(y, []).append(char)

            # 按从上到下排序行
            # pdfplumber 坐标系：(0,0) 在左上角，y 向下递增，因此 y 越大越靠下
            sorted_y = sorted(lines_map.keys())

            # 对每行构造文本并检测字体属性
            line_data = []
            for y in sorted_y:
                line_chars = lines_map[y]
                if not line_chars:
                    continue
                # 按从左到右排序字符
                line_chars.sort(key=lambda c: c['x0'])
                text = ''.join(c.get('text', '') for c in line_chars if c.get('text'))
                # 获取主导字号和粗体属性
                font_sizes = [c.get('size', 12.0) for c in line_chars]
                avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 12
                is_bold_flag = any(is_bold(c.get('fontname', '')) for c in line_chars)
                line_data.append((y, text, avg_font_size, is_bold_flag))

            # 构建表格条目，记录 y 位置
            table_entries = []
            for bbox, table_data in table_bboxes:
                table_y = round(bbox[1])  # 表格顶部 y 坐标
                md_table = parse_table_to_markdown(table_data)
                if md_table:
                    table_entries.append((table_y, md_table))

            # 将文本行和表格按 y 坐标交错合并
            all_items = []  # [(y, 'text'|'table', content, font_size, bold_flag)]
            for y, text, font_size, bold_flag in line_data:
                all_items.append((y, 'text', text, font_size, bold_flag))
            for y, md_table in table_entries:
                all_items.append((y, 'table', md_table, 0, False))
            all_items.sort(key=lambda item: item[0])

            # 将合并后的项处理为 Markdown 块
            prev_font_size = 12.0
            paragraph_buffer = []

            for y, item_type, content, font_size, bold_flag in all_items:
                if item_type == 'table':
                    # 表格：先刷新段落缓冲区
                    if paragraph_buffer:
                        md_lines.append(' '.join(paragraph_buffer))
                        paragraph_buffer = []
                    md_lines.append('')
                    md_lines.append(content)
                    md_lines.append('')
                    continue

                text = content
                if not text.strip():
                    # 空行：刷新段落缓冲区
                    if paragraph_buffer:
                        md_lines.append(' '.join(paragraph_buffer))
                        paragraph_buffer = []
                    md_lines.append('')  # 空行分隔
                    continue

                prefix, cleaned = classify_line(text, font_size, bold_flag, prev_font_size)
                prev_font_size = font_size

                if prefix:  # 标题
                    if paragraph_buffer:
                        md_lines.append(' '.join(paragraph_buffer))
                        paragraph_buffer = []
                    md_lines.append(f"{prefix}{cleaned}")
                    md_lines.append('')  # 标题后空行
                else:
                    # 普通文本：累积到段落
                    paragraph_buffer.append(cleaned)

            # 刷新剩余段落
            if paragraph_buffer:
                md_lines.append(' '.join(paragraph_buffer))
                md_lines.append('')

            # 添加页面分隔符
            if page_num < len(pdf.pages):
                md_lines.append('')
                md_lines.append('<!-- page break -->')
                md_lines.append('')

    result = '\n'.join(md_lines)

    if output_path:
        out_path = Path(output_path)
        out_path.write_text(result, encoding='utf-8')
        logger.info(f"Markdown 已保存至 {out_path.resolve()}")
        return ''
    else:
        return result

def main(input_path=None, output_path=None, verbose=False):
    if input_path is None:
        parser = argparse.ArgumentParser(
            description="使用 pdfplumber 将 PDF 文件转换为 Markdown"
        )
        parser.add_argument("input", help="输入 PDF 文件路径")
        parser.add_argument("output", nargs="?", help="可选的输出 Markdown 文件路径（若省略则输出到标准输出）")
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
        md = convert_pdf_to_markdown(_input, _output)
        if not _output and md:
            # 输出到标准输出
            sys.stdout.write(md)
    except FileNotFoundError as e:
        logger.error(e)
        sys.exit(1)
    except Exception as e:
        logger.error(f"PDF 转换失败：{e}")
        sys.exit(1)

if __name__ == "__main__":
    input_path = "assets\\temp\\Claude Sonnet 4.5 System Card.pdf"
    output_path = input_path.replace(' ', '_').replace('.pdf', '.md')
    main(input_path, output_path, True)
