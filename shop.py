from combat import CombatService
from playerstat import Player


## de shop



class Shopkeeper:


    shoplist = ('''

     1 : Health Potion
     2 : Upgrade Sword
     3 : Leave to tower
    ''')

    def upgrade(self, player: Player):
        if player.gold >= 10:
                shopinput = input().lower()
                match shopinput.lower():
                    case '1':
                        player.potioncount = player.potioncount +1
                        print(player.potioncount)
                    case '2':
                        player.attack = player.attack + 5
                        print(player.attack)
                    case '3':
                        pass
                    case _:
                        print('error')
        elif player.gold < 10:
            ('you are to poor to buy something in my shop')
        

