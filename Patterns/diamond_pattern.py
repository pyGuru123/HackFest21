#Pattern Printing

n = int(input("Enter n value: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(end = ' ')
    for k in range(1, 2 * i):
        if k == 1 or k == i * 2 - 1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, n - i + 1):
        print(' ', end = '')
    for k in range(1, 2 * i):
        if k == 1 or k == i * 2 - 1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
