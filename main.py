#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
import time
import speech_recognition as sr

# Get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    # print("Hello sir, how can i help you?")
    audio = r.listen(source)
    text = r.recognize_google(audio)

    print(text)
