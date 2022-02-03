#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
from datetime import datetime
import time
import os
import speech_recognition as sr
import playsound
from gtts import gTTS
import wolframalpha


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
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said


text = get_audio()
if "hello" in text:
    speak("Hi, how are you sir?")
if "fine" in text:
    speak("Excellent, How can i help you today?")

client = wolframalpha.Client("544R9X-8R9Y6QAR4R")
res = client.query(text)
print(next(res.results).text)
speak(str(next(res.results).text))
