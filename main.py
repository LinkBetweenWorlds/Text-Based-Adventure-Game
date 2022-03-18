import json
from player_data import *
import random
from tkinter import *

window = Tk()
window.title('Text Based Adventure Game')
window.configure(background = 'black')
window.geometry('640x320')
window.minsize(640, 320)
window.maxsize(640, 320)

playerStatsOutput = Text(window, width = 40, height = 9, bg = 'black', fg = 'white')
playerStatsOutput.grid(row = 0, column = 0, sticky = 'w')
playerStatsOutput.configure(state = 'disabled')
#playerInvOutput = Text(window, width = 50, height = 4, bg = "black", fg = "white")
#playerInvOutput.grid(row = 0, column = 1, sticky = "w")

textOutput = Text(window, width = 80, height = 5, wrap = WORD, bg = 'black', fg = 'white')
textOutput.grid(row = 1, column = 0, columnspan = 2, sticky = 'w')
textOutput.configure(state = 'disabled')

Label(window, text = 'Answer:', bg = 'black', fg = 'white', font = 'none 12').grid(row = 2, column = 0, sticky = 'w')

playerAnswerBox = Text(window, width = 80, height = 2, wrap = WORD, bg = 'black', fg = 'white')
playerAnswerBox.grid(row = 3, column = 0, columnspan = 2, sticky = 'w')
playerAnswerBox.configure(state = 'disabled')

textOutput.configure(state = 'normal')
playerAnswerBox.configure(state = 'normal')
textOutput.delete(0.0, END)
playerAnswerBox.delete(0.0, END)
text = "Would you like to play? (yes/no)"
textOutput.insert(END, text)
textOutput.configure(state = 'disabled')

def gameLoop():
    #Get Answer and lock text box and submit button
    answer = playerAnswerBox.get(0.0, END)
    answer = answer.lower().strip()
    playerAnswerBox.delete(0.0, END)
    playerAnswerBox.configure(state = 'disabled')
    enterButton.configure(state = 'disabled')

    #Update Player Stats

    #Ask question



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

enterButton = Button(window, text = 'Submit', width = 6, command = gameLoop, bg = 'gray', fg = 'white')
enterButton.grid(row = 4, column = 0, sticky = 'w')

window.mainloop()