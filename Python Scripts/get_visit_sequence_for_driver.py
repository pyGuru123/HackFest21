"""
Both urllib3 and json are included by python interpreter
But if you face issues use pip install command for the virtual env
e.g. pip install urllib3

Read the docs for more use cases: https://docs.routific.com/docs/
Can be used to get visit sequence when you need a driver to visit some locations
"""
# Step 1: Import http client and set routific vrp url
import urllib3
import json

URL = "https://api.routific.com/v1/vrp"

# Step 2: Prepare visits
visits = {
    "order_1": {
        "location": {
            "name": "6800 Cambie",
            "lat": 49.227107,
            "lng": -123.1163085
        }
    },
    "order_2": {
        "location": {
            "name": "3780 Arbutus",
            "lat": 49.2474624,
            "lng": -123.1532338
        }
    },
    "order_3": {
        "location": {
            "name": "800 Robson",
            "lat": 49.2819229,
            "lng": -123.1211844
        }
    }
}

# Step 3: Prepare vehicles
fleet = {
    "vehicle_1": {
        "start_location": {
            "id": "depot",
            "name": "800 Kingsway",
            "lat": 49.2553636,
            "lng": -123.0873365
        }
    },
    "vehicle_2": {
        "start_location": {
            "id": "depot",
            "name": "800 Kingsway",
            "lat": 49.2553636,
            "lng": -123.0873365
        }
    }
}

# Step 4: Prepare data payload
data = {
    "visits": visits,
    "fleet": fleet
}

# Step 5: Put together request
# This is your demo token, you can also use your personal token
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1MzEzZDZiYTNiMDBkMzA4MDA2ZTliOGEiLCJpYXQiOjEzOTM4MDkwODJ9.PR5qTHsqPogeIIe0NyH2oheaGR-SJXDsxPTcUQNq90E'
# visit https://routific.com/try-it-free/ tp get your own token

http = urllib3.PoolManager()
req = http.request('POST', URL, body=json.dumps(data),
                   headers={'Content-Type': 'application/json', 'Authorization': "bearer " + token})

# Step 6: Get route
res = json.loads(req.data.decode('utf-8'))

print(res)
