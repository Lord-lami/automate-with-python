import re

at_least_8_chars_re =re.compile(r'.{8,}')
contains_uppercase = re.compile(r'[A-Z]')
conatins_lowercase = re.compile(r'[a-z]')
contains_digit = re.compile(r'\d')

print("Enter a strong password for testing")
password = input()

length_match = at_least_8_chars_re.search(password)
uppercase_match = contains_uppercase.search(password)
lowercase_match = conatins_lowercase.search(password)
digit_match = contains_digit.search(password)

weak_password = False

if not length_match:
    weak_password = True
    print("The password is shorter than 8 characters")

if not uppercase_match:
    weak_password = True
    print("The password is missing uppercase characters")

if not lowercase_match:
    weak_password = True
    print("The password is missing lowercase characters")

if not digit_match:
    weak_password = True
    print("The password is missing digit characters")


if not weak_password:
    print("The password is strong!")
else:
    print("The password is weak")

