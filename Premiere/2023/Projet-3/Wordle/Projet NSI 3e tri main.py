import tkinter as tk
import tkinter.messagebox
from random import randint
from time import sleep
from var_wordle import create_squares, create_buttons, find_bcolumn, find_brow

#couleurs
dark_grey = "#777b7d"
yellow = "#c9b458"
green = "#6aaa64"
light_grey = "#d3d6da"
white = "#ffffff"
black = "#000000"


#faire un dictionnaire avec la liste de réponses possibles
#et aussi la liste (en str) de mots de 5 lettres
with open("answers.txt", "r") as file:
    answers = file.read()
    answers = answers.split(',')

    dico = {i + 1 : answers[i] for i in range(len(answers))}

with open("words.txt", "r") as file:
    words = file.read()


#fenetre et frame
def create_main_window():
    wordle = tk.Tk()
    wordle.title("Wordle")
    form_width = 600
    form_height = 700
    screen_width = wordle.winfo_screenwidth()
    screen_height = wordle.winfo_screenheight()

    horizontal_offset = int((screen_width/2) - (form_width/2))
    vertical_offset = int((screen_height/2) - (form_height/2))

    wordle.geometry('{0}x{1}+{2}+{3}'.format(form_width,form_height,horizontal_offset,vertical_offset))
    wordle.resizable(False,False)

    return wordle
wordle = create_main_window()
sf = tk.Frame(wordle, height = 420, width = 350)
sb = tk.Frame(wordle, height = 200, width = 500)
sf.propagate(False)
sb.propagate(False)

#fonctions pour les carrés et boutons dans la fenetre (dans les frames)
slabels = create_squares(sf, white)
blabels = create_buttons(sb, light_grey)

#definition de variables
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
focusedrow = 0
focusedcol = 0
guess = ""
guessed = False
validword = False

#réponse finale avec randint()
ansnum = randint(0, len(dico))
fanswer = list(dico.values())[ansnum]

#event_handler (keyboard input)
def typeEntry(event):
    global focusedrow
    global focusedcol
    global lastrow
    global guessed
    global guess
    global validword
    if event.char in alpha and event.char != "" and focusedcol != 5:
        slabels[focusedrow][focusedcol].config(text = event.char.upper())
        focusedcol += 1
        guess += event.char.lower()

    if event.keysym == "Return" and focusedcol == 5:
        focusedrow += 1
        lastrow = focusedrow - 1
        focusedcol = 0
        guessed = True
        if guess not in words:
            tk.messagebox.showerror("Not a valid word", f"{guess} isn't a valid word!")
            focusedrow -= 1
            focusedcol = 5
            guessed = False
            validword = False
        if guess in words:
            validword = True
        if focusedrow == 6:
            tk.messagebox.showerror("Out of guesses!", f"You didn't find the right answer! It was {fanswer}")
            sleep(3)
            wordle.destroy()
    if event.keysym == "BackSpace" and focusedcol > 0:
        guess = guess[:-1]
        focusedcol -= 1
        slabels[focusedrow][focusedcol].config(text = "")

    else:
        return None

#fonctions pour changer les couleurs des carrés et boutons
def change_label_colors(row, column, bgcolor, fgcolor):
    slabels[row][column].config(bg = bgcolor, fg = fgcolor)

def change_button_colors(row, column, bgcolor, fgcolor):
    blabels[row][column].config(bg = bgcolor, fg = fgcolor)



#placement des carrés et boutons
for r in range(6):
    for c in range(5):
        slabels[r][c].place(x = 70 * c, y = 70 * r)
#boutons
for one in range(10):
    blabels[0][one].place(x = (50 * one + 1), y = 2)

for two in range(9):
    blabels[1][two].place(x = (50 * two + 27), y = 55)

for three in range(7):
    blabels[2][three].place(x = (50 * three + 77), y = 108)


#packing et label.bind()
slabels[focusedrow][focusedcol].focus_set()
slabels[focusedrow][focusedcol].bind("<Key>", typeEntry)
sf.pack(pady = 35)
sb.pack()

#fonction de validation des tentatives du joueur et coloration des carrés et boutons
#en fonction de leur position dans la réponse
def playgame():
    global guessed
    global guess
    global validword
    if guessed == True:
        if guess in words and len(guess) == 5:

            for g in range(5):
                change_label_colors(lastrow, g, dark_grey, white)
                change_button_colors(find_brow(guess[g]), find_bcolumn(guess[g]), dark_grey, white)

            for p in range(5):
                if fanswer[p] in guess:
                    position = guess.index(fanswer[p])
                    change_label_colors(lastrow, position, yellow, black)
                    change_button_colors(find_brow(fanswer[p]), find_bcolumn(fanswer[p]), yellow, black)

            for i in range(5):
                if guess[i] == fanswer[i]:
                    change_label_colors(lastrow, i, green, black)
                    change_button_colors(find_brow(guess[i]), find_bcolumn(guess[i]), green, black)

        if guess == fanswer:
            tk.messagebox.showinfo("Nice!", f"Well played on guessing '{fanswer}'!")
            sleep(3)
            wordle.destroy()
        if validword == True:
            guessed = False
            validword = False
            guess = ""
    wordle.after(16, playgame)

#update window 64 tick (16.4 milliseconds)
wordle.after(16, playgame)
wordle.mainloop()
