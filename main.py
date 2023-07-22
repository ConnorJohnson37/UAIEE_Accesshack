#Connor was here
#Bri was here :)
#Arj is here

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

#Set up API authentication using key
configuration = swagger_client.Configuration()
configuration.api_key['key'] = '49880dc5499b46fa967202042232107'

api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
#Insert variables input by user here
#NOTE: Some data requests require different of inputs
place = 'Tucson' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
date = '2013-10-20' #yyyy-MM-dd format, can be between 0 and 14 days from current date
#days, number of days of weather forecast
#hour, must be between 1 and 24
#More variables to come based on parameters in library functions

#TEST
api_response = api_instance.astronomy(place, date) #get astronomy data based on location and date
pprint(api_response) #print the data (print astronomy class)


print("Hello World")
print("bruh")
