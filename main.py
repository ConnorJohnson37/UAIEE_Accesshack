#Connor was here
#Bri was here :)
#Arj is here

#start using library to access api
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

#Set up city variable based on search bar in index.html
import cgi
form = cgi.FieldStorage()
city =  form.getvalue('entercity')

#Set up API authentication using key
configuration = swagger_client.Configuration()
configuration.api_key['key'] = '49880dc5499b46fa967202042232107'

#api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration)) #configure api

#ALL values for all functions that can be input by a user
q = 'Tucson' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
days = 1 # int | Number of days of weather forecast. Value ranges from 1 to 14
dt = '2023-07-22' # date | Date should be between today and next 14 day in yyyy-MM-dd format. e.g. '2015-01-01'  (optional)
unixdt = 56 # int | Please either pass 'dt' or 'unixdt' and not both in same request. unixdt should be between today and next 14 day in Unix format. e.g. 1490227200  (optional)
end_dt = '2013-10-20' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format<br />'end_dt' should be greater than 'dt' parameter and difference should not be more than 30 days between the two dates.  (optional)
unixend_dt = 56 # int | Date on or after 1st Jan, 2015 in Unix Timestamp format<br />unixend_dt has same restriction as 'end_dt' parameter. Please either pass 'end_dt' or 'unixend_dt' and not both in same request. e.g. unixend_dt=1490227200  (optional)
hour = 10 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

#Most used will most likely be location (currently called q), days (may be set to 14 to show whole week), and dt (date, could also set date to current day)

#All possible calls with given functions. Might not use all of them as options for user
astronomy_data = api_instance.astronomy(q, dt) #astronomy. dt parameter must be on or after Jan 1, 2015
forecast_data = api_instance.forecast_weather(q, days, dt=dt, unixdt=unixdt, hour=hour, lang=lang)
astronomy_data 
#future_weather_data = api_instance.future_weather(q, dt=dt, lang=lang) #date must be between 14 and 300 days from now
#realtime_data = api_instance.realtime_weather(q, lang=lang)
#autocomplete_data = api_instance.search_autocomplete_weather(q)
#timezone_data = api_instance.time_zone(q)
