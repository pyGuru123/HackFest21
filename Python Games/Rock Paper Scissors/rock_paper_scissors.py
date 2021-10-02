import random

user_choice = input("What do you choose, Rock, Paper or Scissor: ")
computer_list = ["Rock","Paper","Scissor"]
computer_choice = random.choice(computer_list)
print("The computer chose", computer_choice)

if (user_choice.lower() == "rock") and (computer_choice == "Paper"):
    print("The Computer has won :( ")
elif (user_choice.lower() == "rock") and (computer_choice == "Scissor"):
    print ("You have won!")
elif (user_choice.lower() == "paper") and (computer_choice == "Rock"):
    print("You have won!")
elif (user_choice.lower() == "paper") and (computer_choice == "Scissor"):
    print("The Computer has won :( ")
elif (user_choice.lower() == "scissor") and (computer_choice == "Rock"):
    print("The Computer has won :( ")
elif (user_choice.lower() == "scissor") and (computer_choice == "Paper"):
    print("You have won!")
elif (user_choice.lower()) and (computer_choice.lower()) == ("rock" or "paper" or "scissor"):
    print("Nobody has won.")