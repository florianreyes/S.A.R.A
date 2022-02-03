#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
from datetime import datetime
import time
import os
import speech_recognition as sr
import playsound
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)  # Recognizes audio using google
        except Exception as e:
            print("Exception: " + str(e))
    return said


speak("hello")
print(get_audio())


# Get audio from the microphone

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     # print("Hello sir, how can i help you?")
#     audio = r.listen(source)
#     text = r.recognize_google(audio)  # Recognizes audio using google
# print(text)
# # Added function to return time when asked

# if str(text).lower() == 'what time is it':
#     t = time.localtime()
#     current_time = time.strftime("%H:%M:%S", t)
#     print(current_time)
