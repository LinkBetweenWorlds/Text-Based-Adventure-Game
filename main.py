import json
import pickle

name = "null"
#Player Level
level = 1
exp = 0
#Player Items
wood = 100
stone = 50
iron_ore = 0
iron = 5
gold_ore = 10
gold = 0
money = 999
#Player Inventory
weapon = "Fists"
weapon_inventory = ["Fists"]
inventory = []
#Player Location
world = 0
#Player Quests
quests_completed = []
quest_current = "null"

def save_data():
    data = [
    name, level, exp, 
    wood, stone, iron_ore, iron, gold_ore, gold, money, 
    weapon, weapon_inventory, inventory, 
    world, 
    quests_completed, quest_current]
    pickle.dump(data, open("player_data.txt", "wb"))

def load_data():
    data = pickle.load(open("player_data.txt", "rb"))
    name = data[0]
    level = data[1]
    exp = data[2]
    wood = data[3]
    stone = data[4]
    iron_ore = data[5]
    iron = data[6]
    gold_ore = data[7]
    gold = data[8]
    money = data[9]
    weapon = data[10]
    weapon_inventory = data[11]
    inventory = data[12]
    world = data[13]
    quests_completed = data[14]
    quest_current = data[15]
    print(data)



answer = input("Would you like to play the game? (yes/no) ").lower().strip()
load_data()
if name == "null":
    name = input("What is your name, travller? ")
    save_data()
else:
    print("Welcome back, " + name)

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

