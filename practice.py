import requests
import os
import json

base_url = 'https://api-2445582011268.apicast.io'
headers = {'Accept': 'application/json', 'user-key': '9dd6c179b9eb4d88aecf274c2fc2210b'}

function_name = '/games/1942?fields=*'

url = base_url + function_name

result = requests.get(url, headers=headers)

print(json.loads(result.text))