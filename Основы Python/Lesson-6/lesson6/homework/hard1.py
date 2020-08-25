# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3


import fileman

import sys

import inspect


def get_arguments_cnt(f):
    """Возвращает кол-во аргументов у функции"""
    # получаем сигнатуру комманды (можно просто запомнить что есть модуль, который позволяет это делать)
    return len(inspect.signature(f).parameters)


def ping():
    print("pong")


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


# комманда - кол-во аргументов
# на самом деле, можно у функции узнать кол-во аргументов
do = {
    "help": print_help,
    "mkdir": fileman.make_dir,
    "ping": ping,
    "cp": fileman.copy_file,
    "rm": fileman.remove_file,
    "cd": fileman.chdir,
    "ls": fileman.curdir
}


def main():
    try:
        # проверяем что пользователь указал правильную комманду
        command = do[sys.argv[1]]
    except (IndexError, KeyError):
        print("пожалуйста укажите комманду, которую надо выполнить")
        print("чтобы узнать список комманд используйте комманду help")
        return 1

    try:
        # параметры комманды начинаютс с индекса 2
        args = [sys.argv[2 + x] for x in range(get_arguments_cnt(command))]
    except IndexError:
        print("Ошибка в параметрах комманды")
        return 1

    msg = fileman.invoke_command(command, *args)
    if msg is not None:
        print(msg)
        return 1
    return 0


if __name__ == '__main__':
    exit(main())
