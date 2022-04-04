from sympy import *
import random

x, f, g, h = symbols('x f g h')


f = (x-1)*(x+2)*(x-4)
g = (x-3)*(x+3)*(x-7)*(x+6)
h = (x-2)*(x+1)*(x-3)*(x+3)*(x-4)


print(f.expand())
print(g.expand())
print(h.expand())

x_i = []
N = 10
for i in range(N):
   x_i.append(random.randint(1, 10))

print(x_i)
