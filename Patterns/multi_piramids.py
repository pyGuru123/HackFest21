col= int(input(" Enter number of columns :"))
pir=int(input("Enter number of pyramids"))
print("generated patter is  :\n")
# for example use col=80, pir=5
d=col//pir
for i in range(1, d):
    for j in range(1, col):
        if(j%(d) <(d-i)):
            print(" ", end="")
        else:
            print("$", end="")
    print("")
