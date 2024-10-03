# main file for nhl_schedule_app

#-------- imports --------
import datetime
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
URL=None                                
page_data=None                                                                          #will contain page data in HTML (soup)
all_schedules=[[0]*2 for _ in range(32)]                                                #contains weekly schedules of all teams. Initialized 2D array with 2 col & 32 rows for 32 teams
selected_week=0                                                                         #saves the selected week for schedule                      

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

#get_url_schedule function will return the url of the current the week (if before oct 7 by default week will be 1. Todo take input and validate week
def get_url_schedule(input_week=-1):                                          
    week_number=input_week                                                              #will save current date

    if input_week==-1:                                                                  
        current_date=datetime.datetime.now() 
        week_number=validate_week(current_date)                                         #validates input
    elif input_week<-1 and input_week>25:
        print("The entered week is not valid. Must be within 1-25. Week 1 will be displayed")
        week_number=0

    generated_url="https://hockey.fantasysports.yahoo.com/hockey/team_games?week="+str(week_number)

    return generated_url

#validate_week will return the week of the [1-25]
def validate_week(input_date):
    output_week=0

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
def get_team_schedule(input_team):
    team_schedule=0
    team_index=team_exists(input_team)                                              #input for team name

    if (team_index==-1):                                                   #if team is found, saves number of games for the week
        team_schedule=all_schedules[team_index][1]


    return team_schedule

#team_exists function, validates if team exists using city name or team name. Returns index of team for all_schedules todo fix teams names with 2 words. Todo change input validation tolower?
def team_exists(input_team):
    team_index=-1                                                                        #index used tracking team in all_schedules
    index=0

    for team in all_schedules:
        team_full_name=team[0].lower()

        if input_team.lower() in team_full_name:
            team_index=index

        index+=1


    return team_index

#todo get_input schedule


#-------- main --------
active_menu=True
selected_team=None
URL=get_url_schedule()
page_data=get_page_data(URL)

while active_menu:
    print("Welcome to the NHL Schedule App\n By Rayan Kharroubi")
    print("1-   Get this week's schedule for league")
    print("2-   Get exact week's schedule for league")
    print("3-   Get specified team's schedule for this week")
    print("4-   Get specified team's for certain week")
    print("5-   Exit\n")
    print("Enter a digit from 1- to select an option:   ")


    selected_menu=input()
    selected_menu.strip()

    if selected_menu=="1":
        get_all_schedules()
        print(all_schedules)
    elif selected_menu=="2":
        print("Enter selected week: ")
        selected_week=int(input())
        URL=get_url_schedule(selected_week)
        page_data=get_page_data(URL)
        print(get_all_schedules())

    elif selected_menu=="3":
        selected_team=input()
        team_schedule=get_team_schedule(selected_team)
        
        if team_schedule !=0:
            print(team_schedule)
        else:
            print("Entered team does not exist")
    elif selected_team=="4":
        print("Enter selected week: ")
        selected_week=int(input())
        get_url_schedule(selected_week)
        page_data=get_page_data(URL)
        get_all_schedules()

        selected_team=input()
        team_schedule=get_team_schedule(selected_team)
        
        if team_schedule !=0:
            print(team_schedule)
        else:
            print("Entered team does not exist")
    elif selected_menu=="5":
        print("Goodbye")
        active_menu=False

        
    
    #print(team_exists("leafs"))
    #print(get_team_schedule())
