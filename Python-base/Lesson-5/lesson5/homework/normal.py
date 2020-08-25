import re
import random

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'


def split_by_upper_case_re(s):
    return re.split(r'[A-Z]+', s)


def split_by_upper_case_loop(s):
    result = []
    j = -1  # -1 будет особым значением
    for i, c in enumerate(s):
        if c.islower():
            if j == -1:
                # первый раз встретили маленькую букву, запомним позицию
                j = i
        elif c.isupper():
            if j != -1:
                # до этого, маленькие буквы встречались, надо добавить интервал в результат
                result.append(s[j:i])
                # сбросили наш счетчик
                j = -1
        else:
            # любой непонятный символ сбрасываем
            j = -1

    if j != -1:
        # в хвосте были маленькие буквы, надо их сохранить
        result.append(s[j:])
    return result


print("Задание 1: A", split_by_upper_case_re(line))
print("Задание 1: B", split_by_upper_case_loop(line))


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'


def find_substr_re(s):
    """Ищет подстроки удовлетворяющие след. правилам задачи."""
    return re.findall('[a-z]{2}([A-Z]+)[A-Z]{2}', s)


def find_substr_loop(s):
    """Ищет подстроку используя циклы."""

    result = []
    # конечный автомат, текущее состояние
    # 0 - начальное состоения, ждем маленькую букву
    # 1 - ждем вторую маленькую букву
    # 2 - ждем большую букву
    # 3 - ждем вторую большую букву
    # 4 - ждем, третью большую букву
    # 5 - ждем, любой символ, который является не большой буквой
    # правила перехода
    # 0 -> 1
    # 1 -> 2, 0,
    # 2 -> 3, 0,
    # 3 -> 4, 0,
    # 4 -> 5, 0,
    state = 0

    j = -1
    for i, c in enumerate(s):
        if 0 == state:
            if c.islower():
                state = 1
        elif 1 == state:
            if c.islower():
                state = 2
            else:
                state = 0
        elif 2 == state:
            if c.isupper():
                # большая буква, ждем следующую
                j = i
                state = 3
            elif not c.islower():
                # не понятный символ, начнем сначала
                state = 0
        elif 3 == state:
            if c.isupper():
                state = 4
            elif c.islower():
                state = 1
            else:
                state = 0
        elif 4 == state:
            if c.isupper():
                state = 5
            elif c.islower():
                state = 1
            else:
                state = 0
        elif 5 == state:
            if not c.isupper():
                # i-2 потому что нужно убрать 2 большие буквы с конца
                result.append(s[j:i-2])
            if c.islower():
                state = 1
    return result


print("Задание 2: А", find_substr_re(line_2))
print("Задание 2: B", find_substr_loop(line_2))

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


def max_subsequence(s):
    """Возвращает самую длинную подпоследовательность с одинаковыми цифрами.

    Note: s должен быть не пустым
    """

    # тут будем хранить максимальный интервал
    max_range = (0, 0)

    j = 0
    # предыдущий элемент
    p = None
    for i, c in enumerate(s):
        if c != p:
            p = c
            if (i - j) > (max_range[1] - max_range[0]):
                max_range = j, i
            j = i
    return s[max_range[0]:max_range[1]]


with open("data.txt", "w", encoding='UTF-8') as f:
    # получаем сразу по 10 цифр, тогда надо будет сделать только 250 вызовов randint, которые довольно такие дорогие
    for _ in range(250):
        f.write(str(random.randint(1000000000, 9999999999)))

    # f.write(random.randint(1, 9))
    # for _ in range(2499):
    #     f.write(str(random.randint(0, 9)))

with open("data.txt", "r", encoding='UTF-8') as f:
    data = f.read()

print("Самая длинная последовательность одинаковых цифр в файле:",
      max_subsequence(data))
