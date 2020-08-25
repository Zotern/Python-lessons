import itertools
import random

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:

matrix = [
    [1, 0, 8],
    [3, 4, 1],
    [0, 4, 2]
]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку

matrix_transpose = [list(x) for x in zip(*matrix)]
print("matrix transpose: ", matrix_transpose)


# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
# number = """
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450"""
#
# number = number.replace("\n", "")

def max_subsequence(s, seq_len=5):
    """
    Поиск наибольшего произведения пяти последовательных цифр в последовательности
    :return: индекс и произвение
    """

    # поскольку у нас все числа > 0, тогда мы можем сначала найти максимальную сумму
    # произведение найдем позже

    # c суммой поступим следующим образом:
    # найдем сумму первых 5 чисел, и если у нас 6 число больше чем первое то сумма с 1 по 6 будет больше
    # соотвественно и произведение будет больше, далее смотрем 7 и 2 и т.д

    # ord('9') - ord('0') == 9
    zero_code = ord('0')

    def num(c):
        # небольшая оптимизация, вместо конвертации оперируем с ascii кодами
        return ord(c) - zero_code

    # считаем сумму первых 5 элементов
    max_sum = 0
    for i in range(seq_len):
        max_sum += num(s[i])

    max_start = 0
    current_sum = max_sum
    # не используем срезы, поскольку они приводят к копированию памяти
    # f(n) = f(n) + f(n-6)
    for i in range(seq_len, len(s)):
        current_sum += num(s[i]) - num(s[i - seq_len])
        # можем сравнивать как символы, поскольку '9' максимальный, а '0' минимальный
        if current_sum > max_sum:
            max_start = i - seq_len
            max_sum = current_sum

    # найдем произведение
    m = 1
    for i in range(max_start, max_start + seq_len):
        m *= num(s[i])

    return max_start, m


def generate_number(digits_count):
    return ''.join(str(random.randint(1000000000, 9999999999)) for _ in range(digits_count // 10))


print("Ответ Задание2: смещение {}, произведение {}".format(*max_subsequence(generate_number(1000))))

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


def is_queens_disposition_safe(queens):
    """
    Проверяет, что при указанной растановке ферзи не бьют друг - друга
    :param queens: список из восеми пар чисел
    """
    for _, queen in enumerate(itertools.combinations(queens, 2)):
        if queen[0][0] == queen[1][0] or \
                queen[0][1] == queen[1][1] or \
                abs(queen[0][0] - queen[1][0]) == abs(queen[0][1] - queen[1][1]):
            return False

    return True


dispositions = [
    [[1, 4], [2, 7], [3, 3], [4, 8], [5, 2], [6, 5], [7, 1], [8, 6]],
    [[1, 4], [2, 7], [3, 3], [4, 8], [5, 2], [6, 5], [7, 1], [8, 4]],
    [[1, 4], [2, 7], [3, 3], [4, 8], [5, 8], [6, 5], [7, 1], [8, 6]],
]

for disposition in dispositions:
    print("{} - is {}".format(disposition, ("not safe", "safe")[is_queens_disposition_safe(disposition)]))