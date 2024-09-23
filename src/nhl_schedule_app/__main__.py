# main file for nhl_schedule_app

#imports
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
URL=None
page_data=None                               #will contain page data in HTML


#-------- functions --------

#The getPageData function will scrape/pull all HTML code using the URL parameter
def get_page_data(URL):
    data=requests.get(URL)
    soup= BeautifulSoup(data.content,'html5lib')
    return soup

#get_all_schedules function will return table of teams and the number of games to play in an array
    def get_all_schedules():
        return None

#The parse_table function will read & return the required data for schedules using the table as a parameter
def parse_table(table_data):
    return table_data

#ToDo function that will determine which week from schedule for URL

#main
page_data=get_page_data("https://hockey.fantasysports.yahoo.com/hockey/team_games?week=1")
print(page_data)
