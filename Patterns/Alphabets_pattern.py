#!/usr/bin/env python
# coding: utf-8

# # Alphabets pattern print using given symbol from A to Z

# ### If a given value is string then for that character pattern will be printed else Z will be printed and if a given value is other than string then that value itself will be printed !
# 
# #### This project is just for fun and will be usefull for displaying any character with pattern 

# In[115]:


#Height and width allows to create a user-defined sized alphabet's pattern, Number of lines for the alphabet's pattern
height = 5

# Number of character width in each line
width = (2 * height) - 1

# Function to find the absolute value of a number D
def abs(d):
	if d < 0:
		return -1*d
	else:
		return d

# Function to print the pattern of 'A'
def printA(pattern):

	n = width // 2
	for i in range(0, height):
		for j in range(0, width+1):
			if (j == n or j == (width - n) or (i == (height // 2) and j > n and j < (width - n))):
				print(pattern, end="")
			else:
				print(end=" ")
		print()
		n = n-1

# Function to print the pattern of 'B'
def printB(pattern) :
	half = height // 2

	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,width) :
			if ((i == 0 or i == height - 1 or i == half) and j < (width - 2)) :
				print(pattern,end="")
			elif (j == (width - 2) and not(i == 0 or i == height - 1 or i == half)) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'C'
def printC(pattern) :

	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height - 1) :
			if (i == 0 or i == height - 1 ) :
				print(pattern,end="")
			else :
				continue
		print()

# Function to print the pattern of 'D'
def printD(pattern) :
	
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height) :
			if ( (i == 0 or i == height - 1) and j < height - 1 ):
				print(pattern,end="")
			elif (j == height - 1 and i != 0 and i != height - 1) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'E'
