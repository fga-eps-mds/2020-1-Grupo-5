import unittest
from src import report_status
from datetime import datetime, timedelta

class ReportStatusTests(unittest.TestCase):

    def test_get_total_days(self):
        day = str(datetime.today() - timedelta(days=1)).replace(' ', 'T')
        data = [{'created_at': str(day) + 'T', 'symptom': ['Tosse']}]
        self.assertEqual(report_status.get_total_days(data), (0, 1, 1))

    def test_get_percentage(self):
        data = [3, 1, 0]
        self.assertEqual('3 dias, 75.0%.', report_status.get_percentage(3, data))

    def test_image_rel(self):
        user_data = {'user_name': 'Test User'}
        expected = 'Olá, Test User! Lembre-se sempre de cuidar de sua saúde.\n\n'
        expected += '😃 - Você esteve bem 3 dias, 75.0%.\n'
        expected += '🤧 - Você esteve mal 1 dias, 25.0%.\n'
        self.assertEqual(expected, report_status.imageRel(user_data, 3, 1, 0))
