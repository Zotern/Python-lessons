"""
В этом модуле собраны полезные функции для работы с файлами и директориями
"""

import os
import shutil


def get_file_full_path(filename):
    """Проверяет что путь указыает на файл и возвращает полный путь."""
    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(filepath):
        raise ValueError("Пожалуйста укажите файл")
    return filepath


def make_dir(dir_name):
    """Создает новую папку в текущей директории."""
    os.mkdir(os.path.join(os.getcwd(), dir_name))


def copy_file(file_name):
    """Копирует файл в текущюю директорию."""

    filepath = get_file_full_path(file_name)
    shutil.copyfile(filepath, f"{filepath}.copy")


def remove_file(file_name):
    """Удаляет файл в текущей директории"""
    os.remove(get_file_full_path(file_name))


def remove_dir(dir_name):
    """Удаляет папку относительно текущей директории"""
    os.rmdir(dir_name)


def chdir(dir_name):
    """Переключает текущую директорию."""
    os.chdir(dir_name)
    curdir()


def curdir():
    print(os.getcwd())


def lsdir(dirname):
    """Вывести содержимое директории."""
    for f in os.listdir(dirname):
        print(f)


def invoke_command(f, *args):
    """Вызывает комманду, в случае успеха возвщает True, иначе пе"""
    try:
        f(*args)
    except ValueError as e:
        return f"Ошибка в аргументе комманды: {e}"
    except FileExistsError:
        return "Такой файл уже существует, выберите другое имя"
    except FileNotFoundError:
        return "Файл не найден, проверьте правильность пути"
    except OSError as e:
        return f"Во время выполнения комманды произошла системная ошибка: {e}"
