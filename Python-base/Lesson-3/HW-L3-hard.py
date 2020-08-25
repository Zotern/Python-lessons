# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
'''
exp = input("Введите выражение: ")

l = exp.split(' ')
l_n = []
n1 = 0
n2 = 0

for i in l:
	if i.isdigit() == True and len(l) == 5:
		l_n.append(i)
		if len(l_n) == 2:
			n1 = l_n[0]
			n2 = l_n[1]
		else:
			n1 = l_n[0]
	elif i.isdigit() != True:
		if len(l) == 5:
			n1 = l[0]
			n2 = l[3]
			xy1 = l[1].split('/')
			xy2 = l[4].split('/')
			x1 = xy1[0]
			y1 = xy1[1]
			x2 = xy2[0]
			y2 = xy2[1]
		elif len(l) == 3:
			if '/' in l[0] and '/' in l[2]:
				xy1 = l[0].split('/')
				xy2 = l[2].split('/')
				x1 = xy1[0]
				y1 = xy1[1]
				x2 = xy2[0]
				y2 = xy2[1]
			elif '/' in l[0]:
				xy1 = l[0].split('/')
				xy2 = l[2]
				x1 = xy1[0]
				y1 = xy1[1]
				x2 = xy2
				y2 = 1
			elif '/' in l[2]:
				xy2 = l[2].split('/')
				x2 = xy2[0]
				y2 = xy2[1]
				xy1 = l[0]
				x1 = xy1
				y1 = 1
			elif '/' not in l:
				xy1 = l[0]
				xy2 = l[2]
				x1 = xy1
				x2 = xy2
				y1 = 1
				y2 = 1
		elif len(l) == 4:
			if '/' in l[0]:
				xy1 = l[0].split('/')
				xy2 = l[3].split('/')
				n2 = l[2]
				x1 = xy1[0]
				y1 = xy1[1]
				x2 = xy2[0]
				y2 = xy2[1]
			elif '/' in l[1]:
				xy1 = l[1].split('/')
				xy2 = l[3].split('/')
				x1 = xy1[0]
				y1 = xy1[1]
				x2 = xy2[0]
				y2 = xy2[1]
				n1 = l[0]
n1 = int(n1)
n2 = int(n2)
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)


if n1 != 0:
	nmr1 = n1 * y1 + x1
	dnm1 = y1
elif n1 == 0:
	nmr1 = x1
	dnm1 = y1


if n2 != 0:
	nmr2 = n2 *y2 + x2
	dnm2 = y2
elif n2 == 0:
	nmr2 = x2
	dnm2 = y2


if dnm1 != dnm2 and '-' in l:
	numerator = nmr1 * dnm2 - nmr2 * dnm1 
	denominator = dnm1 * dnm2
	print('{} {}/{}'.format(numerator // denominator, numerator % denominator, denominator))
elif dnm1 != dnm2 and '+' in l:
	numerator = nmr1 * dnm2 + nmr2 * dnm1 
	denominator = dnm1 * dnm2
	print('{} {}/{}'.format(numerator // denominator, numerator % denominator, denominator)) 
elif dnm1 == dnm2 and '-' in l:
	numerator = nmr1 - nmr2
	denominator = dnm1
	print('{}/{}'.format(numerator, denominator))
elif dnm1 == dnm2 and '+' in l:
	numerator = nmr1 + nmr2
	denominator = dnm1
	print('{}/{}'.format(numerator, denominator))
'''


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


