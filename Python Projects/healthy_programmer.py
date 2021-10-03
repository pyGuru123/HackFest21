from playsound import playsound
import time
def water():
    for i in range(5000):
        time.sleep(1)
        print(i,"\n")
        
    time.sleep(5000)
    print("Please Drink Water\n")
    playsound('C:\\Users\\TUSHAR\\Downloads\\thirsty.MP3')
    c = input("If comepleted write Done\n")
    if c=='DONE':
        print("Good job\n")
        water()

def eyes() :
    time.sleep(1800)
    print("Please close Your eyes and relax\n")
    playsound('')
    c = input("If comepleted write Done\n")
    if c=='DONE':
        print("Good job\n")
        eyes()

def exercise():
    time.sleep(2000)
    print("Please Stand up from your position and Do some exercise\n")
    playsound('')
    c = input("If comepleted write Done")
    if c=='DONE':
        print("Good job\n")
        exercise()         

print("---------WELCOME TO HEALTHY PROGRAMER-------------")
print("WRITE DONE IF YOU COMPLETE YOUR TASKS")
water()
eyes()
exercise()
