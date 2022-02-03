import pyttsx3
engine = pyttsx3.init()

engine.say("te voy a comer la panocha")
engine.runAndWait()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print(voices)
