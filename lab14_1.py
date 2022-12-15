from bs4 import BeautifulSoup
import requests

         
url = 'https://kirik.pro/blog/seo/headers-h1-h6/'                
try:             
    result = requests.get(url)             
    result.raise_for_status()             
    result.text         
except(requests.RequestException, ValueError):             
    print('Server error')             
    False              

soup = BeautifulSoup(url, 'html.parser')         
list = soup.head.title.text        
 
print(list)
f = open('headers.txt','w')
f.writelines(list)
f.close()