from sympy import *
import random


x, f, g, h = symbols('x f g h')

min_x = -10
max_x = 10
x_i = [random.randint(min_x, max_x)]
N = 3
f = x - x_i[0]
for i in range(1, N):
   x_i.append(random.randint(1, 10))
   f *= (x - x_i[i])

print(x_i)
print(f.expand())
print(f)




#5
#6
#7
#8