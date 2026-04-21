# !/usr/bin/env python3
# -*- coding: utf-8 -*-  
"""
Markdown 本地图片迁移工具

功能：
    1. 遍历指定文档或目录下的所有 md 文件
    2. 检测引用了项目根目录下 assets/images 目录中的本地图片
    3. 将图片复制到文档同层级的 images 目录或指定目录的 images 子目录
    4. 更新 md 文件中的图片引用路径
    5. 所有文件处理完成后，删除 assets/images 中已迁移的图片

特性：
    - 支持单文件模式或目录模式
    - 自动检测图片引用（支持相对路径和绝对路径形式）
    - 图片复制后自动更新引用路径
    - 批量处理完成后统一删除源图片

使用：
    1. 修改配置参数 DOCS_DIR
    2. 运行: python migrate_images.py
"""
import os
import re
import shutil
from pathlib import Path
from typing import Set, Dict


# ==================== 配置参数 ====================

# 文档目录：指定要遍历的 markdown 文件所在目录，或单个 md 文件路径
# 支持绝对路径或相对路径（相对于脚本所在位置）
# 示例：
#   - 目录：DOCS_DIR = '../../agent'
#   - 单文件：DOCS_DIR = '../../README.md'
DOCS_DIR = 'embodied_intelligence/papers'

# 源图片目录：项目根目录下的图片存储目录
# 默认为 assets/images
SOURCE_IMAGES_DIR = '../../assets/images'

# 是否在处理完成后删除源图片
# 设为 False 可以只复制不删除，便于检查
DELETE_SOURCE_AFTER_MIGRATE = True

# 跳过的文件列表
# 支持文件名、相对路径、绝对路径
# 示例：SKIP_FILES = ['README.md', 'agent/overview.md']
SKIP_FILES = []

# ==================== 配置结束 ====================


def get_project_root() -> Path:
    """
    获取项目根目录（假设 assets 目录在项目根目录下）
    """
    script_dir = Path(__file__).parent
    return script_dir.parent.parent


def normalize_file_path(file_path: str, base_dir: Path) -> str:
    """
    将文件路径标准化为文件名
    支持三种格式：文件名、相对路径、绝对路径
    """
    path = Path(file_path)
    if path.is_absolute():
        return path.name
    if len(path.parts) > 1:
        return path.name
    return str(path)


def find_referenced_local_images(content: str, md_path: Path, source_image_dir: Path) -> Dict[str, str]:
    """
    从 markdown 内容中找出引用了源图片目录的本地图片
    
    返回：{原始引用路径: 图片文件名} 的字典
    """
    referenced = {}
    
    # 匹配 markdown 图片语法：![alt](path)
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    for match in re.finditer(pattern, content):
        image_path = match.group(2)
        
        # 跳过网络图片
        if image_path.startswith('http://') or image_path.startswith('https://'):
            continue
        
        # 解析图片的实际路径
        try:
            if image_path.startswith('/'):
                # 绝对路径（从项目根目录开始）
                actual_path = get_project_root() / image_path.lstrip('/')
            else:
                # 相对路径（从 md 文件所在目录开始）
                actual_path = (md_path.parent / image_path).resolve()
            
            actual_path = actual_path.resolve()
            
            # 检查图片是否在源图片目录中
            try:
                relative_to_source = actual_path.relative_to(source_image_dir)
                # 这是一个在源目录中的图片
                referenced[match.group(0)] = actual_path.name
            except ValueError:
                # 图片不在源目录中，跳过
                pass
        except Exception as e:
            print(f"  Warning: Failed to resolve path '{image_path}': {e}")
            continue
    
    return referenced


def get_target_image_dir(md_path: Path, docs_dir: Path) -> Path:
    """
    获取目标图片目录
    - 如果处理单个文件：在文件同层级创建 images 目录
    - 如果处理目录：在文档所在层级创建 images 目录
    """
    return md_path.parent / 'images'


def get_relative_image_path(md_path: Path, image_filename: str) -> str:
    """
    计算从 md 文件到目标图片的相对路径
    """
    target_dir = get_target_image_dir(md_path, None)
    
    # 计算从 md 文件到 images 目录的相对路径
    rel_dir = os.path.relpath(target_dir, md_path.parent)
    
    # 确保路径格式正确
    if not rel_dir.startswith('.'):
        rel_dir = './' + rel_dir
    
    return f"{rel_dir}/{image_filename}"


