def pattern(n):
      for i in range(0, n):
           for j in range(0, i + 1):
                print("* ", end="")
           print("&#92r")
      for i in range(n, 0 , -1):
          for j in range(0, i + 1):
               print("* ", end="")
          print("&#92r")
 
pattern(5)