#Imports
import requests
import json
import random
import sys,time
from Functions import Functions
from ascii_art import AscIIArt



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

###shopkeeper + shoplist


shoplist = ('''

     1 : Health Potion
     2 : IRON SWORD
     3 : Leave to tower

''')



















#################
#### GAME #######
#################


#### CHAPTER 1
# dialogue with 1st NPC 

Functions.sprint('You wake up in a dark room')
Functions.sprint('next to you is a sword do you grab it? (yes/no) ')

swordgrab = input().lower()



if swordgrab == "yes":
     attack = attack + startsword
     Functions.sprint('you grab the sword and hold it close while moving outside of the room')
     print('your attack increases and is now ' + str(attack))
else:
     Functions.sprint('you ignore the sword and move outside the room')

Functions.sprint('suddenly an acolyte appears and yells at you in a foreign language')
print('will you attack or try to talk to the acolyte? (attack/talk) ')

#validation
acolytedialogue = input().lower()
while acolytedialogue not in['attack', 'talk']:
     Functions.sprint('your quest cannot continue with your correct input (attack/talk) ')
     acolytedialogue = input().lower()
if acolytedialogue == "attack":
          Functions.sprint('you launch a quick sneak attack against the weird acolyte and you deal critical damage! ')
          print(AscIIArt.zwaardanimatie)
          currentattack = attack * 2
          Functions.sprint('the acolyte his healthpoints are ' + str(acolytehealth))
          Functions.sprint('your quick attack hits for ' + str(currentattack))
          remainingmobhealth = acolytehealth - currentattack
          if remainingmobhealth < 0:
               print('you killed the acolyte')
               Functions.sprint('Going through the clothes of the acolyte you find 5 gold')
               gold = gold + 5 
          else:
               print('')

elif acolytedialogue == "talk":
          Functions.sprint('hi who are you? ')
     #verder te doen



# Game Chapter 2 
Functions.sprint('after killing the acolyte you think about your next steps, should you first check your current status or go through the next door? status/door ')
chapter2 = input()
if chapter2 == 'status':
     print('current attack is ' + str(attack))
     print('current remaining life is ' + str(life))
     print('current Gold is ' + str(gold))
else:
     pass

Functions.sprint('while passing through the door you come to an open court , in the distance you see a tower')
print(AscIIArt.dungeontower)

Functions.sprint('while being amazed at the sight you also see something to your left (tower/left) ')
chapter2dialogue = input().lower()
while chapter2dialogue not in['tower', 'left']:
     Functions.sprint('your quest cannot continue without your correct input (tower/left) ')
     chapter2dialogue = input().lower()
     if chapter2dialogue == "tower":
          Functions.sprint('you carefully walk towards the tower')
     else:
          Functions.sprint('you turn to your left and walk towards a house in the distance')
          print(AscIIArt.shopkeeper)
          Functions.sprint('you enter the shop and find a bunch of items for sale! ')
          print(shoplist)
          shopinput = input().lower
          while shopinput not in['1', '2', '3']:
               Functions.sprint('your quest cannot continue with your correct input (tower/left) ')
               chapter2dialogue = input().lower()
          if shopinput == '3':
               Functions.sprint('you turn to your left and walk towards a house in the distance')
          else:
               print("nog grammed yet")


towertest = input()












































