# main file for nhl_schedule_app

#imports
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
URL=None                                
page_data=None                               #will contain page data in HTML
all_schedules=None                           #contains weekly schedules of all teams   

#-------- functions --------

#The getPageData function will scrape/pull all HTML code using the URL parameter
def get_page_data(URL):
    data=requests.get(URL)
    soup= BeautifulSoup(data.content,'html5lib')
    return soup

#get_all_schedules function will return table of teams and the number of games to play in an array. Removes first element of array
#need to find way of splitting string from global_schedule using digits in order to return proper array
def get_all_schedules():
    global_schedule=page_data.find('table')
    del global_schedule[0]                 
    return global_schedule

#The parse_table function will read & return the required data for schedules using the table as a parameter
def parse_table(table_data):
    return table_data

#ToDo function that will determine which week from schedule for URL

#main
page_data=get_page_data("https://hockey.fantasysports.yahoo.com/hockey/team_games?week=1")
all_schedules=get_all_schedules()
print(type(all_schedules))
