# main file for nhl_schedule_app

#imports
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
URL=None
page_data=None                               #will contain page data in HTML


#-------- functions --------

#The getPageData function will scrape/pull all HTML code using the URL parameter
def getPageData(URL):
    r=requests.get(URL)
    soup= BeautifulSoup(r.content,'html5lib')
    return soup

#ToDo function that will determine which week from schedule for URL

#main
page_data=getPageData("https://hockey.fantasysports.yahoo.com/hockey/team_games?week=1")
print(page_data)
