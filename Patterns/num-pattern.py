#num reverse pattern using python
rows = int(input())

for i in range(rows, 0, -1):

    for j in range(0, i + 1):

        print(j, end=' ')

    print("\r")