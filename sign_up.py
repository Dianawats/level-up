
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

    def submit(self):
        pass
        # e.g send the data to the db

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

    

# SignUp.combine_phone_number()