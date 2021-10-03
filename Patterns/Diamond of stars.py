n=int(input())
firstHalf = (n+1) // 2
secondHalf = n // 2

        #FIRST HALF

currRow = 1
while currRow <= firstHalf :
    spaces = 1
    while spaces <= (firstHalf - currRow) :
        print(" ", end = " ")
        spaces += 1
    currCol = 1
    while currCol <= (2*currRow) - 1 :
        print("*", end ="")
        currCol += 1
    print()
    currRow += 1

        #SECOND HALF

currRow = secondHalf
while currRow >= 1 :
    spaces = 1
    while spaces <= (secondHalf - currRow + 1):
        print(" ", end=" ")
        spaces += 1
    currCol = 1
    while currCol <= (2 * currRow) - 1 :
        print("*", end = "")
        currCol += 1
    print()
    currRow -= 1
