def hollowRhombus(rows):
     
    for i in range (1, rows + 1):
        # Print trailing spaces
         
        for j in range (1, rows - i + 1):
            print (end=" ")
             
        # Print stars after spaces
        # Print stars for each solid rows
         
        if i == 1 or i == rows:
            for j in range (1, rows + 1):
                print ("*",end="")
                 
        # stars for hollow rows
        else:
            for j in range (1,rows+1):
                if (j == 1 or j == rows):
                    print ("*",end="")
                else:
                    print (end=" ")
        # Move to the next line/row
        print()
