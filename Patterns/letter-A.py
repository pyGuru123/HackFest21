# Python3 program to print alphabet A pattern

# Function to display alphabet pattern
def display(n):

	# Outer for loop for number of lines
	for i in range(n):

		# Inner for loop for logic execution
		for j in range((n // 2) + 1):

			# prints two column lines
			if ((j == 0 or j == n // 2) and i != 0 or

				# print first line of alphabet
				i == 0 and j != 0 and j != n // 2 or

				# prints middle line
				i == n // 2):
				print("*", end = "")
			else:
				print(" ", end = "")
		
		print()
	

# Driver Function
display(7)

