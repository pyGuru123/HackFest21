import skimage
import os
from skimage import io
  
# Reading image file
image2 = io.imread('C:\Users\KRISHNA\Desktop\index.jpg')
  
# Setting dimensions boundaries
x = 189 / 2
y = 267 / 2
r = 189 / 6
  
# Iterating to all the pixels in the set boundaries
for i in range(0, 189):
    for j in range(0, 267):
        if i in range(0, 189 / 3):
            image2[i][j] = [255, 128, 64]     # Orange Color
        elif i in range(189 / 3, 189 * 2 / 3):
            image2[i][j] = [255, 255, 255]    # White Color
        else:
            image2[i][j] = [0, 128, 0]        # Green Color
              
            # Equation for 2px thick ring
        if (( pow((x-i), 2) + pow((y-j), 2) ) <= pow(r + 1, 2)) and(( pow((x-i), 2) + pow((y-j), 2) ) >= pow(r-2, 2)):
            image2[i][j] = [0, 0, 255]        # Blue Color
              
# Iterating within the ring 
for i in range(189 / 3, 189 * 2 / 3):
    for j in range(267 / 3, 267 * 2 / 3):
          
        # Equation to draw 4 straight lines
        if ((i == 189 / 2) or (j == 267 / 2) or (i + 39 == j or (i + 39 + j == 266))) and (( pow((x-i), 2) + pow((y-j), 2) ) <= pow(r, 2)) :
            image2[i][j] = [0, 0, 255]        # Blue Color
