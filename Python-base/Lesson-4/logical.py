number = 13
if number > 0 and number != 12:
	print("true")

number2 = number != 13 and 15

print(number2)

def calc_sum(iterable, start):
	start = start or 0
	for i in iterable:
		start += i
	return start

print(calc_sum([1, 2, 3], 1))
print(calc_sum([1, 2, 3], None))

#is


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)
print(a == b)
print(a is c)
print(a == c)

s1 = "hello"
s2 = "hello"

print(s1 is s2, s2 == s1)

i1 = 1
i2 = 1

print(i1 is i2, i2 == i1)

t1 = (1, 2)
t2 = (1, 2)

print(t1 is t2, t2 == t1)

n = None

if n is None:
	print("None")

n = 1
if n is not None:
	print("not None")

# if n == None: - не правильно, нужно использовать is.

def plus(a, b=None):
	return a + (b or 0)

def my_filter(f, iterable):
	f = f or bool
	result = []
	for i in iterable:
		if f(i):
			result.append(i)
	return result

def my_filter2(f, iterable):
	f = f or bool
	return [x for x in iterable if f(x)]

def make_index(iterable):
	"""Возвращает словарь где ключем является элемент приведенный к строке"""
	return {str(x): x for x in iterable}

def make_unique_str(iterable):
	"""Возвращает словарь где ключем является элемент приведенный к строке"""
	return {str(x) for x in iterable}

def make_tuple(iterable):
	"""Возвращает словарь где ключем является элемент приведенный к строке"""
	# return (str(x) for x in iterable) # не кортеж!!!
	return tuple(str(x) for x in iterable) # кортеж
