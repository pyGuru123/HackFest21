'''
Author : Sumit Kumar
Pattern : Rectangle
'''
n, m = input().split()
for i in range(0, int(n)):
    for j in range(0, int(m)):
        print('*', end = '')
    print()
