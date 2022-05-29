from sympy import *
import random
from fractions import Fraction


min_x = -5
max_x = 5
N = 2
x, f = symbols('x f')
roots = []
fraction_roots = True
decimal_roots = False
repeat = True

for i in range(N):
    if fraction_roots:
        while True:
            chisl = random.randint(min_x, max_x)
            znam = random.randint(2, max_x)
            if abs(chisl) != znam and chisl:
                root = Fraction(chisl, znam)
                break
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

# print(f'{1}\u00b2')
# print(f'{1}\u00b3')

#1

#3
