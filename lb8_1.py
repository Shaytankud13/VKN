from array import *
import random as r

masiv = array('i', [])

for i in range ( 10 ):     
    x = r.randint(0, 15)
    masiv.append( x )
    
print("Масив: ", masiv)

for i in range( 10 ):
    for j in range( i+1, 10 ):
        if masiv[i] > masiv[j]:
            buffer = masiv[i]
            masiv[i] = masiv[j]
            masiv[j] = buffer
            
print("Відсортований масив: ", masiv)
            
for c in range (5):
    buffer = masiv[c]
    masiv[c] = masiv[c + 5]
    masiv[c + 5] = buffer
    
print("Поміняні місцями перша і друга половини масиву", masiv)