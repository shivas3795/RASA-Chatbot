# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:28:41 2021

@author: Shivam
"""

import speech_recognition as sr
#sr.energy_threshold = 4372

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak your query: ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        
    except: 
        print("Sorry could not recognized your voice")