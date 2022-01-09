import json

# monster definieren 

class Monster:
    index: str
    name: str
    hit_points: int
    hit_dice: str
    xp: int
    url: str
    challenge_rating: int


    def __init__(self, index: str, name: str, hit_points: int, hit_dice: str, xp: int, url: str, challenge_rating: int,**kwargs) -> None:
        self.index = index
        self.name = name
        self.hit_points = hit_points
        self.hit_dice = hit_dice
        self.xp = xp
        self.url = url
        self.challenge_rating = challenge_rating

    def Getmonstergold (self):
        return self.challenge_rating*10
    
    def mapfromJsonToMonster(json_object):
        monster_dict = json.loads(json_object)
        monster_object = Monster(**monster_dict)
        return monster_object

