from turtle import *        
import random 
from lettres_nsi import *  #autre fichier de thonny avec tous les lettres dessiner avec turtle

#MOT A DEVINER
#liste de mots utilisés dans le jeu
mots = [
    "python", "ordinateur", "clavier", "souris", "ecran", "internet",
    "algorithme", "variable", "fonction", "boucle", "programme",
    "donnees", "reseau", "serveur", "logiciel", "materiel",
    "developpement", "application", "systeme", "securite",

    "voiture", "avion", "bateau", "train", "velo", "moto",
    "route", "autoroute", "garage", "mecanique",

    "chat", "chien", "oiseau", "poisson", "cheval", "lion",
    "tigre", "elephant", "girafe", "singe", "lapin",

    "maison", "appartement", "cuisine", "salon", "chambre",
    "fenetre", "porte", "toit", "jardin", "garage",

    "ecole", "college", "lycee", "universite", "professeur",
    "eleve", "cours", "examen", "devoir", "lecon",

    "football", "basketball", "tennis", "rugby", "natation",
    "course", "cyclisme", "sport", "joueur", "equipe",

    "pomme", "banane", "orange", "fraise", "raisin",
    "carotte", "tomate", "salade", "fromage", "pain",

    "rouge", "bleu", "vert", "jaune", "noir", "blanc",
    "violet", "orange", "rose", "gris"
]

#choix aléatoire du mot à deviner
mot = random.choice(mots)

#VARIABLES
erreurs = 0                         #nombre d'erreurs du joueur
erreurs_max = 6                     #nombre maximum d'erreurs autorisées
lettres_trouvees = ["_"] * len(mot)  #mot caché dans un tableau
lettres_proposees = []             #lettres déjà proposées dans un tableau

#DICTIONNAIRE LETTRES
#associe chaque lettre à une fonction de dessin
lettres_turtle = {
    "a": a, "b": b, "c": c, "d": d, "e": e,
    "f": f, "g": g, "h": h, "i": i, "j": j,
    "k": k, "l": l, "m": m, "n": n, "o": o,
    "p": p, "q": q, "r": r, "s": s, "t": t,
    "u": u, "v": v, "w": w, "x": x, "y": y, "z": z
}

#ECRAN
#création de la fenêtre du jeu et de sa taille
setup(width=1000, height=700)
title("Jeu du pendu")

#TORTUES

#une tortue pour dessiner le pendu
t_dessin = Turtle()
#une tortue pour écrire le texte
t_texte = Turtle()

#on cache les tortues (on ne veut pas voir le curseur)
t_dessin.hideturtle()
t_texte.hideturtle()

#vitesse rapide pour un dessin fluide
t_dessin.speed(50)
t_texte.speed(50)

#on lève le stylo
t_dessin.penup()
t_texte.penup()

#tortue principale utilisée pour dessiner les lettres
hideturtle()
speed(0)
penup()

#DESSIN DU BAS
#dessine les traits pour chaque lettre du mot
positions = [0] * len(mot)

position_x = -350
longueur = 700 / len(mot) - 15

for indice in range(len(mot)):
    t_dessin.goto(position_x, -250)
    t_dessin.setheading(0)
    t_dessin.pendown()
    t_dessin.forward(longueur)
    t_dessin.penup()

    #stocke la position pour afficher les lettres plus tard
    positions[indice] = position_x + longueur / 2
    position_x = position_x + longueur + 15

#POTENCE
#dessine la structure du pendu
t_dessin.goto(-300, 10)
t_dessin.setheading(90)
t_dessin.pendown()
t_dessin.forward(200)
t_dessin.right(90)
t_dessin.forward(100)
t_dessin.right(90)
t_dessin.forward(10)
t_dessin.penup()

#AFFICHAGE
def afficher_lettres():
    #efface l'affichage précédent
    t_texte.clear()
    clear()

    #affiche les lettres trouvées
    for indice in range(len(mot)):
        lettre = lettres_trouvees[indice]

        if lettre != "_":
            penup()
            goto(positions[indice] - 8, -235)
            setheading(0)
            pendown()

            #dessine la lettre
            if lettre in lettres_turtle:
                lettres_turtle[lettre]()

            penup()

    #affiche les vies restantes
    t_texte.goto(150, 200)
    t_texte.write(
        "Vies : " + str(erreurs_max - erreurs),
        font=("Arial", 16, "normal")
    )

    #affiche les lettres déjà proposées
    t_texte.goto(150, 150)
    t_texte.write(
        "Lettres : " + " ".join(lettres_proposees),
        font=("Arial", 14, "normal")
    )

