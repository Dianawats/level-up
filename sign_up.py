
class SignUp:

    """Sign up class with validate email""" 
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = SignUp.validate_email(email_address)
        self.email_address = []
        
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
        # e.g check if the email is in valid format
        return email