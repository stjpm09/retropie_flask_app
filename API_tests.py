import unittest
import requests
import json
from unittest import TestCase


class TestIGBD(TestCase):

    def test_simple_connect(self):
        url = 'http://10.76.100.35:5000/'
        result = requests.get(url)
        text = result.text
        self.assertEqual('Hello, add a query onto the URL to get data.', text)

    def test_no_current_game(self):
        url = 'http://10.76.100.35:5000/current'
        result = requests.get(url)
        text = result.text
        self.assertEqual('[]', text)

    def test_with_current_game(self):
        # this test will only work while playing Super Mario Bros
        url = 'http://10.76.100.35:5000/current'
        result = requests.get(url)
        new_result = json.loads(result.text)
        game_name = new_result[0][0]
        system_name = new_result[0][1]
        start_time = new_result[0][2]
        self.assertEqual("SuperMarioBros(E)", game_name)
        self.assertEqual("nes", system_name)
        self.assertEqual("16:11:05.351403", start_time)

    def test_no_history(self):
        # no games must be played on the pi before this test
        url = 'http://10.76.100.35:5000/history'
        result = requests.get(url)
        text = result.text
        print(text)
        self.assertEqual("[]", text)

    def test_history_with_one_game(self):
        # only mario played on the pi
        url = 'http://10.76.100.35:5000/history'
        result = requests.get(url)
        new_result = json.loads(result.text)
        game_name = new_result[0][0]
        system_name = new_result[0][1]
        self.assertEqual("SuperMarioBros(E)", game_name)
        self.assertEqual("nes", system_name)

    def test_related_to_current_with_no_game_playing(self):
        # no game playing on the pi
        url = 'http://10.76.100.35:5000/relatedToCurrent'
        result = requests.get(url)
        text = result.text
        self.assertEqual('[]', text)

    def test_related_to_current_with_game_playing(self):
        # mario must be playing for this test
        url = 'http://10.76.100.35:5000/relatedToCurrent'
        result = requests.get(url)
        text = result.text
        self.assertEqual(["Super Mario Bros. 3", "Super Mario Bros.", "Super Mario Bros. 2", "Classic NES Series: Super Mario Bros", "Super Mario Bros. Deluxe", "Super Mario Advance: Super Mario Bros. 2", "Super Mario Bros. Crossover", "New Super Mario Bros.", "New Super Mario Bros. 2", "Super Mario Advance 4: Super Mario Bros. 3"], text)
