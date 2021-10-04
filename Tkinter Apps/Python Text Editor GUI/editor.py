import os
from tkinter import *
from tkinter import filedialog
from tkinter import font

window = Tk()
window.title('Python Text Editor.')
window.iconbitmap('python.ico')
window.geometry('1080x660')

# Set variable for open file
global open_status_name
global selected

selected = False
open_status_name = False

# Create new file
def new_file(e):
    my_text.delete("1.0", END)
    window.title('New file - Python Text Editor.')
    status_bar.config(text="New file            ")

    global open_status_name
    open_status_name = False

# Open a file
def open_file(e):
    my_text.delete("1.0", END)

    text_file = filedialog.askopenfilename(
        title="Open file.", 
        filetypes=(
            ("Text Files", "*.txt"),
            ("HTML Files", "*.html"),
            ("Javascript files", "*.js"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
            )
        )
    
    if text_file:

        global open_status_name
        open_status_name = text_file

        name = text_file
        status_bar.config(text=f'{name}     ')

        # Set window title
        name = os.path.basename(text_file)
        name = name.replace("' mode='r' encoding='UTF-8'>", "")
        window.title(f'{name} - Python Text Editor.')

        # Opening the file
        text_file = open(text_file, 'r')
        word = text_file.read()

        my_text.insert(END, word)
        text_file.close()
    else:
        status_bar.config(text="Nothing chosen.         ")

# Save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(
        defaultextension=".*", 
        title="Save file", 
        filetypes=(
            ("Text Files", "*.txt"),
            ("HTML Files", "*.html"),
            ("Javascript files", "*.js"),
            ("Python Files", "*.py"),
            ("All Files", "*.*")
            )
        )
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved: {name}     ')

        name = os.path.basename(text_file)
        name = name.replace("' mode='r' encoding='UTF-8'>", "")
        window.title(f'{name} - Python Text Editor.')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

# Save file
def save_file(e):
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

        status_bar.config(text=f'Saved: {open_status_name}     ')
    else:
        save_as_file()

# Cut Text
def cut_text(e):
    global selected
    if e:
        selected = window.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            window.clipboard_clear()
            window.clipboard_append(selected)

# Copy Text
def copy_text(e):
    global selected

    if e:
        selected = window.clipboard_get()
    
    if my_text.selection_get():
        selected = my_text.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected)

# Paste Text
def paste_text(e):
    global selected

    if e:
        selected = window.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

# Bold text
def bold_it(e):
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    my_text.tag_configure("bold", font=bold_font)

    current_tags = my_text.tag_names("sel.first")

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

# Italics text
def italics_it(e):
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    my_text.tag_configure("italic", font=italics_font)

    current_tags = my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

# Underline text
def underline_it(e):
    underlines_font = font.Font(my_text, my_text.cget("font"))
    underlines_font.configure(underline= True)

    my_text.tag_configure("underline", font=underlines_font)

    current_tags = my_text.tag_names("sel.first")

    if "underline" in current_tags:
        my_text.tag_remove("underline", "sel.first", "sel.last")
    else:
        my_text.tag_add("underline", "sel.first", "sel.last")

# Main frame of editor
my_frame = Frame(window)
my_frame.pack(pady=5)

# Frame vertical scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Frame horizontal scrollbar
horizontal_scroll = Scrollbar(my_frame, orient='horizontal')
horizontal_scroll.pack(side=BOTTOM, fill=X)

# Text body
my_text = Text(
    my_frame, 
    width=90, 
    height=25, 
    font=("Times New Roman", 16), 
    selectbackground='purple', 
    selectforeground='white',
    undo=True,
    yscrollcommand=text_scroll.set,
    xscrollcommand=horizontal_scroll.set,
    wrap="none"
)
my_text.pack()

# Configure Scrollbar
text_scroll.config(command=my_text.yview)
horizontal_scroll.config(command=my_text.xview)

# Create menu
my_menu = Menu(window)
window.config(menu=my_menu)

# Menu file list
file_menu = Menu(my_menu, tearoff="off")

my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New            ", command=lambda: new_file(False), accelerator="Ctrl + N")
file_menu.add_command(label="Open           ", command=lambda: open_file(False), accelerator="Ctrl + O")
file_menu.add_command(label="Save           ", command=lambda: save_file(False), accelerator="Ctrl + S")
file_menu.add_command(label="Save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

# Menu edit list
edit_menu = Menu(my_menu, tearoff="off")

my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut              ", command=lambda: cut_text(False), accelerator="Ctrl + X")
edit_menu.add_command(label="Copy           ", command=lambda: copy_text(False), accelerator="Ctrl + C")
edit_menu.add_command(label="Paste           ", command=lambda: paste_text(False), accelerator="Ctrl + V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl + Z")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="Ctrl + Y")

# Menu text list
text_menu = Menu(my_menu, tearoff="off")
my_menu.add_cascade(label="Text", menu=text_menu)
text_menu.add_command(label="Bold           ", command=lambda: bold_it(False), accelerator="Ctrl + B")
text_menu.add_command(label="Italic           ", command=lambda: italics_it(False), accelerator="Ctrl + L")
text_menu.add_command(label="Underline           ", command=lambda: underline_it(False), accelerator="Ctrl + U")



# Add status bar
status_bar = Label(window, text='Ready          ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Bind shortcut
window.bind('<Control-Key-s>', save_file)
window.bind('<Control-Key-n>', new_file)
window.bind('<Control-Key-o>', open_file)
window.bind('<Control-Key-x>', cut_text)
window.bind('<Control-Key-c>', copy_text)
window.bind('<Control-Key-v>', paste_text)
window.bind('<Control-Key-b>', bold_it)
window.bind('<Control-Key-l>', italics_it)
window.bind('<Control-Key-u>', underline_it)

window.mainloop()