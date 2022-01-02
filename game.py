#Imports
import requests
import json
import random
import sys,time

#monster import acolyte
base_url = "https://www.dnd5eapi.co"
r = requests.get(base_url+"/api/monsters/acolyte")
if not r.status_code == 200:
     raise Exception("Incorrect reply from D&D API. Status code: {}. Text: {}".format(r.status_code, r.text))
monster = r.json()

#basic stats character

life = 100
attack = 1



#print(monster)

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

sprint('You wake up in a dark room')
sprint('next to you is a sword do you grab it? ')


        