n=int(input("Enter the number of terms\n"))
i,j=1,1
while i<=n:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i+=1
    print()
    
