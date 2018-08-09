import unittest
from sign_up import Register


class TestSignup(unittest.TestCase):
    # def test_full_name(self):
    #     name = CombineData('Diana', 'Wats', 'diana@gmail.com',
    #                        '785730287', '+256')
    #     self.assertEqual(name.combine_name(), 'Diana Wats')

    # def test_validate_email_and_returns_email(self):
    #     register = Register.validate_email('diana@gmail.com')
    #     self.assertEqual(register, 'diana@gmail.com')

    # def test_validate_email_and_returns_error(self):
    #     with self.assertRaises(ValueError):
    #         Register.validate_email('diana@gmail.com')

    # def test_validate_email_returns_phone_number(self):
    #     phone = Register.validate_phone('785730287')
    #     self.assertEqual(phone, '785730287')

    def test_user_data_type(self):
        data = Register('first_name', 'last_name')
        user_details = {'first_name':'louis', 'email':'email@email.com', 'phone':783140203}
        user_data = data.register_user(user_details)
        self.assertEqual(200, user_data['status_code'])
        self.assertEqual('valid data format', user_data['message'])

    def test_check_missing_first_name(self):
        data = Register('first_name', 'last_name')
        user_details = {'username':'louis', 'email':'email@email.com', 'phone':783140203}
        user_data = data.register_user(user_details)
        self.assertEqual(400, user_data['status_code'])


    
if __name__ == ' __main__':
    unittest.main()
