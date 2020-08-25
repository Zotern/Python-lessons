# Patterns - устоявщиеся приёмы кода, которые упрощают разработку кода.
# pattern builder - конструирует объект на основе каких-то данных, какой-то логике
# применятется при чтении данных из файла или базы
# шаблон проектирования
# pattern generator



# Паттерн делегирования

class User:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hi", self.name)


def print_object(o):
    """Печатает объект вызывая метод print"""
    o.print()


class Proxy:
    def __init__(self, u):
        self.u = u

    def __getattr__(self, item):
        return getattr(self.u, item)

    def hello(self):
        print("Hello", self.u.name)

    def print(self):
        self.u.hello()


p = Proxy(User("test"))

try:
    print_object(User(""))
except AttributeError:
    pass

print_object(p)
