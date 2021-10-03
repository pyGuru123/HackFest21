from string import ascii_lowercase, ascii_uppercase


def alphapat(n):
     
    # initializing value corresponding to 'A'
    # ASCII value
    num = 65
 
    # outer loop to handle number of rows
    # 5 in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # explicitely converting to char
            ch = chr(num)
         
            # printing char value
            print(ch, end=" ")
     
        # incrementing number
        num = num + 1
     
        # ending line after each row
        print("\r")
#adding flexibility to this code
nch=0
let =input("Upto which letter:\n")
if (let>='A' and let<='Z'):
    nch=int(ord(let)-64)
else:
    nch=0
alphapat(nch)