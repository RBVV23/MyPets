from sympy import *
import random
from fractions import Fraction


# x, f, g, h = symbols('x f g h')
#
# min_x = -10
# max_x = 10


min_x = -5
max_x = 5
N = 2
x, f = symbols('x f')
roots = []
fraction_roots = False
decimal_roots = True
for i in range(N):
    if fraction_roots:
        root = Fraction(random.randint(min_x, max_x), random.randint(1, max_x))
    elif decimal_roots:
        root = random.randint(min_x, max_x) + random.randint(0,10)/10
    else:
        root = random.randint(min_x, max_x)
    roots.append(root)
print(roots)

f = 1
for i in range(N):
    f *= x - roots[i]

print(f)
print(f.expand())

print(f'{1}\u00b2')
print(f'{1}\u00b3')