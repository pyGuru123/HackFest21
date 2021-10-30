import tkinter
import os
from tkinter import *
import tkinter.colorchooser
from tkinter import ttk, filedialog, TclError
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font, families

from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad():
    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisFormatMenu = Menu(__thisMenuBar, tearoff=0)
    __thisViewMenu = Menu(__thisMenuBar, tearoff=0)

    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    # def __init__(self):
    #     """Initialize widgets, methods."""
    #
    #     tkinter.Tk.__init__(self)
    #     self.grid()
    #
    #     fontoptions = families(self)
    #     font = Font(family="Verdana", size=10)
    #
    #     menubar = tkinter.Menu(self)
    #     #fileMenu = tkinter.Menu(menubar, tearoff=0)
    #     __thisFormatMenu = tkinter.Menu(menubar, tearoff=0)
    #     fsubmenu = tkinter.Menu(__thisFormatMenu, tearoff=0)
    #     ssubmenu = tkinter.Menu(__thisFormatMenu, tearoff=0)
    #
    #     # adds fonts to the font submenu and associates lambda functions
    #     for option in fontoptions:
    #         fsubmenu.add_command(label=option, command = lambda: font.configure(family=option))
    #     # adds values to the size submenu and associates lambda functions
    #     for value in range(1,31):
    #         ssubmenu.add_command(label=str(value), command = lambda: font.configure(size=value))
    #
    #         menubar.add_cascade(label="Format", underline=0, menu=__thisFormatMenu)
    #         __thisFormatMenu.add_cascade(label="Font", underline=0, menu=fsubmenu)
    #         __thisFormatMenu.add_cascade(label="Size", underline=0, menu=ssubmenu)
    #         __thisFormatMenu.add_command(label="Color", command=self.color)
    #         __thisFormatMenu.add_command(label="Bold", command=self.bold, accelerator="Ctrl+B")
    #         __thisFormatMenu.add_command(label="Italic", command=self.italic, accelerator="Ctrl+I")
    #         __thisFormatMenu.add_command(label="Underline", command=self.underline, accelerator="Ctrl+U")
    #         self.config(menu=menubar)
    #     # def new(self, *args):
    #     #     """Creates a new window."""
    #     #     app = Notepad()
    #     #     app.title('Python Text Editor')
    #     #     app.option_add('*tearOff', False)
    #     #     app.mainloop()
    #
    #     def color(self):
    #         """Changes selected text color."""
    #         try:
    #             (rgb, hx) = tkinter.colorchooser.askcolor()
    #             self.text.tag_add('color', 'sel.first', 'sel.last')
    #             self.text.tag_configure('color', foreground=hx)
    #         except TclError:
    #             pass
    #
    #     def bold(self, *args):
    #         """Toggles bold for selected text."""
    #         try:
    #             current_tags = self.text.tag_names("sel.first")
    #             if "bold" in current_tags:
    #                 self.text.tag_remove("bold", "sel.first", "sel.last")
    #             else:
    #                 self.text.tag_add("bold", "sel.first", "sel.last")
    #                 bold_font = Font(self.text, self.text.cget("font"))
    #                 bold_font.configure(weight="bold")
    #                 self.text.tag_configure("bold", font=bold_font)
    #         except TclError:
    #             pass
    #
    #     def italic(self, *args):
    #         """Toggles italic for selected text."""
    #         try:
    #             current_tags = self.text.tag_names("sel.first")
    #             if "italic" in current_tags:
    #                 self.text.tag_remove("italic", "sel.first", "sel.last")
    #             else:
    #                 self.text.tag_add("italic", "sel.first", "sel.last")
    #                 italic_font = Font(self.text, self.text.cget("font"))
    #                 italic_font.configure(slant="italic")
    #                 self.text.tag_configure("italic", font=italic_font)
    #         except TclError:
    #             pass
    #
    #     def underline(self, *args):
    #         """Toggles underline for selected text."""
    #         try:
    #             current_tags = self.text.tag_names("sel.first")
    #             if "underline" in current_tags:
    #                 self.text.tag_remove("underline", "sel.first", "sel.last")
    #             else:
    #                 self.text.tag_add("underline", "sel.first", "sel.last")
    #                 underline_font = Font(self.text, self.text.cget("font"))
    #                 underline_font.configure(underline=1)
    #                 self.text.tag_configure("underline", font=underline_font)
    #         except TclError:
    #             pass
    #             """Accelerator bindings. The cut, copy, and paste functions are not
    #                               bound to keyboard shortcuts because Windows already binds them, so if
    #                               Tkinter bound them as well whenever you typed ctrl+v the text would be
    #                               pasted twice."""
    #             self.bind_all("<Control-b>", self.bold)
    #             self.bind_all("<Control-i>", self.italic)
    #             self.bind_all("<Control-u>", self.underline)
    #
    #             self.text = ScrolledText(self, state='normal', height=30, wrap='word', font=Font, pady=2, padx=3,
    #                                      undo=True)
    #             self.text.grid(column=0, row=0, sticky='NSEW')
    #
    #             # Frame configuration
    #             self.grid_columnconfigure(0, weight=1)
    #             self.resizable(True, True)
    #
    #             if __name__ == "__main__":
    #                 app = Notepad()
    #                 app.title("Chintu - Notepad")
    #                 app.option_add('*tearOff', False)
    #                 app.mainloop()
    #

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("Chintu - Notepad")

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        # To give a feature of cut
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)

        # to give a feature of copy
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)

        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        # To give a feature of Font
        #self.__thisFormatMenu.add_command(label="Font", command=self.__thisFormatMenu)
        # FormatMenu = tkinter.Menu(self.__thisMenuBar)
        fsubmenu = tkinter.Menu(self.__thisMenuBar)
        ssubmenu = tkinter.Menu(self.__thisMenuBar)
        fontoptions = families(self.__root)
        font = Font(family="Verdana", size=10)
        # adds fonts to the font submenu and associates lambda functions
        for option in fontoptions:
            fsubmenu.add_command(label=option, command=lambda: font.configure(family=option))
        # adds values to the size submenu and associates lambda functions
        for value in range(1, 31):
            ssubmenu.add_command(label=str(value), command=lambda: font.configure(size=value))


        # To give a feature of editing

        self.__thisMenuBar.add_cascade(label="Format",
                                        menu=self.__thisFormatMenu)
        # adds commands to the menus
        self.__thisFormatMenu.add_cascade(label="Font", underline=0, menu=fsubmenu)
        self.__thisFormatMenu.add_cascade(label="Size", underline=0, menu=ssubmenu)
        self.__thisFormatMenu.add_command(label="Color", command=self.color)
        self.__thisFormatMenu.add_command(label="Bold", command=self.bold, accelerator="Ctrl+B")
        self.__thisFormatMenu.add_command(label="Italic", command=self.italic, accelerator="Ctrl+I")
        self.__thisFormatMenu.add_command(label="Underline", command=self.underline, accelerator="Ctrl+U")

        self.__thisMenuBar.add_cascade(label="View",
                                       menu=self.__thisViewMenu)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout)

        self.__thisViewMenu.add_command(label="Status Bar",
                                        command=self.__showStatusBar)

        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        # self.__root.__thisScrollBar.config(command=self.__thisTextArea.yview)
        # self.__root.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
        self.__root.bind_all("<Control-b>", self.bold)
        self.__root.bind_all("<Control-i>", self.italic)
        self.__root.bind_all("<Control-u>", self.underline)

        # self.__root.__thisTextArea = ScrolledText(self, state='normal', height=30, wrap='word', font=font, pady=2, padx=3, undo=True)
        # self.__root.__thisTextArea.grid(column=0, row=0, sticky='NSEW')

        # Frame configuration
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.resizable(True, True)

    def color(self):
        """Changes selected text color."""
        try:
            (rgb, hx) = tkinter.colorchooser.askcolor()
            self.__thisTextArea.tag_add('color', 'sel.first', 'sel.last')
            self.__thisTextArea.tag_configure('color', foreground=hx)
        except TclError:
            pass

    def bold(self, *args):
        """Toggles bold for selected text."""
        try:
            current_tags = self.__thisTextArea.tag_names("sel.first")
            if "bold" in current_tags:
                self.__thisTextArea.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.__thisTextArea.tag_add("bold", "sel.first", "sel.last")
                bold_font = Font(self.__thisTextArea, self.__thisTextArea.cget("font"))
                bold_font.configure(weight="bold")
                self.__thisTextArea.tag_configure("bold", font=bold_font)
        except TclError:
            pass

    def italic(self, *args):
        """Toggles italic for selected text."""
        try:
            current_tags = self.__thisTextArea.tag_names("sel.first")
            if "italic" in current_tags:
                self.__thisTextArea.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.__thisTextArea.tag_add("italic", "sel.first", "sel.last")
                italic_font = Font(self.__thisTextArea, self.__thisTextArea.cget("font"))
                italic_font.configure(slant="italic")
                self.__thisTextArea.tag_configure("italic", font=italic_font)
        except TclError:
            pass

    def underline(self, *args):
        """Toggles underline for selected text."""
        try:
            current_tags = self.__thisTextArea.tag_names("sel.first")
            if "underline" in current_tags:
                self.__thisTextArea.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.__thisTextArea.tag_add("underline", "sel.first", "sel.last")
                underline_font = Font(self.__thisTextArea, self.__thisTextArea.cget("font"))
                underline_font.configure(underline=1)
                self.__thisTextArea.tag_configure("underline", font=underline_font)
        except TclError:
            pass


    def __showStatusBar(self):
        showinfo("Notepad", "Still in progress")


    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("Notepad", "This is a the new version of notepad through Tk Inter")




    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()



    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    #def __font(self):
     #   self.__thisTextArea.event_generate("<<Font>>")

    def run(self):

        # Run main application
        self.__root.mainloop()

    # Run main application

# root=tkinter.Tk()
notepad = Notepad(width=600, height=400)
notepad.run()
