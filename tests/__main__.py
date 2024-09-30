# main file for tests

#-------- testing grounds for requests --------
import datetime    
import requests
from bs4 import BeautifulSoup

#URL="https://hockey.fantasysports.yahoo.com/hockey/team_games?week=1" #using week of Oct 7 for url
#r=requests.get(URL)

#soup= BeautifulSoup(r.content,'html5lib')

#print(soup.prettify()) will print the whole page. Prettify will adjust formatting

#-------- testing grounds for parsing data (JS) --------  
#print(soup.prettify())


def validate_week(input_date):
    output_week=-1

    if input_date.isocalendar().week<41 and input_date.year==2024:             #Before season start
        output_week=1
    elif input_date.isocalendar().week>=41 and input_date.year==2024:          #During the season for 2024
        output_week=input_date.isocalendar().week-40
    elif input_date.isocalendar().week<=15 and input_date.year==2025:          #During the season for 2025
        output_week=input_date.isocalendar().week+12
    elif input_date.isocalendar().week==16:                                             #Rare exception for last week with 10 days
        output_week=25

    return output_week




current_date=datetime.datetime.now()
date=datetime.datetime(2024,12,30)



season_start=datetime.datetime(2024,10,7)
season_end=datetime.datetime(2025,4,17)

print(validate_week(date))

#print(current_date.isocalendar().week)
#print(date.isocalendar().week)
#print(season_start.isocalendar().week)
#print(season_end.isocalendar().week)

#*data=[]
#for row in table.find_all('tr'):
    #for cell in row.find_all('td'):
        #print(cell.text)



#Possible need to make library to read table
