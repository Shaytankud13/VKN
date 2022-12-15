import math as m

x = float(input("Введіть x: "))
 
def func1 ( x1 ):
    a = m.log( m.fabs(x1 + 1), 10) + 2.9 * m.pow( m.e ,0.1 * x1)
    return(a)
def func2 ( x2 ):
    b = m.sqrt(m.fabs(x2)) + m.pow(x2, 1/3) - m.sin(x2)
    return(b)
def func3 ( x3 ):
    c = 4*x3 + m.pow( m.e, x3) - 4*m.sqrt(m.fabs(x3))
    return(c)

if x > 1 :
    print ("Значення функції: ", round (func1(x), 2))
elif x > -1.1 and x <= 1 :
    print ("Значення функції: ", round (func2(x), 2))
else:
    print ("Значення функції: ", round (func3(x), 2))