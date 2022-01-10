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
from shop import Shopkeeper


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
     print(f'your attack increases and is now {player.attack} ')
else:
     Functions.sprint('you ignore the sword and move outside the room')

monsterlist = ApiService.GetMonsters(ApiService, player)
monster = ApiService.GetRandomMonster(monsterlist)


Functions.sprint(f'suddenly an {monster.name} appears and yells at you ')
print(f'will you attack or try to talk to the {monster.name}? (1 attack / 2 talk) ')


if Functions.validation(Functions):
          Functions.sprint(f'you launch a quick sneak attack against the weird {monster.name} ')
          print(AscIIArt.zwaardanimatie)
          CombatService.Combat(CombatService, monster, player)

else:
          Functions.sprint('hi who are you? ')
          Functions.sprint(f'The {monster.name} responds aggresivly and starts to attack you ! ')
          print(AscIIArt.zwaardanimatie)
          CombatService.Combat(CombatService, monster, player)


# Game Chapter 2 
Functions.sprint(f'after killing the {monster.name} you think about your next steps, should you first check your current status or go through the next door? 1 status / 2 door ')
if Functions.validation(Functions):
     Player.printStats(player)
else:
     pass

Functions.sprint('After checking your stats you pass through a door and you come to an open court , in the distance you see a tower')
print(AscIIArt.dungeontower)

Functions.sprint('while being amazed at the sight you also see something to your left (1 Left / 2 Tower ) ')
if Functions.validation(Functions):
     print(AscIIArt.shopkeeper)
     Functions.sprint('you turn to your left and walk towards a house in the distance')
     Functions.sprint('you enter the shop and find a bunch of items for sale! ')
     print(Shopkeeper.shoplist)
     Shopkeeper.upgrade(Shopkeeper, player)
     Player.printStats(player)
else:
     pass



##chapter 3

Functions.sprint('While in the tower you will have to face 5 enemies and then face the boss are you up for the challenge? (1 shop / 2 enter ) ')
if Functions.validation(Functions):
     print(AscIIArt.shopkeeper)
     print(Shopkeeper.shoplist)
     Shopkeeper.upgrade(Shopkeeper, player)
     Player.printStats(player)
else:
     pass


# Gauntlet Run 5 monsters verslaan 

Functions.sprint('You walk inside the tower room and face your 1st monster ')
CombatService.gauntletrun(CombatService,monster,player)


Functions.sprint('Continue or use Potion? (1 Pot / 2 Continue  test ) ')

if Functions.validation(Functions):
     CombatService.usepotion(CombatService, player)
     Player.printStats(player)
else:
     pass

Functions.sprint('You continue and face your 2nd monster ')
CombatService.gauntletrun(CombatService,monster,player)

Functions.sprint('Continue or use Potion? (1 Pot / 2 Continue ) ')
if Functions.validation(Functions):
     CombatService.usepotion(CombatService, player)
else:
     pass

Functions.sprint('You continue and and face your 3d monster ')
CombatService.gauntletrun(CombatService,monster,player)

Functions.sprint('Continue or use Potion? (1 Pot / 2 Continue ) ')
if Functions.validation(Functions):
     CombatService.usepotion(CombatService, player)
else:
     pass

Functions.sprint('You continue and and face your 4th monster ')
CombatService.gauntletrun(CombatService,monster,player)

Functions.sprint('Continue or use Potion? (1 Pot / 2 Continue ) ')
if Functions.validation(Functions):
     CombatService.usepotion(CombatService, player)
else:
     pass

Functions.sprint('You continue and face your 5th monster ')
CombatService.gauntletrun(CombatService,monster,player)

Functions.sprint('Continue or use Potion? (1 Pot / 2 Continue ) ')
if Functions.validation(Functions):
     CombatService.usepotion(CombatService, player)
else:
     pass

Functions.sprint('You continue and face your BOSS ')
CombatService.dragonmonster(CombatService,monster,player)

Functions.sprint('CONGRATZ ! you have won')
einde = input()


# Functions.sprint('You continue and face BOSS ')












































