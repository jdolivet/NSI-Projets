from turtle import *

# CREATION DE LA FENETRE

# Création de l'écran turtle
screen = Screen()

# Taille de la fenêtre
screen.setup(900, 700)

# Couleur de fond
screen.bgcolor("black")

# Titre de la fenêtre
screen.title("Plateforme de Jeux")


# CREATION DU STYLO

# Création du turtle qui va écrire le texte
pen = Turtle()

# Cache la tortue
pen.hideturtle()

# Couleur du texte
pen.color("white")

pen.up()


# MENU PRINCIPAL

def menu():

    # Efface tout le texte précédent
    pen.clear()

    # Met le fond en noir
    screen.bgcolor("black")

    # Titre principal
    pen.goto(0, 250)
    pen.write("PLATEFORME DE JEUX",
              align="center",
              font=("Arial", 35, "bold"))

    # Option 1 : Pendu
    pen.goto(0, 120)
    pen.write("1 - PENDU",
              align="center",
              font=("Arial", 25, "normal"))

    # Option 2 : Snake
    pen.goto(0, 40)
    pen.write("2 - SNAKE",
              align="center",
              font=("Arial", 25, "normal"))

    # Option 3 : Morpion
    pen.goto(0, -40)
    pen.write("3 - MORPION",
              align="center",
              font=("Arial", 25, "normal"))

    # Aide
    pen.goto(0, -220)
    pen.write("Appuie sur 1 2 ou 3",
              align="center",
              font=("Arial", 18, "italic"))


# FONCTION JEU PENDU

def pendu():

    # Efface le menu
    pen.clear()

    # Change la couleur du fond, car c'était tout noir donc on arriver pas à voir
    screen.bgcolor("white")

    # Lance le fichier du pendu
    import Pendu.py


# FONCTION JEU SNAKE

def snake():

    # Efface le menu
    pen.clear()

    # Change la couleur du fond
    screen.bgcolor("white")
    
    # Lance le fichier du jeu snake
    import Snake.py



# FONCTION JEU MORPION

def morpion():

    # Efface le menu
    pen.clear()
    
    # Change la couleur du fond
    screen.bgcolor("white")

    # Lance le fichier du morpion
    import Morpion.py


# GESTION DES TOUCHES

# Permet d'écouter le clavier
screen.listen()

screen.onkey(pendu, "1")

screen.onkey(snake, "2")

screen.onkey(morpion, "3")


# LANCEMENT DU MENU

# Affiche le menu principal
menu()

# Garde la fenêtre ouverte
done()
