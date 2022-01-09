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
        print(f'current gold is', player.gold)
        if player.gold >= 10:
                shopinput = input().lower()
                match shopinput.lower():
                    case '1':
                        player.potioncount = player.potioncount +1
                        player.gold = player.gold - 5 
                        print(f'Potioncount is', player.potioncount)
                        print(f'current gold is', player.gold)
                    case '2':
                        player.attack = player.attack + 5
                        print(f'current attack is', player.attack )
                        player.gold = player.gold - 10
                        print(f'current gold is', player.gold)
                    case '3':
                        pass
                    case _:
                        print('error')
        elif player.gold < 10:
            ('you are to poor to buy something in my shop')
        

