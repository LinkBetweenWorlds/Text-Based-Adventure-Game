import player_stats as ps

answer = input("Would you like to play the game? (yes/no) ").lower().strip()
ps.name = input("What should I call you be? ")
print("Hello, " + ps.name)

if answer == "yes":
    print("What do you want to do?")
    tasks = ""
    if ps.level >= 1:   
        tasks += ("Chop ")
        tasks += ("Fight ")
    if ps.level >= 5:
        tasks = ("Mine ")
        tasks += ("Smelt ")
    print(tasks)
    answer = input("What do you want? ").lower().strip()

else:
    print("Ok, bye!")