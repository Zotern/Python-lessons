"""
Скрипт копирует себя в файл <имя>.copy
"""

import shutil
import sys

this_file = sys.argv[0]
shutil.copyfile(this_file, this_file + ".copy")
