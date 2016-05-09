' Goal : Learn fundamental Python argument passing techniques'

def mypow(base, exp):
    'raise base to the power of exp'
    return base ** exp

print (mypow(2,5))                          # positional argument---> order matters

print(mypow(exp=5, base=2))                 # keyword arguments ---> name matters
            
print (mypow(2, exp=5))                     # hybrid argument ---> positional arguments go before keywords


arguments =(2,5)                            # cheap container, tupples are compact and fast
print(mypow(arguments[0], arguments[1]))    # need to unpack before you make function call


arguments =(2,5)                            # cheap container, tupples are compact and fast
print(mypow(*arguments))    # need to unpack before you make function call


print()

def f(a,b)
    
