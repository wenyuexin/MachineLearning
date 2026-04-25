#!/usr/bin/env python3
"""
日志工具模块

提供统一的日志配置，默认将日志文件保存到 assets/logs 目录下。

用法：
    from logger import setup_logger

    logger = setup_logger(__name__)
    logger.info("这条消息会同时输出到控制台和日志文件")

日志文件默认保存在：<本模块所在目录>/../logs/<调用脚本名>.log
即 assets/logs/pdf_to_text.log、assets/logs/pdf_to_md.log 等
"""

import logging
import sys
from pathlib import Path

# 本模块所在目录（assets/scripts/）的上一级的 logs/（即 assets/logs/）
_LOG_DIR = Path(__file__).resolve().parent.parent / "logs"


def setup_logger(name: str = None, level: int = logging.INFO) -> logging.Logger:
    """
    配置并返回一个同时输出到控制台和文件的 Logger。

    参数：
        name: Logger 名称，通常传 __name__。
        level: 日志级别，默认 INFO。

    返回：
        配置好的 Logger 实例。

    日志文件保存位置：assets/logs/<调用脚本名>.log
    """
    logger = logging.getLogger(name)

    # 避免重复添加 handler（模块被多次导入时）
    if logger.handlers:
        return logger

    logger.setLevel(level)

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    # 控制台 handler
    console = logging.StreamHandler(sys.stderr)
    console.setFormatter(fmt)
    logger.addHandler(console)

    # 文件 handler：保存到 assets/logs/
    _LOG_DIR.mkdir(exist_ok=True)
    caller_stem = Path(sys.argv[0]).stem
    log_file = _LOG_DIR / f"{caller_stem}.log"

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    return logger
