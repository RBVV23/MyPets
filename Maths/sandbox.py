from sympy import *
import random


# x, f, g, h = symbols('x f g h')
#
# min_x = -10
# max_x = 10
# x_i = [random.randint(min_x, max_x)]
# N = 3
# f = x - x_i[0]
# for i in range(1, N):
#    x_i.append(random.randint(1, 10))
#    f *= (x - x_i[i])
#
# print(x_i)
# print(f.expand())
# print(f)

min_x = -5
max_x = 5
N = 3
x, f = symbols('x f')
roots = []
fraction = False
for i in range(N):
    if fraction:
        ...
    else:
        root = random.randint(min_x, max_x)
    roots.append(root)

print(roots)

f = 1
for i in range(N):
    f *= x - roots[i]

print(f)
print(f.expand())