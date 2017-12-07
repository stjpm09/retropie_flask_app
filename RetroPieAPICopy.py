from flask import Flask
import json
import pymysql
import requests

app = Flask(__name__)


@app.route('/')
def connect():
    return 'Hello, add a query onto the URL to get data.'


@app.route('/current')
def current_game_search():
    server = 'localhost'
    database = 'RetroPie'
    user = 'root'

    # database connection
    conn = pymysql.connect(host=server, user=user, db=database)
    cursor = conn.cursor()
    sql = 'SELECT game_name, system_name, game_start_time FROM CurrentGame'
    cursor.execute(sql)
    games = []
    for game in cursor:
        games.append(game)
    return json.dumps(games)


@app.route('/history')
def games_played_search():
    server = 'localhost'
    database = 'RetroPie'
    user = 'root'

    # database connection
    conn = pymysql.connect(host=server, user=user, db=database)
    cursor = conn.cursor()
    sql = 'SELECT game_name, system_name FROM GamesPlayed'
    cursor.execute(sql)
    games = []
    for game in cursor:
        games.append(game)
    return json.dumps(games)


@app.route('/relatedToCurrent')
def show_related_games_to_current():
    server = 'localhost'
    database = 'RetroPie'
    user = 'root'

    # database connection
    conn = pymysql.connect(host=server, user=user, db=database)
    cursor = conn.cursor()
    sql = 'SELECT game_name FROM CurrentGame'
    cursor.execute(sql)

    base_url = 'https://api-2445582011268.apicast.io'
    headers = {'Accept': 'application/json', 'user-key': '9dd6c179b9eb4d88aecf274c2fc2210b'}

    games = []
    for game in cursor:
        games.append(game)

    if len(games) == 0:
        return '[]'

    function_name = '/games/?search=' + str(games[0])
    url = base_url + function_name
    result = requests.get(url, headers=headers)
    game_info = json.loads(result.text)
    game_list = []

    for game in game_info:
        id = str(game['id'])
        new_function = '/games/' + id
        new_url = base_url + new_function
        new_result = requests.get(new_url, headers=headers)
        each_game = json.loads(new_result.text)
        game_list.append(each_game[0]['name'])
    return json.dumps(game_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

