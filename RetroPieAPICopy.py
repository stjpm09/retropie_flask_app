from flask import Flask
import json
import pymysql

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
    sql = 'SELECT * FROM CurrentGame'
    cursor.execute(sql)
    games = []
    for game in cursor:
        games.append(game)
    print(games)
    return json.dumps(games)


@app.route('/history')
def games_played_search():
    server = 'localhost'
    database = 'RetroPie'
    user = 'root'

    # database connection
    conn = pymysql.connect(host=server, user=user, db=database)
    cursor = conn.cursor()
    sql = 'SELECT * FROM GamesPlayed'
    cursor.execute(sql)
    games = []
    for game in cursor:
        games.append(game)
    return json.dumps(games)


@app.route('/beenPlayed')
def game_been_played(game):
    server = 'localhost'
    database = 'RetroPie'
    user = 'root'

    # database connection
    conn = pymysql.connect(host=server, user=user, db=database)
    cursor = conn.cursor()
    sql = 'SELECT * FROM GamesPlayed'
    cursor.execute(sql)
    if game in cursor:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True)
