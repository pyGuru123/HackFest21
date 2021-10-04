# Function to print given string in the zigzag form in `k` rows
def printZigZag(s, k):
 
    # base case
    if k == 0:
        return
 
    # base case
    if k == 1:
        print(s, end='')
        return
 
    # print first row
    for i in range(0, len(s), (k - 1) * 2):
        print(s[i], end='')
 
    # print middle rows
    for j in range(1, k - 1):
 
        down = True
        i = j
 
        while i < len(s):
            print(s[i], end='')
            if down:            # going down
                i += (k - j - 1) * 2
            else:               # going up
                i += (k - 1) * 2 - (k - j - 1) * 2
 
            down = not down     # switch direction
 
    # print last row
    for i in range(k - 1, len(s), (k - 1) * 2):
        print(s[i], end='')
 
 
if __name__ == '__main__':
 
    s = 'THISPROBLEMISAWESOME'
    k = 4
 
    printZigZag(s, k)
 