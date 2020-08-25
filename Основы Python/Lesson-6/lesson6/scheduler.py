# student
# teacher
# classroom
# lesson


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
        lesson.add_student(self)

    def display_information(self, lessons):
        """Печатает информацию о студенте"""
        super().display_information()
        print('age:', self.age)
        print("lessons:")
        for l in lessons.lessons_by_student(self):
            print(l)


class Teacher(Person):
    """Класс для сущности преподователь"""
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    def participate(self, lesson):
        """Взять курс для обучения."""
        lesson.teacher = self

    def display_information(self, lessons):
        super().display_information()
        print("lessons:")
        for l in lessons.lessons_by_teacher(self):
            print(l)


class ClassRoom:
    def __init__(self, location, seats):
        self.location = location
        self.seats_num = seats


class Lesson:
    """Описывает понятие Урок."""
    def __init__(self):
        self.name = None
        self.hours = 0
        self.classroom = None
        self._students = []
        self._teacher = None

    def add_student(self, student):
        if len(self._students) < self.classroom.seats_num:
            self._students.append(student)
        else:
            raise ValueError("no seats")

    def has_student(self, student):
        """Проверяет что данный студент записан на курс"""
        return student in self._students

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        if self._teacher is not None:
            raise ValueError("already has teacher")
        self._teacher = teacher

    def __str__(self):
        return f'name:{self.name}; hours:{self.hours}'


class Scheduler:
    def __init__(self):
        self._lessons = {}

    def add_lesson(self, name, hours, classroom):
        python_lesson = Lesson()
        python_lesson.name = name
        python_lesson.hours = hours
        python_lesson.classroom = classroom
        self._lessons[name] = python_lesson

    def get_lesson(self, name):
        try:
            return self._lessons[name]
        except KeyError:
            raise ValueError(f"there is no lesson with name {name}")

    def lessons_by_teacher(self, teacher):
        """Возвращает список курсов, которые ведет указанный преподователь."""
        result = []
        for l in self._lessons.values():
            if l.teacher is teacher:
                result.append(l)
        return result

    def lessons_by_student(self, student):
        """Возвращает список курсов, на которые записан студент."""
        result = []
        for l in self._lessons.values():
            if l.has_student(student):
                result.append(l)
        return result


# Student(*args) ~ Student.__init__(*args)

persons = [
    Student("Ivan", "Ivanov", 16),
    Student("Petr", "Ivanov", 17),
    Teacher("Fedor", "Petrov"),
    Teacher("Boris", "Sergeev"),
]

scheduler = Scheduler()

scheduler.add_lesson("python", 16, ClassRoom("web", 2))

print("Persons:")

for person in persons:
    person.participate(scheduler.get_lesson("python"))

for person in persons:
    person.display_information(scheduler)
