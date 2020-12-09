import unittest
from src import signup

class SignupTests(unittest.TestCase):

    def test_signup_validation_management(self):
        user_data = {'Email': 'testeemail'}
        user_data['Keyboard'] = [['Username', 'Email'],
                                ['Senha', 'Raça'],
                                ['Trabalho', 'Genero sexual'],
                                ['Localização', 'Cancelar']]
        self.assertIn('Entrada inválida', signup.validation_management(user_data, 'Email'))

        user_data = {'Email': 'teste@email.com'}
        user_data['Keyboard'] = [['Username', 'Email'],
                                ['Senha', 'Raça'],
                                ['Trabalho', 'Genero sexual'],
                                ['Localização', 'Cancelar']]
        self.assertIn('Perfeito', signup.validation_management(user_data, 'Email'))

    def test_update_missing_info(self):
        user_data = {'Username': 'Usuario Teste', 'Email': 'teste@teste.com', 'Senha': 'Senha12345', 'Raça': 'Branco', 'Trabalho': 'Não',
					'Genero sexual': 'Homem Cis', 'País': 'Brasil', 'Estado': 'Distrito Federal', 'Cidade': 'Gama'}
        user_data['Keyboard'] = [['Username', 'Email✅'],
                            	['Senha✅', 'Raça✅'],
                            	['Trabalho✅', 'Genero sexual✅'],
                            	['Localização✅', 'Cancelar']]
        signup.required_data = (['Username'])
        self.assertIn('Agora que adicionou', signup.update_missing_info(user_data))
        self.assertIn(['Done'], user_data['Keyboard'])

        user_data = {'Username': 'Usuario Teste', 'Email': 'teste@teste.com', 'Senha': 'Senha12345', 'Raça': 'Branco',
					'Genero sexual': 'Homem Cis', 'País': 'Brasil', 'Estado': 'Distrito Federal', 'Cidade': 'Gama'}
        user_data['Keyboard'] = [['Username✅', 'Email✅'],
                            	['Senha✅', 'Raça✅'],
                            	['Trabalho✅', 'Genero sexual✅'],
                            	['Localização✅', 'Cancelar'], ['Done']]
        signup.required_data = set()
        self.assertIn('pode me dizer', signup.update_missing_info(user_data))
        self.assertNotIn(['Done'], user_data['Keyboard'])

if __name__ == '__main__':
    unittest.main()
