import random
Maclist = []
for i in range(1,7):
    RANDSTR = "".join(random.sample("0123456789abcdef",2))
    Maclist.append(RANDSTR)
RANDMAC = ":".join(Maclist)
print (RANDMAC)
