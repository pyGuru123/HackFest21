def pattern(n):
     k = n - 2
     for i in range(n, -1 , -1):
          for j in range(k , 0 , -1):
               print(end=" ")
          k = k + 1    
          for j in range(0, i+1):
               print("* " , end="")
          print(" ")
     k = 2*n - 2
     for i in range(0 , n+1):
          for j in range(0 , k):
               print(end="")
          k = k - 1
          for j in range(0, i + 1):
               print("* ", end="")
          print(" ")

pattern(5)
#error issue to be opened