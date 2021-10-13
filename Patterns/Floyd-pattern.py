#Floyd triangle pattern.


rows = int(input("Enter the total Number of Rows: "))
number = 1

print("Floyd's Pattern") 
for i in range(1, rows + 1):
    for j in range(1, i + 1):        
        print(number, end = '  ')
        number = number + 1
    print()
