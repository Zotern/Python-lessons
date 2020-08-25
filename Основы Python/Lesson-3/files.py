with open("text.txt", "wt", encoding="utf-8") as f:
	f.write("hello world")
with open("text.txt", "r") as f:
	print(f.read())

with open("text.txt", "r") as f:
	for line in map(lambda x: x.upper(), f):
		print(line)


# r - для чтения, если файл не существует - ошибка
# w - для записи, если файл существует - перезапишется, не сущетсвует - создан
# a - если сущетсвует, добавит в конец, если нет - создаст файл
# x - существует - ошибка, не существует - создаст

# t - текстовый файл
# b - бинарный файл
