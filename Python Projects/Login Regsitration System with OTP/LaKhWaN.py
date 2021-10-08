"""
Welcome to this project. This project gives an idea how an OTP based Login Register system is created.
I have used SMTP Library (Simple mail transfer protocol) with which I am sending the OTP the client.
I have used MySQL Database for storing the email, username and password.
You can find the SQL file too. 
Note: If you want to use this, you have to enter your email ID and password so it can use that email.
You can create a new one if you don't want to give personal. If you want to get from me, ask me over whatsapp.
"""
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
import random
import smtplib
import time

# Creating a server to send mails.
# Enter the details for your email id and password you create a new one too. This e-mail would be used to send emails. for OTP
# Change your@email.com to your email and password to your password.
# Make sure you turn off the less secure app so that you can use your email to send emails.
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("lakhwanpython@gmail.com","Lakhwanpython96")

# Creating a connnection and cursor with the database and checking the connection.
try:
    mydb = sql.connect(host="localhost",user="root",passwd="",database="python")
    print("Connection with database established successfully! - REGISTER.PY")
except:
    print("Failed to connect with the database. Exiting...")
    exit()
mycursor = mydb.cursor()

# Functions
def otpGen():
    length = 5
    otp = str(random.randrange(0,9))
    for i in range(length):
        otp+=str(random.randrange(0,9))
    return otp

def Otp():  
    email = emailEntry.get()
    if email !='' and '@' not in email:
        msg = "Please enter correct email!"
    elif email == '':
        msg = "Please don't leave this field blank!"
    else:
        global otp
        otp = otpGen()
        print(otp,email)
        server.sendmail("lakhwanpython@gmail.com",email,otp)
        msg = "One Time Password has been sent to you mail!"
    messagebox.showinfo("Register",msg)

def otpLogin():
    username = usernameEntry.get()
    query = f"SELECT email FROM users WHERE username = '{username}'"
    mycursor.execute(query)
    try:
        email = mycursor.fetchone()[0]
    except:
        messagebox.showinfo("Login","No User found!")
        return None
    global otp
    otp = otpGen()
    print(otp,email)
    server.sendmail("lakhwanpython@gmail.com",email,otp)
    messagebox.showinfo("Login","OTP has been sent to your email!")

def login():
    global username
    username = usernameEntry.get()
    password = passwordEntry.get()
    OTP = otpEntry.get()
    query = f"SELECT password FROM users WHERE username = '{username}'"
    mycursor.execute(query)
    try:
        password_sql = mycursor.fetchone()[0]
    except:
        messagebox.showinfo("Login","No User found!")
        return None
    if password == password_sql:
            if otp == OTP:
                messagebox.showinfo("Login","You have logged In")
                root.destroy()
                HomeWindow()
            else:
                messagebox.showinfo("Login","You have entered incorrect OTP please try again.")
    else:
        messagebox.showinfo("Login","You have entered incorrect password please try again!")

def register():
    username = usernameEntry.get()
    password = passwordEntry.get()
    email = emailEntry.get()
    OTP = otpEntry.get()

    query = f"SELECT username FROM users"
    mycursor.execute(query)
    users = mycursor.fetchall()
    for user in users:
        if user[0] == username:
            messagebox.showinfo("Register","Username already taken")
            return None
    if len(password) < 6:
        messagebox.showinfo("Register","Password length must be 6-24 characters")
        return None
    if OTP != otp:
        messagebox.showinfo("Register","Incorrect OTP please try again.")
        return None
    query = f"INSERT INTO users VALUES('{username}','{email}','{password}')"
    mycursor.execute(query)
    mydb.commit()
    messagebox.showinfo("Register","You have been registered please login to continue.")
    root.destroy()
    mainWindow()

def back():
    root.destroy()
    mainWindow()

def RegWindow():
    global root
    root = Tk()
    root.title("Register - LaKhWaN")
    root.geometry("800x600")
    root.configure(bg="#3399ff")
    # Labels
    Label(root,text="Registration",font="courier 25 bold underline",bg="#3399ff").grid(row=0,column=0)
    Label(root,text="",bg="#3399ff").grid(row=1,column=0)
    Label(root,text="Username: ",font="courier 15 bold",bg="#3399ff").grid(row=2,column=0)
    Label(root,text="Password: ",font="courier 15 bold",bg="#3399ff").grid(row=3,column=0)
    Label(root,text="Email: ",font="courier 15 bold",bg="#3399ff").grid(row=4,column=0)
    Label(root,text="OTP: ",font="courier 15 bold",bg="#3399ff").grid(row=5,column=0)

    # Creating Enteries

    username = StringVar()
    password = StringVar()
    email = StringVar()
    otp = StringVar()

    global usernameEntry
    global emailEntry
    global passwordEntry
    global otpEntry

    usernameEntry = Entry(root,textvariable=username,bg="#3399ff")
    passwordEntry = Entry(root,textvariable=password,bg="#3399ff")
    emailEntry = Entry(root,textvariable=email,bg="#3399ff")
    otpEntry = Entry(root,textvariable=otp,bg="#3399ff")

    usernameEntry.grid(row=2,column=1)
    passwordEntry.grid(row=3,column=1)
    emailEntry.grid(row=4,column=1)
    otpEntry.grid(row=5,column=1)

    # Creating Button

    Button(root,text="Register",command=register,padx=30,bg="#33ccff").grid(row=6,column=1)
    Button(root,text="Back",command=back,padx=30,bg="#33ccff").grid(row=6,column=0)
    Button(root,text="Get OTP",command=Otp,padx=10,bg="#33ccff").grid(row=4,column=3,padx=10)
    root.mainloop()

