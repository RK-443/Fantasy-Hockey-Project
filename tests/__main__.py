# main file for tests

#-------- testing grounds for requests --------
import datetime    
import requests
from bs4 import BeautifulSoup

#URL="https://hockey.fantasysports.yahoo.com/hockey/team_games?week=1" #using week of Oct 7 for url
#r=requests.get(URL)

#soup= BeautifulSoup(r.content,'html5lib')

#print(soup.prettify()) will print the whole page. Prettify will adjust formatting

#-------- testing grounds for parsing data (JS) --------  
#print(soup.prettify())

current_date=datetime.datetime.now()

print(current_date.month)

#*data=[]
#for row in table.find_all('tr'):
    #for cell in row.find_all('td'):
        #print(cell.text)



#Possible need to make library to read table
