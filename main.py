import json
from player_data import *
from monster_data import *
from weapon_data import *
from armor_data import *
from player_inventory import *
import random
from tkinter import *
import asynctkinter as at
import time
from PIL import Image, ImageTk

answer = ""

#Set up game window
window = Tk()
window.title('Xenorule')
window.configure(background = 'black')
window.geometry('960x480')
window.minsize(920, 480)
window.maxsize(920, 480)
window.resizable(width = NO, height = NO)
ico = Image.open('appicon.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

playerStatsOutput = Text(window, width = 57, height = 9, bg = 'black', fg = 'white')
playerStatsOutput.grid(row = 0, column = 0, sticky = 'w')
playerStatsOutput.configure(state = 'disabled')
playerEquipOutput = Text(window, width = 57, height = 9, bg = 'black', fg = 'white')
playerEquipOutput.grid(row = 0, column = 1, sticky = 'w')
playerEquipOutput.configure(state = 'disabled')
#playerInvOutput = Text(window, width = 50, height = 4, bg = "black", fg = "white")
#playerInvOutput.grid(row = 0, column = 1, sticky = "w")

textOutput = Text(window, width = 115, height = 10, wrap = WORD, bg = 'black', fg = 'white')
textOutput.grid(row = 1, column = 0, columnspan = 2, sticky = 'w')
textOutput.configure(state = 'disabled')

Label(window, text = 'Answer:', bg = 'black', fg = 'white', font = 'none 12').grid(row = 2, column = 0, sticky = 'w')

playerAnswerBox = Text(window, width = 115, height = 4, wrap = WORD, bg = 'black', fg = 'white')
playerAnswerBox.grid(row = 3, column = 0, columnspan = 2, sticky = 'w')
playerAnswerBox.configure(state = 'disabled')

async def startGame():
    global name
    global type_class
    global weapon
    global weapon_inventory
    textOutput.configure(state = 'normal')
    textOutput.delete(0.0, END)
    text = ""
    if name == "None":
        text += "Welcome to Xenorule!\n"
        text += "What is your name travller?"
        textOutput.insert(END, text)
        textOutput.configure(state = 'disabled')
        playerAnswerBox.configure(state = 'normal')
        submitButton.configure(state = 'normal')
        await at.event(submitButton, '<Button>')
        nameAnswer = playerAnswerBox.get(0.0, END).strip()
        await at.sleep(500, after=submitButton.after)
        name = nameAnswer
        textOutput.configure(state = 'disabled')
        saveData()
        if type_class == "None":
            at.start(startGame())
        else:
            at.start(gameLoop())
    if type_class == "None":
        text += "What class would you like to be?\n"
        text += "Mage: Cast powerful spells to destory their enemies.\n"
        text += "Paladin: Slash up their enemies with a sword.\n"
        text += "Archer: Picks off their enemies from afar with a bow."
        textOutput.insert(END, text)
        textOutput.configure(state = 'disabled')
        playerAnswerBox.configure(state = 'normal')
        submitButton.configure(state = 'normal')
        await at.event(submitButton, '<Button>')
        await at.sleep(500, after = submitButton.after)
        if answer == 'mage':
            type_class = '"Mage"'
            weapon = mage_weapons[0]
            weapon_inventory.insert(0, mage_weapons[0])
        if answer == 'paladin':
            type_class = '"Paladin"'
            weapon = paladin_weapons[0]
            weapon_inventory.insert(0, paladin_weapons[0])
        if answer == 'archer':
            type_class = '"Archer"'
            weapon = archer_weapons[0]
            weapon_inventory.insert(0, archer_weapons[0])
        saveData()
        if name == 'None':
            at.start(startGame())
        else:
            at.start(gameLoop())
    else:
        textOutput.configure(state = 'disabled')
        at.start(gameLoop())

async def gameLoop():
    global answer
    global level
    global exp
    global wood
    global stone
    global iron_ore
    global iron
    global gold_ore
    global gold
    global money

    nextButton.configure(state = 'disabled')
    submitButton.configure(state = 'normal')

    #Update Player Stats
    updatePlayerStats()

    #Ask question
    textOutput.configure(state = 'normal')
    textOutput.delete(0.0, END)
    text = ''
    text += ('What would you like to do?\n')
    #Options
    text += ('Fight\n')
    text += ('Chop\n')
    text += ('Mine\n')
    text += ('Heal\n')
    if level >= 3:
        text += ('Shop\n') 
    if level >= 5:
        text += ('Smelt\n')
    if level >= 7:  
        text += ('Travel\n')
    if level >= 10:
        text += ('Quests\n')
    if level >= 15:
        text += ('Enchant\n')
    textOutput.insert(END, text)
    textOutput.configure(state = 'disabled')
    playerAnswerBox.configure(state = 'normal')
    submitButton.configure(state = 'normal')
    await at.event(submitButton, '<Button>')
    await at.sleep(500, after=submitButton.after)

    if answer == 'chop':
        wood_gained = (random.randint(3, 8) * level)
        textOutput.configure(state = 'normal')
        textOutput.delete(0.0, END)
        text = 'You go to the forest and chop down some trees.\n'
        text += 'You gained ' + str(wood_gained) + ' wood.'
        wood += wood_gained
        saveData()
        textOutput.insert(END, text)
        textOutput.configure(state = 'disabled')
        nextButton.configure(state = 'normal')
        await at.event(nextButton, '<Button>')
        at.start(gameLoop())
    if answer == 'mine':      
        textOutput.configure(state = 'normal')
        textOutput.delete(0.0, END)
        text = 'You went down into the mines to get some stone'
        stone_gained = (random.randint(3, 8) * level)
        if level < 5:
            text += '.\n'
            text += 'You gained ' + str(stone_gained) + ' stone.\n'
        if level >= 5:
            text += ', and ores.\n'
            iron_ore_gained = (random.randint(2, 5) * level)
            gold_ore_gained = (random.randint(1, 4) * level)
            iron_ore += iron_ore_gained
            gold_ore += gold_ore_gained
            text += 'You gained ' + str(stone_gained) + ' stone.\n'
            text += 'You gained ' + str(iron_ore_gained) + ' iron ore.\n'
            text += 'You gained ' + str(gold_ore_gained) + ' gold ore.'
        stone += stone_gained
        saveData()
        textOutput.insert(END, text)
        textOutput.configure(state = 'disabled')
        await at.event(nextButton, '<Button>')
        at.start(gameLoop())
    if answer == 'fight':
        at.start(fight())
    if answer == 'heal':
        at.start(heal())
    if answer == 'exit':
        exitGame()
    else:
        at.start(gameLoop())

async def fight():
    global exp
    global health
    global health_max
    global mp
    global mp_max
    textOutput.configure(state = 'normal')
    textOutput.delete(0.0, END)
    text = 'Hello'
    textOutput.insert(END, text)
    await at.event(nextButton, '<Button>')
    at.start(gameLoop())

async def heal():
    print('Start heal')
    await at.sleep(500, after = submitButton.after)
    global health
    global health_max
    global mp
    global mp_max
    textOutput.configure(state = 'normal')
    textOutput.delete(0.0, END)
    health_pots = small_health_pot + medium_health_pot + large_health_pot + max_health_pot
    mp_pots = small_mp_pot + medium_mp_pot + large_mp_pot + max_mp_pot
    if (health_pots == 0) and (mp_pots == 0):
        text = "You don't have any potions to use.\n"
        text += 'You might be able to buy some from the shop.'
    else:
        text = 'Which potions would you like to use?'
        if small_health_pot > 0:
            text += ('Small Health Potion x' + small_health_pot + ' Restores 10 health points.\n')
        if medium_health_pot > 0:
            text += ('Medium Health Potion x' + medium_health_pot + ' Restores 35 health points.\n')
        if large_health_pot > 0:
            text += ('Large Health Potion x' + large_health_pot + ' Restores 80 health points.\n')
        if max_health_pot > 0:
            text += ('Max Health Potion x' + max_health_pot + ' Restores all your health points.\n')
        if small_mp_pot > 0:
            text += ('Small MP Potion x' + small_mp_pot + ' Restores 10 MP points.\n')
        if medium_mp_pot > 0:
            text += ('Medium MP Potion x' + medium_mp_pot + ' Restores 35 MP points.\n')
        if large_mp_pot > 0:
            text += ('Large MP Potion x' + large_mp_pot + ' Restores 80 MP points.\n')
        if max_mp_pot > 0:
            text += ('Max MP Potion x' + max_mp_pot + ' Restores all your MP points.\n')
    textOutput.insert(END, text)
    textOutput.configure(state = 'disabled')
    nextButton.configure(state = 'normal')
    await at.event(nextButton, '<Button>')
    saveInvData()
    at.start(gameLoop())

def grabText():
    global answer
    submitButton.configure(state = 'disabled')
    answer = playerAnswerBox.get(0.0, END)
    answer = answer.lower().strip()
    playerAnswerBox.delete(0.0, END)
    playerAnswerBox.configure(state = 'disabled')

async def check_levelup():
    global level
    global exp
    global health
    global health_max
    global mp
    global mp_max
    exp_needed = 50 * level

    if exp >= exp_needed:
        level += 1
        exp = 0
        health_max += 10
        mp_max += 10
        health = health_max
        mp = mp_max
        textOutput.configure(state = 'normal')
        textOutput.delete(0.0, END)
        text = ('You leveled you to level ' + str(level) + '!\n')
        text += ('Health: ' + str(health_max) + '\n')
        text += ('MP: ' + str(mp_max) + '\n')
        textOutput.insert(END, text)
        textOutput.configure(state = 'disabled')
        nextButton.configure(state = 'normal')
        await at.event(nextButton, '<Button>')
        at.start(gameLoop())
    else:
        at.start(gameLoop())

def updatePlayerStats():
    #Player Stats
    playerStatsOutput.configure(state = 'normal')
    playerStatsOutput.delete(0.0, END)
    exp_needed = 50 * level
    stats = ''
    stats += ('Level: ' + str(level) + '\n')
    stats += ('Experience: ' + str(exp) + ' / ' + str(exp_needed) + '\n')
    stats += ('Health: ' + str(health) + ' / ' + str(health_max) + '\n')
    stats += ('MP: ' + str(mp) + ' / ' + str(mp_max) + '\n')
    stats += ('Wood: ' + str(wood) + '\n')
    stats += ('Stone: ' + str(stone) + '\n')
    stats += ('Iron Ore: ' + str(iron_ore))
    stats += (' | Iron: ' + str(iron) + '\n')
    stats += ('Gold Ore: ' + str(gold_ore))
    stats += (' | Gold: ' + str(gold) +'\n')
    stats += ('Money: ' + str(money))
    playerStatsOutput.insert(END, stats)
    playerStatsOutput.configure(state = 'disabled')

    #Player Equip
    playerEquipOutput.configure(state = 'normal')
    playerEquipOutput.delete(0.0, END)
    equipText = ''
    equipText += ('Class: ' + type_class + '\n')
    equipText += ('Weapon: ' + weapon + '\n')
    equipText += ('Armor: ' + armor + '\n')
    playerEquipOutput.insert(END, equipText)
    playerEquipOutput.configure(state = 'disabled')

def saveData():
    f = open("player_data.py", "w")

    f.write("name = \"" + name + "\"\n")
    f.write("level = " + str(level) + "\n")
    f.write('type_class = "' + type_class + '"\n')
    f.write("exp = " + str(exp) + "\n")
    f.write("health = " + str(health) + "\n")
    f.write("health_max = " + str(health_max) + "\n")
    f.write("mp = " + str(mp) + "\n")
    f.write("mp_max = " + str(mp_max) + "\n")
    f.write("wood = " + str(wood) + "\n")
    f.write("stone = " + str(stone) + "\n")
    f.write("iron_ore = " + str(iron_ore) + "\n")
    f.write("iron = " + str(iron) + "\n")
    f.write("gold_ore = " + str(gold_ore) + "\n")
    f.write("gold = " + str(gold) + "\n")
    f.write("money = " + str(money) + "\n")
    f.write('weapon = "' + weapon + '"\n')
    f.write("weapon_inventory = " + str(weapon_inventory) + "\n")
    f.write("armor = \"" + armor + "\"\n")
    f.write("armor_inventory = " + str(armor_inventory) + "\n")
    f.write("inventory = " + str(inventory) + "\n")
    f.write("world = " + str(world) + "\n")
    f.write("quests_completed = " + str(quests_completed) + "\n")
    f.write('quest_current = "' + quest_current + '"\n')

    f.close()

def saveInvData():
    f = open('player_inventory.py', 'w')

    f.write('small_health_pot = ' + str(small_health_pot) + '\n')
    f.write('medium_health_pot = ' + str(medium_health_pot) + '\n')
    f.write('lagre_health_pot = ' + str(large_health_pot) + '\n')
    f.write('max_health_pot = ' + str(max_health_pot) + '\n')
    f.write('small_mp_pot = ' + str(small_mp_pot) + '\n')
    f.write('medium_mp_pot = ' + str(medium_mp_pot) + '\n')
    f.write('large_mp_pot = ' + str(large_mp_pot) + '\n')
    f.write('max_mp_pot = ' + str(max_mp_pot) + '\n')

    f.close()

def exitGame():
    saveData()
    window.destroy()
    exit()

#startButton = Button(window, text = 'Start', width = 6, command = startGame, bg = 'gray', fg = 'white')
#startButton.grid(row = 4, column = 0, sticky = 'w')
nextButton = Button(window, text = 'Next', width = 6, bg = 'gray', fg = 'white')
nextButton.grid(row = 4, column = 0, sticky = 'w')
nextButton.configure(state = 'disabled')
submitButton = Button(window, text = 'Submit', width = 6, command = grabText, bg = 'gray', fg = 'white')
submitButton.grid(row = 5, column = 0, sticky = 'w')
submitButton.configure(state = 'disabled')
exitButton = Button(window, text = 'Exit', width = 6, command = exitGame, bg = 'gray', fg = 'white')
exitButton.grid(row = 6, column = 0, sticky = 'w')

#async def some_task():
#    #label['text'] = 'Something'
#    playerAnswerBox.configure(state = 'normal')
#    event = await at.event(testButton, '<Button>')

#    test = playerAnswerBox.get(0.0, END)

#    print("Button pressed")
#    print(test)

#at.start(some_task())

at.start(startGame())

window.mainloop()