def LoginWindow():
    global root
    root = Tk()
    root.title("Login - LaKhWaN")
    root.geometry("800x600")
    root.configure(bg="#3399ff")
    # Labels
    Label(root,text="Login",font="courier 25 bold underline",bg="#3399ff").grid(row=0,column=0)
    Label(root,text="",bg="#3399ff").grid(row=1,column=0)
    Label(root,text="Username: ",font="courier 15 bold",bg="#3399ff").grid(row=2,column=0)
    Label(root,text="Password: ",font="courier 15 bold",bg="#3399ff").grid(row=3,column=0)
    Label(root,text="OTP: ",font="courier 15 bold",bg="#3399ff").grid(row=4,column=0)

    # Creating Enteries

    username = StringVar()
    password = StringVar()
    otp = StringVar()

    global usernameEntry
    global passwordEntry
    global otpEntry

    usernameEntry = Entry(root,textvariable=username,bg="#3399ff")
    passwordEntry = Entry(root,textvariable=password,bg="#3399ff")
    otpEntry = Entry(root,textvariable=otp,bg="#3399ff")

    usernameEntry.grid(row=2,column=1)
    passwordEntry.grid(row=3,column=1)
    otpEntry.grid(row=4,column=1)

    # Creating Button

    Button(root,text="Login",command=login,padx=30,bg="#33ccff").grid(row=5,column=1)
    Button(root,text="Back",command=back,padx=30,bg="#33ccff").grid(row=5,column=0)
    Button(root,text="Get OTP",command=otpLogin,padx=10,bg="#33ccff").grid(row=4,column=3,padx=10)
    root.mainloop()

def btnRegWindow():
    root.destroy()
    RegWindow()

def btnLoginWindow():
    root.destroy()
    LoginWindow()

def Exit():
    root.destroy()

def mainWindow():
    global root
    root = Tk()
    root.title("Home - LaKhWaN")
    root.geometry("800x600")
    root.configure(bg="#3399ff")
    
    frame = Frame(root,bg="#3399ff")
    frame.pack(side=TOP)

    Label(frame,text="Welcome to LaKhWaN's Project",font="courier 23 bold italic",bg="#3399ff").pack(side=TOP)
    Label(frame,text="Please login in to continue",font="comicsansms 16",bg="#3399ff").pack(side=TOP)

    frame1 = Frame(root,borderwidth=2,relief=SUNKEN,bg="#3399ff")
    frame1.pack(side=TOP)
    Button(frame1,text="Register",padx=10,pady=3,command=btnRegWindow,bg="#33ccff").pack(side=LEFT,padx=5,pady=5)
    Button(frame1,text="Exit",padx=10,pady=3,command=Exit,bg="#33ccff").pack(side=LEFT,padx=5,pady=5)
    Button(frame1,text="Log In",padx=10,pady=3,command=btnLoginWindow,bg="#33ccff").pack(side=RIGHT,padx=5,pady=5)

    root.mainloop()

def changePass():
    root.destroy()
    changePassWindow()

def changePassWindow():
    global root
    root = Tk()
    root.title("Password Change - LaKhWaN")
    root.geometry("343x333")
    root.configure(bg="#3399ff")

    Label(root,text="Password Changer\n",font="courier 23 bold",bg="#3399ff").pack(side=TOP)

    frame = Frame(root,bg="#3399ff")
    frame.pack(side=TOP)

    Label(frame,text="Current Password: ",font="comicsans 10 bold",bg="#3399ff").grid(row=0,column=0)
    Label(frame,text="New Password: ",font="comicsans 10 bold",bg="#3399ff").grid(row=1,column=0)

    global currPass
    global newPass

    currPass = StringVar()
    newPass = StringVar()

    currPassEntry = Entry(frame,textvariable=currPass,bg="#3399ff")
    currPassEntry.grid(row=0,column=1)

    newPassEntry = Entry(frame,textvariable=newPass,bg="#3399ff")
    newPassEntry.grid(row=1,column=1)

    Button(frame,text="Submit",command=btnChangePass,bg="#33ccff").grid(row=2,column=1,ipadx=30)

    root.mainloop()

