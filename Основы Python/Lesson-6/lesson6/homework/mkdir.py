"""
Скрипт создает папки dir_1 ... dir_9 в текущей директории
"""

import os


if __name__ == '__main__':
    for i in range(1, 10):
        os.mkdir(f"dir_{i}")
