# main file for nhl_schedule_app

#-------- imports --------
import datetime
import requests
from bs4 import BeautifulSoup

#-------- global variables --------
global URL                               
global page_data                                                                         #will contain page data in HTML (soup)
global all_schedules                                    #contains weekly schedules of all teams. Initialized 2D array with 2 col & 32 rows for 32 teams
global selected_week                                                                     #saves the selected week for schedule                      

#-------- functions --------

#set_page_data function will scrape/pull all HTML code using the URL parameter
def set_page_data(URL):
    data=requests.get(URL)
    soup= BeautifulSoup(data.content,'html5lib')
    globals()["page_data"]=soup  

#set_all_schedules function will set table of teams and the number of games to play in an array. 2x32
def set_all_schedules():

    table=page_data.find('table') 
    table_body=table.find('tbody')
    rows=table_body.find_all('tr')
    array_schedules=[[0]*2 for _ in range(32)] 

    index=0

    for row in rows: 
        team_name=row.find('td', {"class":"Alt Last name first Tst-team"}).text         #stores team name of the row
        nb_games=row.find('td', {"class":"stat Tst-games"}).text                        #stores nb of games played 

        array_schedules[index][0]=team_name
        array_schedules[index][1]=nb_games
        
        index+=1
    
    globals()["all_schedules"]=array_schedules

#set_url_schedule function will set the url of the current the week by default (if before oct 7 by default week will be 1. Todo take input and validate week
def set_url_schedule(input_week=-1):                                          
    week_number=input_week                                                              #will save current date

    if input_week==-1:                                                                  
        current_date=datetime.datetime.now() 
        week_number=validate_week(current_date)                                         #validates input
        globals()["selected_week"]=week_number
    elif input_week<-1 and input_week>25:
        print("The entered week is not valid. Must be within 1-25. Week 1 will be displayed")
        week_number=0

    globals()["URL"]="https://hockey.fantasysports.yahoo.com/hockey/team_games?week="+str(week_number)

#refresh_schdules function will call up 2 functions in order fetch new required data
def refresh_schedules():
    set_page_data(globals()["URL"])
    set_all_schedules()

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

    if (team_index!=-1):                                                   #if team is found, saves number of games for the week
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

#get_input_week will return user's input for selected week
def get_input_week():
    print("Enter selected week: ")
    input_week=int(input())
    return input_week

#search_team function manages input and validation or search. & 
def search_team():
    team_search=True

    while team_search:
        print("Enter team name or city:    ")
        selected_team=input()
        team_schedule=get_team_schedule(selected_team)
        
        if team_schedule !=0:
            team_search=False
        else:
            print("Entered team does not exist")

    print("Nb of Games for "+selected_team+" for Week "+str(selected_week)+": "+str(team_schedule))


#-------- main --------
active_menu=True
selected_team=None
selected_week=-1
all_schedules=[[0]*2 for _ in range(32)]     
set_url_schedule()
set_page_data(globals()["URL"])
set_all_schedules()

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

    if selected_menu=="1":                                                                  #Current week's schedule
        set_all_schedules()
        print(all_schedules)
    elif selected_menu=="2":                                                                #Selected week's schedule
        selected_week=get_input_week()
        set_url_schedule(selected_week)
        refresh_schedules()
        print(globals()["all_schedules"])
    elif selected_menu=="3":                                                                #Selected team's schedule for current week
        search_team()
    elif selected_team=="4":                                                                #Selected team's Schedule for specified week
        selected_week=get_input_week()
        refresh_schedules()
        set_all_schedules()
        search_team()
    elif selected_menu=="5":
        print("Goodbye")
        active_menu=False

        
    
    #print(team_exists("leafs"))
    #print(get_team_schedule())
