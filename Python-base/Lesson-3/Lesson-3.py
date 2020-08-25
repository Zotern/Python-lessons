def average(*args):
	"""
	:param args: числа
	:return: число, среднее арифмитическое для аргументов
	"""
	return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))

numbers = [1, 2, 3, 4]
numbers2 = list(map(lambda x: x**2, numbers))
numbers3 = list(filter(lambda x: 0 == x % 2, numbers))
numbers4 = list(zip(numbers[::2], numbers[1::2]))

#list(map(lambda x: x**2, numbers)) эквивалентны, то есть равны <=> [x**2 for x in numbers]
#list(filter(lambda x: 0 == x % 2, numbers)) <=> 
#[x for x in numbers if x % 2 == 0]


print("numbers", numbers)
print("numbers2", numbers2)
print("numbers3", numbers3)
print("numbers4", numbers4)

def add_prefix(s, prefix=""):
	"""Добаляет prefix к строке s."""
	return prefix + " " + s

print(add_prefix("hello", "world"))

def say_hello(**kwargs):
	"""Формиирует приветствие используя переменное число аргументов."""
	template = "Hello {first_name} {second_name}"

	kwargs.setdefault("first_name", "unknown")
	kwargs.setdefault("second_name", "unknown")
	return template.format(**kwargs)

print(say_hello(first_name="Ivan", second_name="Petrov"))
print(say_hello(first_name="Dima", second_name="Tolstokhlebov"))

def some_func(*args, **kwargs):
	print(type(args), args)
	print(type(kwargs), kwargs)

some_func(1, 2, p=1, q=2)
some_func()
some_func(q=1)
some_func(1)

def pass_by_value(a):
	"""Пример передачи по значению."""
	a = 2

n = 4
pass_by_value(n)
print(n)

def update_dict(d, **kwargs):
	"""обновляет словарь."""
	d.update(kwargs)

d = {"1": 1}
update_dict(d, a=2, b=3)
print(d)