def process_markdown_file(
    md_path: Path, 
    source_image_dir: Path,
    copied_images: Set[str]
) -> bool:
    """
    处理单个 markdown 文件
    复制引用的本地图片并更新引用路径
    
    返回：文件是否被修改
    """
    print(f"\nProcessing: {md_path}")
    
    # 读取文件内容
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找出引用了源图片目录的图片
    referenced = find_referenced_local_images(content, md_path, source_image_dir)
    
    if not referenced:
        print("  No local images from assets/images found")
        return False
    
    print(f"  Found {len(referenced)} local image(s) to migrate")
    
    # 获取目标图片目录
    target_image_dir = get_target_image_dir(md_path, None)
    
    # 确保目标目录存在
    target_image_dir.mkdir(parents=True, exist_ok=True)
    
    # 记录修改
    modified = False
    new_content = content
    
    # 处理每个图片引用
    for original_ref, image_filename in referenced.items():
        source_image_path = source_image_dir / image_filename
        
        # 检查源图片是否存在
        if not source_image_path.exists():
            print(f"  Warning: Source image not found: {image_filename}")
            continue
        
        # 复制图片到目标目录
        target_image_path = target_image_dir / image_filename
        
        if target_image_path.exists():
            print(f"  Image already exists, skipping copy: {image_filename}")
        else:
            shutil.copy2(source_image_path, target_image_path)
            print(f"  Copied: {image_filename} -> {target_image_path}")
        
        # 记录已复制的图片
        copied_images.add(image_filename)
        
        # 更新引用路径
        # 从原始引用中提取 ![alt](path) 格式
        match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', original_ref)
        if match:
            alt_text = match.group(1)
            new_image_path = get_relative_image_path(md_path, image_filename)
            new_ref = f'![{alt_text}]({new_image_path})'
            new_content = new_content.replace(original_ref, new_ref)
            modified = True
            print(f"  Updated reference: {image_filename}")
    
    # 如果有修改，重写文件
    if modified:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  File updated: {md_path}")
    
    return modified


def main():
    """
    主函数
    """
    # 获取脚本所在目录
    script_dir = Path(__file__).parent
    
    # 解析文档路径
    project_root = get_project_root()
    if DOCS_DIR:
        docs_path = Path(DOCS_DIR)
        if not docs_path.is_absolute():
            # 相对路径相对于项目根目录
            docs_path = project_root / docs_path
    else:
        docs_path = project_root
    
    docs_path = docs_path.resolve()
    
    # 解析源图片目录
    source_image_dir = Path(SOURCE_IMAGES_DIR)
    if not source_image_dir.is_absolute():
        source_image_dir = script_dir / source_image_dir
    source_image_dir = source_image_dir.resolve()
    
    # 检查路径是否存在
    single_file_mode = docs_path.is_file() and docs_path.suffix == '.md'
    
    if single_file_mode:
        if not docs_path.exists():
            print(f"Error: File does not exist: {docs_path}")
            return
        actual_docs_dir = docs_path.parent
    else:
        if not docs_path.exists():
            print(f"Error: Directory does not exist: {docs_path}")
            return
        actual_docs_dir = docs_path
    
    if not source_image_dir.exists():
        print(f"Error: Source image directory does not exist: {source_image_dir}")
        return
    
    # 打印信息
    if single_file_mode:
        print(f"Single file mode: {docs_path}")
    else:
        print(f"Docs directory: {docs_path}")
    print(f"Source image directory: {source_image_dir}")
    print(f"Delete source after migrate: {DELETE_SOURCE_AFTER_MIGRATE}")
    
    # 获取要处理的 md 文件列表
    if single_file_mode:
        all_md_files = [docs_path]
    else:
        all_md_files = list(docs_path.rglob('*.md'))
    
    # 应用跳过列表
    if SKIP_FILES:
        skip_names = {normalize_file_path(f, actual_docs_dir) for f in SKIP_FILES}
        md_files = [f for f in all_md_files if f.name not in skip_names]
        print(f"Skip files: {SKIP_FILES}")
    else:
        md_files = all_md_files
    
    print(f"Files to process: {len(md_files)}")
    
    # 记录已复制的图片
    copied_images: Set[str] = set()
    
    # 处理每个文件
    modified_count = 0
    for md_path in md_files:
        if process_markdown_file(md_path, source_image_dir, copied_images):
            modified_count += 1
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Files processed: {len(md_files)}")
    print(f"  Files modified: {modified_count}")
    print(f"  Images migrated: {len(copied_images)}")
    
    # 删除源图片
    if DELETE_SOURCE_AFTER_MIGRATE and copied_images:
        print(f"\nDeleting source images from {source_image_dir}:")
        for image_name in sorted(copied_images):
            source_path = source_image_dir / image_name
            if source_path.exists():
                source_path.unlink()
                print(f"  Deleted: {image_name}")
        print(f"  Total deleted: {len(copied_images)}")
    
    print("\nDone!")


if __name__ == '__main__':
    main()