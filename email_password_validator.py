import re


class TextColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


email_pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

password_pattern = re.compile(r'([A-Za-z0-9$%#@]{7,}[0-9])')

print(f'Enter a valid {TextColors.UNDERLINE}Email{TextColors.ENDC} and {TextColors.UNDERLINE}Password{TextColors.ENDC}')

while True:
    email = input('Enter your Email: ')
    if email_pattern.match(email):
        password = input('Enter your Password: ')
        if password_pattern.match(password):
            print(f'The Email: {TextColors.UNDERLINE}{email}{TextColors.ENDC} and Password: {TextColors.UNDERLINE}{password}{TextColors.ENDC} you entered are valid!')
            break
        else:
            print(f'{TextColors.WARNING}The password must be atleast 8 char long and have atleast 1 number and 1 letter!{TextColors.ENDC}')
    else:
        print(f'{TextColors.WARNING}Invalid Email, try again!{TextColors.ENDC}')
