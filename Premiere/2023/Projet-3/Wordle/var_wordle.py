#Définition des variables pour les carrés (Labels) où apparaitront les input du joueur

import tkinter as tk


def create_squares(frame, color):
    r1c1 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r1c2 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r1c3 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r1c4 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r1c5 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)

    r2c1 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r2c2 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r2c3 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r2c4 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r2c5 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)

    r3c1 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r3c2 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r3c3 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r3c4 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r3c5 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)

    r4c1 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r4c2 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r4c3 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r4c4 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r4c5 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)

    r5c1 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r5c2 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r5c3 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r5c4 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r5c5 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)

    r6c1 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r6c2 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r6c3 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r6c4 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)
    r6c5 = tk.Label(frame, font=("Arial", 10, "bold"), text="", width=8, height=4, borderwidth=1, bg = color)

    slabels = [[r1c1, r1c2, r1c3, r1c4, r1c5],
               [r2c1, r2c2, r2c3, r2c4, r2c5],
               [r3c1, r3c2, r3c3, r3c4, r3c5],
               [r4c1, r4c2, r4c3, r4c4, r4c5],
               [r5c1, r5c2, r5c3, r5c4, r5c5],
               [r6c1, r6c2, r6c3, r6c4, r6c5]]

    return slabels

def create_buttons(frame, color):
    bQ = tk.Label(frame, text='Q', width=6, height=3, bg = color)
    bW = tk.Label(frame, text='W', width=6, height=3, bg = color)
    bE = tk.Label(frame, text='E', width=6, height=3, bg = color)
    bR = tk.Label(frame, text='R', width=6, height=3, bg = color)
    bT = tk.Label(frame, text='T', width=6, height=3, bg = color)
    bY = tk.Label(frame, text='Y', width=6, height=3, bg = color)
    bU = tk.Label(frame, text='U', width=6, height=3, bg = color)
    bI = tk.Label(frame, text='I', width=6, height=3, bg = color)
    bO = tk.Label(frame, text='O', width=6, height=3, bg = color)
    bP = tk.Label(frame, text='P', width=6, height=3, bg = color)
    bA = tk.Label(frame, text='A', width=6, height=3, bg = color)
    bS = tk.Label(frame, text='S', width=6, height=3, bg = color)
    bD = tk.Label(frame, text='D', width=6, height=3, bg = color)
    bF = tk.Label(frame, text='F', width=6, height=3, bg = color)
    bG = tk.Label(frame, text='G', width=6, height=3, bg = color)
    bH = tk.Label(frame, text='H', width=6, height=3, bg = color)
    bJ = tk.Label(frame, text='J', width=6, height=3, bg = color)
    bK = tk.Label(frame, text='K', width=6, height=3, bg = color)
    bL = tk.Label(frame, text='L', width=6, height=3, bg = color)
    bZ = tk.Label(frame, text='Z', width=6, height=3, bg = color)
    bX = tk.Label(frame, text='X', width=6, height=3, bg = color)
    bC = tk.Label(frame, text='C', width=6, height=3, bg = color)
    bV = tk.Label(frame, text='V', width=6, height=3, bg = color)
    bB = tk.Label(frame, text='B', width=6, height=3, bg = color)
    bN = tk.Label(frame, text='N', width=6, height=3, bg = color)
    bM = tk.Label(frame, text='M', width=6, height=3, bg = color)

    lbuttons =[[bQ, bW, bE, bR, bT, bY, bU, bI, bO, bP],
               [bA, bS, bD, bF, bG, bH, bJ, bK, bL],
               [bZ, bX, bC, bV, bB, bN, bM]]

    return lbuttons

def find_bcolumn(gletter):
    if gletter == "q" or gletter == "a" or gletter == "z":
        return 0
    if gletter == "w" or gletter == "s" or gletter == "x":
        return 1
    if gletter == "e" or gletter == "d" or gletter == "c":
        return 2
    if gletter == "r" or gletter == "f" or gletter == "v":
        return 3
    if gletter == "t" or gletter == "g" or gletter == "b":
        return 4
    if gletter == "y" or gletter == "h" or gletter == "n":
        return 5
    if gletter == "u" or gletter == "j" or gletter == "m":
        return 6
    if gletter == "i" or gletter == "k":
        return 7
    if gletter == "o" or gletter == "l":
        return 8
    if gletter == "p":
        return 9

row_one = "qwertyuiop"
row_two = "asdfghjkl"
row_three = "zxcvbnm"

def find_brow(gletter):
    if gletter in row_one:
        return 0
    if gletter in row_two:
        return 1
    if gletter in  row_three:
        return 2
