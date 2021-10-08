# Biulding a Basic Voice recorder using Python

#Import necessary modules
import sounddevice as sd
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import queue
import soundfile as sf
import threading
from PIL import ImageTk, Image

# Creating the root winodw
root = Tk()
root.geometry("300x400")
root.title("Your Voice Recorder")
root.config(bg="white")

recording = False
audio_exists = False    

# Queue to save audio 
q = queue.Queue()

# Fit data into queue
def call_function(indata, frames, time, status):
    q.put(indata.copy())

# Functions to play, stop and record audio
def threading_rec(x):

    if x == 1:
        # the thread is activated when recording is selected
        t1=threading.Thread(target= record_audio)
        t1.start()
        
    elif x == 2:
        # set the flag to false to stop recording
        global recording
        recording = False
        messagebox.showinfo(message="Recording finished!")

    elif x == 3:
        if audio_exists:
            # Play the recording is it exists
            data, fs = sf.read("recording.wav", dtype='float32') 
            sd.play(data,fs)
            sd.wait()
        else:
            # Show error message if recording is not found
            messagebox.showerror(message="No recordings found, record something to play")

# Recording function
def record_audio():
    
    global recording 
    recording= True   
    global audio_exists 

    #Create a file to save the audio
    messagebox.showinfo(message="Recording Audio. Speak into the mic")

    with sf.SoundFile("trial.wav", mode='w', samplerate=44100,channels=2) as file:
        
    #Create an input stream to record audio without a preset time
        with sd.InputStream(samplerate=44100, channels=2, callback=call_function):
            while recording == True:
                #Set the variable to True to allow playing the audio later
                audio_exists =True
                #write into file
                file.write(q.get())
                
# Button to record audio
record_btn = Button(root, text="Record Audio",bg="green", command=lambda m=1:threading_rec(m))
# Stop button
stop_btn = Button(root, text="Stop Recording",bg="red", command=lambda m=2:threading_rec(m))
# Play button
play_btn = Button(root, text="Play Recording", bg="blue",command=lambda m=3:threading_rec(m))

# Position buttons
img = ImageTk.PhotoImage(Image.open("mic3.png"))
#panel = tk.Label(root, image = img)
imglabel = Label(root, image=img).grid(row=1, column=1)


record_btn.grid(row=1,column=1)
record_btn.place(x=10, y=150)
stop_btn.grid(row=1,column=0)
stop_btn.place(x=10, y=200)
play_btn.grid(row=1,column=2)
play_btn.place(x=10, y=250)
root.mainloop()

