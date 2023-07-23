#Connor was here
#Bri was here :)
#Arj is here



#From here to next comment must be included in every portion where data is needed

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import datetime

mkey = '49880dc5499b46fa967202042232107'
city = 'Tucson'

def change_city(something):
    city = str(something)

def init_data(city): 
    try:
        configuration = swagger_client.Configuration()
        configuration.api_key['key'] = '49880dc5499b46fa967202042232107'
        api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
        return api_instance.forecast_weather(city, 7)
    except:
        print("Make sure that the City is spelled correctly. Else make sure to choose a big city nearest to you.")

#Here is the end of the portion that needs to be included



#Choose funtions that are needed and put them in a print statement fro the vlaues that you want  

def current_temp():
    '''
    Initializes data for the rest of the stuff
    '''
    api_response = init_data()
    return api_response._current.temp_f

def current_time():
    '''
    Pulls the current time
    '''
    return datetime.now().strftime("%H:%M:%S")
    
def date(num):
    ''' 
    INPUT a value between 0 and 6 for the day (ahead of your current day) of the month that you want to pull from. 
    '''
    try:
        api_response = init_data()
        return api_response.forecast.forecastday[num]._date, api_response.forecast.forecastday[num]._date.strftime("%m/%d/%Y")    
    except:
        print("Remember to print an integer from 0-6.")

def forecast(num):
    '''
    Input a value between 0 and 6 for the day (ahead of your current day) of the month that you want to pull from. 
    '''
    try:
        api_response = init_data()
        return api_response.forecast.forecastday[6]._hour[11]._temp_f, api_response.forecast.forecastday[6]._hour[23]._temp_f     
    except:
        print("Remember to print an integer from 0-6.")
def wind(num):
    '''
    Input a value between 0 and 6 for the day (ahead of your current day) of the month that you want to pull from.
    Returns tuple with wind direcction and speed
    '''
    try:
        api_response = init_data()
        return api_response.forecast.forecastday[6]._hour[11].wind_dir, api_response.forecast.forecastday[6]._hour[11].wind     
    except:
        print("Remember to print an integer from 0-6.")

def sun_and_moon_stuff(num):
    '''
    Input a value between 0 and 6 for the day (ahead of your current day) of the month that you want to pull from.
    Returns tuple with sun rise, sun set time, and moon phase
    '''
    try:
        api_response = init_data()
        return api_response.forecast.forecastday[6].astro.sunrise, testing.forecast.forecastday[6].astro.sunset, testing.forecast.forecastday[6].astro.moon_phase  
    except:
        print("Remember to print an integer from 0-6.")

def humidity(num):
    '''
    Input a value between 0 and 6 for the day (ahead of your current day) of the month that you want to pull from.
    Returns humidity value as a string
    '''
    try:
        api_response = init_data()
        return str(testing.forecast.forecastday[6].hour[11]) + "%"
    except:
        print("Remember to print an integer from 0-6.")

if __name__ == '__main__':
    main()


init_data(city)
print(current_temp())