def btnChangePass():
    query = f"SELECT password FROM users WHERE username = '{username}'"
    mycursor.execute(query)
    passwd = mycursor.fetchone()[0]
    password = currPass.get()
    newPassword = newPass.get()
    if passwd == password:
        if newPassword == passwd:
            messagebox.showinfo("Change Password","You entered the same password, please try again.")
            return None
        else:
            query = f"UPDATE users SET password ='{newPassword}'\
            WHERE username= '{username}'"
            mycursor.execute(query)
            mydb.commit()
            messagebox.showinfo("Change Password","Password updated successfully. Going Back to menu...")
            root.destroy()
            HomeWindow()
    else:
        messagebox.showerror("Change Password","You have entered wrong password. Please try again.")

def HomeWindow():
    global root
    root = Tk()
    root.title("Home - LaKhWaN")
    root.geometry("800x600")
    root.configure(bg="#3399ff")
    
    Label(root,text="Home - LaKhWaN",font="courier 23 bold underline",bg="#3399ff").pack(side=TOP)
    Label(root,text="What would you like to do?\n",font="courier 13 bold underline",bg="#3399ff").pack(side=TOP)

    frame = Frame(root,borderwidth=2,relief=GROOVE,bg="#3399ff")
    frame.pack(side=TOP)

    Button(frame,text="Chat Lobby (Under development)",padx=34,pady=5,command=ChatWindowLoad,bg="#33ccff").grid(row=0,column=0,ipadx=10,ipady=10)
    Button(frame,text="Change Password",padx=30,pady=5,command=changePass,bg="#33ccff").grid(row=0,column=1,ipadx=10,ipady=10)
    root.mainloop()

def mainChatWindow():
    global root
    root = Tk()
    root.title(f"LaKhWaN - {username} - {chatId}")
    root.configure(bg="#3399ff")

    global txtYourMessage
    global txtMessages
    

    txtMessages = Text(root, width=50)
    txtMessages.grid(row=0, column=0, padx=10, pady=10)

    txtYourMessage = Entry(root, width=50)
    txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

    btnSendMessage = Button(root, text="Send", width=20, command=sendMessage,bg="#33ccff")
    btnSendMessage.grid(row=2, column=0, padx=10, pady=10)
    btnSendMessage = Button(root, text="Send", width=20, command=sendMessage,bg="#33ccff")
    btnSendMessage.grid(row=2, column=1, padx=10, pady=10)
    btnSendMessage = Button(root, text="Exit", width=20,command=Exit,bg="#33ccff")
    btnSendMessage.grid(row=2, column=2, padx=10, pady=10)

    root.mainloop()
        
def refresh():
    listenMsg()

def sendMessage():
    msg = txtYourMessage.get()
    query = f'INSERT INTO tkchat VALUES("{chatId}","{username}","{msg}")'
    mycursor.execute(query)
    mydb.commit()
    txtMessages.insert(END,username+": "+msg + "\n")

def listenMsg(lastmsg=""):
    query = f"SELECT username,msg FROM tkchat WHERE username != '{username} AND chatId = {chatId}'"
    mycursor.execute(query)
    msgs = mycursor.fetchall()
    mydb.commit()
    for i in range(len(msgs)-1,0,-1):
        if msgs[i][0] != username:
            user = msgs[i][0]
            LastMsg = msgs[i][1]
            break
    if msgs!= []:
        # time.sleep(1)
        if LastMsg.lower() != lastmsg.lower():
            txtMessages.insert(END,user+": "+LastMsg + "\n")
            return LastMsg
    else:
        print("No new message yet!")

def enterChat():
    # global username
    global chatId

    # username = usernameEntry.get()
    chatId = chatIdEntry.get()
    # if len(username) <6:
        # messagebox.showinfo("Chat","Please enter username between 6-24 length")
        # return None
    if len(chatId) < 3:
        messagebox.showinfo("Chat","Please enter valid Chat-ID (3 character).")
        return None
    
    root.destroy()
    mainChatWindow()

def ChatWindowLoad():
    return None
    root.destroy()
    ChatWindow()

def ChatWindow():
    global root
    root = Tk()
    root.title("Chat - LaKhWaN")
    root.geometry("333x333")
    root.configure(bg="#3399ff")

    Label(root,text="Lobby Id: ",font="courier 18 bold",bg="#3399ff").grid(row=1,column=0)

    chatId = StringVar()
    global chatIdEntry

    chatIdEntry = Entry(root,textvariable=chatId,bg="#3399ff")
    chatIdEntry.grid(row=1,column=1,ipadx=10,ipady=3)

    Button(root,text="Enter",command=enterChat,padx=50,bg="#33ccff").grid(row=3,column=1)

    root.mainloop()


if __name__ == "__main__":
    mainWindow()
