from prettytable import PrettyTable

print('--------------WELCOME TO XYZ Shop--------------\n')
table = PrettyTable(['Item Name', 'Item Price'])
total = 0

while 1:
    name = input('Enter Item name:')

    # 'q' to exit and print the table 
    if name != 'q':
        price = int(input('Enter the Price:'))

        # store all the prices in 'total' 
        total += price
        table.add_row([name, price])
        continue

    elif name == 'q':
        break

table.add_row(['TOTAL', total])
print(table)
print('\nThanks for shopping with us :)')
print('Your total bill amount is ', total, '/-\n')
x = int(input("Press 1 to exit---"))
