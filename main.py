#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
from datetime import datetime
import speech_recognition as sr
import playsound
from gtts import gTTS
import wolframalpha
import yfinance as yf


# stocks = {'apple': 'aapl',
#           'microsoft': 'msft', 'tesla': 'tsla', 'alibaba': 'baba'}


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
            speak("sorry sir, i couldn't hear you properly.")
    return said


# def get_stock_info(stock):
#     ticker=yf.Ticker(stock)


text = get_audio()
# if "hello" in text:
#     speak("Hi, how are you sir?")
# if "fine" in text:
#     speak("Excellent, How can i help you today?")


# for word in text:
#     if word in stocks.keys():
#         # get_stock_info(stocks[word])
#         print('hola capo')
#     else:
#         client = wolframalpha.Client("544R9X-8R9Y6QAR4R")
#     res = client.query(text)
#     speak(str(next(res.results).text))
#     print(next(res.results).text)
