# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
import wikipedia
import speech_recognition as sr
from os import system
import os
import webbrowser
from googlesearch import search
import smtplib
#system('say {}'.format(text))
print(os.getcwd())
# os.chdir('/Users/rohitmattu')
# print(os.getcwd())


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 & hour < 12:
        system(f'say Good Morning!!')
    elif hour > 12 & hour < 16:
        system(f'say Good Afternoon!!')
    else:
        system(f'say Good Evening!!')

    system(f'say Hi, Rohit Mattu. My name is Coco How may I help you ?')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening . . .')
        audio = r.record(source, duration=5)
        text = r.recognize_google(audio)

        return text


def takeemail():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('What do you want to say ?')
        audio = r.record(source, duration=7)
        mail_ = r.recognize_google(audio)

        return mail_


if __name__ == "__main__":
    wishme()
    while True:

        text = takecommand().lower()
        print(text)

        if 'wikipedia' in text:
            system(f'say Searching Wikipedia')
            text = text.replace('wikipedia', '')
            result = wikipedia.summary(text, sentences=1)
            print(result)
            system(f"say {result}")
        elif 'open google' in text:
            system(f'say Searching google')
            print('Searching Google..')
            webbrowser.open('https://www.google.in')
        elif 'on google' in text:
            text = text.replace('on google', '')
            system(f'say {text}')
            for j in search(text, lang='en', num=10, start=0, stop=2, pause=2.0):
                print(j)
                webbrowser.open(j)

        elif 'youtube' in text:
            text = text.replace('on youtube', '')
            webbrowser.open(
                'https://www.youtube.com/results?search_query='f'{text}')

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            system(f'say Sir, The time is {strTime}')
        elif 'date' in text:
            system(f'say {datetime.datetime.now().date()}')
        elif 'whatsapp' in text:
            os.system('open /Applications/Whatsapp.app')
        elif 'send email' in text:
            try:
                gmail_add = 'your_email_address'
                gmail_pass = 'your_password'
                contents = takeemail().lower()
                print(contents)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_add, gmail_pass)
                server.sendmail(gmail_add, 'sender_address', contents)
                server.close()
            except:
                print('Sorry, Rohit I can\'t able to send this email')
