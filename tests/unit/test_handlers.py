import unittest
from src import handlers

class HandlersTests(unittest.TestCase):
	def test_signup_handler(self):
		self.assertTrue(handlers.signup_handler())

	def test_login_handler(self):
		self.assertTrue(handlers.login_handler())

	def test_profile_handler(self):
		self.assertTrue(handlers.perfil_handler())

	def test_tips_handler(self):
		self.assertTrue(handlers.tips_handler())

if __name__ == '__main__':
    unittest.main()
