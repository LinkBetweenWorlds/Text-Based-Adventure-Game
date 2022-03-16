import json

name = "null"
#Player Level
level = 1
exp = 0
#Player Items
wood = 0
stone = 10
iron_ore = 0
gold_ore = 0
iron = 20
gold = 0
money = 7489
#Player Inventory
weapon = "Fists"
weapon_inventory = ["Fists"]
inventory = []
#Player Location
world = 0

def save_data():
    print("Saving")
    file = open('player_data.txt' , 'w+')
    data = {"name": name, "level": level, "exp": exp,
           "wood": wood,"stone": stone, "iron_ore": iron_ore, "iron": iron, "money": money,
          "weapon": weapon, "weapon_inventory": weapon_inventory, "inventory": inventory}
    json.dump(data, file)
    print("Saved")


answer = input("Would you like to play the game? (yes/no) ").lower().strip()
if name == "null":
    name = input("What is your name, travller? ")
    save_data()

if answer == "yes":
    print("What do you want to do?")
    tasks = ""
    if level >= 1:   
        tasks += ("Chop ")
        tasks += ("Fight ")
    if level >= 5:
        tasks = ("Mine ")
        tasks += ("Smelt ")
    print(tasks)
    answer = input("What do you want? ").lower().strip()

else:
    print("Ok, bye!")

