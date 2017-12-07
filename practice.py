import requests
import os
import json

base_url = 'https://api-2445582011268.apicast.io'
headers = {'Accept': 'application/json', 'user-key': '9dd6c179b9eb4d88aecf274c2fc2210b'}

function_name = '/games/?search=SuperMarioBros(E)'

url = base_url + function_name

result = requests.get(url, headers=headers)

game_info = json.loads(result.text)

games = []

for game in game_info:
    id = str(game['id'])
    new_function = '/games/' + id
    new_url = base_url + new_function
    new_result = requests.get(new_url, headers=headers)
    each_game = json.loads(new_result.text)
    games.append(each_game[0]['name'])
print(games)


