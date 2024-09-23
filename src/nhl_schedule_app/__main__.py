# main file for nhl_schedule_app

#imports
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
URL=None
soup=None                               #will contain page data in HTML


#-------- functions --------

#The getPageData function will scrape/pull all HTML code using the URL parameter
def getPageData(URL):
    r=requests.get(URL)
    soup= BeautifulSoup(r.content,'html5lib')

#ToDo function that will determine which week from schedule for URL

#main

