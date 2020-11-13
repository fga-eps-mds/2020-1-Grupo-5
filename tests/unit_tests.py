import unittest
from src import utils

class UtilsTests(unittest.TestCase):

	def test_is_logged(self):
		user_data = {}
		self.assertFalse(utils.is_logged(user_data))

		user_data = {'AUTH_TOKEN': 'GENERIC'}
		self.assertTrue(utils.is_logged(user_data))

	def test_set_to_str(self):
		required_data = set(['Username', 'Senha', 'Raça', 'Trabalho'])
		result = utils.set_to_str(required_data)
		self.assertIn('Username', result)
		self.assertIn('Senha', result)
		self.assertIn('Raça', result)
		self.assertIn('Trabalho', result)

	def test_dict_to_str(self):
		user_data = {'Username': 'User Teste', 'Senha': 'Senha12345', 'Trabalho': 'Não'}
		result = utils.dict_to_str(user_data)
		self.assertIn('Username - User Teste', result)
		self.assertIn('Senha - Senha12345', result)
		self.assertIn('Trabalho - Não', result)

	def test_validaNome(self):
		nome = 'Menor'
		self.assertFalse(utils.validaNome(nome))
		nome = 'Igual---'
		self.assertTrue(utils.validaNome(nome))
		nome = 'Maior----'
		self.assertTrue(utils.validaNome(nome))

	def test_validaSenha(self):
		senha = 'Menor'
		self.assertFalse(utils.validaSenha(senha))
		senha = 'Igual---'
		self.assertTrue(utils.validaSenha(senha))
		senha = 'Maior----'
		self.assertTrue(utils.validaSenha(senha))

	def test_validaEmail(self):
		email = 'invalido'
		self.assertFalse(utils.validaEmail(email))
		email = 'valido@gmail.com'
		self.assertTrue(utils.validaEmail(email))
	
	def test_validaGenero(self):
		genero = 'outro'
		self.assertTrue(utils.validaGenero(genero))
		genero = 'Outro'
		self.assertTrue(utils.validaGenero(genero))
		genero = 'errado'
		self.assertFalse(utils.validaGenero(genero))

	def test_validaRaca(self):
		# Certo 
		raca = 'branco'
		self.assertTrue(utils.validaRaca(raca))
		# Certo maiúsculo
		raca = 'Negro'
		self.assertTrue(utils.validaRaca(raca))
		# Errado
		raca = 'errado'
		self.assertFalse(utils.validaRaca(raca))

		
	def test_validaTrabalho(self):
		# Certo 
		trabalho = 'não'
		self.assertTrue(utils.validaTrabalho(trabalho))
		# Certo maiúsculo
		trabalho = 'Sim'
		self.assertTrue(utils.validaTrabalho(trabalho))
		# Errado
		trabalho = 'errado'
		self.assertFalse(utils.validaTrabalho(trabalho))

	def test_validations_login(self):
		data = {"Email": "valido@gmail.com"}
		self.assertTrue(utils.validations_login(data))

		data = {"Email": "valido@gmail.com", "Senha": "valida--"}
		self.assertTrue(utils.validations_login(data))

		data = {"Email": "invalido"}
		self.assertFalse(utils.validations_login(data))

		data = {"Email": "valido@gmail.com", "Senha": "errada"}
		self.assertFalse(utils.validations_login(data))

	def test_validations_signup(self):
		# Username
		data = {"Username": "errado"}
		self.assertFalse(utils.validations_signup(data))
		data = {"Username": "valido--"}
		self.assertTrue(utils.validations_signup(data))
		# Email
		data = {"Email": "errado",}
		self.assertFalse(utils.validations_signup(data))
		data = {"Email": "valido@gmail.com"}
		self.assertTrue(utils.validations_signup(data))
		# Senha
		data = {"Senha": "errado"}
		self.assertFalse(utils.validations_signup(data))
		data = {"Senha": "valido--"}
		self.assertTrue(utils.validations_signup(data))
		# Genero sexual 
		data = {"Genero sexual": "invalido"}
		self.assertFalse(utils.validations_signup(data))
		data = {"Genero sexual": "Outro"}
		self.assertTrue(utils.validations_signup(data))
		# Raca
		data = {"Raça": "invalida"}
		self.assertFalse(utils.validations_signup(data))
		data = {"Raça": "Outro"}
		self.assertTrue(utils.validations_signup(data))
		# Trabalho
		data = {"Trabalho": "invalido"}
		self.assertFalse(utils.validations_signup(data))
		data = {"Trabalho": "Sim"}
		self.assertTrue(utils.validations_signup(data))
		
		# Todos
		data = {"Username": "valido--", "Email": "valido@gmail.com", "Senha": "valida--",
				 "Genero sexual": "Outro", "Trabalho": "Sim", "Raça": "Outro"}
		self.assertTrue(utils.validations_signup(data))
		self.assertEqual({"Username": "valido--", "Email": "valido@gmail.com", "Senha": "valida--",
				 "Genero sexual": "Outro", "Trabalho": "Sim", "Raça": "Outro"}, data)

		data = {"Username": "errado", "Email": "invalido", "Senha": "errada",
				 "Genero sexual": "invalido", "Trabalho": "invalido", "Raça": "invalida"}
		self.assertFalse(utils.validations_signup(data))
		self.assertNotEqual({"Username": "errado", "Email": "invalido", "Senha": "errada",
				 "Genero sexual": "invalido", "Trabalho": "invalido", "Raça": "invalida"}, data)

	def test_image(self):
		text = {'user_name': 'Usuario Teste', 'race': 'Pardo', 'risk_group': True}
		expected_reply = 'Atualmente essas são as suas informações: \n\nUsername: Usuario Teste\nRaça: Pardo\nGrupo de Risco: Sim'
		self.assertEqual(expected_reply, utils.geraString(text))

	def test_geraString(self):
		text = {"user_name" : 'User', "gender" : 'Gender'}
		# Certo
		self.assertEqual("Atualmente essas são as suas informações: \n\nUsername: User\nGenero sexual: Gender", utils.geraString(text))
		# Tópico a menos
		self.assertNotEqual("Atualmente essas são as suas informações: \n\nUsername: User\n", utils.geraString(text))
		# Informação errada
		self.assertNotEqual("Atualmente essas são as suas informações: \n\nUsername: User0\nGenero sexual: Gender", utils.geraString(text))
		# Tópico a mais
		self.assertNotEqual("Atualmente essas são as suas informações: \n\nUsername: User\nGenero sexual: Gender\n Grupo de Risco: Sim", utils.geraString(text))

	def test_remove_check_mark(self):
		text = 'Senha✅'
		self.assertEqual('Senha', utils.remove_check_mark(text))


	def test_update_check_mark(self):
		keyboard = [['Username✅', 'Email'],
                    ['Senha', 'Raça'],
                    ['Trabalho✅', 'Genero sexual'],
                    ['Localização', 'Cancelar']]
		category = 'Raça'
		validation = True
		utils.update_check_mark(keyboard, category, validation)
		self.assertTrue(['Senha', 'Raça✅'] in keyboard)
		
		category = 'Username'
		validation = False
		utils.update_check_mark(keyboard, category, validation)
		self.assertFalse(['Username✅', 'Email'] in keyboard)


	def test_update_required_data(self):
		received_data = set(['Username', 'Email', 'Senha', 'Trabalho'])
		required_data = {'Email', 'Raça', 'Genero sexual', 'Localização'}
		utils.update_required_data(received_data, required_data)
		self.assertFalse('Email' in required_data)


	def test_form_filled(self):
		keyboard = [['Email', 'Senha'],
                    ['Cancelar']]
		utils.form_filled(keyboard)
		self.assertTrue(['Done'] in keyboard)


	def test_undone_keyboard(self):
		keyboard = [['Email', 'Senha'],
                    ['Cancelar'],
                    ['Done']]
		utils.undone_keyboard(keyboard)
		self.assertFalse(['Done'] in keyboard)


	def test_unreceived_info(self):
		received_data = set(['Username', 'Email', 'Senha'])
		required_data = {'Raça', 'Genero sexual'}
		utils.unreceived_info(received_data, required_data, ("Username", "Email", "Senha","Raça", "Trabalho", "Genero sexual"))
		self.assertTrue('Trabalho' in required_data)


if __name__ == '__main__':
    unittest.main()
