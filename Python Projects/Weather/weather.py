
import json
import requests
from pprint import pprint 
import sys

#Get the api key from Open Weather Map website
api_key = ''

city_name = input("City: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city_name
weather_data = requests.get(base_url).json()
json_str = json.dumps(weather_data)

#load the json to a string
resp = json.loads(json_str)

#print the resp
print (resp)

#extract an element in the response
print (resp['name'])
