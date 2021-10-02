# Code

row=15    
col=18    
str=""    
for i in range(1,row+1):    
    if((i<=3)or(i>=7 and i<=9)or(i>=13 and i<=15)):    
        for j in range(1,col):    
            str=str+"*"    
        str=str+"\n"    
    elif(i>=4 and i<=6):    
        for j in range(1,5):    
            str=str+"*"    
        str=str+"\n"    
    else:    
        for j in range(1,14):    
            str=str+" "    
        for j in range(1,5):    
            str=str+"*"    
        str=str+"\n"    
print(str) 


OUTPUT

*****************
*****************
*****************
****
****
****
*****************
*****************
*****************
             ****
             ****
             ****
*****************
*****************
*****************
