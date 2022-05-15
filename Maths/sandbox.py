from sympy import *
import random


x, f, g, h = symbols('x f g h')


# f = (x-1)
g = (x-3)*(x+3)*(x-7)*(x+6)
h = (x-2)*(x+1)*(x-3)*(x+3)*(x-4)


# print(f.expand())
# print(g.expand())
# print(h.expand())

min = -10
max = 10
x_i = [random.randint(min, max)]
N = 3
f = x - x_i[0]
for i in range(1,N):
   x_i.append(random.randint(1, 10))
   f = f*(x-x_i[i])


print(x_i)
print(f.expand())
print(f)



