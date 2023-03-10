import os
import time 
import secrets
import string
import ctypes
from random import randint
import pyttsx3
import datetime
import webbrowser
import requests
import wikipedia
import speech_recognition as sr
import pyaudio
from selenium import webdriver
import json

num, head_or_tails_value = 0, 0
query, data, length = "", "", ""
pw, characters = (''.join(secrets.choice(characters) for _ in range(length))), string.digits + string.ascii_letters + string.punctuation
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
CONDITION = True
query_final = []
machine = Plattform()
class Plattform():
    def __init__(self):
        self.operating_system = "UNIX"
        self.ram = None
        self.storage = None
        
def plattform_detection():
    try:
        os.mkdir("./con")
        os.rmdir("./con")
    except:
        machine.operating_system = "WINDOWS"
                 
def roll():
    print(str(randint(1,6)))

def head_or_tails():
    head_or_tails_value = randint(1, 2)
    if head_or_tails_value > 1:
        respond("Head")
        print("Head")
    else:
        respond("Tails")
        print("Tails")


def program_or_website_to_open():
    if 'google' or 'Google' in query_final:
        webbrowser.open_new_tab("https://www.google.com")
        respond("Google is open")
        
    if 'reddit' or 'Reddit' in query_final:
        webbrowser.open_new_tab("https://www.reddit.com/")
        respond("Reddit is open")

    if 'github' or 'Github' or 'GitHub' in query_final:
        webbrowser.open_new_tab("https://github.com/")
        respond("Github is open")

    
    if 'youtube' or 'Youtube' or 'YouTube' in query_final:
        webbrowser.open_new_tab("https://www.youtube.com/")
        respond("Youtube is open")

    else:
        print("Repeat your command...")
        return(query)
    
def respond(audio):
    engine.say(audio)
    engine.runAndWait()

def talk():
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print(audio)
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        query_final = query.split()
        print(f"User said: {query}\n")
        print(query)
    except Exception as equalex:
        print(equalex)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

if __name__=='__main__':
    print("mainloop")
    clear = lambda: os.system('cls')
    plattform_detection()
    while True: 
        query_final = talk().lower()
    
        if CONDITION == True: 
            print("Condition fulfilled")
            respond("Hi, I am Alter Ego, your personal virtual assistent")
            while(1):
                respond("How can I help you?")
                query_final = talk().lower()

                if query_final == 0: 
                    continue

                if "stop" in str(query_final) or "exit" in str(query_final) or "bye" in str(query_final) or "goodbye" in str(query_final):
                    CONDITION = True
                    respond("Ok, bye and take care.")
                    break
             
                if 'time' or 'Time' in query_final:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    respond(f"the time is {strTime}")     
        
                if 'search' or 'Search' in query_final:
                    query_final = query_final.replace("search", "")
                    webbrowser.open_new_tab(query_final)
                    time.sleep(5)
                if 'open' or 'Open' in query_final:
                    program_or_website_to_open()
                    time.sleep(5)
                    print("waiting 5 seconds")
                if 'head or tails' or 'Head or Tails' in query_final:
                    head_or_tails()
                    time.sleep(5) #trailing whitespace  

                if 'random password' or 'Random Password' in query_final:
                    length = int(input(("Desired password length(If it should be secure at least 16, 40 should be fine): ")))
                    print(pw)
                    time.sleep(5)
                if 'cube' or 'Cube' in query_final:
                    roll()
                    time.sleep(5)
                elif 'wikipedia' or 'Wikipedia' in query_final:
                    respond('Searching Wikipedia')
                    query_final = query_final.replace("wikipedia", "")
                    results = wikipedia.summary(query_final, sentences=3)
                    respond("According to Wikipedia")
                    print(results)
                    respond(results)
                else:
                    respond("Application not available")
