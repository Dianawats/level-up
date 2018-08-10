# from flask import jsonif
import re


class Register:
    """Sign up class with validate phone number and email""" 

    def __init__(self, first_name, last_name, 
                 phone_number, email_address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.password = password 

    def validate_email(self):
        if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email_address):
            return 'invalid email_address'
        return self.email_address

    # def __init__(self, first_name, last_name):
    #     self.fname = first_name
    #     self.lname = last_name
    #     self.email = ''
    #     self.phone = ''
    #     self.data = None

    # def register_user(self, user_data):
    #     # check if data is in dictionary format
    #     if type(user_data).__name__ != 'dict':
    #         return {'message': 'invalid data format', 'status_code': 400}

    #     if 'first_name' not in user_data.keys():
    #         print('here')
    #         return {'message': 'first_name is missing', 'status_code': 400}

    #     return {'message': 'valid data format', 'status_code': 200}
   
    def combine_name(self):
        full_name = '{}  {}'.format(self.first_name, self.last_name)
        print(full_name)
        return full_name

    def validate_password(self):
        if not re.match(r"[A-Za-z0-9@#]", self.password):
            return 'invalid password'
        elif len(self.password) < 8:
            return 'Password should be atleast of eight xters long'
        return 'Valid password entered'
