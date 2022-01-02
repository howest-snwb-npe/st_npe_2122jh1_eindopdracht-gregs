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
print(monster)
#basic stats character

life      = 100
attack    = 1
Gold      = 0

startsword = 5
ironsword = 10
silversword = 20

######################
#### Functions #######
######################

# Function slow text
def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

acolytehealth = (monster.get('hit_points'))
# print(acolytehealth)


# zwaard animatie 
def swordattack(sword):
     sword = print(   '        />_________________________________ ' \
                    ' [########[]_________________________________> ' \
                             ' \>')

swordattack()



#################
#### GAME #######
#################


# dialogue with 1st NPC 

sprint('You wake up in a dark room')
sprint('next to you is a sword do you grab it? (yes/no) ')

swordgrab = input()
if swordgrab == "yes":
     attack = attack + startsword
     sprint('you grab the sword and hold it close while moving outside of the room')
     print('your attack increases and is now ' + str(attack))
else:
     sprint('you ignore the sword and move outside the room')

sprint('suddenly an acolyte appears and yells at you in a foreign language')
print('will you attack or try to talk to the acolyte? (attack/talk')

acolytedialogue = input()

if acolytedialogue == "attack":
     sprint('you launch a quick sneak attack against the weird acolyte and you deal critical damage! ')
     currentattack = attack * 2 
     remainingmobhealth = acolytehealth - currentattack
     if remainingmobhealth < 0:
          print('you killed the acolyte')
          sprint('after going through the clothes of the acolyte you find 5 gold')
          Gold = Gold + 5
     else:
          print('')

else:
     print('hi who are you? ')
     #verder te doen





        