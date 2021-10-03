#function to print floyds triangle

def floydTriangle(n):

    c=0

    
    for i in range(1,n+1):


        for j in range(0,i):

            c+=1

            print(c, end=" ")


        print()


n=int(input("Enter the number of rows: "))


floydTriangle(n)

