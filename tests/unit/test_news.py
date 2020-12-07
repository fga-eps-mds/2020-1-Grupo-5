import unittest
from src import news

class NewsTests(unittest.TestCase):

    def test_string_date(self):
        self.assertEqual('segunda-feira, 07 de dezembro de 2020', news.stringDate('Monday, 07 December 2020'))
