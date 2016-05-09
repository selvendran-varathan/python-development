''' Goal: Create the world's most brief set of notes and quick reference
          for tools useful for expressing tests elagantly
'''


score = 75
ports_in_use = [10, 14, 6, 7, 20]
dead_port = [12, 8, 15, 25]
allowed_ports = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22]

def is_even(x):
    'Predicate return false if x is even'
    return True if x%2==0 else False

#print('pass' if score <= 70 else 'fail')
assert 0 <= score <= 100
