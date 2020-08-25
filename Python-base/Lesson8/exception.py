import sys

try:
    raise ValueError
    print("never called")
except ValueError:
    print("catch value error")


class MyValueError(ValueError):
    pass


class MyError(Exception):
    pass


try:
    raise MyError("test")
    print("never called")
except MyError:
    print("catch value error")

try:
    raise MyValueErrorError("test")
    print("never called")
except MyError:
    print("catch value error")
except Exception:
    print("never run")


try:
    raise MyValueError("test")
    print("never called")
except ValueError:
    print("catch value error")
    print(sys.exc_info())


try:
    try:
        raise MyValueError("test")
    except ValueError:
        print(sys.exc_info())
        raise
except Exception as e:
    print(e)
    raise
