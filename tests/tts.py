import pyttsx3
engine = pyttsx3.init()

engine.say("hello sir, how can i help you")
engine.runAndWait()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print(voices)
