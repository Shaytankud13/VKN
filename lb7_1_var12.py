import random as r

st = input("Введіть рядок: ")
uplet = "QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗФІВАПРОЛДЯЧСМИТЬЖЄХЇБЮ"
upword = " "
check = 0
up = 0


for st_el in st:
    if st_el in uplet and check == " " or st_el in uplet and check == 0:
        upword = upword + str(st_el)
        up = 1
    elif up == 1 and st_el != " ":
        upword = upword + str(st_el)
    elif st_el == " " and upword[-1] != " ":
        up = 0
        upword = upword + str(st_el)
        
    check = st_el

print(upword)

st_list = st.split(" ")
for el in st_list:
    if el == '':
        st_list.remove(el)
        
ran_st_list = []
while len(ran_st_list) < len(st_list):
    ind = r.randint(0, len(st_list)-1)
    if st_list[ind] not in ran_st_list:
        ran_st_list.append(st_list[ind])    

print (ran_st_list)