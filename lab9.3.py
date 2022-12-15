fdict = dict([("Украина", "44,13 млн"), ("Германия", "83,24 млн"), ("Франция", "67,39 млн"), ("США", "329,5 млн"), ("Китай", "1,402 млрд.")])
print("Словарь(Страна :Население)")
print(fdict)
sdict = dict([("Украина", "603 700 км^2"),("Германия", "357 588 км^2"),("Франция", "543 940 км^2"),("США", "9 834 00 км^2"),("Китай", "9 597 00 км^2")]) # словарь
print("Словарь(Страна :Площадь)")
print(sdict)
slist = list(sdict.values())
tdict = {}
tlist = list(fdict.keys())
for key, value in fdict.items():
    for i in tlist:
        if (i== key):
            tdict.update({fdict.get(i): sdict.get(i)})
print("\nСловарь Значение : Значение")
for key, value in tdict.items():
        print(key,'|',value)