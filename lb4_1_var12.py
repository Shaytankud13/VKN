import math as m

x = float(input("Введіть x: "))

a = m.cos(x) + m.sin(2*x)
b = m.pow(4, 2*x)
c = m.log(m.fabs(x + 1), m.e)
f = a/b-c

print(f)