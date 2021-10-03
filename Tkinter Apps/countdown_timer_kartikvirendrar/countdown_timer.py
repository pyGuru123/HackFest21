from tkinter import *
import time
count = Tk()
count.geometry("1200x700")
count. title('Countdown Timer')

hr=StringVar() 
mn=StringVar() 
sc=StringVar() 
hr.set("00") 
mn.set("00") 
sc.set("00")
hourEntry= Entry(count, width=3, font=("Arial",18,""), textvariable=hr) 
hourEntry.place(x=550,y=200) 
minuteEntry= Entry(count, width=3, font=("Arial",18,""), textvariable=mn) 
minuteEntry.place(x=600,y=200) 
secondEntry= Entry(count, width=3, font=("Arial",18,""), textvariable=sc) 
secondEntry.place(x=650,y=200)

def start(): 
    try: 
        a = int(hr.get())*3600 + int(mn.get())*60 + int(sc.get()) 
    except: 
        messagebox.showinfo("Countdown Timer","Input value incorrect")
    while a >-1: 
        m= a//60
        s=a%60
        h=0
        if m>60:
            h=a//60
            m=a%60
        hr.set("{0:2d}".format(h))
        mn.set("{0:2d}".format(m))
        sc.set("{0:2d}".format(s))
        count.update()
        time.sleep(1)
        if (a==0):
            messagebox.showinfo("Countdown Timer","Time,s Up")
        a-=1
        
strbtn = Button(count, text='Start Counter', width=20, height= 3, command=start)
strbtn.place(x=550,y=400)

def reset():
    hr.set("{0:2d}".format(0))
    mn.set("{0:2d}".format(0))
    sc.set("{0:2d}".format(0))
    count.update()
    
rsbtn = Button(count, text='Reset Counter', width=20, height= 3, command=reset)
rsbtn.place(x=550,y=500)
mainloop()