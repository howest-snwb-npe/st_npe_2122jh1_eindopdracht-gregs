

######################
#### Combat  #########
######################

import tabulate
import random
from playerstat import Player
from monsterstats import Monster


class CombatService:

    def CheckCriticalHit(critChance):
        if random.random() <= (critChance/100):
            return True
        else:
            return False

    def AttackMove(criticalHit, player: Player):
        if criticalHit:
            return player.attack * 2
        else:
            return player.attack

    def MonsterAttack(monster: Monster):
        totalDamage = 0
        diceRolls = monster.hit_dice.split('d')
        for x in range(int(diceRolls[0])):
            damage = random.randint(1, int(diceRolls[1]))
            totalDamage = totalDamage + damage
        return totalDamage

    def Combat(self, monster: Monster, player: Player):
        remainingmobhealth = monster.hit_points
        while not self.is_dead(remainingmobhealth):

            if monster.hit_points == remainingmobhealth:
                print(
                    f"The {monster.name} has {remainingmobhealth} hp")
            else:
                print(
                    f"The {monster.name} has {remainingmobhealth} hp left")

            isCrit = (self.CheckCriticalHit(player.critChance))
            if isCrit:
                print("You land a critical hit!")

            playerDamage = self.AttackMove(isCrit, player)
            print(f"You hit the {monster.name} for {playerDamage} damage")
            remainingmobhealth = remainingmobhealth - playerDamage
            if self.is_dead(remainingmobhealth):
                break
            monsterDamage = self.MonsterAttack(monster)
            print(f"The {monster.name} hits you for {monsterDamage} damage")
            player.life = player.life - monsterDamage
            if self.is_dead(player.life):
                print(
                    f"The {monster.name} has SLAIN YOU NOOB!")
                exit()
            print(f"you have {player.life} hp left")

        print(f"you killed the {monster.name}")
        print(
            f"after going through the clothes of the {monster.name} you find {monster.Getmonstergold()} gold")
        player.AddGold(monster.Getmonstergold())
        player.AddExp(monster.xp)

    def is_dead(health):
        if health <= 1:
            return True
        else:
            return False

    def CombatAction():
        actions = ["Attack", "Run"]
        print("What do you want to do")
        print(tabulate.tabulate([actions], tablefmt="grid"))
        playerInput = input()
        match playerInput.lower():
            case 'attack':
                return "attack"
            case 'run':
                return "run"
            case _:
                return "attack"
    def is_dead(health):
        if health <= 1:
            return True
        else:
            return False