import unittest
from src import location
from telegram import Location

class LocationTests(unittest.TestCase):

    def test_reverse_geo(self):
        current_location = Location(-0.124583, 51.500729)
        user_data = {}
        location.reverseGeo(current_location, user_data)
        self.assertEqual('United Kingdom', user_data['País'])
        self.assertEqual('England', user_data['Estado'])
        self.assertEqual('City of Westminster', user_data['Cidade'])

if __name__ == '__main__':
    unittest.main()
