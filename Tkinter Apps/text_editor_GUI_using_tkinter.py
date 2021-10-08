# Building a basic text editor using python

# importing all things from tkinter
from tkinter import *

# creating the root window 
root = Tk()
root.geometry("750x500")

root.title("Your Notepad")

# Fixing the minimum and maximum possible dimensions of window
root.minsize(height=250, width=350)
root.maxsize(height=250, width=350)

# adding scrollbar
scrollbar = Scrollbar(root)

# packing scrollbar
scrollbar.pack(side=RIGHT,fill=Y)

text_info = Text(root, yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

# configuring the scrollbar
scrollbar.config(command=text_info.yview)

# executing the program
root.mainloop()
