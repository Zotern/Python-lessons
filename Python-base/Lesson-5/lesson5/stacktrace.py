def func1():
    import traceback
    stack = traceback.format_stack()
    print('called from ', stack[1])


def func2():
    func1()


def func3():
    func2()


func3()
