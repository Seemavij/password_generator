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
​

            


