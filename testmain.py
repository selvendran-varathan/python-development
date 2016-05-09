
print('My Name is:',__name__)
print('What can I do?\n',__doc__)


if __name__ == '__main__':
    print('I must not have been imported')

import math
print(math.cos(3.0))

def square(x):
    'Return square of x'
    return x*x

print(square(5))

def squares():
    squares1 = []
    s = [10,20,30]
    for x in s:
        squares1.append(square(x))
    print(squares1)
squares()


brands = {
    'tom': 'mac',
    'jenny': 'pc',
    'susan': 'andriod'

}

print(type(brands))
print(len(brands))
print(brands['jenny'])

print(brands.keys())
print(brands.values())
print(brands.items())

class Computer:
    'First Class'

    kind='first class attribute'


    





