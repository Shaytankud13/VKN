import random as r
s = int(input("Введіть бажану кількість номерів: "))
def rand_number():
    number = "+999-"
    for i in range (7):
        if i == 0:
            c = r.randint(100,999) 
            number = number + str(c) + "-"
        if i == 3 or i == 5:
            number = number +"-"
    
        n = r.randint(0,9)
        number = number + str(n)

    return(number)

for nums in range(s):
    print(rand_number())
