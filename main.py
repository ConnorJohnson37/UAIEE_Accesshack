#Connor was here
#Bri was here :)
#Arj is here

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

#Set input variables for call functions
import cgi
form = cgi.FieldStorage()
city =  form.getvalue('entercity') #get city entered by user in index.html
days = 7 #show 7 day forcast
dt = '2023-07-22' #date FIXME set to today's date
unixdt = 56 # int | Please either pass 'dt' or 'unixdt' and not both in same request. unixdt should be between today and next 14 day in Unix format. e.g. 1490227200  (optional)
lang = 'lang_example' #language

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
