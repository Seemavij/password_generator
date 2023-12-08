import random
import string
import gspread

from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('passwordgenerator')


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


def get_password_length():
    length_valid = False
    while length_valid is False:
        length = input('Enter Password Length: (Max 15)  ')
        length_valid = validate_input(length, ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
        if length_valid is False:
            print('Invalid length')
    return length


def get_password_type():
    type_valid = False
    while type_valid is False:
        password_type = input('Password Type: Enter "1" for Numerical, "2" for AlphaNumerical  ')
        type_valid = validate_input(password_type, ['1', '2'])
        if type_valid is False:
            print('Invalid password type')
    return password_type


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


def generate_random_password(password_length, valid_chars):
    return ''.join(random.SystemRandom().choice(valid_chars) for _ in range(password_length))


def save_password(username, password):
    valid_input = False
    print(f"This is the generated password: {password}")
    while valid_input is False:
        print('Enter "1" to save your username and password')
        print('Enter "2" to not save')
        option = input("")
        valid_input = validate_input(option, ['1', '2'])
        if valid_input is False:
            print('Invalid option')
        else:
            if option == "1":
                worksheet.append_row([username, password])
                print("Username and password saved")
            else:
                 print("Username and password not saved")



def menu():
    quit_generator = False
    print("WELCOME TO PASSWORD GENERATOR")
    while quit_generator is False:
        print('Enter "1" to generate a password')
        print('Enter "2" to exit')
        option = input("")
        quit_generator = validate_input(option, ['1', '2'])
        if quit_generator is False:
            print('Invalid option')
        else:
            if option == "1":
                username = get_username()
                password_length = get_password_length()
                password_type = get_password_type()
                char_set = string.digits + string.ascii_uppercase+string.punctuation + string.punctuation
                if password_type == '1':
                    char_set = string.digits
                password = generate_random_password(int(password_length), char_set)
                print(f"This is the generated password: {password}")

            else:
                print("Thank you for using PASSWORD GENERATOR, goodbye")
                quit_generator = True


if __name__ == "__main__":
    menu()
    
