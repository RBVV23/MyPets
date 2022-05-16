from sympy import *
import random


x, f, g, h = symbols('x f g h')

min = -10
max = 10
x_i = [random.randint(min, max)]
N = 3
f = x - x_i[0]
for i in range(1, N):
   x_i.append(random.randint(1, 10))
   f *= (x-x_i[i])

print(x_i)
print(f.expand())
print(f)
