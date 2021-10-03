def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print('10', end="")
        print("  ")
#again adding user input for this for favolous pattern and removing the &#92r
num=int(input("Enter no between 1 to 10\n"))
pattern(num)