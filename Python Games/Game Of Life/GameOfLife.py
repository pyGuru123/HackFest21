# Life Game

#things to do:
#TURN THE WET INTO DRY
#branching for choices
#add user choices/input
#add surnames  

import random

#global variables 
game_status = "alive"
age = -1
gender = ""
name = ""
cause_death = ""

name_male_list = ['John','Elliot','Paul','Mario','Eduardo','Bob','Paul The Panda','Ro The Hut','Ramster','Bill','Dude','Fred','Thomas','Dimebig the guitar big dude','David','Thor', 'Le Dog','WhoCares','Qwerty', 'Ricky', 'King of Spades', 'Java The Big Monster of Verbosity', 'Racedriver', 'Not So Mad Max', 'Arthur', 'Zakk The Barbarian', 'Martian Spy']

name_female_list = ['Maria','Danielle','Nina','Kitty','Debbie','Marie','Kassandra', 'Ana', 'Paty','Kenga','Queen','Brianna','Mina','Ferggie from Korea','Mioko','Sabrinna','Vilma','NineVolt','Monica','Livia Burned', 'Fanny', 'Babe','Queen of Python', 'Ariel','Tatooed Girl', 'Pinup Queen', 'Chick', 'Queen of Spades',   ]

causes_death_list = ['infected mushroom', 'a lighting went straight for the head', 'poisoned apple','sadness', 'game over', 'bad joke', 'stage diving', 'moshing with a barbarian', 'jumped too many holes','followed the rabbit to the wrong hole','forgot to define the type on a Java variable', 'played Pokemoon while crossing the road', 'broke the 8th string on a djent riff', 'missed a Meshuggah concert in town', 'too much happiness at the same time', 'lost the heart in a gamble', 'went to the crossroad and signed the wrong contract', ]

#default chance values for a life event to occur, both arguments of randint()
low_chance = 1
high_chance = 75

# varibales for messages inside the loop, so they only get printed once.
learn_python_message = False
learn_c = False
sad_message = False
job_message = False
college_message = False
married_message = False
kids_message = False
retire_message = False

#Functions definitions
def it_lives():
    life_index = chance_dice(0,1)
    if life_index == 0:
        print("From out of the blue, a new life is created. \n One cell. Infinite possibilities.")
        print("\n0\n")
        print("00\n")
        print("00000000\n00000000\n")
        print("some time later...")
    elif life_index == 1:
        print("Welcome to life as you are now a single cell")
        print("\n0\n")
        print("00\n")
        print("00000000\n00000000\n")
        print("A while later...")

def set_gender():
    gender_dice = random.randint(0,1)
    if gender_dice == 0:
        return "female"
    elif gender_dice == 1:
        return "male"
    gender_print()
    
def gender_print():
    print("... a large group of awesome cells is around...\n")
    print("...then a coin is flipped and a gender is chosen. \nThe cromossomes responsible for this task looks like this:")
    if gender == "female":
        print("\nXX")
    else:
        print("\nXY")
    print("\n ...so your gender is " + gender + ".")   
def set_name():
    if gender == "male":
        name_index_male = random.randint(0 , int(len(name_male_list)) -1 )
        return name_male_list[int(name_index_male)]
        
    if gender == "female":
        name_index_female = int(random.randint(0 , int(len(name_female_list))) -1 )
        return name_female_list[int(name_index_female)]

def name_print():
    print("Some super fun python puzzle returns a name:")
    print("The name given to you is \"" + str(name) + "\".")
    print("\nAnd here goes your yearbook:")
 
def get_death():
    cause_index = int(random.randint(0, int(len(causes_death_list))) -1 )
    cause_death = str(causes_death_list[int(cause_index)])
    return cause_death

def death():
    print("\n======== R.I.P ========")
    print("\"" + str(name) + "\"" +" just passed away. \nCause of death: " + get_death() + ".")
    if age <=18:
        print("So sad it had to go so soon...just kiddin, ITS JUST A GAME!")
    print("\nOne last wish: PRESS THE RUN BUTTON AGAIN!\n")
    
def natural_death():
    print("\n======== R.I.P ========")
    print("\"" + str(name) + "\"" +" just passed away by natural causes, had great fun and a long life.")
    print("Oh, one last wish: PRESS THE RUN BUTTON AGAIN!")
   
    
def chance_dice(a,b):
    return int(random.randint(a,b))
    
# End of function definitions

#       LifeGame by I.B.
#beguinning linear storytelling

it_lives()
gender = set_gender()
name = set_name()
name_print()

#End of linear story telling

#age loop
while game_status == "alive":
    
    age = age + 1
    
    #print ages
    if age != 0:
        print("age: " + str(age))   
           
     #random life event
    event_chance = random.randint(low_chance, high_chance)
    if event_chance == 66:
        game_status = "dead" 
   
   #weights in chance for life events as ages increases.
    if age <= 6:
        high_chance = 200 
    elif age <= 12:
        high_chance = 150
    elif age <= 16:
        high_chance = 120 
    elif age >= 65:
        high_chance = 75
    elif age >= 75:
        high_chance = 70
    elif age >= 80:
        high_chance = 67
   
   #never is late for python 
    if age == chance_dice(12,37) and learn_python_message == False:
        print("You really got luck and started to learn Python!")
        learn_python_message = True;
        
    
    if age == chance_dice(12,37) and learn_c == False:
        print("You went oldschool and started to learn C.")
        learn_c = True;
        
   
    if age == chance_dice(4,7):
        chance_first_school = chance_dice(0,4)
        if chance_first_school != 1:
            print("First day at new school yaaa.")
            chance_friends = chance_dice(0,1)
            if chance_friends == 0:
                print("But you don't have that many friends yet.")
            elif chance_friends == 1:
                print("You've made many friends.")    
    
    #teenager
    if age == 16:
        chance_gift = random.randint(0,2)
        if chance_gift == 1:
            print("Highschool is boring but you figured that you have a gift for something you wish to do for the rest of your life.")
    #college
    if age >= 25 and college_message == False:
        college_message = True
        chance_college = chance_dice(1,5)
        if chance_college == 3:
            print("You got into college!")
            married_message = True
        elif chance_college == 4:
            print("You started the Computer Science college and guess what you had to learn on your first period: Python! Yeeeeah!")
            
    #marriage
    if age >= 25 and married_message == False:
        married_message = True
        chance_married = chance_dice(1,5)
        if chance_married == 3:
            print("You got married!")
        elif chance_married == 4:
            print("You feel in love and got married with Python!")
            
            
    #kids
    if age >= 25 and kids_message == False:
        kids_message = True
        if married_message == True:
            print("What nice couple you make! Congratulations, you gonna have a child!")
        elif married_message == False:
            print("After a short abduction you had a cute little alien child.")
    
    #work
    if age >= 20 and age <= 65:
        job_chance = chance_dice(1,15)
        if job_chance == 5:
            print("You got a new job!")
    
    #retirement
    if age >= 65 and retire_message == False:
        retire_chance = chance_dice(1,3)
        if retire_chance == 2:
            print("You worked all your life and now got a good retirement...lots of free time to spend with the family.")
        retire_message = True
            
    #death by life event
    if game_status == "dead":
        death()
    
    #natural death by elder age
    if age >= 75:
        old_age_death = chance_dice(0,4)
        if old_age_death == 1:
            game_status = "dead"
            natural_death()
            
#end of age loop   


