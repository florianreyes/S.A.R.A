#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model("/Users/usuario/Desktop/sara/model")
rec = KaldiRecognizer(model, 16000)

# Opens microphone for listening
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4096)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())

print(rec.FinalResult)
