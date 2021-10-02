n = int(input("enter the value of n:"))
for i in range(1,n+1):
    for k in range(0,n-i):
        print(" ",end='')
    if(i%2==1):
        for j in range(0,2*i-1):
            print("*",end='')
    else:
        for j in range(0,2*i-1):
            print("-",end='')
    print()
for i in range(n,1,-1):
    for k in range(n,i-1,-1):
        print(" ",end='')
    if(i%2==1):
        for j in range(2*i-2,1,-1):
            print("-",end='')
    else:
        for j in range(2*i-2,1,-1):
            print("*",end='')
    print() 
