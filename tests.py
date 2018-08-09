import unittest
from sign_up import Register, CombineData


class TestSignup(unittest.TestCase):
    def test_full_name(self):
        name = CombineData('Diana', 'Wats', 'diana@gmail.com',
                           '785730287', '+256')
        self.assertEqual(name.combine_name(), 'Diana Wats')

    def test_validate_email_and_returns_email(self):
        register = Register.validate_email('diana@gmail.com')
        self.assertEqual(register, 'diana@gmail.com')

    def test_validate_email_and_returns_error(self):
        with self.assertRaises(ValueError):
            Register.validate_email('diana@gmail.com')

    
if __name__ == ' __main__':
    unittest.main()
