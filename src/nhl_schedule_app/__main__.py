# main file for nhl_schedule_app

#imports
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
URL=None                                
page_data=None                                  #will contain page data in HTML (soup)
all_schedules=[[0]*2]*32                        #contains weekly schedules of all teams. Initialized 2D array with 2 col & 32 rows for 32 teams


#-------- functions --------

#The getPageData function will scrape/pull all HTML code using the URL parameter
def get_page_data(URL):
    data=requests.get(URL)
    soup= BeautifulSoup(data.content,'html5lib')
    return soup

#get_all_schedules function will return table of teams and the number of games to play in an array. Removes first element of array
#need to find way of splitting string from global_schedule using digits in order to return proper array
def get_all_schedules():

    table=page_data.find('table') 
    table_body=table.find('tbody')
    rows=table_body.find_all('tr')

    index=0

    for row in rows:
        
        team_name=row.find('td', {"class":"Alt Last name first Tst-team"}).text
        nb_games=row.find('td', {"class":"stat Tst-games"}).text

        all_schedules[index][0]=team_name
        all_schedules[index][1]=nb_games

        print(team_name)
        #print(cols)
    
    return all_schedules

#The parse_table function will read & return the required data for schedules using the table as a parameter
def parse_table(table_data):
    return table_data

#ToDo function that will determine which week from schedule for URL

#main
page_data=get_page_data("https://hockey.fantasysports.yahoo.com/hockey/team_games?week=1")
all_schedules=get_all_schedules()
print(all_schedules)
