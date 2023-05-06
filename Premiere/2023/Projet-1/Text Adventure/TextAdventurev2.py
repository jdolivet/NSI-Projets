import json
from time import sleep
import os
from playsound import playsound

ffile = open(os.path.join(os.getcwd(), 'Text_TextAdventurev2.json'))
file = json.loads(ffile.read())

choicecode = [""]
end = False
tutorialend = False
halloffame = []
vineboom = False


def typewriter(string):
    global vineboom
    for c in string:
        print(c, end="")
        sleep(0.005)
        if c == "[" and vineboom:
            playsound(os.path.join(os.getcwd(), 'vineboom.mp3'))
    print("")

def turn(code):
    global end
    global tutorialend
    global vineboom
    findinfile = ''.join(code)
    answer = None
    while answer == None:
        try:
            if "Vineboom" in file[findinfile]:
                vineboom = True
            typewriter(file[findinfile]["Text"])
            nboptions = len(file[findinfile]["Options"])
            for i in range(nboptions):
                option = file[findinfile]["Options"][i]
                typewriter(f"{i+1}- {option}")
            typewriter("Please select an option:")
            answer = input("> ")
            optionnb = int(answer)-1
            if optionnb < 0:
                answer = None
                [None][2]
            chosenoption = file[findinfile]["Options"][optionnb]
            typewriter(f"You chose option {answer}: {chosenoption}")
            end = file[findinfile]["Ending"]
            tutorialend = file[findinfile]["End of the Tutorial"]
        except:
            answer = None
            typewriter("An error has occured, please try again. If the error persists, please restart the code.")
            sleep(1)
            choicecode.pop()
    return answer


def run():
    global choicecode
    global halloffame
    global end
    while end == False:
        choicecode.append(turn(choicecode))
        if tutorialend:
            choicecode = ["0"]
        if end:
            choicecode[-1] = ""
    typewriter("That's the end of your journey. Please enter a name for your run, so that it will always be registered in the Hall of fame.")
    halloffame.append([input("> "), ''.join(choicecode)])
    typewriter(
        f"{halloffame[len(halloffame)-1][0]} will be registered in the hall of fame.")
    typewriter("Hall of fame:")
    for i in range(len(halloffame)):
        typewriter(f"{halloffame[i][0]}, Choice code: {halloffame[i][1]}")

    again = True
    while again:
        typewriter("Do you wish to play again?")
        typewriter("1- Yes")
        typewriter("2- No (Your hall of fame will be cleared)")
        typewriter("3- Start again from a given choice code")
        ans = input("> ")

        if ans == "1":
            typewriter("Restarting game...")
            end = False
            choicecode = ["0"]
            run()
            again = False
        elif ans == "2":
            typewriter("Thank you for playing!")
            again = False
            exit()
        elif ans == "3":
            end = False
            againans = True
            while againans:
                typewriter("Please insert choice code (remove the last digit of any hall of fame choice code if you don't want an instant death):")
                choicecode = list(input("> "))
                try:
                    typewriter("Restarting from choice code...")
                    run()
                except:
                    typewriter("Invalid choice code, please try again. If the error persists, please restart the code.")

        else:
            typewriter("Invalid input, please try again.")


run()
