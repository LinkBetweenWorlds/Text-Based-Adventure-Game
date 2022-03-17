import json
from player_data import *
import random
from tkinter import *

window = Tk()
window.title("Text Based Adventure Game")
window.configure(background = "white")
window.geometry("640x320")

playerStatsOutput = Text(window, width = 50, height = 9, bg = "black", fg = "white")
playerStatsOutput.grid(row = 0, column = 0, sticky = "w")
#playerInvOutput = Text(window, width = 50, height = 4, bg = "black", fg = "white")
#playerInvOutput.grid(row = 0, column = 1, sticky = "w")

textOutput = Text(window, width = 100, height = 6, wrap = WORD, bg = "white")
textOutput.grid(row = 1, column = 0, columnspan = 2, sticky = "w")

Button(window, text = "Submit", width = 6).grid(row = 2, column = 0, sticky = "w")

textOutput.delete(0.0, END)
text = "Would you like to play? (yes/no)"
textOutput.insert(END, text)

window.mainloop()

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

def ask_question():
    #Set Variables
    global name
    global level
    global exp
    global wood
    global stone
    global iron_ore
    global iron
    global gold_ore
    global gold
    global money
    global weapon
    global weapon_inventory
    global inventory
    global world
    global quests_completed
    global quest_current

    #Update Game Window
    playerStatsOutput.delete(0.0, END)
    #playerInvOutput.delete(0.0, END)
    textOutput.delete(0.0, END)

    playerStatsText = (
        "Name: " + name + "\n" +
        "Level: " + str(level) + "\n" +
        "Experience: " + str(exp) + "\n"
        )
    playerStatsOutput.insert(END, playerStatsText)
    #Player Options
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
    textOutput.insert(END, "Options: " + "\n" + tasks)

def game_loop():
    #Set Variables
    global name
    global level
    global exp
    global wood
    global stone
    global iron_ore
    global iron
    global gold_ore
    global gold
    global money
    global weapon
    global weapon_inventory
    global inventory
    global world
    global quests_completed
    global quest_current

    #Update Game Window
    playerStatsOutput.delete(0.0, END)
    #playerInvOutput.delete(0.0, END)
    textOutput.delete(0.0, END)

    playerStatsText = (
        "Name: " + name + "\n" +
        "Level: " + str(level) + "\n" +
        "Experience: " + str(exp) + "\n"
        )
    playerStatsOutput.insert(END, playerStatsText)
    #Player Options
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
    textOutput.insert(END, "Options: " + "\n" + tasks)
    answer = input("what do you want to do? ").lower().strip()
    if answer == "inventory" or "inv":
        print("Wood: " + str(wood) + "\n")
        print("Stone: " + str(stone) + "\n")
        print("Iron Ore: " + str(iron_ore) + "\n")
    if answer == "chop":
        print("You went to the forst and chopped down some trees.")
        wood_gained = random.randint(2, 8) * level
        wood += wood_gained
        print("You gained " + str(wood_gained) + " wood.")
        save_data()
        game_loop()