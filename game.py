#Imports
import requests
import json
import random


#monster import acolyte
base_url = "https://www.dnd5eapi.co"
r = requests.get(base_url+"/api/monsters/acolyte")
if not r.status_code == 200:
     raise Exception("Incorrect reply from D&D API. Status code: {}. Text: {}".format(r.status_code, r.text))
monster = r.json()

print(monster)