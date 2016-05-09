''' Goal - Learn how OOP works in Python and how its used in PyATS

Structure of the implementations
--------------------------------

* classes hold **SHARED** information

    1) ''__name__'' a string with the name given at birth
    2) ''__dict__'' 


Namespaces
----------

* globals: ''__name__'', ''__doc__'',''Dog'', ''d'', ''e'', ''f''
* Dog:     ''__name__'', ''__doc__'',''kind''
* instance: ''name''


'''
class Animal:
    'A generic animal class'

    kind='critter'

    def __init__(self,n):
        self.name=n

class Jumper:
    'Mixing class to add jumber capabilities'

    def jump(self):
        print('Weee ! %s is jumping' % self.name)
class Cat(Animal,Jumper):
    'A fenine'
    kind='fenine'
    def talk(self):
        print('Meow! %s is purring' % self.name)
class Dog(Animal):
    'A simple canine class'
    kind = 'canine'
    def talk(self):
        print('Woof! %s is barking' % self.name)

d = Dog('Fido')
e = Dog('Buddy')
f = Dog('Checkers')
g = Cat('Buddy')


pets = [d ,e, f,g]

for pet in pets:
    pet.talk()


