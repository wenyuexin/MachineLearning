# !/usr/bin/env python3
# -*- coding: utf-8 -*-  
"""
Markdown 远程图片提取工具

功能：
    1. 遍历指定目录及其子目录下的所有 md 文件
    2. 提取 markdown 中的远程图片链接（http/https）
    3. 下载图片到指定目录，文件名使用 UUID
    4. 更新 md 文件中的图片引用为本地相对路径

特性：
    - 支持配置 DOCS_DIR 指定文档目录
    - 支持配置 IMAGES_DIR 指定图片保存目录（默认为文档目录下的 images 子目录）
    - 支持配置 INCLUDE_FILES 指定处理的文件
    - 支持配置 SKIP_FILES 跳过指定文件
    - 已处理的文件（包含本地图片引用）会自动跳过
    - 下载失败时保留原始远程链接

使用：
    命令行模式：
        python extract_image.py [<path>] [--images_dir <path>] [--include <file1> <file2>] [--skip <file1> <file2>]

    代码调用模式：
        main(docs_dir='../../README.md', images_dir='../../asserts/images', include_files=['file.md'])
"""
import os
import re
import uuid
import requests
import argparse
from pathlib import Path
from urllib.parse import urlparse


def download_image(url: str, save_dir: Path) -> str:
    """
    下载图片并保存到本地
    返回本地文件名（包含扩展名）
    """
    try:
        # 发送请求下载图片
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # 确定文件扩展名
        ext = '.png'  # 默认扩展名
        
        # 从 Content-Type 获取扩展名
        content_type = response.headers.get('Content-Type', '')
        if 'jpeg' in content_type or 'jpg' in content_type:
            ext = '.jpg'
        elif 'png' in content_type:
            ext = '.png'
        elif 'gif' in content_type:
            ext = '.gif'
        elif 'webp' in content_type:
            ext = '.webp'
        elif 'svg' in content_type:
            ext = '.svg'
        else:
            # 尝试从 URL 获取扩展名
            parsed_url = urlparse(url)
            path = parsed_url.path
            # 移除查询参数中的特殊字符
            path = path.split('?')[0]
            path = path.split('#')[0]
            
            if path.endswith('.jpg') or path.endswith('.jpeg'):
                ext = '.jpg'
            elif path.endswith('.png'):
                ext = '.png'
            elif path.endswith('.gif'):
                ext = '.gif'
            elif path.endswith('.webp'):
                ext = '.webp'
            elif path.endswith('.svg'):
                ext = '.svg'
        
        # 生成 UUID 文件名
        filename = f"{uuid.uuid4()}{ext}"
        filepath = save_dir / filename
        
        # 保存图片
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded: {url} -> {filename}")
        return filename
        
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None


def get_relative_path(from_file: Path, to_dir: Path) -> str:
    """
    计算从文件到目标目录的相对路径
    """
    # 获取文件所在目录
    from_dir = from_file.parent
    # 计算相对路径
    rel_path = os.path.relpath(to_dir, from_dir)
    # 确保路径以 ./ 开头（如果是同级目录）
    if not rel_path.startswith('.'):
        rel_path = './' + rel_path
    return rel_path


def process_markdown_file(md_path: Path, image_dir: Path, docs_dir: Path) -> None:
    """
    处理单个 markdown 文件
    下载其中的远程图片并更新引用
    """
    print(f"\nProcessing: {md_path}")

    # 读取文件内容
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配远程图片链接的正则表达式
    # 格式: ![alt](http://... 或 https://...)
    # 注意：已经指向本地的图片路径不会被匹配
    pattern = r'!\[([^\]]*)\]\((https?://[^)]+)\)'

    # 计算从 md 文件到图片目录的相对路径
    rel_image_dir = get_relative_path(md_path, image_dir)

    # 检查是否已经有本地图片引用（指向配置的 IMAGES_DIR）
    # 使用动态匹配，避免重复处理
    local_pattern = re.escape(rel_image_dir) + r'/[^)]+'
    if re.search(local_pattern, content):
        print(f"  Warning: File already contains local image references")
        print(f"  Skipping to avoid duplicate downloads")
        return

    # 记录是否需要更新文件
    modified = False

    def replace_image(match):
        nonlocal modified
        alt_text = match.group(1)
        url = match.group(2)

        # 下载图片
        filename = download_image(url, image_dir)

        if filename:
            modified = True
            # 返回新的本地引用路径（使用相对路径）
            return f'![{alt_text}]({rel_image_dir}/{filename})'
        else:
            # 下载失败，保留原链接
            return match.group(0)

    # 替换所有匹配的图片链接
    new_content = re.sub(pattern, replace_image, content)

    # 如果有修改，重写文件
    if modified:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {md_path}")


def normalize_file_path(file_path: str, base_dir: Path) -> str:
    """
    将文件路径标准化为文件名
    支持三种格式：
    - 文件名：'计算机网络.md'
    - 相对路径：'interview/计算机网络.md'
    - 绝对路径：'/Users/xxx/CodeBook/interview/计算机网络.md'
    """
    path = Path(file_path)
    
    # 绝对路径：直接取文件名
    if path.is_absolute():
        return path.name
    
    # 相对路径包含目录：取文件名
    if len(path.parts) > 1:
        return path.name
    
    # 纯文件名：直接返回
    return str(path)


