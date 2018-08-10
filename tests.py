import unittest
from sign_up import Register


class TestSignup(unittest.TestCase):
    
    def test_model_is_created(self):
        register = Register('dian', 'wats', '785730287', 
                            'diana@gmail.com', '98765')

    # def test_validate_email_and_returns_email(self):
    #     register = Register.validate_email('diana@gmail.com')
    #     self.assertEqual(register, 'diana@gmail.com')

    def test_valid_email(self):
        register = Register('dian', 'wats', '785730287', 
                            'diana@gmail.com', '98765')
        self.assertEqual(register.validate_email(), 'diana@gmail.com')

    # def test_invalid_email(self):
    #     register = Register('dian', 'wats', '785730287', 'wats.com', '98765')
    #     self.assertEqual(register.validate_email(), 'Invalid email address!')

    def test_not_combine_non_alphabet_names(self):
        register = Register('98765', 'wats', '785730283', 
                            'diana@gmail.com', '98765')
        self.assertEqual(register.combine_name(), 'Names must be alphabets')

    def test_combines_alphabet_names(self):
        register = Register('Dinwats', 'Wats', '785730287', 
                            'diana@gmail.com', '98766')
        self.assertEqual(register.combine_name(), 'Dinwats Wats')

    def test_validate_password_length(self):
        register = Register('Dian', 'Wats', '785730287', 
                            'dian@gmail.com', '3W#T3')
        self.assertEqual(register.validate_password(), 'Password not exceed ten xters long')



if __name__ == '__main__':
    unittest.main()
