import sys

DEFAULT_TYPE = str


def input_list(typename, etype=None):
    """Получить список разделенных запятой."""
    result = input("Введите список %s, разделённых запятыми: " % typename).split(',')
    if etype is not None:
        try:
            result = [etype(x.strip()) for x in result]
        except ValueError:
            print("ошибка ввода.", file=sys.stderr)
            exit(1)

    return result


print("new version")


if __name__ == "__main__":
    print("вы ввели", input_list("числа", int))
