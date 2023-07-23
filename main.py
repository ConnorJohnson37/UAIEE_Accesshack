#Connor was here
#Bri was here :)
#Arj is here

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

def init_data(): 
    try:
        configuration = swagger_client.Configuration()
        configuration.api_key['key'] = mkey
        api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
        return api_instance.forecast_weather(city, 7)
    except:
        print("Make sure that the City is spelled correctly. Else make sure to choose a big city nearest to you.")


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

def main():
    pass

if __name__ == '__main__':
    main()

#Sets values to variables based on api call just made
astronomy_data = api_instance.astronomy(qTEMP, dt) #astronomy. dt parameter must be on or after Jan 1, 2015
print(astronomy_data['sunrise'])
#forecast_data = api_instance.forecast_weather(qTEMP, days, dt=dt, unixdt=unixdt, hour=hour, lang=lang)
#Runs into issue accessing single elements 