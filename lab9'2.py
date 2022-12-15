A = ('A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','*','+',',','-','.','/','1','2','3','4','5','6','7','8','9')

tl = list()
tl2 = list()
tl3 = list()

for i in A:
  if i >= chr(97) and i <= chr (122) or i >= chr(65) and i <= chr(90) :
    tl.append(i)
    C = (tl)

for i in A:
  if i >= chr(42) and i <= chr (47) :
    tl2.append(i)
    E = (tl2)

for i in A:
  if i >= chr(48) and i <= chr(57) :
    tl3.append(i)
    B = (tl3)

print("A: ")
print(A)
print("B: ")
print(B)
print("C: ")
print(C)
print("E: ")
print(E)
