import tkinter
import random
from tkinter import PhotoImage

# Configuration de la taille et des dimensions du plateau de jeu.
LIGNES = 25
COLONNES = 25
TAILLE_CASE = 30

# Détermination des dimensions de la fenêtre basée sur les dimensions du plateau.
LARGEUR_FENETRE = TAILLE_CASE * COLONNES
HAUTEUR_FENETRE = TAILLE_CASE * LIGNES

# Classe pour représenter une case du plateau.
class Case:
    def __init__(self, x, y):
        self.x = x  # Coordonnée horizontale
        self.y = y  # Coordonnée verticale

# Initialisation de l'interface graphique.
fenetre = tkinter.Tk()
fenetre.title("HUNGRY SNAKE")
fenetre.resizable(False, False)

# Création du canvas où le jeu se déroulera.
canvas = tkinter.Canvas(fenetre, bg="dark blue", width=LARGEUR_FENETRE, height=HAUTEUR_FENETRE, borderwidth=0, highlightthickness=0)
canvas.pack()
fenetre.update()

# Fonction pour lire le meilleur score depuis le fichier.
def obtenir_meilleur_score():
    try:
        with open("meilleur_score.txt", "r") as fichier:
            return int(fichier.read())
    except FileNotFoundError:
        return 0 # S'il ne trouve pas le ficher, il retourne 0 et le ficher sera crée dans la prochaine fonction.

# Fonction pour mettre à jour le fichier du meilleur score si le nouveau score est supérieur.
# Si fichier n'est pas crée dans le directoire, il le crée automaticamente.
def mettre_a_jour_meilleur_score(nouveau_score):
    meilleur_score = obtenir_meilleur_score()
    if nouveau_score > meilleur_score:
        with open("meilleur_score.txt", "w") as fichier:
            fichier.write(str(nouveau_score))
        return nouveau_score
    return meilleur_score

meilleur_score = obtenir_meilleur_score()

# Fonction déclenchée pour démarrer le jeu, elle nettoie le canvas et prépare le jeu.
def demarrer_jeu(event):
    global update_id
    canvas.delete("all")
    dessiner()
    fenetre.bind("<KeyRelease>", changer_direction)
    fenetre.unbind("<KeyPress>")

# Affichage du logo et des instructions pour commencer le jeu.
image_logo = PhotoImage(file='logo.png')
canvas.create_image(LARGEUR_FENETRE / 2, HAUTEUR_FENETRE / 3, image=image_logo)
canvas.create_text(LARGEUR_FENETRE / 2, HAUTEUR_FENETRE * 0.8, text="Appuyez sur une des touches fléchées pour démarrer", fill="black", font="Arial 20")

fenetre.bind("<KeyPress>", demarrer_jeu)

serpent = Case(TAILLE_CASE * 5, TAILLE_CASE * 5)
nourriture = Case(TAILLE_CASE * 10, TAILLE_CASE * 10)
vitesseX = 0
vitesseY = 0
corps_serpent = []
partie_terminee = False
score = 0
update_id = None

# Fonction pour changer la direction du serpent en fonction des touches pressées.
def changer_direction(e):
    global vitesseX, vitesseY, partie_terminee
    if partie_terminee and e.keysym == 'r':
        redemarrer_jeu()
        return
    directions = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
    if e.keysym in directions:
        dx, dy = directions[e.keysym]
        if not (vitesseX == -dx and vitesseY == -dy):  # Vérifie pour empêcher le serpent de se retourner sur lui-même.
            vitesseX, vitesseY = dx, dy

# Fonction pour redémarrer le jeu après une partie terminée.
def redemarrer_jeu():
    global serpent, nourriture, corps_serpent, partie_terminee, score, vitesseX, vitesseY, update_id, meilleur_score
    if update_id:
        fenetre.after_cancel(update_id)
    serpent = Case(TAILLE_CASE * 5, TAILLE_CASE * 5)
    nourriture = Case(TAILLE_CASE * 10, TAILLE_CASE * 10)
    corps_serpent = []
    score = 0
    vitesseX = 0
    vitesseY = 0
    partie_terminee = False
    meilleur_score = mettre_a_jour_meilleur_score(score)
    dessiner()

