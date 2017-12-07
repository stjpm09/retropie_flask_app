import requests


class MySQLMock:

    def populate_tables(self):
        current_game = {}
        games_played = {}

        url = 'http://10.76.100.35:5000/current'
        result = requests.get(url)
        game_name = result.text

        current_game['game_name'] = game_name

        url = 'http://10.76.100.35:5000/history'
        result = requests.get(url)
        history = result.text

        for count in range(len(history) - 1):
            games_played['game_name'] = history[count]



