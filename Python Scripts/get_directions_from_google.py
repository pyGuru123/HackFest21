"""
install module for usage: handy for API calls
pip install requests
"""
import requests

"""
Get your API key using the below docs and replace the variable API_KEY
https://developers.google.com/maps/documentation/directions/get-directions
"""

"""
Can be used to get directions when you have an origin, destination
and some points in between the origin and the destination
"""
API_KEY = "API_KEY"
BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json' \
           '?key=' + API_KEY + \
           '&origin=49.2472501,-122.7552604' \
           '&destination=49.2472501,-122.7552604' \
           '&waypoints=' \
           '49.2472501,-122.7552604|' \
           '49.2810138,-123.0602546|' \
           '49.2810138,-123.0602546|' \
           '49.2472501,-122.7552604'

try:
    response = requests.get(BASE_URL)
    response.raise_for_status()
    response_json = response.json()
    if response.status_code == 200 and response_json['status'] == 'OK':
        print('Success response: {}'.format(response_json))
    else:
        print('Error in fetching directions from google', response.text)
except requests.exceptions.HTTPError as error:
    print('Error in API call', error)
