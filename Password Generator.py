import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
           'V','W','X','Y','Z']
numbers = "1234567890"
symbols = "!@#$%^&*()_-+={[}]':;?/>.<,|`~"

no_of_letters = int(input("How many letters do you want the password to have? "))
no_of_numbers = int(input("How many numbers do you want the password to have? "))
no_of_symbols = int(input("How many symbols do you want the password to have? "))

password = ""

for x in range (1, no_of_letters + 1):
    password_char = random.choice(letters)
    password += password_char

for y in range(1, no_of_numbers + 1):
    password_char = random.choice(numbers)
    password += password_char

for z in range (1, no_of_symbols + 1):
    password_char = random.choice(symbols)
    password += password_char

new_password = "".join(random.sample(password,(no_of_letters + no_of_numbers + no_of_symbols)))

print(f"Your Password is {new_password}")