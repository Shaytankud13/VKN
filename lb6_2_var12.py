import math as m

x = float( input("введіть значення x: "))
a = int( input("\nвведіть початкове значення лічильника a: "))
b = int( input("введіть кінцеве значення лічильника b: "))
h = float( input("введіть значення кроку циклу : "))
 

while a < b:
    f = m.pow(x, 1/3) + m.fabs(m.sin(x))
    print ( f, "\n")
    x = x + h
    a = a + h

