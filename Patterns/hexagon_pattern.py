count = int(input("Enter the length of side: "))

length = 2 * count - 1

for top in range(0, count):

        col = top + count

        for k in range(0, col):
        
                if ((k == count + top - 1) or (k == count - top - 1)):
                        print("*", end = "")
                else:
                        print(" ", end = "")
        
        print("")

for mid in range(0, count - 2):

        for j in range(0, length):
                
                if (j == 0 or j == length - 1):
                        print("*", end = "")
                else:
                        print(" ", end = "")
        
        print("")

reverse = count - 1
for down in range(reverse, -1, -1):
        col = down + count
        for k in range(0, col):
                if ((k == count + down - 1) or (k == count - down - 1)):
                        print("*", end = "")
                else:
                        print(" ", end = "")
                        
        print("")
