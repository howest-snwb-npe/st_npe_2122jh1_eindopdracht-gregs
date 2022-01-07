import math
import random

class Player:
    def __init__(self) -> None:
        self.life = 100
        self.attack = 1
        self.gold = 0
        self.critChance = 10
        self.playerExperience = 0
        self.playerLevel = 1
    
    def printStats(self):
        print(self.life, self.attack, self.gold, self.critChance,
              self.playerExperience, self.playerLevel)
    
    
            

    

