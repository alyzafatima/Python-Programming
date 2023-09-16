import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
symbol = ['#', '$', '_', '!', '@', '^', '&', '(', ')', '*', '?']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters_count = int(input("How many letter you want in password:"))
symbols_count = int(input("How many symbols you want in password:"))
numbers_count = int(input("How many numbers you want in password:"))

password_list = []
i = 0
while i < letters_count:
    password_list.append(random.choice(letters))
    i = i + 1

i = 0
while i < symbols_count:
    password_list.append(random.choice(symbol))
    i = i + 1

i = 0
while i < numbers_count:
    password_list.append(random.choice(numbers))
    i = i + 1

random.shuffle(password_list)

passwd = ""
for char in password_list:
    passwd += char
print("Here is strong password for you:", passwd)