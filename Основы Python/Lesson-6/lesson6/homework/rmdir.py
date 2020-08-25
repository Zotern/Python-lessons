"""
Скрипт удаляет папки dir_1 ... dir_9 из текущей директории
"""

import os


if __name__ == '__main__':
    for i in range(1, 10):
        os.rmdir(f"dir_{i}")