'''
def split(l, n):
	l[n] = l[n].split(' ')
	while '' in l[n]:
		l[n].remove('')

def cost_of_one_hour(worker):
	return int(dworkers[worker].get('salary')) // int(dworkers[worker].get('watch_rate'))

def difference_watch_rate(worker, dworker):
	return int(dhours[worker].get('actual_watch_rate')) - int(dworkers[dworker].get('watch_rate'))

def act_salary(worker):
	if difference_watch_rate(worker, worker) > 0:
		return (cost_of_one_hour(worker) * 2) * difference_watch_rate(worker, worker) + int(dworkers[worker].get('salary'))
	elif difference_watch_rate(worker, worker) < 0:
		return int(dworkers[worker].get('salary')) + (cost_of_one_hour(worker) * difference_watch_rate(worker, worker))

def write_to_file(worker):
	if worker == 'worker5':
		f.write(dworkers[worker].get('name'))
		f.write('\t')
		f.write(dworkers[worker].get('surname'))
		f.write('\t')
		f.write(str(act_salary(worker)))
		f.write('\n')
	else:
		f.write(dworkers[worker].get('name'))
		f.write('\t')
		f.write(dworkers[worker].get('surname'))
		f.write('\t')
		f.write('\t')
		f.write(str(act_salary(worker)))
		f.write('\n')


with open ('workers.txt', 'r') as f:
	workers = f.read()
	l_workers = workers.split('\n')
	while '' in l_workers:
		l_workers.remove('')
	l_workers = sorted(l_workers)
	split(l_workers, 0)
	split(l_workers, 1)
	split(l_workers, 2)
	split(l_workers, 3)
	split(l_workers, 4)
	split(l_workers, 5)
	split(l_workers, 6)

	dworkers = {'worker1': {'name': l_workers[0][0], 'surname': l_workers[0][1], 'salary': l_workers[0][2], 'watch_rate': l_workers[0][4]},
				'worker2': {'name': l_workers[1][0], 'surname': l_workers[1][1], 'salary': l_workers[1][2], 'watch_rate': l_workers[1][4]},
				'worker3': {'name': l_workers[2][0], 'surname': l_workers[2][1], 'salary': l_workers[2][2], 'watch_rate': l_workers[2][4]},
				'worker4': {'name': l_workers[4][0], 'surname': l_workers[4][1], 'salary': l_workers[4][2], 'watch_rate': l_workers[4][4]},
				'worker5': {'name': l_workers[5][0], 'surname': l_workers[5][1], 'salary': l_workers[5][2], 'watch_rate': l_workers[5][4]},
				'worker6': {'name': l_workers[6][0], 'surname': l_workers[6][1], 'salary': l_workers[6][2], 'watch_rate': l_workers[6][4]} }


with open ('hours_of.txt', 'r') as f:
	hours_of = f.read()
	l_hours = hours_of.split('\n')
	l_hours = sorted(l_hours)
	split(l_hours, 0)
	split(l_hours, 1)
	split(l_hours, 2)
	split(l_hours, 3)
	split(l_hours, 4)
	split(l_hours, 5)
	split(l_hours, 6)

	dhours = {  'worker1': {'name': l_hours[0][0], 'surname': l_hours[0][1], 'actual_watch_rate': l_hours[0][2]},
				'worker2': {'name': l_hours[1][0], 'surname': l_hours[1][1], 'actual_watch_rate': l_hours[1][2]},
				'worker3': {'name': l_hours[2][0], 'surname': l_hours[2][1], 'actual_watch_rate': l_hours[2][2]},
				'worker4': {'name': l_hours[4][0], 'surname': l_hours[4][1], 'actual_watch_rate': l_hours[4][2]},
				'worker5': {'name': l_hours[5][0], 'surname': l_hours[5][1], 'actual_watch_rate': l_hours[5][2]},
				'worker6': {'name': l_hours[6][0], 'surname': l_hours[6][1], 'actual_watch_rate': l_hours[6][2]} }

with open ('salary.txt', 'w') as f:
	f.write(str(l_hours[3][0]))
	f.write('\t')
	f.write(str(l_hours[3][1]))
	f.write('\t')
	f.write('\t')
	f.write(str(l_workers[3][2]))
	f.write('\n')
	write_to_file('worker1')
	write_to_file('worker2')
	write_to_file('worker3')
	write_to_file('worker4')
	write_to_file('worker5')
	write_to_file('worker6')
'''

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_A, fruits_B, fruits_C ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
#print(list(map(chr, range(ord('А'), ord('Я')+1))))

def first_letter_sort(letter):
	"""
	Создаёт список из исходного по первой букве, которая указывается.
	letter - переменная в которую передаётся буква, по которой следует сортировка слов.
	"""
	fruits_by_ltr = []
	for i in fruits:
		if i[0:1] in alphabet:
			if i[0:1] == letter:
				fruits_by_ltr.append(i)

	fruits_by_ltr = set(fruits_by_ltr)
	fruits_by_ltr = list(fruits_by_ltr)
	fruits_by_ltr.sort()
	return fruits_by_ltr


alphabet = list(map(chr, range(ord('А'), ord('Я')+1)))

with open ('fruits.txt', 'r') as f:
	fruits = f.read()
	fruits = fruits.split('\n')
	while '' in fruits:
		fruits.remove('')

for i in fruits:
	if i[0:1] in alphabet:
		with open ('fruits_' + i[0:1] + '.txt', 'w') as f:
			f.write(str(first_letter_sort(i[0:1])))