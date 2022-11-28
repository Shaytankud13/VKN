import math as m

x = float( input("введіть значення x: "))
a = float( input("\nвведіть a: "))
b = float( input("введіть b: "))
h = float( input("введіть значення кроку циклу: "))

b = x + b

for i in range(10000):
    
    f = m.pow(x, 1/3) + m.fabs(m.sin(x))
    print ( f, "\n")
    x = x + h
    
    if a + x > b:
        break

