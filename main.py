import json
from player_data import *
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
    textOutput.configure(state = 'normal')
    textOutput.delete(0.0, END)
    text = ""
    if name == "None":
        text += "Welcome to Xenorule!"
        text += "\n"
        text += "What is your name travller?"
        textOutput.insert(END, text)
        textOutput.configure(state = 'disabled')
        playerAnswerBox.configure(state = 'normal')
        submitButton.configure(state = 'normal')
        event = await at.event(submitButton, '<Button>')
        nameAnswer = playerAnswerBox.get(0.0, END).strip()
        await at.sleep(500, after=submitButton.after)
        name = nameAnswer
        textOutput.configure(state = 'disabled')
        saveData()
        gameLoop()
    else:
        textOutput.configure(state = 'disabled')
        gameLoop()

def gameLoop():
    global level
    global exp
    global wood
    global stone
    global iron_ore
    global iron
    global gold_ore
    global gold
    global money

    #Update Player Stats
    playerStatsOutput.configure(state = 'normal')
    playerStatsOutput.delete(0.0, END)
    stats = ''
    stats += ('Level: ' + str(level) + '\n')
    stats += ('Experience: ' + str(exp) + '\n')
    stats += ('Wood: ' + str(wood) + '\n')
    stats += ('Stone: ' + str(stone) + '\n')
    stats += ('Iron Ore: ' + str(iron_ore))
    stats += (' | Iron: ' + str(iron) + '\n')
    stats += ('Gold Ore: ' + str(gold_ore))
    stats += (' | Gold: ' + str(gold) +'\n')
    stats += ('Money: ' + str(money))
    playerStatsOutput.insert(END, stats)
    playerStatsOutput.configure(state = 'disabled')

    #Ask question
    textOutput.configure(state = 'normal')
    textOutput.delete(0.0, END)
    text = ''
    text += ('What would you like to do?\n')
    #Options
    text += ('Fight\n')
    text += ('Chop\n')
    text += ('Mine\n')
    if level >= 5:
        text += ('Smelt\n')
    if level >= 7:
        text += ('Shop\n')
        text += ('Travel\n')
    if level >= 10:
        text += ('Quests\n')
    textOutput.insert(END, text)
    textOutput.configure(state = 'disabled')


def grabText():
    global answer
    submitButton.configure(state = 'disabled')
    answer = playerAnswerBox.get(0.0, END).lower().strip()
    playerAnswerBox.delete(0.0, END)
    playerAnswerBox.configure(state = 'disabled')

def saveData():
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
    f.write("armor = \"" + armor + "\"\n")
    f.write("armor_inventory = " + str(armor_inventory) + "\n")
    f.write("inventory = " + str(inventory) + "\n")
    f.write("world = " + str(world) + "\n")
    f.write("quests_completed = " + str(quests_completed) + "\n")
    f.write("quest_current = \"" + quest_current + "\"\n")

    f.close()

def exitGame():
    saveData()
    window.destroy()
    exit()

#startButton = Button(window, text = 'Start', width = 6, command = startGame, bg = 'gray', fg = 'white')
#startButton.grid(row = 4, column = 0, sticky = 'w')
submitButton = Button(window, text = 'Submit', width = 6, command = grabText, bg = 'gray', fg = 'white')
submitButton.grid(row = 4, column = 0, sticky = 'w')
submitButton.configure(state = 'disabled')
exitButton = Button(window, text = 'Exit', width = 6, command = exitGame, bg = 'gray', fg = 'white')
exitButton.grid(row = 5, column = 0, sticky = 'w')

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