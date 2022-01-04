# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:15:16 2021

@author: Shivam
"""
# rasa run actions
#
import requests

sender = input()
bot_message = ""

while bot_message!="Bye":
    message = input("What is your message\n")
    print("Sending message now...")
    r = requests.post('http://localhost:5002/webhooks/rest/webhook',json={"sender":sender, "message":message})
    
    print("Bot says ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")