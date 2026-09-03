import pyxel
import random
from labyrinthes import labyrinthes, labyrinthe

TAILLE = 11
N = 16
x = 1
y = 1
niveau = 1
mort = False
gagne = False
perdu = False
vies = 5

def charger()->None:
    """charge un nouveau labyrinthe et remet le joueur au début."""

    global labyrinthe
    global x
    global y
    global mort

    labyrinthe = random.choice(labyrinthes)
    labyrinthes.remove(labyrinthe)

    x = 1
    y = 1
    mort = False

def deplacer(dx:int, dy:int)->None:
    """deplace le joueur horizontalement et verticalement,
    et vérifie si le joueur arrive sur un mur."""

    global x
    global y
    global mort

    nx = x + dx
    ny = y + dy

    if labyrinthe[ny][nx] == 1:
        if niveau == 2 or niveau == 4 or niveau == 6:
            mort = True
        return

    x = nx
    y = ny

def update()->None:
    """gère le fonctionnement du jeu,
    vérifie les déplacements, les vies, la mort, le changement de niveau et si le joueur a gagné ou perdu."""

    global niveau
    global gagne
    global perdu
    global vies

    if vies == 0:
        perdu = True

    if mort:
        if pyxel.btnp(pyxel.KEY_SPACE):
            charger()
            vies -= 1
        return

    if gagne or perdu:
        return

    if pyxel.btnp(pyxel.KEY_LEFT):
        deplacer(-1, 0)
    elif pyxel.btnp(pyxel.KEY_RIGHT):
        deplacer(1, 0)
    elif pyxel.btnp(pyxel.KEY_UP):
        deplacer(0, -1)
    elif pyxel.btnp(pyxel.KEY_DOWN):
        deplacer(0, 1)

    if x == 14 and y == 14:
        if niveau < 6:
            niveau += 1
            charger()
        else:
            gagne = True

def draw()->None:
    """dessine tout ce que le joueur voit,
    le labyrinthe, le joueur, la sortie et les informations du jeu."""

    global vies

    pyxel.cls(7)

    if mort:
        pyxel.text(76, 55, "MORT !", 8)
        pyxel.text(41, 76, f"vies restantes = {vies-1}", 8)
        pyxel.text(41, 96, "ESPACE = recommencer", 0)
        return

    if gagne:
        pyxel.text(59, 69, "GAGNÉ ! :)", 8)
        return
    if perdu:
        pyxel.text(59, 69, "PERDU ! :( ", 8)
        return

    for i in range(N):
        for j in range(N):
            if ((niveau == 3) or (niveau == 4)) and ((abs(i - x) > 2) or (abs(j - y) > 2)):
                continue
            if ((niveau == 5) or (niveau == 6)) and ((abs(i - x) > 1) or (abs(j - y) > 1)):
                continue
            if labyrinthe[j][i] == 1:
                pyxel.rect(i * TAILLE, j * TAILLE, TAILLE, TAILLE, 0)

    pyxel.rect(14 * TAILLE, 14 * TAILLE, TAILLE, TAILLE, 11) # sortie
    pyxel.rect(x * TAILLE + 2, y * TAILLE + 2, TAILLE/2, TAILLE/2, 8) #joueur

    pyxel.text(2, 2, "Niveau " + str(niveau), 8)
    pyxel.text(143, 2, "Vies = " + str(vies), 8)
