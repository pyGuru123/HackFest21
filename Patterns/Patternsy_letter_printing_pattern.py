str="";    
for Row in range(0,7):    
    for Col in range(0,7):     
        if (((Col == 1 or Col == 5) and Row < 2) or Row == Col and Col > 0 and Col < 4 or (Col == 4 and Row == 2) or ((Col == 3) and Row > 3)):  
            str=str+"*"    
        else:      
            str=str+" "    
    str=str+"\n"    
print(str);    
