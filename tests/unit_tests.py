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


if __name__ == '__main__':
    unittest.main()
