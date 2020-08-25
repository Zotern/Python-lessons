import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
	x = 1
	y = 1
	l = [y, x]

	for i in range(m):
		x = x + y
		y = x - y
		l.append(x)

	return l[n - 1:m]



print(fibonacci(1, 3))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    m = origin_list[0]
    for i in origin_list:
    	if i > m:
    		m = i
    return m

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, i):
	return [i for i in i if func(i) == True]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
a = [1, 2, 3, 4, 5, 6]
print(my_filter(lambda x : x % 2 == 0, a))
print(my_filter(lambda x : x['name'] == 'python', dict_a))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def define_parall_points():
	"""
	Определяем, являются ли данные точки вершинами параллелограмма,
	сравнивая по парно стороны.
	"""
	def side_length(x1, x2, y1, y2):
		"""
		Находим длину стороны
		param: x1, y1 - координаты точки.
		param: x2, y2 - координаты точки.
		"""
		return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

	a1 =  float(input("Введите координаты точки a1: "))
	a2 =  float(input("Введите координаты точки a2: "))
	b1 =  float(input("Введите координаты точки b1: "))
	b2 =  float(input("Введите координаты точки b2: "))
	c1 =  float(input("Введите координаты точки c1: "))
	c2 =  float(input("Введите координаты точки c2: "))
	d1 =  float(input("Введите координаты точки d1: "))
	d2 =  float(input("Введите координаты точки d2: "))

	ab = side_length(b1, a1, b2, a2)
	dc = side_length(c1, d1, c2, d2)
	ad = side_length(d1, a1, d2, a2)
	bc = side_length(c2, b2, c1, b1)

	if ab == dc and bc == ad:
		return("Точки являются вершинами параллелограмма")
	else:
		return("Точки не являются вершинами параллелограмма")

print(define_parall_points())
