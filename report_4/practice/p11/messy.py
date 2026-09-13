def foo():
    x = 1
    y = 2
    return x + y


def bar():
    unused = 42
    return foo()
