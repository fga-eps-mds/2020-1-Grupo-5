import unittest
from src import login

class LoginTests(unittest.TestCase):

    def test_update_received_information(self):
        user_data = {'choice': 'Senha'}
        self.assertEqual('Senha', login.update_received_information(user_data, 'Senha12345'))
        self.assertEqual('Senha12345', user_data['Senha'])
        self.assertNotIn('choice', user_data)

    def test_validation_management(self):
        user_data = {'Email': 'testeemail'}
        user_data['Keyboard'] = [['Email', 'Senha'],
                        		['Cancelar']]
        self.assertIn('Entrada inválida', login.validation_management(user_data, 'Email'))

        user_data = {'Email': 'teste@email.com'}
        user_data['Keyboard'] = [['Email', 'Senha'],
                        		['Cancelar']]
        self.assertIn('Perfeito', login.validation_management(user_data, 'Email'))

    def test_update_missing_info(self):
        user_data = {'Email': 'teste@email.com', 'Senha': 'Senha12345'}
        user_data['Keyboard'] = [['Email', 'Senha'],
                            	['Cancelar']]
        login.required_data = (['Senha'])
        login.update_missing_info(user_data)
        self.assertIn(['Done'], user_data['Keyboard'])
        self.assertNotIn('Senha', login.required_data)

        user_data = {'Email': 'teste@testeemail.com'}
        user_data['Keyboard'] = [['Email', 'Senha'],
								['Cancelar'], ['Done']]
        login.required_data = set()
        login.update_missing_info(user_data)
        self.assertNotIn(['Done'], user_data['Keyboard'])
        self.assertIn('Senha', login.required_data)

if __name__ == '__main__':
    unittest.main()
