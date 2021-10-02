import random
import string

lowercase = list(string.ascii_lowercase)   # We can use string.ascii_letters instead of uppercase + lowercase letters
uppercase = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

final = lowercase + uppercase + numbers + symbols 

def generatePassword(length):
    '''Generates a random password of given length.'''
    random.shuffle(final)
    password = ''.join(final[0:length])
    return password

while True:
    passwordLength = int(input("Enter Your Password Length:\t"))
    print(f"Your {passwordLength} Digit Random Password Is:\t {generatePassword(passwordLength)}\n")
