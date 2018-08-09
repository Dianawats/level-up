
import re


class Register:
    """Sign up class with validate phone number and email""" 

    def __init__(self, first_name, last_name, country_code, 
                 phone_number, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.country_code = country_code
        self.phone_number = Register.validate_phone(phone_number)
        self.email_address = Register.validate_email(email_address)    
        
    @staticmethod
    def validate_phone(phone_number):
                
        rule = re.compile(r"^[0-9]{10,14}$")
        if not rule.search(phone_number):
            print("Invalid phone number")
            raise ValueError("Wrong phone number")
        else:
            return phone_number

    @staticmethod
    def validate_email(email_address):
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.[a-zA-Z]*$")
        if not EMAIL_REGEX.match(email_address):
            print('invalid email_address')
            raise ValueError("Wrong email_address format")
        else:
            print('valid email_address')
            print(email_address)
            return email_address

        
class CombineData(Register):

    def __init__(self, first_name, last_name, email_address, 
                 phone_number, country_code):
        super().__init__(self, first_name, last_name, 
                         email_address, 
                         phone_number, 
                         country_code)

    def combine_name(self):
        full_name = '{}  {}'.format(self.first_name, self.last_name)
        print(full_name)
        return full_name

    def combine_phone_number(self):
        full_number = '{}{}'.format(self.country_code, self.phone_number)
        print(full_number)
        return full_number

    def combine_all_data_and_save_it_to_file(self):

        all_data = '{} {} {}{} {}'.format(self.first_name, self.last_name,
                                          self.email_address,
                                          self.phone_number, 
                                          self.country_code)
        save_data = all_data + '\n'
        data = open('data.txt', 'a')
        data.write(save_data)
        data.close()
        print(all_data)
        return all_data

        
name = CombineData('Diana', 'Wats', 'diana@gmail.com', '785730287', '+256')
name.combine_phone_number()
name.combine_name()
name.combine_all_data_and_save_it_to_file()