def printE(pattern) :
	
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height) :
			if ( (i == 0 or i == height - 1) or (i == height // 2 and j <= height // 2) ):
				print(pattern,end="")
			else :
				continue
		print()

# Function to print the pattern of 'F'
def printF(pattern) :
	
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height) :
			if ( (i == 0) or (i == height // 2 and j <= height // 2) ):
				print(pattern,end="")
			else :
				continue
		print()

# Function to print the pattern of 'G'
def printG(pattern) :

	for i in range(0,height) :
		for j in range(0,width-1) :
			if ((i == 0 or i == height - 1) and (j == 0 or j == width - 2)) :
				print(end=" ")
			elif (j == 0) :
				print(pattern,end="")
			elif (i == 0 and j <= height) :
				print(pattern,end="")
			elif (i == height // 2 and j > height // 2) :
				print(pattern,end="")
			elif (i > height // 2 and j == width - 2) :
				print(pattern,end="")
			elif (i == height - 1 and j < width - 1 ) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'H'
def printH(pattern) :
	
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height) :
			if ( (j == height - 1) or (i == height // 2) ):
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'I'
def printI(pattern) :
	
	for i in range(0,height) :
		for j in range(0,height) :
			if ( i == 0 or i == height - 1 ):
				print(pattern,end="")
			elif ( j == height // 2 ) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'J'
def printJ(pattern) :
	
	for i in range(0,height) :
		for j in range(0,height) :
			if ( i == height - 1 and (j > 0 and j < height - 1) ):
				print(pattern,end="")
			elif ( (j == height - 1 and i != height - 1) or (i > (height // 2) - 1 and j == 0 and i != height - 1) ) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'K'
def printK(pattern) :
	half = height // 2
	dummy = half
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,half+1) :
			if ( j == abs(dummy) ):
				print(pattern,end="")
			else :
				print(end=" ")
		print()
		dummy = dummy -1

# Function to print the pattern of 'L'
def printL(pattern) :
	
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height+1) :
			if ( i == height - 1 ):
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'M'
def printM(pattern) :
	counter = 0
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height+1) :
			if ( j == height ):
				print(pattern,end="")
			elif ( j == counter or j == height - counter - 1 ) :
				print(pattern,end="")
			else :
				print(end=" ")
		if(counter == height // 2) :
			counter = -99999
		else :
			counter = counter + 1
		
		print()

# Function to print the pattern of 'N'
def printN(pattern) :
	counter = 0
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height+1) :
			if ( j == height ):
				print(pattern,end="")
			elif ( j == counter) :
				print(pattern,end="")
			else :
				print(end=" ")
		counter = counter + 1
		print()

# Function to print the pattern of 'O'
def printO(pattern) :
	space = height // 3
	width = height // 2 + height // 5 + space + space
	for i in range(0,height) :
		for j in range(0,width + 1) :
			if ( j == width - abs(space) or j == abs(space)):
				print(pattern,end="")
			elif( (i == 0 or i == height - 1) and j > abs(space) and j < width - abs(space) ) :
				print(pattern,end="")
			else :
				print(end=" ")

		if( space != 0 and i < height // 2) :
			space = space -1
		elif ( i >= (height // 2 + height // 5) ) :
			space = space -1

		print()

# Function to print the pattern of 'P'
def printP(pattern) :
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height) :
			if ( (i == 0 or i == height // 2) and j < height - 1 ):
				print(pattern,end="")
			elif ( i < height // 2 and j == height - 1 and i != 0 ) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'Q'
def printQ(pattern) :
	printO(pattern)
	d = height
	for i in range(0,height//2) :
		for j in range(0,d+1) :
			if ( j == d ):
				print(pattern,end="")
			else :
				print(end=" ")
		print()
		d = d+1

# Function to print the pattern of 'R'
def printR(pattern) :
	half = (height // 2)
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,width) :
			if ( (i == 0 or i == half) and j < (width - 2) ):
				print(pattern,end="")
			elif ( j == (width - 2) and not(i == 0 or i == half) ) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'S'
def printS(pattern) :
	for i in range(0,height) :
		for j in range(0,height) :
			if ( (i == 0 or i == height // 2 or i == height - 1) ):
				print(pattern,end="")
			elif ( i < height // 2 and j == 0 ) :
				print(pattern,end="")
			elif ( i > height // 2 and j == height - 1 ) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'T'
def printT(pattern) :
	for i in range(0,height) :
		for j in range(0,height) :
			if ( i == 0 ):
				print(pattern,end="")
			elif ( j == height // 2 ) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'U'
def printU(pattern) :
	for i in range(0,height) :
		if (i != 0 and i != height - 1) :
			print(pattern,end="")
		else :
			print(end = " ")
		for j in range(0,height) :
			if ( ((i == height - 1) and j >= 0 and j < height - 1) ):
				print(pattern,end="")
			elif ( j == height - 1 and i != 0 and i != height - 1 ) :
				print(pattern,end="")
			else :
				print(end=" ")
		print()

# Function to print the pattern of 'V'
def printV(pattern) :
	counter = 0
	for i in range(0,height) :
		for j in range(0,width+1) :
			if ( j == counter or j == width - counter - 1 ):
				print(pattern,end="")
			else :
				print(end=" ")

		counter = counter + 1
		print()

# Function to print the pattern of 'W'
def printW(pattern) :
	counter = height // 2
	for i in range(0,height) :
		print(pattern,end="")
		for j in range(0,height+1) :
			if ( j == height ):
				print(pattern,end="")
			elif ( (i >= height // 2) and (j == counter or j == height - counter - 1) ) :
				print(pattern,end="")
			else :
				print(end=" ")
		if( i >= height // 2) :
			counter = counter + 1
		print()

# Function to print the pattern of 'X'
def printX(pattern) :
	counter = 0
	for i in range(0,height+1) :
		for j in range(0,height+1) :
			if ( j == counter or j == height - counter ):
				print(pattern,end="")
			else :
				print(end=" ")
		counter = counter + 1
		print()

# Function to print the pattern of 'Y'
def printY(pattern) :
	counter = 0
	for i in range(0,height) :
		for j in range(0,height+1) :
			if ( j == counter or j == height - counter and i <= height // 2 ):
				print(pattern,end="")
			else :
				print(end=" ")
		print()
		if (i < height // 2) :
			counter = counter + 1

# Function to print the pattern of 'Z'
def printZ(pattern) :
	counter = height - 1
	for i in range(0,height) :
		for j in range(0,height) :
			if ( i == 0 or i == height - 1 or j == counter ):
				print(pattern,end="")
			else :
				print(end=" ")
		counter = counter - 1
		print()


# Function print the pattern of the
# alphabets from A to Z

def patternprint(values,pattern="*") :
    """
    This function returns symbols in a pattern form for any given characters

Inputs:
    1. values [Required]
    2. pattern [Optional]

Output: output data depends on given inputs

Example: 
    Input: patternprint('Oct','L')
    Output: 
                 LLLL 
                L    L
                L    L
                L    L
                 LLLL 
                LLLLL
                L
                L
                L
                LLLLL
                LLLLL
                  L  
                  L  
                  L  
                  L  
    """
    if isinstance(values, str):
        for character in values:
            if isinstance(character, str):
                character=character.upper()
                if character == 'A' :  printA(pattern)
                elif character == 'B':  printB(pattern)
                elif character == 'C':  printC(pattern)
                elif character == 'D':  printD(pattern)
                elif character == 'E':  printE(pattern),
                elif character == 'F':  printF(pattern),
                elif character == 'G':  printG(pattern),
                elif character == 'H':  printH(pattern),
                elif character == 'I':  printI(pattern),
                elif character == 'J':  printJ(pattern),
                elif character == 'K':  printK(pattern),
                elif character == 'L':  printL(pattern),
                elif character == 'M':  printM(pattern),
                elif character == 'N':  printN(pattern),
                elif character == 'O':  printO(pattern),
                elif character == 'P':  printP(pattern),
                elif character == 'Q':  printQ(pattern),
                elif character == 'R':  printR(pattern),
                elif character == 'S':  printS(pattern),
                elif character == 'T':  printT(pattern),
                elif character == 'U':  printU(pattern),
                elif character == 'V':  printV(pattern),
                elif character == 'W':  printW(pattern),
                elif character == 'X':  printX(pattern),
                elif character == 'Y':  printY(pattern)
                else : printZ(pattern)
            else:
                print(str(character))
    else:
        print(str(values))
#Adding user input modifiying the file it helps the user to input their own
ch=input("enter a word you want to see:\n")
ch1=input("enter character you want to work with\n");
patternprint(ch,ch1)
