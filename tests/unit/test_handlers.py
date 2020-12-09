import unittest
from src import handlers
from telegram import ReplyKeyboardMarkup

class HandlersTests(unittest.TestCase):

	def get_reply_markup(self):
		user_data = {}
		reply_keyboard = [  ['Login','Registrar'],
							['Sobre','Finalizar'],
							['Ajuda']   ]
		markup = ReplyKeyboardMarkup(reply_keyboard)
		self.assertEqual(markup, handlers.get_reply_markup(user_data))
	
		user_data = {'AUTH': 'TESTE'}
		reply_keyboard = [  ['Minhas informações','Editar perfil'],
                            ['Sobre','Logout'],
						    ['Ajuda','Dicas']   ]
		markup = ReplyKeyboardMarkup(reply_keyboard)
		self.assertEqual(markup, handlers.get_reply_markup(user_data))

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
