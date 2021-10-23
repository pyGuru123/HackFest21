import requests
import json

url = 'slack webhook url'
message = {'text': 'Finished Execution'}
response = requests.post(url, data = json.dumps(message))
print(response)
