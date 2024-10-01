# main file for nhl_schedule_app

#-------- imports --------
import datetime
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
URL=None                                
page_data=None                                  #will contain page data in HTML (soup)
all_schedules=[[0]*2 for _ in range(32)]                      #contains weekly schedules of all teams. Initialized 2D array with 2 col & 32 rows for 32 teams


#-------- functions --------

#getPageData function will scrape/pull all HTML code using the URL parameter
def get_page_data(URL):
    data=requests.get(URL)
    soup= BeautifulSoup(data.content,'html5lib')
    return soup

#get_all_schedules function will return table of teams and the number of games to play in an array. 2x32
def get_all_schedules():

    table=page_data.find('table') 
    table_body=table.find('tbody')
    rows=table_body.find_all('tr')

    index=0

    for row in rows: 
        team_name=row.find('td', {"class":"Alt Last name first Tst-team"}).text         #stores team name of the row
        nb_games=row.find('td', {"class":"stat Tst-games"}).text                        #stores nb of games played 

        all_schedules[index][0]=team_name
        all_schedules[index][1]=nb_games
        
        index+=1
    
    return all_schedules

#parse_table function will read & return the required data for schedules using the table as a parameter
def parse_table(table_data):
    return table_data

#get_url_schedule function will return the url of the current the week (if before oct 7 by default week will be 1)
def get_url_schedule(input_week=-1):                                          #will save current date
    week_number=input_week                                                

    if input_week==-1:
        current_date=datetime.datetime.now() 
        week_number=validate_week(current_date)
    elif input_week<-1 and input_week>25:
        print("The entered week is not valid. Must be within 1-25. Week 1 will be displayed")
        week_number=0

    generated_url="https://hockey.fantasysports.yahoo.com/hockey/team_games?week="+str(week_number)

    return generated_url

#validate_week will return the week of the [1-25]
def validate_week(input_date):
    output_week=0
    print(type(input_date))
    if input_date.isocalendar().week<41 and input_date.year==2024:                      #Before season start
        output_week=1
    elif input_date.isocalendar().week>=41 and input_date.year==2024:                   #During the season for 2024
        output_week=input_date.isocalendar().week-40
    elif input_date.isocalendar().week<=15 and input_date.year==2025:                   #During the season for 2025
        output_week=input_date.isocalendar().week+12
    elif input_date.isocalendar().week==16:                                             #Rare exception for last week with 10 days
        output_week=25

    return output_week

#get_team_schedule returns the number of games played from the team entered in parameter
def get_team_schedule(all_schedules, input_team):
    team_schedule=0

    for schedule in all_schedules:
        if schedule[0]==input_team:
            team_schedule=schedule[1]
    
    if team_schedule==0:
        print("Team not found")

    return team_schedule


#-------- main --------
URL=get_url_schedule(1)
page_data=get_page_data(URL)
all_schedules=get_all_schedules()
print(all_schedules)
