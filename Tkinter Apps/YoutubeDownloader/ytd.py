from tkinter import *
from pytube import YouTube
import os

d_font = ("Arial",10,"bold")

def check():
    video = YouTube(url.get())
    title.config(text=video.title)

window = Tk()
window.title("Youtube Downloader")
window.minsize(height=400,width = 800)
window.config(padx=10,pady=20)

head_l = Label(text="Youtube downloader Pro",font=("Arial",24,"bold"))
head_l.grid(column =2 , row=0)

url_label = Label(text="Youtube Link:",font=d_font)
url_label.grid(column=0,row=1)

url = Entry()
url.grid(column=1,row=1,columnspan=5)

check = Button(text="Check it!",command=check)
check.grid(column=6,row =1,sticky="EW")

def download():
    video = YouTube(url.get())
    destination = '.'
    if selected.get() == "mp3":
        audio_stream = video.streams.get_audio_only()
        out_file = audio_stream.download(output_path=destination)
        d_info.config(text="Downloaded!")
        base,ext = os.path.splitext(out_file)
        new_file = base+'.mp3'
        os.rename(out_file, new_file)
    elif selected.get() == '720p':
        try:
            stream = video.streams.filter(progressive = True,res='720p').first()
            out_file = stream.download(output_path=destination)
            d_info.config(text="Downloaded!")
        except:
            stream=video.streams.filter(progressive = True,res='360p').first()
            out_file = stream.download(output_path=destination)
            d_info.config(text="Downloaded!")
    
    else:
        stream=video.streams.filter(progressive = True,res='360p').first()
        out_file = stream.download(output_path=destination)
        d_info.config(text="Downloaded!")

name_l = Label(text="Name:",font=d_font)
name_l.grid(column=1,row=4)
title = Label(text="Click check to know!")
title.grid(column=2,row=4)


selected = StringVar()
selected.set("mp3")

dropdown = OptionMenu( window,selected, "mp3","720p",'360p')


download_button = Button(text="Download",command=download)







d_info = Label()




window.mainloop()