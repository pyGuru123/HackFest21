# Importing some modules

import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import pyttsx3
import datetime
import pywhatkit as kit

# Setting up our bot and its speed of speaking
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',170)

r=sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tosay(query):
    speak("You said {}".format(query))

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning sir.")
    elif hour>=12 and hour <18:
        speak("Good Afternoon sir.")
    else:
        speak("Good evening sir.")
    speak("I am your new assistant, is there anything I can do for you sir?")

def listen():
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
    except:
        speak("I can't understand what you said.")
        return "None"
    return text
if __name__ == "__main__":
    wish()
    while True:
        input('Press enter to start speaking...')
        query = listen().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(result )
        elif 'open youtube' in query:
            speak("Opening Youtube, give me a second.")
            webbrowser.open("https:://www.youtube.com")
        elif 'open google' in query:
            speak("Opening google, give me a second.")
            webbrowser.open("https:://www.google.com")
        elif 'open facebook' in query:
            speak("Opening facebook, give me a second.")
            webbrowser.open("https:://www.facebook.com")
        elif 'open instagram' in query:
            speak("Opening instagram, give me a second.")
            webbrowser.open("https:://www.instagram.com")
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak("The current time is {}".format(strTime))
        elif 'how are you' in query:
            speak("I am fine sir, how are you.")
        elif 'i am fine' in query:
            speak("Glad to hear that.")
        elif 'repeat' in query:
            tosay(query)
        elif 'play song':
            speak("Playing your song, enjoy!")
            kit.playonyt(query)
        elif ['type','write'] in query:
            print(query)
        else:
            speak("Sorry to say, but I can't do this right now.")