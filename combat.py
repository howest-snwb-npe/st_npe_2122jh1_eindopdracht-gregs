


######################
#### Combat  #########
######################

import random
from playerstat import Player


class CombatService:

    def CheckCriticalHit(critChance):
        if random.random() <= (critChance/100):
            return True
        else:
            return False
        
    # def AttackMove(criticalHit, player: Player):
    #     if criticalHit:
    #         return Player.CalculateDamage(player) * 2
    #     else:
    #         return Player.CalculateDamage(player)

    # def MonsterAttack(monster: Monster, player: Player):
    #     totalDamage = 0
    #     diceRolls = monster.hit_dice.split('d')
    #     for x in range(int(diceRolls[0])):
    #         damage = random.randint(1, int(diceRolls[1]))
    #         totalDamage = totalDamage + damage
    #     totalDamage = totalDamage - Player.CalculateDamageReduction(player)
    #     if Player.CalculateDamageReduction(player) > 0:
    #         print(
    #             f"Your {player.equipedArmor.name} has blocked {Player.CalculateDamageReduction(player)} damage!")
    #     return totalDamage

    # def Combat(self, monster: Monster, player: Player):
    #     remainingmobhealth = monster.hit_points
    #     while not self.is_dead(remainingmobhealth):
    #         triedToRun = False
    #         if monster.hit_points == remainingmobhealth:
    #             print(
    #                 f"The {monster.name} has {remainingmobhealth} hp")
    #         else:
    #             print(
    #                 f"The {monster.name} has {remainingmobhealth} hp left")
    #         if self.CombatAction() == "run":
    #             triedToRun = True
    #             if self.RunAway(player, monster):
    #                 break

    #         if not triedToRun:
    #             isCrit = (self.CheckCriticalHit(player.critChance))
    #             if isCrit:
    #                 print("You land a critical hit!")

    #             playerDamage = self.AttackMove(isCrit, player)
    #             print(f"You hit the {monster.name} for {playerDamage} damage")
    #             remainingmobhealth = remainingmobhealth - playerDamage

    #         monsterDamage = self.MonsterAttack(monster, player)
    #         print(f"The {monster.name} hits you for {monsterDamage} damage")
    #         player.life = player.life - monsterDamage
    #         if self.is_dead(player.life):
    #             print(
    #                 f"The {monster.name} has SLAIN YOU NOOB!")
    #             exit()
    #         print(f"you have {player.life} hp left")

    #     else:
    #         print(f"you killed the {monster.name}")
    #         print(
    #             f"after going through the clothes of the {monster.name} you find {monster.GetMonsterGold()} gold")
    #         self.loot()
    #         player.AddGold(monster.GetMonsterGold())
    #         player.AddExp(monster.xp)

    # def is_dead(health):
    #     if health < 1:
    #         return True
    #     else:
    #         return False

    # def CombatAction():
    #     actions = ["Attack", "Run"]
    #     print("What do you want to do")
    #     print(tabulate.tabulate([actions], tablefmt="grid"))
    #     playerInput = input()
    #     match playerInput.lower():
    #         case 'attack':
    #             return "attack"
    #         case 'run':
    #             return "run"
    #         case _:
    #             return "attack"

    # def RunAway(player: Player, monster: Monster):
    #     if player.playerSpeed >= int(''.join(filter(str.isdigit, monster.speed['walk']))):
    #         print("You ran away succesfully")
    #         return True
    #     else:
    #         print("You failed to run away")
    #         return False