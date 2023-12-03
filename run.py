import random
import string
​
​
def validate_input(user_input, valid_values_list):
    if not user_input:
        return False
    return user_input.lower() in valid_values_list

def get_username():
    user_name_valid = False
    while user_name_valid is False:
        username = input('Please enter your username:  ')
        if username:
            user_name_valid = True
        else:
            print('Invalid username')
    return username
​
​def get_password_length():
    length_valid = False
    while length_valid is False:
        length = input('Enter Password Length: (Max 15)  ')
        length_valid = validate_input(length, ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
        if length_valid is False:
            print('Invalid length')
    return length

            


