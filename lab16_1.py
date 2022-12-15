#Зобразити  графік  функції 𝑦=0,3𝑥ଶ+|𝑥|, 𝑥∈[−10;10],  тип  лінії  – штрихпунктирна, колір лінії – зелений.
#Зберегти графік у файл function.png.

import  numpy as np 
import matplotlib.pyplot as plt 
import math 
x = linspace(0, 10, 51)  
y = 3*x+math.fabs(x) 
plt.plot(x, y, 'g--', label='3*x+math.fabs(x)')  
plt.axis([0, 10, 0, 10])  # задання [xmin, xmax, ymin, ymax]  
plt.xlabel('x')    # позначення осі абсцис  
plt.ylabel('y')    # позначення осі ординат  
plt.title('Qudratic function')  # назва графіка  
plt.legend()       # вставка легенди (тексту в label)  
plt.show()
plt.savefig('function.png', dpi=400)