# Importing modules

import wikipedia
import pyttsx3
import speech_recognition as sr
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import *

# Setting up engines and loading GUI
app = QtWidgets.QApplication([])
window = uic.loadUi("design.ui")

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',170)

r=sr.Recognizer()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
    except:
        speak("Couldn't understand what do you mean.")
        return None
    return text

def speakBtn():
    speak("O")
    query = listen()
    if query is not None:
        query = query.lower()
        speak(f"Searching on wikipedia about {query} please hold on.")
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=2)
        print(result)
        window.box2.clear()
        window.box2.setPlainText(result)
        speak(f"According to wikipedia, {result}")

if __name__=="__main__":
    window.speakButton.clicked.connect(speakBtn)
    window.show()
    app.exec()
