import speech_recognition as sr
import playsound
from gtts import gTTS
import yfinance as yf
import matplotlib.pyplot as plt


stocks = {'apple': 'AAPL',
          'microsoft': 'MSFT', 'tesla': 'TSLA', 'alibaba': 'BABA', 'apples': 'AAPL', 'teslas': 'TSLA', 'alibabas': 'BABA'}

stock_actions = ['dividends', 'cashflow', 'financials']


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Hello Sir, how can i help you?")
        print("Hello Sir, how can i help you?")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
            # speak("sorry sir, i couldn't hear you properly.")
    return said


def get_stocks(t):
    text_l = t.lower()
    for word in text_l.split():
        if word in stocks.keys():
            ticker = yf.Ticker(stocks[word])
            for action in text_l.split():
                if action == "dividends":
                    df = ticker.dividends
                    data = df.resample('Y').sum()
                    data = data.reset_index()
                    data['Year'] = data['Date'].dt.year
                    plt.figure()
                    plt.bar(data['Year'], data['Dividends'])
                    plt.xlabel('Year')
                    plt.ylabel('Dividend Yield ($)')
                    plt.title(
                        '{} historic dividend yield'.format(word))
                    plt.xlim(2000, 2020)
                    plt.show()
                elif action == "cash":
                    print(ticker.cashflow)
                elif action == "major":
                    print(ticker.major_holders)
                elif action == "institutional":
                    print(ticker.institutional_holders)

                else:
                    pass

        else:
            pass


text = get_audio()
speak("of course sir.")
get_stocks(text)
