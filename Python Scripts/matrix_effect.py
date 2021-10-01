#! python3

import os
import random

c = random.randint(1, 6)
length = random.randint(12, 20)
text_color = f'0{c}'
with open('matrix.bat','w') as file:
	file.write('@echo off\n')
	file.write(f'color {text_color}\n')
	file.write(':a \n')
	file.write(f"echo {'%random%' * length}\n")
	file.write('goto a')

os.system('matrix.bat')