"""
Скрипт выводит список папок в текущей директории
"""

import os

if __name__ == '__main__':
    for x in sorted(filter(os.path.isdir, os.listdir(os.curdir))):
        print(x)
