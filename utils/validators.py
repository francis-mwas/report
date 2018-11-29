import re


class Validation:
    """
    phone number validation, phone number must start with a digit and end with
    a digit, and must be 10 digits only in this format xxxx-xxx-xxx.
    """

    def validate_phone_number(self, phoneNumber):
        return re.match(r'^\d{4}-\d{3}-\d{3}$', phoneNumber)
    """ username must contain only alphanumeric characters and a min of 4 character """

    def validate_username(self, username):
        return re.match("^[a-zA-Z0-9]{4,}$", username)
    """ email must start not start with @ and can contain only one @ and must not end with @ """

    def validate_email(self, email):
        return re.match("[^@]+@[^@]+\.[^@]+$", email)
    """ input strings must start with letters and can contain alphanumeric and special characters """

    def validate_input_strings(self, input_strings):
        return re.match("^[a-zA-Z0-9.-_@]", input_strings)
    """ checking whether a user is an admin or not """

    # def validate_if_is_admin(self, is_admin):
    #     if is_admin !=True or False:
          
    
        
