import math
import random
import tabulate

from monsterstats import Monster

# Player stats definieren & initialiseren (not sure wrm -> none maar werkt zo)
## def __init__(self, n): doesn't have a return type. def __init__(self, n) -> None:


class Player:
    def __init__(self) -> None:
        self.hp = 100
        self.attack = 3
        self.gold = 20
        self.critChance = 10
        self.playerExperience = 1000
        self.playerLevel = 1
        self.potioncount = 1 
    
    def printStats(self):

        print("HP", self.hp,"ATT", self.attack,"GOLD", self.gold,"CRIT", self.critChance,
              "XP", self.playerExperience,"LVL", self.playerLevel,"POTS", self.potioncount)
        
    def AddGold(self, goldgained):
            self.gold = self.gold + goldgained

    def levelUp(self, levelsGained):
        for x in range(levelsGained):
            self.hp = self.hp + 100
            self.attack = self.attack+5
            self.critChance = self.critChance+1
            print(
                f"You lifepoints has increased to {self.hp}, attack to {self.attack}, chance to crit to {self.critChance}")
     
    def AddExp(self, expGained):
        self.playerExperience = self.playerExperience + expGained
        originalLevel = self.playerLevel
        if self.playerExperience >= self.playerLevel * 1000:
            playerLevel = math.floor(self.playerExperience/1000)
            print(f"your level has increased to {playerLevel}")
            self.levelUp(self.playerLevel - originalLevel)
    

            

    

