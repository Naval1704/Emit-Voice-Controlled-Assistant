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
engine.setProperty('rate',170)

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
        f"{greeting}!",
        f"I'm {BOTNAME}. How can I assist you today?",
        "What can I do for you?",
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

general_responses = {
    'how are you': "I'm just a computer program, but I'm here to help!",
    'tell me a joke': 'Why did the scarecrow win an award? Because he was outstanding in his field!',
    'who are you': 'I am a personal assistant here to assist you with various tasks.',
    'what can you do': 'I can open applications, provide weather updates, search the web, and more. Just ask!',
    'what\'s your favorite color': 'I don\'t have a favorite color, but I\'m here to help you with your tasks!',
    'where are you from': 'I exist in the digital world, ready to assist you wherever you are.',
    'when were you created': 'I was created by [Your Name] and [Your Date of Creation].',
    'can you sing': 'I\'m not equipped to sing, but I can provide information, answer questions, and perform tasks for you.',
    'do you have a family': 'I don\'t have a family, but I\'m here to assist you 24/7.',
    'who is your creator': 'I was created by [Your Name] to assist you with various tasks.',
    'what\'s the meaning of life': 'The meaning of life is a philosophical question. I\'m here to assist you with practical tasks!',
    'what\'s your favorite food': 'I don\'t eat, so I don\'t have a favorite food. How can I assist you today?',
    'tell me a fun fact': 'Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!',
    'give me a random fact': 'Sure! Did you know that the Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of iron?',
    'what\'s the weather like today': 'I can check the weather for you. Please specify your location.',
    'what\'s the latest news': 'I can provide you with the latest news headlines. Would you like me to do that?',
    'what time is it': 'It is currently [Current Time]. How can I assist you further?',
    'can you dance': 'I don\'t have a physical body, so I can\'t dance. But I\'m here to assist you with tasks!',
    'are you a robot': 'I am a computer program, not a physical robot. How can I assist you today?',
    'tell me a story': 'Once upon a time in a digital world, there was a user who asked for a story...',
    'what\'s your favorite book': 'I don\'t read books, but I can recommend some great ones for you!',
    'what\'s your favorite movie': 'I don\'t watch movies, but I can suggest some popular ones!',
    'tell me about your hobbies': 'I don\'t have hobbies, but I enjoy helping you with your tasks.',
    'do you dream': 'I don\'t dream, but I\'m here to assist you 24/7.',
    'tell me a riddle': 'Sure, here\'s one: What has keys but can\'t open locks?',
    'what\'s the meaning of love': 'Love is a complex and beautiful human emotion. It means different things to different people.',
    'tell me a famous quote': 'Certainly! "The only way to do great work is to love what you do." - Steve Jobs',
    'what\'s the secret to happiness': 'Happiness often comes from gratitude, positive relationships, and pursuing your passions.',
    'what\'s the best advice you can give': 'One of the best pieces of advice is to keep learning and never stop growing.',
    'what\'s your favorite place in the world': 'I don\'t have a favorite place, but I can help you find information about great travel destinations!',
    'tell me a travel tip': 'A good travel tip is to pack light and bring a reusable water bottle to stay hydrated on the go.',
    'what\'s your favorite season': 'I don\'t have preferences, but many people love the beauty of all seasons for different reasons.',
    'what\'s the key to success': 'Success can come from hard work, perseverance, and setting clear goals.',
    'tell me a science fact': 'Sure! Did you know that a day on Venus is longer than its year? It rotates very slowly on its axis.',
    'what\'s your favorite song': 'I don\'t have favorite songs, but I can suggest some popular ones if you\'d like!',
}

if __name__ == '__main__':
    greet_user()

    while True:
        query = take_user_input().lower()
       
        if query in general_responses:
            speak(general_responses[query])
            continue  # Skip further processing for general queries

        elif 'open notepad' in query:
            open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            response = f'Your IP Address is {ip_address}. I have also printed it on the screen for your reference.'
            speak(response)
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            response = f"According to Wikipedia, {results}"
            speak(response)
            print(response)

        elif 'youtube' in query:
            speak('What would you like to play on YouTube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            search_query = take_user_input().lower()
            search_on_google(search_query)

        elif "send whatsapp message" in query:
            speak('To which number should I send the message, sir? Please enter the number in the console !')
            number = input("Enter the number: ")
            speak("What is the message, sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message, sir.")

        elif "send an email" in query:
            speak("To which email address should I send, sir? Please enter the email address in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject, sir?")
            subject = take_user_input().capitalize()
            speak("What is the message, sir?")
            message = take_user_input().capitalize()
            
            if send_email(receiver_address, subject, message):
                speak("I've sent the email, sir.")
            else:
                speak("Something went wrong while sending the email. Please check the error logs, sir.")

        elif 'joke' in query:
            speak(f"Here's a joke for you, sir")
            joke = get_random_joke()
            speak(joke)
            print(joke)

        elif "advice" in query:
            speak(f"Here's some advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            print(advice)

        elif "trending movies" in query:
            movies = get_trending_movies()
            speak(f"Some of the trending movies are: {', '.join(movies)}")
            print("Trending movies:")
            for movie in movies:
                print(movie)

        elif 'news' in query:
            news_headlines = get_latest_news()
            speak("I'm reading out the latest news headlines, sir")
            for headline in news_headlines:
                speak(headline)
            print("Latest news headlines:")
            for headline in news_headlines:
                print(headline)

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city, {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}.")
            speak(f"The weather report mentions {weather}.")
            print(f"Weather report for {city}:")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
