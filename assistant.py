from datetime import datetime
from email.mime import audio
from random import random
from tkinter.tix import MAIN
from zlib import Z_DEFAULT_COMPRESSION
from pip import main
import pyttsx3
import wikipedia
import webbrowser
import os
import random
import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # it takes mic inp and gives str op

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print('Listening...')
        r.pous_theshold = 1

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print('User said: ', query)
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return None
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail@gmail.com', 'your pass')
    server.sendmail('bhagvatwathmutthe123@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
    # logic for task
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            n = random.randint(0, 48)
            music_dir = 'C:\\Users\\bhagv\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'open code' in query:
            codePath = "C:\\Users\\bhagv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'mail to' in query:
            try:
                speak('What should i say?')
                content = takeCommand()
                to = 'gauravmutthe@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send email")

        elif 'what is your name' in query:
            speak('My name is Jarvis')

        elif 'what is my name' in query:
            speak('Your name is Bhagvat')

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