def main(docs_dir=None, images_dir=None, include_files=None, skip_files=None):
    """
    主函数：遍历指定目录下的所有 md 文件或处理单个文件
    
    参数：
        docs_dir: 文档目录路径或单个 md 文件路径，支持绝对路径或相对路径
        images_dir: 图片保存目录路径，支持绝对路径或相对路径。若为 None，则使用 docs_dir 下的 images 子目录
        include_files: 只处理的文件列表，支持文件名、相对路径或绝对路径。若为 None 或空列表，处理所有文件
        skip_files: 跳过的文件列表，格式同 include_files。若为 None 或空列表，不跳过任何文件
    """
    # 如果没有传递参数，使用 argparse 解析命令行
    if docs_dir is None:
        parser = argparse.ArgumentParser(
            description="Markdown 远程图片提取工具：下载远程图片并更新本地引用"
        )
        parser.add_argument(
            "docs_dir", nargs="?", metavar="PATH",
            help="文档目录路径或单个 md 文件路径"
        )
        parser.add_argument(
            "--docs_dir", "-d", dest="docs_dir_opt",
            help="文档目录路径或单个 md 文件路径"
        )
        parser.add_argument(
            "--images_dir", "-i",
            help="图片保存目录路径（默认为文档目录下的 images 子目录）"
        )
        parser.add_argument(
            "--include", "-n",
            nargs="*",
            help="只处理的文件列表"
        )
        parser.add_argument(
            "--skip", "-s",
            nargs="*",
            help="跳过的文件列表"
        )
        args = parser.parse_args()
        _docs_dir = args.docs_dir or args.docs_dir_opt
        _images_dir = args.images_dir
        _include_files = args.include
        _skip_files = args.skip
    else:
        _docs_dir = docs_dir
        _images_dir = images_dir
        _include_files = include_files
        _skip_files = skip_files

    # 获取脚本所在目录，用于解析相对路径
    script_dir = Path(__file__).parent

    # 解析文档目录
    if _docs_dir:
        docs_path = Path(_docs_dir)
        if not docs_path.is_absolute():
            docs_path = script_dir / docs_path
    else:
        # 默认使用脚本所在目录的祖父目录
        docs_path = script_dir.parent.parent

    docs_path = docs_path.resolve()

    # 检查 docs_path 是否指向单个 md 文件
    single_file_mode = docs_path.is_file() and docs_path.suffix == '.md'

    if single_file_mode:
        # 单文件模式：使用文件所在目录作为 docs_dir
        actual_docs_dir = docs_path.parent
        if not docs_path.exists():
            print(f"Error: File does not exist: {docs_path}")
            return
    else:
        # 目录模式
        actual_docs_dir = docs_path
        if not docs_path.exists():
            print(f"Error: Docs directory does not exist: {docs_path}")
            return

    # 解析图片目录
    if _images_dir:
        image_dir = Path(_images_dir)
        if not image_dir.is_absolute():
            image_dir = script_dir / image_dir
    else:
        # 如果为空，默认设置为文档目录下的 images 子目录
        image_dir = actual_docs_dir / 'images'

    image_dir = image_dir.resolve()

    if single_file_mode:
        print(f"Single file mode: {docs_path}")
        print(f"Docs directory: {actual_docs_dir}")
    else:
        print(f"Docs directory: {docs_path}")
    print(f"Image directory: {image_dir}")

    # 获取要处理的 md 文件列表
    if single_file_mode:
        all_md_files = [docs_path]
    else:
        # 递归查找所有子目录下的 md 文件
        all_md_files = list(docs_path.rglob('*.md'))

    # 根据配置筛选文件
    if _include_files:
        # 只处理指定的文件（支持多种路径格式）
        include_names = {normalize_file_path(f, actual_docs_dir)
                         for f in _include_files}
        md_files = [f for f in all_md_files if f.name in include_names]
        print(f"Include files: {_include_files}")
    else:
        md_files = all_md_files

    # 跳过指定的文件
    if _skip_files:
        # 支持多种路径格式
        skip_names = {normalize_file_path(f, actual_docs_dir)
                      for f in _skip_files}
        md_files = [f for f in md_files if f.name not in skip_names]
        print(f"Skip files: {_skip_files}")

    print(f"Files to process: {len(md_files)}")

    # 确保 image 目录存在
    image_dir.mkdir(parents=True, exist_ok=True)

    # 处理每个文件
    for md_path in md_files:
        process_markdown_file(md_path, image_dir, actual_docs_dir)

    print("\nDone!")


if __name__ == '__main__':
    # 示例：通过 hardcode 方式调用
    # main(
    #     docs_dir='../../README.md',
    #     images_dir='../../asserts/images',
    #     include_files=['llm/models/deepseek/DeepSeek_V4_Technical_Report.md'],
    #     skip_files=[]
    # )
    
    # 默认使用命令行参数模式
    main()