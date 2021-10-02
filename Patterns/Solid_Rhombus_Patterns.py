def solidRhombus(rows):
     
    for i in range (1,rows + 1):
         
        # Print trailing spaces
         
        for j in range (1,rows - i + 1):
            print (end=" ")
             
        # Print stars after spaces
         
        for j in range (1,rows + 1):
            print ("*",end="")
             
        # Move to the next line/row
        print()
