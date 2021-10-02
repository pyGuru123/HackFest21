#function to print floyd’s triangle

def floydTriangle(n):

    c=0

    
    for i in range(1,n+1):


        for j in range(0,i):

            c+=1

            print(c, end=” “)


        print()


n=int(input(“Enter the number of rows: “))


floydTriangle(n)

#Output
Enter the number of rows: 7
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 