#DESSIN DU PENDU
def dessiner_pendu():
    #dessine une partie du pendu selon le nombre d'erreurs
    if erreurs == 1:
        t_dessin.goto(-200, 160)
        t_dessin.setheading(0)
        t_dessin.pendown()
        t_dessin.circle(20)
        t_dessin.penup()

    elif erreurs == 2:
        t_dessin.goto(-200, 160)
        t_dessin.setheading(-90)
        t_dessin.pendown()
        t_dessin.forward(60)
        t_dessin.penup()

    elif erreurs == 3:
        t_dessin.goto(-200, 140)
        t_dessin.setheading(-135)
        t_dessin.pendown()
        t_dessin.forward(40)
        t_dessin.penup()

    elif erreurs == 4:
        t_dessin.goto(-200, 140)
        t_dessin.setheading(-45)
        t_dessin.pendown()
        t_dessin.forward(40)
        t_dessin.penup()

    elif erreurs == 5:
        t_dessin.goto(-200, 100)
        t_dessin.setheading(-135)
        t_dessin.pendown()
        t_dessin.forward(40)
        t_dessin.penup()

    elif erreurs == 6:
        t_dessin.goto(-200, 100)
        t_dessin.setheading(-45)
        t_dessin.pendown()
        t_dessin.forward(40)
        t_dessin.penup()

#FIN DU JEU
def verifier_fin():
    #si toutes les lettres sont trouvées : gagné
    if "_" not in lettres_trouvees:
        t_texte.goto(0, 100)
        t_texte.write("GAGNÉ !", align="center", font=("Arial", 24, "bold"))
        return True

    #si trop d'erreurs : perdu
    if erreurs >= erreurs_max:
        t_texte.goto(0, 100)
        t_texte.write("PERDU ! Mot : " + mot, align="center", font=("Arial", 24, "bold"))
        return True

    return False

#LOGIQUE DU JEU
def jouer(lettre):
    global erreurs
    global lettres_proposees

    #vérifie si le jeu est déjà terminé
    if verifier_fin():
        return

    lettre = lettre.lower()

    #ignore si la lettre a déjà été proposée
    if lettre in lettres_proposees:
        return

    lettres_proposees = lettres_proposees + [lettre]

    #vérifie si la lettre est dans le mot
    if lettre in mot:
        for indice in range(len(mot)):
            if mot[indice] == lettre:
                lettres_trouvees[indice] = lettre
    else:
        erreurs = erreurs + 1
        dessiner_pendu()

    afficher_lettres()
    verifier_fin()

#TOUCHES CLAVIER
#chaque touche appelle la fonction jouer()

def touche_a(): jouer("a")
def touche_b(): jouer("b")
def touche_c(): jouer("c")
def touche_d(): jouer("d")
def touche_e(): jouer("e")
def touche_f(): jouer("f")
def touche_g(): jouer("g")
def touche_h(): jouer("h")
def touche_i(): jouer("i")
def touche_j(): jouer("j")
def touche_k(): jouer("k")
def touche_l(): jouer("l")
def touche_m(): jouer("m")
def touche_n(): jouer("n")
def touche_o(): jouer("o")
def touche_p(): jouer("p")
def touche_q(): jouer("q")
def touche_r(): jouer("r")
def touche_s(): jouer("s")
def touche_t(): jouer("t")
def touche_u(): jouer("u")
def touche_v(): jouer("v")
def touche_w(): jouer("w")
def touche_x(): jouer("x")
def touche_y(): jouer("y")
def touche_z(): jouer("z")

#associe chaque touche du clavier à une fonction
def activer_touches():
    onkey(touche_a, "a")
    onkey(touche_b, "b")
    onkey(touche_c, "c")
    onkey(touche_d, "d")
    onkey(touche_e, "e")
    onkey(touche_f, "f")
    onkey(touche_g, "g")
    onkey(touche_h, "h")
    onkey(touche_i, "i")
    onkey(touche_j, "j")
    onkey(touche_k, "k")
    onkey(touche_l, "l")
    onkey(touche_m, "m")
    onkey(touche_n, "n")
    onkey(touche_o, "o")
    onkey(touche_p, "p")
    onkey(touche_q, "q")
    onkey(touche_r, "r")
    onkey(touche_s, "s")
    onkey(touche_t, "t")
    onkey(touche_u, "u")
    onkey(touche_v, "v")
    onkey(touche_w, "w")
    onkey(touche_x, "x")
    onkey(touche_y, "y")
    onkey(touche_z, "z")

#LANCEMENT DU JEU
afficher_lettres()   #affiche le jeu au début
listen()             #active l'écoute du clavier
activer_touches()    #active les touches
done()               #lance la boucle principale
def lancer():

    print("Jeu du pendu")