'Learn how decorator works in python'


def mark_cool(func):
    func.cool = True
    return func

@mark_cool
def square(x):
    return x ** 2
square = mark_cool(square)

def cube(x):
    return x ** 3

@mark_cool
def collatz(x):
    return 3*x + 1 if x % 2 else x // 2

functions = [square, cube, collatz]
for func in functions:
    if getattr(func, 'cool', False):
        print(func(10), '<--', func.__name__)
        
