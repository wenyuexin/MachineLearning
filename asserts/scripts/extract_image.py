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
    - 支持配置 IMAGES_DIR 指定图片保存目录（默认为文档目录下的 image 子目录）
    - 支持配置 INCLUDE_FILES 指定处理的文件
    - 支持配置 SKIP_FILES 跳过指定文件
    - 已处理的文件（包含本地图片引用）会自动跳过
    - 下载失败时保留原始远程链接

使用：
    1. 修改配置参数 DOCS_DIR 和 IMAGES_DIR
    2. 运行: python extract_image.py
"""
import os
import re
import uuid
import requests
from pathlib import Path
from urllib.parse import urlparse


# ==================== 配置参数 ====================

# 文档目录：指定要遍历的 markdown 文件所在目录，或单个 md 文件路径
# 支持绝对路径或相对路径（相对于脚本所在位置）
# 示例：
#   - 目录：DOCS_DIR = '../../supervised_learning' 或 DOCS_DIR = '../../reinforce_learning'
#   - 单文件：DOCS_DIR = '../../README.md' 或 DOCS_DIR = '../../reinforce_learning/学习路线.md'
DOCS_DIR = '../../README.md'

# 图片目录：指定下载图片的保存位置
# 支持绝对路径或相对路径
# 如果为空字符串，则默认设置为 DOCS_DIR 下的 image 子目录
# 示例：IMAGES_DIR = '../../asserts/images'
#   或 IMAGES_DIR = '../../supervised_learning/dpo/image'
IMAGES_DIR = '../../asserts/images'

# 只处理指定的文件列表
# 支持三种格式：
#   - 文件名：'学习路线.md'
#   - 相对路径：'reinforce_learning/学习路线.md'
#   - 绝对路径：'/Users/xxx/MachineLearning/README.md'
# 设为 None 或空列表表示处理所有文件
# 示例：INCLUDE_FILES = ['README.md', 'reinforce_learning/学习路线.md']
INCLUDE_FILES = []

# 跳过的文件列表
# 支持格式同上，设为 None 或空列表表示不跳过任何文件
# 示例：SKIP_FILES = ['README.md', 'reinforce_learning/学习路线.md']
SKIP_FILES = []

# ==================== 配置结束 ====================


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


def main():
    """
    主函数：遍历指定目录下的所有 md 文件或处理单个文件
    """
    # 获取脚本所在目录，用于解析相对路径
    script_dir = Path(__file__).parent

    # 解析文档目录
    if DOCS_DIR:
        docs_path = Path(DOCS_DIR)
        if not docs_path.is_absolute():
            docs_path = script_dir / docs_path
    else:
        # 默认使用脚本所在目录的祖父目录（保持向后兼容）
        docs_path = script_dir.parent.parent

    docs_path = docs_path.resolve()

    # 检查 DOCS_DIR 是否指向单个 md 文件
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
    if IMAGES_DIR:
        image_dir = Path(IMAGES_DIR)
        if not image_dir.is_absolute():
            image_dir = script_dir / image_dir
    else:
        # 如果为空，默认设置为文档目录下的 image 子目录
        image_dir = actual_docs_dir / 'image'

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
    if INCLUDE_FILES:
        # 只处理指定的文件（支持多种路径格式）
        include_names = {normalize_file_path(f, actual_docs_dir)
                         for f in INCLUDE_FILES}
        md_files = [f for f in all_md_files if f.name in include_names]
        print(f"Include files: {INCLUDE_FILES}")
    else:
        md_files = all_md_files

    # 跳过指定的文件
    if SKIP_FILES:
        # 支持多种路径格式
        skip_names = {normalize_file_path(f, actual_docs_dir)
                      for f in SKIP_FILES}
        md_files = [f for f in md_files if f.name not in skip_names]
        print(f"Skip files: {SKIP_FILES}")

    print(f"Files to process: {len(md_files)}")

    # 确保 image 目录存在
    image_dir.mkdir(parents=True, exist_ok=True)

    # 处理每个文件
    for md_path in md_files:
        process_markdown_file(md_path, image_dir, actual_docs_dir)

    print("\nDone!")
    

if __name__ == '__main__':
    main()