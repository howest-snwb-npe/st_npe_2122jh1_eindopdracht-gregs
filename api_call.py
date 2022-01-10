import requests
import json
import random
from playerstat import Player
from monsterstats import Monster


base_url = "https://www.dnd5eapi.co"


##monster oproepen + hergebruik stuk Koen

class ApiService:
    def GetMonsters(self, player: Player):

        response = requests.get(
            base_url+"/api/monsters?challenge_rating=" + str(self.get_rating(player.playerLevel)))
        if not response.status_code == 200:
            raise Exception("Incorrect reply from D&D API. Status code: {}. Text: {}".format(
                response.status_code, response.text))
        return response.json()

    def get_rating(playerLevel):
        playerLevel
        if playerLevel <= 3:
            return 0.25


    def GetRandomMonster(monsters):
        aantal = monsters["count"]
        monster_nr = random.randint(0,aantal-1)
        monster_url = monsters["results"][monster_nr]["url"]

        r = requests.get(base_url+monster_url)
        if not r.status_code == 200:
            raise Exception("Incorrect reply from D&D API. Status code: {}. Text: {}".format(r.status_code, r.text))
        return Monster.mapfromJsonToMonster(json.dumps(r.json()))

    def Impossible_monster(self):

        response = requests.get(
            base_url+"/api/monsters/young-red-dragon")
        if not response.status_code == 200:
            raise Exception("Incorrect reply from D&D API. Status code: {}. Text: {}".format(
                response.status_code, response.text))
        return response.json()


