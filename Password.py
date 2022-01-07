import random
import time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome, this is a random password generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []


for l in range(1, nr_letters+1):
    password.append(random.choice(letters))
    

for n in range(1, nr_numbers+1):
    password.append(random.choice(numbers))

for s in range(1, nr_symbols+1):
    password.append(random.choice(symbols))

print("Now will be created a random password for you")
time.sleep(2)

random.shuffle(password)

final_password = ""

for p in range(len(password)):
    final_password += password[p]

print(final_password)