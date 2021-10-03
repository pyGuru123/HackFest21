#Program for replecating a vending machine
import random
import os
#now we are defining functions for our work
n=0
def select(choice):
    if choice==1:
        print("---------------------------------WELCOME TO SNACK SECTION--------------------------------------------------------------------------------------")
        print("1. French Fries\n"+"2. Burger  \n"+"3. Veg Roll\n")
        snack=int(input("Enter your choices\n"))
        if snack==1:
            print("---------------------------------------------------------------------------")
            print("PAY ₹50 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)
        elif snack ==2:
             print("---------------------------------------------------------------------------")
             print("PAY ₹75 and collect your item\n")
             print("---------------------------------------------------------------------------")
             n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
             select(n)
        

        elif snack ==3:
            print("---------------------------------------------------------------------------")
            print("PAY ₹100 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n) 
          
        else:
            print("You Entered A wrong choice")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)

    elif choice ==2:
        
        print("----------------------------------WELCOME TO CHOCOLATES SECTION---------------------------------------------------------------------------------------------")
        print("1. FRUIT AND NUT\n"+"2. FUSE  \n"+"3  CRACKER\n" +"4.  MILKY BAR \n")
        chlt=int(input("Enter your choices\n"))
        if chlt==1:
            print("---------------------------------------------------------------------------")
            print("PAY ₹60 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)
        elif chlt ==2:
             print("---------------------------------------------------------------------------")
             print("PAY ₹45 and collect your item\n")
             print("---------------------------------------------------------------------------")
             n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
             select(n)
        

        elif chlt ==3:
            print("---------------------------------------------------------------------------")
            print("PAY ₹150 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n) 

        elif  chlt==4:
            print("---------------------------------------------------------------------------")
            print(" PAY ₹40 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)
        
        else:
            print("---------------------------------------------------------------------------")
            print("You Entered A wrong choice")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)        

            
    elif choice ==3:
        
        print("---------------------------------------WELCOME TO CANDIES SECTION--------------------------------------------------------")
        print("1. ECLAIRS\n"+"2. MANGO  \n"+"3  HUGS\n" +"4.  KISME \n")
        cnd=int(input("Enter your choices\n"))
        if cnd==1:
            print("---------------------------------------------------------------------------")
            print("PAY ₹5 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)
        elif cnd ==2:
             print("---------------------------------------------------------------------------")
             print("PAY ₹2 and collect your item\n")
             print("---------------------------------------------------------------------------")
             n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
             select(n)
        

        elif cnd ==3:
            print("---------------------------------------------------------------------------")
            print("PAY ₹3 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n) 

        elif  cnd==4:
            print("---------------------------------------------------------------------------")
            print(" PAY ₹1 and collect your item")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)
        
        else:
            print("You Entered A wrong choice")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)    

    elif choice ==4:
        
        print("----------------------------WELCOME TO MEAL SECTION------------------------------------------------------------------------------------------")
        print("1. CHOLE BHATURE\n"+"2. SHAMBHAR DOSA \n"+"3  IDLI\n" +"4.  SANDWHICHS \n")
        meal=int(input("Enter your choices\n"))
        if meal==1:
            print("---------------------------------------------------------------------------")
            print("PAY ₹120 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)
        elif meal ==2:
             print("---------------------------------------------------------------------------")
             print("PAY ₹150 and collect your item\n")
             print("---------------------------------------------------------------------------")
             n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
             select(n)
        

        elif meal ==3:
            print("---------------------------------------------------------------------------")
            print("PAY ₹80 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n) 

        elif  meal==4:
            print("---------------------------------------------------------------------------")
            print(" PAY ₹85 and collect your item\n")
            print("---------------------------------------------------------------------------")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)
        
        else:
            print("You Entered A wrong choice")
            n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
            select(n)
    elif choice==5:
        print("Thank You for using Service\n")
        exit
        
    else:
        print("You enter a wrong choice\n")
        n=int(input( " 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+"Enter Your choice again\n"))
        select(n)


print("-------------------WELCOME----------------")
print("-----------SELECT YOUR CHOICES------------")
print(" 1. SNACKS\n"+" 2. CHOCOLATES  \n"+" 3. CANDIES\n"+" 4. MEAL\n"+" 5. EXIT\n")
choice=int(input("Enter Your Choice\n"))
select(choice)