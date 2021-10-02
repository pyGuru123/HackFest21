import pyttsx3

engine = pyttsx3.init('espeak')

voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[2].id)
# engine.setProperty('rate', 150)

i = 0
for voice in voices:
    print(i, voice.id)
    i += 1
