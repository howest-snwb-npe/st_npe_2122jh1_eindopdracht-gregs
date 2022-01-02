#######################################################################
### Hernoem dit bestand naar jouw voornaam_achternaam_opdr1.py      ###
### Tot aan het volgende commentaarblok hoef je niets te wijzigen   ###
### Af en toe kom je print() in commentaar tegen, dit is debug-code ###
#######################################################################



import requests
# als je een error krijgt op deze lijn voer dan het volgende uit in een command prompt:
# pip install requests = py -m pip install requests
import json
import random

#py -m pip install tabulate 
from tabulate import tabulate 

#while true loop start 

again = True
while again is True:     

    base_url = "https://www.dnd5eapi.co"

    #   Deze request haalt een lijst met monsters op
    print("Monster lijst wordt opgehaald")
    r = requests.get(base_url+"/api/monsters")
    if not r.status_code == 200:
        raise Exception("Incorrect reply from D&D API. Status code: {}. Text: {}".format(r.status_code, r.text))
    monster = r.json()
    #print(antw)



    # Kies een willekeurig nummer tussen 0 en het aantal monsters
    
    aantal = monster["count"]
    monster_nr = random.randint(0,aantal-1)
    print ("We kiezen uit" , aantal , "monsters")
    # Haal de index (naam) op van het gekozen getal
    #print(antw["results"][monster_nr])
    monster_url = monster["results"][monster_nr]["url"]
    #print(monster_url)

    # Deze request haalt een willekeurig monster op
    # Documentatie: http://www.dnd5eapi.co/docs/#monster-section
    print("Willekeurig monster wordt voor je gekozen")
    r = requests.get(base_url+monster_url)
    if not r.status_code == 200:
        raise Exception("Incorrect reply from D&D API. Status code: {}. Text: {}".format(r.status_code, r.text))
    monster = r.json()

    # Print de JSON van het willekeurig monster
    # print(json.dumps(monster, indent=4))

    ################################################################
    ### Vanaf hier ga je verder, volgens de opdracht op leho
    ### Na elke bullet die je succesvol afwerkt, maak je een commit
    ### De print() van hierboven mag je in commentaar zetten
    ################################################################

    #create new var for actions
    aantal = monster.get('actions')

    #names + fault tolerantie voor aantal acties + in var plaatsen

    aanval =[] 
    for index in range(len(aantal)):
        aanval.append(monster.get('actions')[index]["name"])

    

# tabulate tabel vorm output // + inhoudscreatie in var 
    Tabel = (tabulate([[monster.get('name'), monster.get('size'),monster.get('hit_points'),monster.get('strength'),monster.get('intelligence'),
                    (aanval)]] ,
                    ["Naam", "Grootte", "Hit","Kracht" ,"Intelligentie", "Acties"], tablefmt="grid"))
    print(Tabel)

#input var + save functie // naam in var plaatsen
    naam = (monster.get('name'))
    
    # opvangen error "/" 
    sign_er = "/" 
    if sign_er in naam:
        print("pas op er is een syntax error met dit monster")
    else:
        pass


    save = input("Wil je het bestand opslaan? y/n  ")
    if save == "y":
        with open(naam + '.txt', 'w') as f:
            f.write(Tabel)
            print("Bestand werd opgeslaan & je kan het bestand in je library terug vinden onder naam van " + naam +".txt")
    else:
        print("Niet opgeslaan")

#while true loop + ander var maken voor input

    inpt_again = input("Wil je nog een keer?  y/n  ")
    if inpt_again == "y":
        print("Nog eens")
    else:
        again = False
        print("We stoppen ermee")





#
# old command in case of needed use to be deleted after finish
#

#print testing 
# print(antw.get('name'))
# print(antw.get('size'))

#print(monster.get('actions'['name']))
#actions = print(monster.get('actions'[1]))

# print (actions)
# print(monster("actions"))

#for item in monster.get('actions'):
#    print(item)

# print(monster.get('actions')[0]["name"])
# print(monster.get('actions')[1]["name"])
# print(monster.get('actions')[2]["name"])
# print(monster.get('actions')[3]["name"])




