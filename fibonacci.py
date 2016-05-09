''' Goal: write program for fibonacci series

'''

def fib(n):
    a,b = 0,1

    while b<n:
        print(b, end=',')
        a, b = b, a+b

def test_num():

    x = int(input("Please enter a number"))

    if x < 0:
        x=0
        print('Negative changed to zero')
    elif x == 0:
        print('zero')
    elif x == 1:
        print('Single')
    else:
        print('more')


def prime():
       n = int(input("Please enter a number"))

       for x in range(2,n):
           for y in range(2,x):
               if(x % y == 0):
                   print(x,' equals ', y, ' * ',x//y)
                   break
           else:
                print(x, 'is a prime number')

def numtype():
    for num in range(2,10):
        if num % 2 == 0:
            print("Found an even number",num)
        else:
            print("Found an odd number",num)


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


                
    
