'''Goal: Create the world's most brief set of notes and quick reference
         for tools usefull for expressing tests elegantly
'''

score = 75
ports_in_use = [10, 14, 6, 7, 20]
dead_port = [12, 8, 15, 25]
allowed_ports = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22]


def is_even(x):
    'Predicate return true if x is even'
    return x % 2 == 0

print('pass' if score >= 70 else 'fail')                # Ternary operator or conditional expression
assert  0 <= score <= 100                               # Chained comparisons
assert score > 50 and not is_even(score)                # short-cirtuit "and"
assert score in {55, 65, 75, 85, 95}                    # fast membership test


# Objective: Make sure that none of the ports in use are dead #######################
# Version 1 (worst solution)
overlap = False
for port in ports_in_use:
    if port in dead_port:
        overlap = True

assert not overlap


# version 2: List comprehension reads like English has no flag variable
assert not any([port in dead_port for port in ports_in_use])

# Version 3: Generator Expression which are memory efficient
assert not any((port in dead_port for port in ports_in_use))

# Version 4: Semi high level concept, "interception" runs at C speed, no early-out, and build
assert not set(ports_in_use).intersection(set(dead_port))

# Version 5: (Best Way): Highest level concept
assert set(ports_in_use).isdisjoint(set(dead_port))



