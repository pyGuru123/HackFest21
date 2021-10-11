import random
# creating a list of letters numbers and symbol for use in password as characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

# Asking user to input numbers of letters,synbols and numbers which he/she want to keep in password. 

nm_letters = int(input("How many letters would you like in your password?\n"))

nm_symbols = int(input(f"How many symbols would you like?\n"))

nm_numbers = int(input(f"How many numbers would you like?\n"))



# Passord generation code
password_list = []

for char in range(1,nm_letters + 1) :
    password_list.append(random.choice(letters))


for char in range(1,nm_symbols + 1) : 
    password_list.append(random.choice(symbols))


for char in range(1,nm_numbers + 1) : 
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

final_password = ""

for char in password_list : 
    final_password+=char

# Printing the final password

print(f"Your final password is {final_password} save it for future use.")







