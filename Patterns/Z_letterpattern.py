#pattern to print "Z" letter
result="";    
for i in range(0,7):    
    for j in range(0,7):     
        if (((i == 0 or i == 6) and j >= 0 and j <= 6) or i+j==6):  
            result=result+"*"    
        else:      
            result=result+" "    
    result=result+"\n"    
print(result);
