import random
import string

 def validate_input(user_input, valid_values_list):
    if not user_input:
        return False
    return user_input.lower() in valid_values_list
​​
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
 def get_password_length():
    length_valid = False
    while length_valid is False:
        length = input('Enter Password Length: (Max 15)  ')
        length_valid = validate_input(length, ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
        if length_valid is False:
            print('Invalid length')
    return length
​
​
 def get_password_type():
    type_valid = False
    while type_valid is False:
        password_type = input('Password Type: Enter "1" for Numerical, "2" for AlfaNumerical  ')
        type_valid = validate_input(password_type, ['1', '2'])
        if type_valid is False:
            print('Invalid password type')
    return password_type
​
​
 def get_excluded_chars():
    chars_excluded = ''
    exclude_answer_valid = False
    while exclude_answer_valid is False:
        want_to_exclude = input('Do you want to exclude some chars from the password generation? (Yes/No) ')
        exclude_answer_valid = validate_input(want_to_exclude, ['yes', 'no'])
        if exclude_answer_valid is False:
            print('Invalid option')
        else:
            if want_to_exclude.lower() == 'yes':
                chars_excluded = input('Enter the excluded chars:  ')
    return chars_excluded
​
​
 def generate_random_password(password_length, valid_chars):
    return ''.join(random.SystemRandom().choice(valid_chars) for _ in range(password_length))
​
​
get_username()
get_password_length()
get_password_type()
get_excluded_chars()
print(generate_random_password(12, string.digits+string.ascii_uppercase+string.punctuation))
​
​
​
  
    
    

​


