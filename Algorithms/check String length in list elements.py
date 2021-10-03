def checker(lst):
    b=[]
    d=[]
    for i in lst:
        c=0
        for j in i:
            c+=1
        if c<=5:
            b.append(i)
        else:
            d.append(i)
    return d,b
list=[]
n=(int(input('How many names you want to eneter? :')))
for i in range(n):
    a=input('Enter the string')
    list.append(a)
print(list)
p,q=checker(list)
print("tring's length greater than 5",p)
print("strings's length less than or equal 5",q)

