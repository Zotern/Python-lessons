import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_dirs(name, qty=0):
	try:
		if qty > 0:
			for i in range(1, qty + 1):
				os.makedirs(name + str(i))
				print("Папка {} успешно создана".format(name + str(i)))
		else:
			os.makedirs(name)
			print("Папка {} успешно создана".format(name))
	except FileExistsError:
		print("Папка с таким названием уже есть!")


def delete_dirs(name, qty=0):
	try:
		if qty > 0:
			for i in range(1, qty + 1):
				os.rmdir(name + str(i))
				print("Папки {} успешно удалены".format(name + str(i)))
		else:
			os.rmdir(name)
			print("Папка {} успешно удалена".format(name))
	except FileNotFoundError:
		print("Папки с таким названием нет!")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def look_into_folder():
	print(os.listdir())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file(f):
	file = f
	file_copy = 'copy_of_' + f
	shutil.copyfile(file, file_copy)


def del_file(name):
	files = os.listdir('')
	for i in files:
		if i.startswith(name):
			os.remove(i)


def change_folder():
	try:
		os.chdir(input("Выберите папку: "))
		print("Вы успешно перешли в папку ", os.getcwd())
	except FileNotFoundError:
		print("Папки с таким названием нет!")
