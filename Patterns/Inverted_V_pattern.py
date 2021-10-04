# Python Implementation to print
# the pattern
 
# Function definition
def pattern(n):
    k = 0
    for i in range(n - 1, -1, -1):
 
        # outer gap loop
        for j in range(n - 1, k, -1):
            print(' ', end = '')
 
        # 65 is ASCII of 'A'
        print(chr(i + 65), end = '')
 
        # inner gap loop
        for j in range(1, k * 2):
            print(' ', end = '')
        if i<n-1:
            print(chr(i + 65), end = '')
        print()
        k += 1
 
# Driver Code
 
# taking size from the user
n = 5
 
# function calling
pattern(n)

# Output
#     E
#    D D
#   C   C
#  B     B
# A       A