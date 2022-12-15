colors = ("Red", "Orange", "Yellow",
"Green", "Blue", "Purple", "Pink")
fruit = ("Apple", "Apricot", "Avocado",
"Pineapple", "Banana", "Pear", "Peach")

N = int(input("Введите количество словосочетаний: "))
for i in range(0, len(colors)):
    for j in range(0, len(fruit)):
        print(colors[i] + " " + fruit[j]
+ "\n")

