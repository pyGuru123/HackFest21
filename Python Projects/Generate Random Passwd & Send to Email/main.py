import tkinter
import random

class PWGenGui(tkinter.Frame):
    def __init__(self, master=None):
        self.consonants = "abcdfghjklmnpqrstvwxz"
        self.vowels = "aiueo"
        self.numbers = "0123456789"
        self.symbols = "§$%&?#+"
        self.email ="@gmail.com"

        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.consonantsLabel = tkinter.Label(self)
        self.consonantsLabel["text"] = "Username :"
        self.consonantsLabel.pack(padx="5px")
        self.consonantsEntry = tkinter.Entry(self)
        self.consonantsName = tkinter.StringVar()
        self.consonantsName.set(self.consonants)
        self.consonantsEntry["textvariable"] = self.consonantsName
        self.consonantsEntry.pack(ipadx="50px", pady="5px")

        self.vowelsLabel = tkinter.Label(self)
        self.vowelsLabel["text"] = "Consonant :"
        self.vowelsLabel.pack(padx="5px")
        self.vowelsEntry = tkinter.Entry(self)
        self.vowelsName = tkinter.StringVar()
        self.vowelsName.set(self.vowels)
        self.vowelsEntry["textvariable"] = self.vowelsName
        self.vowelsEntry.pack(ipadx="50px", pady="5px")

        self.numbersLabel = tkinter.Label(self)
        self.numbersLabel["text"] = "Number :"
        self.numbersLabel.pack(padx="5px")
        self.numbersEntry = tkinter.Entry(self)
        self.numbersName = tkinter.StringVar()
        self.numbersName.set(self.numbers)
        self.numbersEntry["textvariable"] = self.numbersName
        self.numbersEntry.pack(ipadx="50px", pady="5px")

        self.symbolsLabel = tkinter.Label(self)
        self.symbolsLabel["text"] = "Special Character :"
        self.symbolsLabel.pack(padx="5px")
        self.symbolsEntry = tkinter.Entry(self)
        self.symbolsName = tkinter.StringVar()
        self.symbolsName.set(self.symbols)
        self.symbolsEntry["textvariable"] = self.symbolsName
        self.symbolsEntry.pack(ipadx="50px", pady="5px")

        self.emailLabel = tkinter.Label(self)
        self.emailLabel["text"] = "Email Destination :"
        self.emailLabel.pack(padx="5px")
        self.emailEntry = tkinter.Entry(self)
        self.emailName = tkinter.StringVar()
        self.emailName.set(self.email)
        self.emailEntry["textvariable"] = self.emailName
        self.emailEntry.pack(ipadx="50px", pady="5px")

        self.label = tkinter.Label(self)
        self.label["text"] = "Password Are Generate"
        self.label.pack(padx="5px")
        self.spinEntry = tkinter.Spinbox(self)
        self.spin = tkinter.IntVar()
        self.spinEntry["textvariable"] = self.spin
        self.spinEntry["from_"] = 0
        self.spinEntry["to"] = 1000
        self.spinEntry.pack(after=self.label, padx="5px")

        self.labelLength = tkinter.Label(self)
        self.labelLength["text"] = "Character Are Generate"
        self.labelLength.pack(padx="5px", after=self.spinEntry)
        self.spinEntryLength = tkinter.Spinbox(self)
        self.spinLength = tkinter.IntVar()
        self.spinEntryLength["textvariable"] = self.spinLength
        self.spinEntryLength["from_"] = 0
        self.spinEntryLength["to"] = 1000
        self.spinEntryLength.pack(after=self.labelLength, padx="5px")

        self.easyCheck = tkinter.Checkbutton(self)
        self.easyCheck.pack(after=self.spinEntryLength)
        self.easyCheck["text"] = "Simple Password"
        self.easy = tkinter.BooleanVar()
        self.easy.set(True)
        self.easyCheck["variable"] = self.easy

        self.amountCheck = tkinter.Checkbutton(self)
        self.amountCheck.pack(after=self.spinEntryLength)
        self.amountCheck["text"] = "Any Number"
        self.amount = tkinter.BooleanVar()
        self.amountCheck["variable"] = self.amount

        self.symbolsCheck = tkinter.Checkbutton(self)
        self.symbolsCheck.pack(after=self.spinEntryLength)
        self.symbolsCheck["text"] = "Special Character"
        self.symbols = tkinter.BooleanVar()
        self.symbolsCheck["variable"] = self.symbols

        self.genButton = tkinter.Button(self)
        self.genButton["text"] = "Generate"
        self.genButton["command"] = self.generate
        self.genButton.pack(padx="10px", pady="5px")

        self.textOutput = tkinter.Text(self)
        self.textOutput.pack(fill="both", padx="5px", pady="5px")
        self.textOutput.tag_config("hacker", foreground="green")
        self.textOutput.tag_config("warning", foreground="red")

    def generate(self):
        import smtplib

        sender = 'your email@gmail.com' #your email
        receiver =self.emailEntry
        password = 'your password' #your password

        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(sender, password)

        msg = 'input your messages here' #input message

        smtpserver.sendmail(sender, receiver, msg)
        print('Sent')
        smtpserver.close()

        self.consonants = self.consonantsName.get()
        self.consonantsList = [i for i in self.consonants]
        self.vowels = self.vowelsName.get()
        self.vowelsList = [i for i in self.vowels]
        self.allList = self.consonantsList + self.vowelsList

        self.textOutput.delete(1.0, "end")
        if self.spin.get() == 0 or self.spinLength.get() == 0:
            self.textOutput.insert("end", "Theres Nothing Password You Input", "warning")
            return 0

        for i in range(0, self.spin.get()):
            output = ""
            characterBool = True
            if self.easy.get():
                if self.amount.get():
                    for k in range(0, self.spinLength.get() - 1):
                        if characterBool == True:
                            output += random.choice(self.consonantsList)
                            characterBool = False
                        else:
                            output += random.choice(self.vowelsList)
                            characterBool = True
                    output += random.choice(self.numbers)
                else:
                    for k in range(0, self.spinLength.get()):
                        if characterBool == True:
                            output += random.choice(self.consonantsList)
                            characterBool = False
                        else:
                            output += random.choice(self.vowelsList)
                            characterBool = True
            else:
                for k in range(0, self.spinLength.get()):
                    output += random.choice(self.allList)

            output += "\n"
            self.textOutput.insert("end", output, "hacker")

if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("300x700")
    root.wm_title("Random Password Generator")
    app = PWGenGui(root)
    app.mainloop()
