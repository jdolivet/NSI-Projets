from turtle import *
import time

# Création de la fenêtre et configuration de base
screen = Screen()
screen.setup(400, 500)          # taille de la fenêtre en pixels
screen.title("Morpion")         # titre de la fenêtre
screen.tracer(0)                # désactive l’animation automatique pour un rendu plus fluide lors des mises à jour

# Configuration du stylo pour dessiner la grille et les symboles
hideturtle()
pensize(3)
speed(0)

# Création de la grille (tableau 3x3 vide) pour stocker les valeurs "X", "O" ou "" (vide)
grille = [["" for _ in range(3)] for _ in range(3)]

joueur = "X"        # joueur actuel ("X" commence toujours)
jeu_fini = False
jeu_commence = False  # indique si on est sur l’écran de start

# Dessine la grille du morpion
def dessiner_grille():
    clear()
    color("black")

    # lignes verticales
    penup()
    goto(-50, 150)
    pendown()
    goto(-50, -150)

    penup()
    goto(50, 150)
    pendown()
    goto(50, -150)

    # lignes horizontales
    penup()
    goto(-150, 50)
    pendown()
    goto(150, 50)

    penup()
    goto(-150, -50)
    pendown()
    goto(150, -50)

# Dessine un X
def dessiner_x(x, y):
    color("red")

    penup()
    goto(x - 20, y - 20)
    pendown()
    goto(x + 20, y + 20)

    penup()
    goto(x - 20, y + 20)
    pendown()
    goto(x + 20, y - 20)

# Dessine un O
def dessiner_o(x, y):
    color("blue")

    penup()
    goto(x, y - 20)
    pendown()
    circle(20)

# Convertit une case en coordonnées écran (x, y) du centre de la case
def coord_case(row, col):
    x = -100 + col * 100
    y = 100 - row * 100
    return x, y

# Convertit un clic x, y en case de la grille 
def obtenir_case(x, y):
    col = int((x + 150) // 100)
    row = int((150 - y) // 100)
    return row, col

# Affiche un message en bas de l’écran
def afficher_message(msg, couleur="black"):
    penup()
    goto(0, -200)
    color(couleur)
    write(msg, align="center", font=("Arial", 16, "bold"))

# Dessine le bouton "Rejouer" après une victoire ou un match nul
def dessiner_bouton():
    penup()
    goto(-50, -300)
    pendown()
    color("purple")

    # rectangle du bouton 
    for _ in range(2):
        forward(100)
        left(90)
        forward(40)
        left(90)

    penup()
    goto(0, -290)
    write("Rejouer", align="center", font=("Arial", 12, "bold"))

# Dessine l’écran de démarrage avec le bouton START et le titre MORPION
def dessiner_start():
    clear()

    # bouton START au centre de l’écran
    penup()
    goto(-60, -20)
    pendown()
    color("green")

    for _ in range(2):
        forward(120)
        left(90)
        forward(50)
        left(90)

    penup()
    goto(0, -10)
    write("START", align="center", font=("Arial", 16, "bold"))

    # titre MORPION en haut
    penup()
    goto(0, 100)
    color("black")
    write("MORPION", align="center", font=("Arial", 24, "bold"))

# Vérifie si un joueur a gagné
def verifier_victoire():
    lignes = []

    # lignes et colonnes 
    for i in range(3):
        lignes.append([(i,0),(i,1),(i,2)])  # ligne
        lignes.append([(0,i),(1,i),(2,i)])  # colonne 

    # diagonales
    lignes.append([(0,0),(1,1),(2,2)])
    lignes.append([(0,2),(1,1),(2,0)])

    # vérifie chaque ligne pour voir si les 3 cases sont identiques et non vides
    for ligne in lignes:
        a,b,c = ligne
        if grille[a[0]][a[1]] != "" and \
           grille[a[0]][a[1]] == grille[b[0]][b[1]] == grille[c[0]][c[1]]:
            return ligne

    return None

# Vérifie si c’est un match nul
def match_nul():
    for ligne in grille:
        for case in ligne:
            if case == "":
                return False
    return True

# Animation de la ligne gagnante
def animation(ligne):
    color("gold")
    pensize(6)

    x1, y1 = coord_case(ligne[0][0], ligne[0][1])
    x2, y2 = coord_case(ligne[2][0], ligne[2][1])

    penup()
    goto(x1, y1)
    pendown()

    # animation progressive de la ligne gagnante
    for i in range(20):
        nx = x1 + (x2 - x1) * (i / 20)
        ny = y1 + (y2 - y1) * (i / 20)
        goto(nx, ny)
        screen.update()
        time.sleep(0.01)

    goto(x2, y2)
    pensize(3)

# Réinitialise le jeu
def reset():
    global grille, joueur, jeu_fini
    grille = [["" for _ in range(3)] for _ in range(3)] # grille vide
    joueur = "X"
    jeu_fini = False
    dessiner_grille() # redessine la grille
    screen.update()

# Fonction appelée à chaque clic souris pour gérer les interactions du jeu
def clic(x, y):
    global joueur, jeu_fini, jeu_commence

    # Si on est sur l’écran start on vérifie si le clic est sur le bouton START pour commencer le jeu
    if not jeu_commence:
        if -60 < x < 60 and -20 < y < 30:  # clic sur START
            jeu_commence = True
            reset()
        return

    # bouton rejouer
    if -50 < x < 50 and -300 < y < -260:
        reset()
        return

    # si le jeu est fini on ignore les clics sauf sur le bouton rejouer
    if jeu_fini:
        return

    # récupère la case cliquée
    row, col = obtenir_case(x, y)

    # vérifie que la case est valide et que le jeu n’est pas fini avant de jouer
    if 0 <= row < 3 and 0 <= col < 3:
        if grille[row][col] == "":   # si la case est vide on peut jouer
            grille[row][col] = joueur

            cx, cy = coord_case(row, col)

            # dessine X ou O
            if joueur == "X":
                dessiner_x(cx, cy)
                joueur = "O"
            else:
                dessiner_o(cx, cy)
                joueur = "X"

            # vérifie si c'est une victoire victoire et affiche l’animation et le message de victoire si c’est le cas
            victoire = verifier_victoire()

            if victoire:
                animation(victoire)
                afficher_message("Victoire !", "green")
                dessiner_bouton()
                jeu_fini = True

            # sinon vérifie si c'est un match nul
            elif match_nul():
                afficher_message("Match nul !", "orange")
                dessiner_bouton()
                jeu_fini = True

    screen.update()   # met à jour l’écran après chaque clic

# Lancement du jeu
dessiner_start()        # affiche l'écran de départ
screen.onclick(clic)   # détecte les clics de la souris
done()

def lancer():

    print("Jeu du morpion")