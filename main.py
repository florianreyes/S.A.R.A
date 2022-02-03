#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
from datetime import datetime
import time
import speech_recognition as sr

# Get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    # print("Hello sir, how can i help you?")
    audio = r.listen(source)

    #  Recognizes audio using google
    text = r.recognize_google(audio)

    # Added function to return time when asked
    if str(text).lower() == 'what time is it':
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
