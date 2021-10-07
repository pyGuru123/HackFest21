s = 5  
asciiValue = 65  
m = (2 * s) - 2  
for i in range(0, s):  
    for j in range(0, m):  
        print(end=" ")  
    # Decreased the value of after each iteration  
    m = m - 1  
    for j in range(0, i + 1):  
        alphabate = chr(asciiValue)  
        print(alphabate, end=' ')  
        # Increase the ASCII number after each iteration  
        asciiValue += 1  
    print()  
