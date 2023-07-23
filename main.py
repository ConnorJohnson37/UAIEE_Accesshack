#Connor was here
#Bri was here :)
#Arj is here

#start using library to access api
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

#Set up API authentication using key
configuration = swagger_client.Configuration()
configuration.api_key['key'] = '49880dc5499b46fa967202042232107'

api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration)) #configure api

#ALL values for all functions that can be input by a user
qTEMP = 'Tucson' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
hour = 10 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)

#Sets values to variables based on api call just made
forecast_data = api_instance.forecast_weather(qTEMP, days, dt=dt, unixdt=unixdt, hour=hour, lang=lang)
print(forecast_data.date)
