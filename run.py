import random
import string
​
​
def validate_input(user_input, valid_values_list):
    if not user_input:
        return False
    return user_input.lower() in valid_values_list




