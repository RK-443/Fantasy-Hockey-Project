# main file for tests

#-------- testing grounds for requests --------    
import requests
from bs4 import BeautifulSoup

URL="https://www.dailyfaceoff.com/nhl-weekly-schedule/2024-10-07" #using week of Oct 7 for url
r=requests.get(URL)

soup= BeautifulSoup(r.content,'html5lib')

#print(soup.prettify()) will print the whole page

#-------- testing grounds for parsing data (JS) --------  
print(soup)
table=soup.find('table', attrs={'class':'relative w-full table-fixed border-collapse'})

data=[]
for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        print(cell.text)



#Possible need to make library to read table
