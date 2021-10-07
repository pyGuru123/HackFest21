from tkinter import *
from tkinter import messagebox as tampil
from PIL import ImageTk, Image

import math

window=Tk()
window.title('Segiempat Sembarang')
window.configure(bg='#10171f')

openFile = Image.open("segiempat.jpg")
getImage = ImageTk.PhotoImage(openFile)

varAB=DoubleVar()
varBC=DoubleVar()
varCD=DoubleVar()
varDA=DoubleVar()
sudut1=DoubleVar()
sudut2=DoubleVar()
sudut3=DoubleVar()
sudut4=DoubleVar()

def hitung():
	msg=""
	try:
		totalSisi=varAB.get()+varBC.get()+varCD.get()+varDA.get()
		totalSudut=sudut1.get()+sudut2.get()+sudut3.get()+sudut4.get()
		varS=totalSisi/2
		#√(s - a)(s - b)(s - c)(s - d)
		hluas=(varS-varAB.get())*(varS-varBC.get())*(varS-varCD.get())*(varS-varDA.get())
		luas=round(math.sqrt(hluas),2)
		print(f"""totalSisi:{totalSisi}
			varS:{varS}
			hluas:{hluas}
			luas:{luas}
			""")
		msg="LUAS : "+str(luas)+"\nTOTAL SUDUT : "+str(totalSudut)	
	except Exception as e:
		msg="Please Enter Valid Number -- "+str(e)
	tampil.showinfo(title='!NOTICE', message=msg)

def reset():
	sisiAB.delete(0,END)
	sisiBC.delete(0,END)
	sisiCD.delete(0,END)
	sisiDA.delete(0,END)
	tSudut1.delete(0,END)
	tSudut2.delete(0,END)
	tSudut3.delete(0,END)
	tSudut4.delete(0,END)

labelimg=Label(window,image=getImage)
labelimg.grid(row=0,column=4,padx=6,columnspan=2,rowspan=6)
labelSisi=Label(window,text='SISI',font='Helvetica 10 bold',bg='#f7bb00')
labelSisi.grid(row=0,column=0,sticky='EW',columnspan=2)
labelSudut=Label(window,text='SUDUT',font='Helvetica 10 bold',bg='#1D9DCE')
labelSudut.grid(row=0,column=2,sticky='EW',columnspan=2)
bHitung=Button(window,text='Hitung',command=hitung,bg='green',fg='white',width=10,height=3,font='Arial 11',activebackground='orange')
bHitung.grid(row=5,column=0,padx=6,columnspan=2)
bReset=Button(window,text='Reset',command=reset,bg='#1D9DCE',fg='white',width=10,height=3,font='Arial 11',activebackground='orange')
bReset.grid(row=5,column=2,padx=6,columnspan=2)

labelAB=Label(window,text='SISI AB : ',bg='#10171f',fg='white',font='Courier 11 bold')
labelAB.grid(row=1,column=0,sticky='E',padx=7)
labelBC=Label(window,text='SISI BC : ',bg='#10171f',fg='white',font='Courier 11 bold')
labelBC.grid(row=2,column=0,sticky='E',padx=7)
labelCD=Label(window,text='SISI CD : ',bg='#10171f',fg='white',font='Courier 11 bold')
labelCD.grid(row=3,column=0,sticky='E',padx=7)
labelDA=Label(window,text='SISI DA : ',bg='#10171f',fg='white',font='Courier 11 bold')
labelDA.grid(row=4,column=0,sticky='E',padx=7)

labelSudut1=Label(window,text='SUDUT α1 : ',bg='#10171f',fg='white',font='Courier 11 bold')
labelSudut1.grid(row=1,column=2,sticky='E',padx=7)
labelSudut2=Label(window,text='SUDUT α2 : ',bg='#10171f',fg='white',font='Courier 11 bold')
labelSudut2.grid(row=2,column=2,sticky='E',padx=7)
labelSudut3=Label(window,text='SUDUT α3 : ',bg='#10171f',fg='white',font='Courier 11 bold')
labelSudut3.grid(row=3,column=2,sticky='E',padx=7)
labelSudut4=Label(window,text='SUDUT α4 : ',bg='#10171f',fg='white',font='Courier 11 bold')
labelSudut4.grid(row=4,column=2,sticky='E',padx=7)



sisiAB=Entry(window,bd=4,width=9,font='Arial 13 bold',textvariable=varAB,justify='center')
sisiAB.grid(row=1,column=1,pady=7)
sisiBC=Entry(window,bd=4,width=9,font='Arial 13 bold',textvariable=varBC,justify='center')
sisiBC.grid(row=2,column=1,pady=7)
sisiCD=Entry(window,bd=4,width=9,font='Arial 13 bold',textvariable=varCD,justify='center')
sisiCD.grid(row=3,column=1,pady=7)
sisiDA=Entry(window,bd=4,width=9,font='Arial 13 bold',textvariable=varDA,justify='center')
sisiDA.grid(row=4,column=1,pady=7)

tSudut1=Entry(window,bd=4,width=9,font='Arial 13 bold',textvariable=sudut1,justify='center')
tSudut1.grid(row=1,column=3,pady=7)
tSudut2=Entry(window,bd=4,width=9,font='Arial 13 bold',textvariable=sudut2,justify='center')
tSudut2.grid(row=2,column=3,pady=7)
tSudut3=Entry(window,bd=4,width=9,font='Arial 13 bold',textvariable=sudut3,justify='center')
tSudut3.grid(row=3,column=3,pady=7)
tSudut4=Entry(window,bd=4,width=9,font='Arial 13 bold',textvariable=sudut4,justify='center')
tSudut4.grid(row=4,column=3,pady=7)

window.mainloop()

