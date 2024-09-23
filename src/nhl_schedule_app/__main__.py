# main file for nhl_schedule_app

#imports
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
URL=None
soup=BeautifulSoup                               #will contain page data in HTML


#-------- functions --------

#The getPageData function will scrape/pull all HTML code using the URL parameter
def getPageData(URL):
    r=requests.get(URL)
    soup= BeautifulSoup(r.content,'html5lib')

#ToDo function that will determine which week from schedule for URL

#main
getPageData("https://hockey.fantasysports.yahoo.com/hockey/team_games?week=1")
print(soup.prettify())
