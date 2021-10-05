try:
    n = int(input("Enter number of rows: "))
except ValueError:
    print(" ")
    print("Input number only!")
    n = int(input("Enter number of rows: "))

pls = [1]
for i in range(n):
    print(pls)
    psc = []
    psc.append(pls[0])
    for i in range(len(pls) - 1):
        psc.append(pls[i] + pls[i + 1])
    psc.append(pls[-1])
    pls = psc
