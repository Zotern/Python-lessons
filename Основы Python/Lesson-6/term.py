# student
# teacher
# classroom
# lesson

#Обход деревьев, читать

class Person:
	"""Класс для сущности человек"""
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def display_information(self):
		print(self.__class__.__name__)
		print('name:', self.firstname, self.lastname)


class Student(Person):
	"""Класс для сущности студент."""

	def __init__(self, firstname, lastname, age):
		super().__init__(firstname, lastname)
		self.age = age
		self.lessons = set()

	def participate(self, lesson):
		"""присоединится к лекции."""
		self.lessons.add(lesson)

	def display_information(self):
		"""Печатает информацию о студенте."""
		super().display_information()
		print('age:', self.age)
		print('lessons:', ''.join(map(str, sorted(self.lessons))))


class Teacher(Person):
	"""Класс для сущности преподаватель."""
	def __init__(self, firstname, lastname):
		super().__init__(firstname, lastname)
		self.lessons = set()

	def participate(self, lesson):
		"""Взять курс для обучения."""
		self.lessons.add(lesson)
		
	def display_information(self):
		"""Печатает информацию о преподавателе."""
		super().display_information()
		print('lessons:', ''.join(map(str, sorted(self.lessons))))


class ClassRoom:
	"""docstring for ClassRoom"""
	def __init__(self, location, seats):
		self.location = location
		self.seats_num = seats

		
class Lesson:
	"""Класс для сущности урок."""
	def __init__(self):
		self.name = None
		self.hour = 0
		self.classroom = None

	def display_information(self):
		print("Lesson")
		print("name:", self.name)
		print("hours:", self.hours)

	def __str__(self):
		return f'name:{self.name}; hours:{self.hours}'
		#self.display_information()

persons = [
	Student("Ivan", "Ivanov", 16),
	Student("Petr", "Ivanov", 17),
	Teacher("Fedor", "Petrov")
]

python_lesson = Lesson()
python_lesson.name = "Python"
python_lesson.hours = 16
python_lesson.classroom = ClassRoom("online", 60)

for person in persons:
	person.participate(python_lesson)

for person in persons:
	person.display_information()
