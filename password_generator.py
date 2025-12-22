import string
import random
letters = list(string.ascii_lowercase)
digits = list(string.digits)
symbols = list(string.punctuation)


# easy generator

password = ""

in_letters = int(input("Enter number of letters you want in your password: "))
in_symbols = int(input("Enter number of symbols you want in your password: "))
in_numbers = int(input("Enter number of numbers you want in your password: "))

for i in range(1,in_letters+1):
    password+= random.choice(letters)
for i in range(1, in_symbols):
    password+= random.choice(symbols)
for i in range(1,in_numbers):
    password+= random.choice(digits)

print(password)
