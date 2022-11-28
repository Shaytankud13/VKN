import numpy as np

st1 = input("Введіть перший рядок чисел: ")
st2 = input("Введіть другий рядок чисел: ")
st3 = input("Введіть третій рядок чисел: ")
suma = 0

st1_list = st1.split(" ")
st2_list = st2.split(" ")
st3_list = st3.split(" ")

masiv = np.zeros((3, len(st1_list)), dtype=int)

for i in range(3):
    for j in range (len(st1_list)):
        if i == 0:
            masiv[i][j] = st1_list[j]
        elif i == 1:
            masiv[i][j] = st2_list[j]
        else:
            masiv[i][j] = st3_list[j]
        
        if i == 0 and j % 2 != 0:
            suma = suma + int(st1_list[j])
        elif i == 1 and (i+j) % 2 != 0:
            suma = suma + int(st2_list[j])
        elif i == 2 and (i+j) % 2 != 0:
            suma = suma + int(st3_list[j])
                   

print(masiv)
print("Сума всіх елементів масиву, для яких сума індексів i+j – число непарне: ", suma)