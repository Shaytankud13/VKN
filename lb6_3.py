import math as m

x = float( input("введіть значення x: "))
a = int( input("\nвведіть початкове значення лічильника a: "))
b = int( input("введіть кінцеве значення лічильника b: "))
h = float( input("введіть значення кроку циклу : ")) 

func_list = []
sorted_func_list = []
zeros = 0

while a < b:
    f = m.pow(x, 1/3) + m.fabs(m.sin(x))
    print ( f, "\n")
    func_list.append(f)
    sorted_func_list.append(f) 
    x = x + h
    a = a + h
    if f == 0:
        zeros += 1

sorted_func_list.sort()

el1 = sorted_func_list[0]
el2 = sorted_func_list[1]

ind1 = func_list.index(el1)
ind2 = func_list.index(el2)

print(func_list)
print("індекси двох найменших елементів списку: ",ind1,",",ind2)
if zeros != 0:
    print("кількість нулів функції", zeros)