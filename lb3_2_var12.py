import sys
w = float( sys.argv[1])
l = float( sys.argv[2])
h = float( sys.argv[3])
k = float( sys.argv[4])

wk = w*k
lk = l*k
hk = h*k

S = 2*(wk*lk)+2*(wk*hk)+2*(hk*lk)
V = wk*lk*hk

print("Площа поверхні :", round(S,2) )
print("Об'єм :", round(V,2) )