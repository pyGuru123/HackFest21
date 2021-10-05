str=""
for Row in range(0,7):    
    for Col in range(0,7):     
        if (Col == 1 or Col == 5 or (Row == Col and Col != 0 and Col != 6)):  
            str=str+"♥"    
        else:      
            str=str+" "    
    str=str+"\n"    
print(str);
