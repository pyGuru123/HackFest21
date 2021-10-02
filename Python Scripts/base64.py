"""
Encrypt or Decrypt Given String with Base64
Author: https://github.com/akashrchandran
"""

#imports
import base64
import inquirer


#Decrypts the given string from the user
def Decrypt(string: str):
    return base64.b64decode(string.encode("utf-8"))

#Encrypts the given string from the user
def Encrypt(string: str):
    return base64.b64encode(string.encode("utf-8"))


print('Base64 Encryptor/Decryptor\n')

#Promting if user wants to decrypt or encrypt the string
select_mode = [
  inquirer.List('mode',
                message="Select Mode",
                choices=['Encrypt', 'Decrypt'],
            ),
]
answer = inquirer.prompt(select_mode)

#taking users input
string_input = input(f'Please Enter the String to {answer["mode"]}: ').strip()

#Calling the respective function
result = globals()[answer['mode']](string_input)

# Printing the encryptrd/decrypted string
print('\nYour Base64 {}ed String is: {}'.format(answer["mode"], result.decode("utf-8")))
