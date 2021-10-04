#Python Program to Generate Password

import random
passlen = int(input("Enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)

# Sample output
# Enter the length of password7
# ^H0%koE
