from tkinter import *

def click():
    answer = textEntry.get()
    output.delete(0.0, END)
    output.insert(END, answer)

def close():
    window.destroy()
    exit()

window = Tk()
window.title("Text Based Adventure Game")
window.configure(background = "black")
window.geometry("640x320")

Label(window, text="Hello World.", bg="black", fg="white", font="times 12 bold").grid(row=0, column=0, sticky="w")

textEntry = Entry(window, width=20, bg="white")
textEntry.grid(row=1, column=0, sticky="w")

Button(window, text="Submit", width=6, command=click).grid(row=2, column=0, sticky="w")

Label(window, text="Output: ", bg="black", fg="white", font="times 12 bold").grid(row=3, column=0, sticky="w")

output = Text(window, width=75, height=6, wrap=WORD, bg="white")
output.grid(row=4, column=0, columnspan=2, sticky="w")

Button(window, text="Exit", width=14, command=close).grid(row=5, column=0, sticky="w")

window.mainloop()