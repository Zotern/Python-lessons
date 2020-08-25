import sys

# import parser

# parser.py
# 1. текущая директория скрипта, откуда импорт
# 2. пути в переменной PYTHONPATH
# 3. системные библиотеки


def print_list(parser_module):
    l = parser_module.input_list("строки")
    print(l)


def import_module_in_function():
    import parser
    l = parser.input_list("строки")
    print(l)


# print(sys.modules)
# import_module_in_function()
# print(sys.modules)
# import_module_in_function()

# print_list(parser)

for p in sys.path:
    print(p)


# print(sys.path)
# print(sys.modules)

