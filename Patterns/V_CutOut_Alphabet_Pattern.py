for i in range(65, 70):
    for j in range(65, 70):
        if(j <= i):
            a = chr(j)
            print(a, end="")
        else:
            print(" ", end="")
    for k in range(69, 64, -1):
        if(k <= i):
            b = chr(k)
            print(b, end="")
        else:
            print(" ", end="")
    print()