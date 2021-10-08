
def createPattern(n : int):
	for i in range(1, 2 * n):
		for k in range(1, 2 * n):
			if i == k or (i + k) == 2 * n:
				print("*", end ="")
			else:
				print(" ", end = "")
		print()



print("Enter the number of rows : ")
n = int(input())
print()
createPattern(n)