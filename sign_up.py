
import re


class SignUp:

    """Sign up class with validate email""" 
    def __init__(self, first_name, last_name, email_address, 
                 phone_number, country_code):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = SignUp.validate_email(email_address)
        self.phone_number = SignUp.validate_number(phone_number)
        self.country_code = country_code
        
    """Combines first and lastname into a single name"""
    def combined_name(self):
        self.first_name = "Diana"
        self.last_name = "Naki"
        fullName = "first_name" + " " + "last_name"
        print(fullName)


class CombineForm(SignUp):

    def __init__(self, first_name, last_name, email_address, 
                 phone_number, country_code):
        super().__init__(self, first_name, last_name, email_address, 
                         phone_number, country_code)

    def combine_name(self):
        full_name = '{}  {}'.format(self.first_name, self.last_name)
        print(full_name)
        return full_name

    def combine_phone_number(self):
        full_number = '{}{}'.format(self.country_code, self.phone_number)
        print(full_number)
        return full_number

    def combine_all_data_and_save_to_file(self):
        all_data = '{} {} {}{} {}'.format(self.first_name, self.last_name, self.country_code, self.phone_number, self.email_address)
        save_data = all_data + '\n'
        data = open('data.txt', 'a')
        data.write(save_data)
        data.close()
        print(all_data)
        return all_data

    @staticmethod
    def validate_email(email):
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.[a-zA-Z]*$")
        if not EMAIL_REGEX.match(email):
            print('invalid email')
            raise ValueError("Wrong email format")
        else:
            print('valid email')
            print(email)
            return email

    @staticmethod
    def combine_phone_number(self):
        whole_number = '{}{}'.format(self.country_code, self.phone_number)
        print(whole_number)
        return whole_number

    

    SignUp.combine_phone_number()
    name.combine_phone_number()
    name = CombineData('diana', 'naki', '+256', '75875858', 'diand@gmail.com')

    name.combine_name()
    name.combine_all_data_and_save_to_file(