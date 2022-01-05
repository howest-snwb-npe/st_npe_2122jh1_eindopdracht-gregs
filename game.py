#Imports
import requests
import json
import random
import sys,time
from Functions import slowprint

#monster import acolyte
base_url = "https://www.dnd5eapi.co"
r = requests.get(base_url+"/api/monsters/acolyte")
if not r.status_code == 200:
     raise Exception("Incorrect reply from D&D API. Status code: {}. Text: {}".format(r.status_code, r.text))
acolyte = r.json()
#print(json.dumps(acolyte, indent=4))
#basic stats character

global life
life      = 100
global attack
attack    = 1
global Gold
gold      = 0

startsword = 5
ironsword = 10
silversword = 20

######################
#### Functions #######
######################


acolytehealth = (acolyte.get('hit_points'))

#def add gold
def AddGold(gold):
     gold + gold

# zwaard animatie 
zwaardanimatie =  (''' 
                          '/>________________________________ ' \n
               ' [########[]________________________________/ ' \n
                         ' \>' 
                         
     ''')


###shopkeeper 

shopkeeper = ('''
           `'::::.
             _____A_
         __/       /\___
         __/__/\__/  \___
     ---/__|" '' "| /___/\----
        |''|"'||'"| |' '||
        `""`""))""`"`""""`
     ''')
     









































#################
#### GAME #######
#################


#### CHAPTER 1
# dialogue with 1st NPC 

slowprint.sprint('You wake up in a dark room')
slowprint.sprint('next to you is a sword do you grab it? (yes/no) ')

swordgrab = input().lower()
while swordgrab not in['yes', 'no']:
     slowprint.sprint('your quest cannot continue with your correct input (yes/no) ')
     swordgrab = input().lower()
if swordgrab == "yes":
     attack = attack + startsword
     slowprint.sprint('you grab the sword and hold it close while moving outside of the room')
     print('your attack increases and is now ' + str(attack))
else:
     slowprint.sprint('you ignore the sword and move outside the room')

slowprint.sprint('suddenly an acolyte appears and yells at you in a foreign language')
print('will you attack or try to talk to the acolyte? (attack/talk) ')

#validation
acolytedialogue = input().lower()
while acolytedialogue not in['attack', 'talk']:
     slowprint.sprint('your quest cannot continue with your correct input (attack/talk) ')
     acolytedialogue = input().lower()
if acolytedialogue == "attack":
          slowprint.sprint('you launch a quick sneak attack against the weird acolyte and you deal critical damage! ')
          print(zwaardanimatie)
          currentattack = attack * 2
          slowprint.sprint('the acolyte his healthpoints are ' + str(acolytehealth))
          slowprint.sprint('your quick attack hits for ' + str(currentattack))
          remainingmobhealth = acolytehealth - currentattack
          if remainingmobhealth < 0:
               print('you killed the acolyte')
               slowprint.sprint('Going through the clothes of the acolyte you find 5 gold')
               gold = gold + 5 
          else:
               print('')

elif acolytedialogue == "talk":
          slowprint.sprint('hi who are you? ')
     #verder te doen



# Game Chapter 2 
slowprint.sprint('after killing the acolyte you think about your next steps, should you first check your current status or go through the next door? status/door ')
chapter2 = input()
if chapter2 == 'status':
     print('current attack is ' + str(attack))
     print('current remaining life is ' + str(life))
     print('current Gold is ' + str(gold))
else:
     pass

slowprint.sprint('while passing through the door you come to an open court , in the distance you see a tower and to your left there is small house')











































