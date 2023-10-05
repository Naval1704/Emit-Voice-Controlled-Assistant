import pyttsx3
import requests
from datetime import datetime
from decouple import config
from requests import get
import speech_recognition as sr
from random import choice

from utils import opening_text
import subprocess as sp
from geopy.geocoders import Nominatim
import pytz
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
import json

load_dotenv()

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

#set rate 
engine.setProperty('rate',190)

#set Volume 
engine.setProperty('volume', 1.0)

#set Vocie
voices = engine.getProperty('voices')
""" to some more voices 1st download the voice from Google or any other platform and upload it in registry editor in your systerm"""
engine.setProperty('voice',  voices[0].id)

# #************ TEXT TO SPEECH ***************

def speak( text ):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.now().hour

    if 6 <= hour < 12:
        greeting = "Good morning Sir"
    elif 12 <= hour < 16:
        greeting = "Good afternoon Sir"
    elif 16 <= hour < 23:
        greeting = "Good evening Sir"
    else:
        greeting = "Hello Sir"

    messages = [
        f"{greeting}, {USERNAME}!",
        f"I'm {BOTNAME}. How can I assist you today?",
        "aaaahhhhhh fuckkkkk",
    ]

    for message in messages:
        speak(message)

def take_user_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en-in').lower()

        if 'exit' in query or 'stop' in query:
            hour = datetime.now().hour
            if 6 <= hour < 12:
                speak("Goodbye for now! Have a productive morning.")
            elif 12 <= hour < 16:
                speak("Goodbye for now! Enjoy your afternoon.")
            elif 16 <= hour < 23:
                speak("Goodbye for now! Have a pleasant evening.")
            else:
                speak("Goodbye for now! Take care.")

            exit()

        return query

    except sr.UnknownValueError:
        speak('Sorry, I could not understand what you said. Could you please repeat that?')
    except sr.RequestError:
        speak('I encountered an error while processing your request. Please try again later.')

    return 'None'

from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_camera, open_cmd, open_notepad
from pprint import pprint

if __name__ == '__main__':
    greet_user()

    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")