import math
import random

class Player:
    def __init__(self) -> None:
        self.life = 100
        self.attack = 3
        self.gold = 0
        self.critChance = 10
        self.playerExperience = 1000
        self.playerLevel = 1
    
    def printStats(self):
        print(self.life, self.attack, self.gold, self.critChance,
              self.playerExperience, self.playerLevel)
        
    def AddGold(self, goldGained):
        self.gold + goldGained

    def levelUp(self, levelsGained):
        for x in range(levelsGained):
            self.life = self.life + 100
            self.attack = self.attack+5
            self.critChance = self.critChance+1
            print(
                f"You lifepoints has increased to {self.life}, attack to {self.attack}, chance to crit to {self.critChance}")
     
    def AddExp(self, expGained):
        self.playerExperience = self.playerExperience + expGained
        originalLevel = self.playerLevel
        if self.playerExperience >= self.playerLevel * 1000:
            playerLevel = math.floor(self.playerExperience/1000)
            print(f"your level has increased to {playerLevel}")
            self.levelUp(self.playerLevel - originalLevel)
    

            

    

