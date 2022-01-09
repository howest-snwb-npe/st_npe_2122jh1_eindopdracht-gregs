#Imports
import requests
import json
import random
import sys,time
from Functions import Functions
from ascii_art import AscIIArt
from combat import CombatService
from playerstat import Player
from api_call import ApiService


#print(json.dumps(acolyte, indent=4))

######################
#### Functions #######
######################



#def add gold

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
Functions.sprint('next to you is a sword do you grab it? (1 yes / 2 no)  ')



if Functions.validation(Functions):
     player = Player()
     player.attack = player.attack + 5 
     Functions.sprint('you grab the sword and hold it close while moving outside of the room')
     print('your attack increases and is now ' + str(player.attack))
else:
     Functions.sprint('you ignore the sword and move outside the room')

monsterlist = ApiService.GetMonsters(ApiService, player)
monster = ApiService.GetRandomMonster(monsterlist)

Functions.sprint(f'suddenly an {monster.name} appears and yells at you in a foreign language')
print(f'will you attack or try to talk to the {monster.name}? (1 attack / 2 talk) ')


if Functions.validation(Functions):
          Functions.sprint(f'you launch a quick sneak attack against the weird {monster.name} and you deal critical damage! ')
          print(AscIIArt.zwaardanimatie)
          CombatService.Combat(CombatService, monster, player)

else:
          Functions.sprint('hi who are you? ')
     #verder te doen



# Game Chapter 2 
Functions.sprint('after killing the acolyte you think about your next steps, should you first check your current status or go through the next door? status/door ')
chapter2 = input()


Functions.sprint('while passing through the door you come to an open court , in the distance you see a tower')
print(AscIIArt.dungeontower)

Functions.sprint('while being amazed at the sight you also see something to your left (1 tower / 2 left) ')


if Functions.validation(Functions):
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












































