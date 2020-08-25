# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
'''
equation = input("Введите уравнение прямой вида y = kx + b, например:y = -12x + 11111140.2121: ")
x = float(input("Введите значение x: "))
# вычислите и выведите y
split_equation = equation.split(' ')
k = split_equation[2]
k = k.split('x')
k = float(k[0])
b = float(split_equation[4])
y = k * x + b
print(y)
y = k * x - b
print(y)
'''
# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'

date = input("Введите дату в формате dd.mm.yyyy: ")

date = date.split(".")
day = date[0]
month = date[1]
year = int(date[2])

monthes = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "12"]
days = ["01", "02", "03", "04", "05",
		    "06", "07", "08", "09", "10", 
		    "12", "13", "14", "15", "16",
		    "17", "18", "19", "20", "21",
		    "22", "23", "24", "25", "26",
		    "27", "28", "29", "30", "31"]

if day in days and month in monthes and year in range(1, 9999):
	print("Дата введена корректно")
else:
	print("Дата введена не корректно")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

floor = []
rooms = []
n = 1
k = 1

while True:
    room_number = int(input('Введите номер от 1 до 2000000000\n'))

    if 1 <= room_number <= 2000000000:

        while n <= room_number: # не придумал условия лучше, для того чтобы комната точно была в башне
            for i in range(n):
                floor.append(n) # создаем список этажей с количеством комнат для этажа
            n += 1

        for i in range(len(floor)):
            for j in range(1, floor[i] + 1):
                rooms.append(k) # набираем комнаты на этаж
                k += 1

            if room_number in rooms: # проверяем есть ли искомая комната на этаже
                print(i + 1, rooms.index(room_number) + 1)
                break

            rooms = []

        break

    else:
        print('Вы неправильно ввели номер')