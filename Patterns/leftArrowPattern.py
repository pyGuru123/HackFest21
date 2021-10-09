#left-arrow pattern
n=int(input())
st=2*n
for i in range(n):
    for j in range(st):
        print("*",end=" ")
    if i!=n-1:
        print()
    st=st-2
for i in range(n+1):
    for j in range(st):
        print("*",end=" ")
    print()
    st=st+2