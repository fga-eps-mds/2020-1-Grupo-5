import unittest
from datetime import date
from src.CustomCalendar import CustomCalendar

class CalendarTests(unittest.TestCase):

	def test_calendar(self):
		calendar, step = CustomCalendar(locale='br', max_date=date.today()).build()
		self.assertTrue(calendar)
		self.assertEqual(step, 'y')

if __name__ == '__main__':
    unittest.main()
