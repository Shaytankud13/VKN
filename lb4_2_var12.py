import math as m

def abh(c, d, e):
    count = (1/3)*c*d*e
    return(count)
def ln(el):
    count = m.log(el, m.e)
    return(count)
    
x = float(input("Введіть x: "))
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))
y = float(input("Введіть y: "))

V = abh(a, b, h) * m.cos(x) + ln(y)

print("V =",V)