from bs4 import BeautifulSoup
import requests 
r=requests.get('https://date.nager.at./PublicHoliday/Country/UA') 
if r.status_code==200:     
    wbs=BeautifulSoup(r.text,'html.parser')     
    namelist=wbs.find_all()     
    for name in namelist:         
        print(name.get_text())

        f = open('holidays.txt', 'w')
        f.writelines(name.get_text())