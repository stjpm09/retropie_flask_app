import unittest
from unittest import TestCase
import requests
import json


class TestIGBD(TestCase):

    def test_simple_connect(self):
        url = '10.76.100.35:5000/'
        result = requests.get(url)
        return json.loads(result.text)
