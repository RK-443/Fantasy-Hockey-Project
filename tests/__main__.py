# main file for tests

#testing grounds for requests    
import requests
from bs4 import BeautifulSoup

URL="https://www.dailyfaceoff.com/nhl-weekly-schedule/2024-10-07" #using week of Oct 7 for url
r=requests.get(URL)

pageData= BeautifulSoup(r.content,'html5lib')

print(pageData.prettify())
