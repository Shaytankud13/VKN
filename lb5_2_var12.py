import math as m

xA = float(input("\nвведіть координату x для точки A: "))
yA = float(input("введіть координату y для точки A: "))
xB = float(input("\nвведіть координату x для точки B: "))
yB = float(input("введіть координату y для точки B: "))
xC = float(input("\nвведіть координату x для точки C: "))
yC = float(input("введіть координату y для точки C: "))

def dis(x, y):
    d = m.sqrt(m.pow(x, 2)+m.pow(y, 2))
    return(d)

if dis(xA, yA) > dis(xB, yB) and dis(xA, yA) > dis(xC, yC):
    print("\nВідстань від точки A до центра координат найбільша")
elif dis(xB, yB) > dis(xA, yA) and dis(xB, yB) > dis(xC, yC):
    print("\nВідстань від точки B до центра координат найбільша")
else:
    print("\nВідстань від точки C до центра координат найбільша")