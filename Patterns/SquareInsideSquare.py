n= int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if ((i==1 or i==n or j==1 or j==n) or (i>=3 and i<=n-2 and j>=3 and j<=n-2) and (i==3 or i==n-2 or j==3 or j==n-2)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

'''

Output:

* * * * * * * 
*           * 
*   * * *   * 
*   *   *   * 
*   * * *   * 
*           * 
* * * * * * * 

'''
