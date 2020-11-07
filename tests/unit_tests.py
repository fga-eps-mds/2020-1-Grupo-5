import unittest
from src import utils

class UtilsTests(unittest.TestCase):

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
