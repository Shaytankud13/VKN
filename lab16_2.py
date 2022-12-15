#аписати  програму,  яка  виведе  на  екран  гістограму,  
# з  якою зустрічаються на сайті prometheus.org.ua ключові слова «дистанційна», «курс», «програмування», “Python”

import numpy as np
import pylab
import requests
import matplotlib.pyplot as plt

url = 'https://prometheus.org.ua/'

try:             
    result = requests.get(url)             
    result.raise_for_status()             
    result.text         
except(requests.RequestException, ValueError):             
    print('Server error')             
    False        

a = url.count("дистанційна")
b = url.count("курс")
c = url.count("програмування")
d = url.count("Python")

x=np.array([1,2,3,4]) 

spisok=[]

spisok.append(a)
spisok.append(b)
spisok.append(c)
spisok.append(d)

y = np.array(spisok)

pylab.bar(x,y)
pylab.show()