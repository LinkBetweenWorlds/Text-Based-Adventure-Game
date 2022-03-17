import json
from player_data import *
import random

def save_data():
    f = open("player_data.py", "w")

    f.write("name = \"" + name + "\"\n")
    f.write("level = " + str(level) + "\n")
    f.write("exp = " + str(exp) + "\n")
    f.write("wood = " + str(wood) + "\n")
    f.write("stone = " + str(stone) + "\n")
    f.write("iron_ore = " + str(iron_ore) + "\n")
    f.write("iron = " + str(iron) + "\n")
    f.write("gold_ore = " + str(gold_ore) + "\n")
    f.write("gold = " + str(gold) + "\n")
    f.write("money = " + str(money) + "\n")
    f.write("weapon = \"" + weapon + "\"\n")
    f.write("weapon_inventory = " + str(weapon_inventory) + "\n")
    f.write("inventory = " + str(inventory) + "\n")
    f.write("world = " + str(world) + "\n")
    f.write("quests_completed = " + str(quests_completed) + "\n")
    f.write("quest_current = \"" + quest_current + "\"\n")

    f.close()

def game_loop():
    global wood
    global stone
    print("Options")
    tasks = ""
    if level >= 1:
        tasks += ("Inventory" + "\n")
        tasks += ("Player Stats" + "\n")
        tasks += ("Chop" + "\n")
        tasks += ("Fight" + "\n")
    if level >= 5:
        tasks += ("Mine" + "\n")
        tasks += ("Smelt" + "\n")
    if level >= 7:
        tasks += ("Travel" + "\n")
    print(tasks)
    answer = input("what do you want to do? ").lower().strip()
    if answer == "inventory" or "inv":
        print("Wood: " + str(wood) + "\n")
        print("Stone: " + str(stone) + "\n")
    if answer == "chop":
        print("You went to the forst and chopped down some trees.")
        wood_gained = random.randint(2, 8) * level
        wood += wood_gained
        print("You gained " + str(wood_gained) + " wood.")
        save_data()
        game_loop()


answer = input("Would you like to play the game? (yes/no) ").lower().strip()
if name == "null":
    name = input("What is your name, travller? ")
    save_data()
else:
    print("Welcome back, " + name)

if answer == "yes":
   game_loop()
else:
    print("Ok, bye!")