# Fonction pour déplacer le serpent, gérer les collisions et la consommation de nourriture.
def deplacer():
    global serpent, nourriture, corps_serpent, partie_terminee, score, meilleur_score
    # Vérifie si la partie est terminée pour arrêter le déplacement.
    if partie_terminee:
        meilleur_score = mettre_a_jour_meilleur_score(score)
        return
    # Vérifie les collisions avec les bords de la fenêtre.
    if serpent.x < 0 or serpent.x >= LARGEUR_FENETRE or serpent.y < 0 or serpent.y >= HAUTEUR_FENETRE:
        partie_terminee = True
        meilleur_score = mettre_a_jour_meilleur_score(score)
        return
    # Vérifie les collisions avec le corps du serpent.
    for case in corps_serpent:
        if serpent.x == case.x and serpent.y == case.y:
            partie_terminee = True
            meilleur_score = mettre_a_jour_meilleur_score(score)
            return
    # Gestion de la consommation de nourriture.
    if serpent.x == nourriture.x and serpent.y == nourriture.y:
        corps_serpent.append(Case(nourriture.x, nourriture.y))
        generer_nourriture()
        score += 1
    # Déplacement du serpent en ajoutant une nouvelle tête et en supprimant la queue.
    for i in range(len(corps_serpent) - 1, -1, -1):
        case = corps_serpent[i]
        if i == 0:
            case.x = serpent.x
            case.y = serpent.y
        else:
            case_prec = corps_serpent[i - 1]
            case.x = case_prec.x
            case.y = case_prec.y
    serpent.x += vitesseX * TAILLE_CASE
    serpent.y += vitesseY * TAILLE_CASE

# Fonction pour générer de la nourriture à un emplacement aléatoire qui n'est pas occupé par le serpent.
def generer_nourriture():
    global nourriture, corps_serpent
    # Boucle jusqu'à trouver une position libre pour la nourriture.
    while True:
        nouvelle_position = Case(random.randint(0, COLONNES - 1) * TAILLE_CASE, random.randint(0, LIGNES - 1) * TAILLE_CASE)
        if all(nouvelle_position.x != case.x or nouvelle_position.y != case.y for case in corps_serpent):
            nourriture = nouvelle_position
            break

# Fonction principale pour dessiner tous les éléments du jeu sur le canvas.
def dessiner():
    global serpent, nourriture, corps_serpent, partie_terminee, score, update_id, meilleur_score
    deplacer()
    canvas.delete("all")
    # Dessine la nourriture et le serpent sur le canvas.
    canvas.create_rectangle(nourriture.x, nourriture.y, nourriture.x + TAILLE_CASE, nourriture.y + TAILLE_CASE, fill='red')
    canvas.create_rectangle(serpent.x, serpent.y, serpent.x + TAILLE_CASE, serpent.y + TAILLE_CASE, fill='dark green')
    for case in corps_serpent:
        canvas.create_rectangle(case.x, case.y, case.x + TAILLE_CASE, case.y + TAILLE_CASE, fill='dark green')
    # Affiche les messages en cas de fin de partie ou affiche le score actuel.
    if partie_terminee:
        canvas.create_text(LARGEUR_FENETRE / 2, HAUTEUR_FENETRE / 2 - 35, font="Arial 20", text="Partie Terminée", fill="white")
        canvas.create_text(LARGEUR_FENETRE / 2, HAUTEUR_FENETRE / 2 + 5, font="Arial 20", text="Score: {}".format(score), fill="white")
        canvas.create_text(LARGEUR_FENETRE / 2, HAUTEUR_FENETRE / 2 + 45, font="Arial 16", text="Cliquez 'R' pour relancer le jeu", fill="white")
        canvas.create_text(LARGEUR_FENETRE / 2, HAUTEUR_FENETRE / 2 + 85, font="Arial 16", text="Meilleur Score: {}".format(meilleur_score), fill="white")
    else:
        canvas.create_text(30, 20, font="Arial 10", text="Score: {}".format(score), fill="white")
        canvas.create_text(58, 40, font="Arial 10", text="Meilleur Score: {}".format(meilleur_score), fill="white")
    update_id = fenetre.after(100, dessiner)

fenetre.mainloop()