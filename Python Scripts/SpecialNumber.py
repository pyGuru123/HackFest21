sum=0  
# Ask user to enter the number  
num=int(input("Enter a number:"))   
temp=num  
# Using while loop  
while(num):  
    i=1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print("Given number is a strong number")  
else:  
    print("Given number is not a strong number")  
