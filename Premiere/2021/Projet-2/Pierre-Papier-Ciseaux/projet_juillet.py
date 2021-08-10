from random import randint 
import tkinter as tk
from tkinter.constants import ANCHOR, BOTH, BOTTOM, LEFT, NONE, RAISED, TOP 
from tkinter import Label, PhotoImage

score_joueur_1 = 0 
score_joueur_2 = 0
ami_ou_ordi = 0 # <- variable pour arranger l'interface dependant si c'est contre ordi ou joueur

#creation de la fenetre et le fond d'image
fenetre = tk.Tk()
fenetre.title("Pierre Feuille Ciseaux")
backgroundfenetre = PhotoImage(file = "wallpaper_nsi.png")
label_fond = Label(fenetre, image = backgroundfenetre)
label_fond.place(x= 0, y = 0) 

panneau_boutons = tk.Frame(fenetre)
reglesdejeu = tk.Label(panneau_boutons, 
                       text = """Pressionez 0 si vous jouez contre un ordi
Pressionez 1 si vous jouez avec un ami""", font = 25)

#panneau avec le compte du score qui va apparaitre apres
panneau_score = tk.Frame(fenetre)
label_de_score_1 = tk.Label(fenetre, text= f"Score Joueur 1: {score_joueur_1}",
                            font = "20", relief= tk.RAISED)
label_de_score_2 = tk.Label(fenetre, text= f"Score Joueur 2: {score_joueur_2}", 
                            font = "20", relief= tk.RAISED) 

#panneau de boutons gauche et droite individuelle
panneau_boutons_gauche = tk.Frame(fenetre)
panneau_boutons_gauche.pack(side = tk.LEFT)
bouton_joueur_gauche0 = tk.Button(panneau_boutons_gauche, 
                                  text= "Pierre", width = 20, height = 5, font = 15)
bouton_joueur_gauche1 = tk.Button(panneau_boutons_gauche, 
                                  text = "Feuille", width = 20, height = 5, font = 15)
bouton_joueur_gauche2 = tk.Button(panneau_boutons_gauche, 
                                  text = "Ciseaux", width = 20, height = 5, font = 15)

panneau_boutons_droite = tk.Frame(fenetre)
panneau_boutons_droite.pack(side = tk.RIGHT)
bouton_joueur_droite0 = tk.Button(panneau_boutons_droite, 
                                  text= "Pierre", width = 20, height = 5, font = 15)
bouton_joueur_droite1 = tk.Button(panneau_boutons_droite, 
                                  text = "Feuille", width = 20, height = 5, font = 15)
bouton_joueur_droite2 = tk.Button(panneau_boutons_droite, 
                                  text = "Ciseaux", width = 20, height = 5, font = 15)

#canvas qui va afficher les images avec le tour des joueurs
canevas_gauche = tk.Canvas(fenetre, width = 256, height = 500,
                           background = "grey32")
canevas_droite = tk.Canvas(fenetre, width = 256, height = 500,
                           background= "grey64") 

#boutons si on joue contre un ordi or contre un autre joueurs
btn0 = tk.Button(panneau_boutons, text = "Ordinateur", width = 20, height = 5)
btn1 = tk.Button(panneau_boutons, text = "Joueurs", width = 20, height = 5)
btn0.pack()
btn1.pack()
panneau_boutons.pack()
reglesdejeu.pack(side = tk.TOP)

ami_ou_ordi = 0 #variable pour configuer l'interface

#fonctions pour ranger l'interface et preparer pour jouer
def range_jeu():
    """Cache les boutons qu'on nous presente a l'ouverture,
    affiche les canvas et nous presente au moins les boutons pour un joueur."""
    panneau_score.place(relx = 0.5, rely = 0.6, anchor= "center")
    label_de_score_1.pack()
    label_de_score_2.pack()
    canevas_gauche.pack(padx = 8, pady = 8, side = tk.LEFT)
    canevas_droite.pack( padx = 8, pady = 8, side = tk.RIGHT)
    btn0.forget()
    btn1.forget()
    bouton_joueur_gauche0.pack()
    bouton_joueur_gauche1.pack()
    bouton_joueur_gauche2.pack()

def changetextOrdi(event):
    """Configure l'interface et créer du texte sur les canvas pour jouer contre
    un ordinateur"""
    global reglesdejeu
    global ami_ou_ordi
    range_jeu()
    reglesdejeu.config(text = "Choisissez un des trois choix")
    canevas_gauche.create_text(128,200, text= "Joueur",fill=
        "black",font=('Helvetica 15 bold'))
    canevas_droite.create_text(128,200, text= "Ordinateur",fill=
        "black",font=('Helvetica 15 bold'))
    ami_ou_ordi = 1
   
def changetextDeux(event): 
    """Configure l'interface et créer du texte sur les canvas pour jouer contre
    un joueur"""
    global reglesdejeu
    global ami_ou_ordi
    change_text_premier_joueur()
    range_jeu()
    canevas_gauche.create_text(128,200, text= "Joueur 1",fill=
        "black",font=('Helvetica 15 bold'))
    canevas_droite.create_text(128,200, text= "Joueur 2",fill=
        "black",font=('Helvetica 15 bold'))
    bouton_joueur_droite0.pack()
    bouton_joueur_droite1.pack()
    bouton_joueur_droite2.pack()
       
btn0.bind("<Button-1>", changetextOrdi)
btn1.bind("<Button-1>", changetextDeux)


#variables pour savoir qui a gagne et montrer les images du tour du joueur
joueur_gauche = int()
ordinateur_aleatoire = int()
joueur_droite = int()
photo_pierre = PhotoImage(file = "rock.png")
photo_feuille = PhotoImage(file = "paper.png")
photo_ciseaux = PhotoImage(file = "scissors.png")

#fonctions vont determiner quelle a ete le tour de chacun
def evenement_ordinateur():
    global ordinateur_aleatoire
    ordinateur_aleatoire = randint(0,2)

def evenement_pierre_gauche(event):
    global joueur_gauche
    joueur_gauche = 0
    if ami_ou_ordi == 1:
        gagnante_contre_ordi()

def evenement_feuille_gauche(event):
    global joueur_gauche
    joueur_gauche = 1 
    if ami_ou_ordi == 1:
        gagnante_contre_ordi()
  
def evenement_ciseaux_gauche(event):
    global joueur_gauche
    joueur_gauche = 2 
    if ami_ou_ordi == 1:
        gagnante_contre_ordi()

def evenement_pierre_droite(event):
    global joueur_droite
    joueur_droite = 0
    gagnante_contre_ami()
    
def evenement_feuille_droite(event):
    global joueur_droite
    joueur_droite = 1
    gagnante_contre_ami()
    
def evenement_ciseaux_droite(event):
    global joueur_droite
    joueur_droite = 2
    gagnante_contre_ami()

#remets le texte après apparaitre durant une seconde le resultat du tour
def change_text_premier_joueur():
    reglesdejeu.config(text ="""Joueur 1 vous commencé""")

#fonctions pour montrer par des images representatives les tours des joueurs après le resultat
def photos_choix_gauche():
    """Montre avec des images le tour du joueur a gauche"""
    if joueur_gauche == 0:
        canevas_gauche.create_image(35,110, image = photo_pierre, anchor = tk.NW)   
    elif joueur_gauche == 1:
        canevas_gauche.create_image(35,110, image = photo_feuille, anchor = tk.NW)
    elif joueur_gauche == 2:
        canevas_gauche.create_image(35,110, image = photo_ciseaux, anchor = tk.NW)

def photos_choix_ordi():
    """Montre avec des images le tour de l'ordinateur"""
    if ordinateur_aleatoire == 0:
        canevas_droite.create_image(35,110, image = photo_pierre, anchor = tk.NW)   
    elif ordinateur_aleatoire == 1:
        canevas_droite.create_image(35,110, image = photo_feuille, anchor = tk.NW)
    elif ordinateur_aleatoire== 2:
        canevas_droite.create_image(35,110, image = photo_ciseaux, anchor = tk.NW)

def photos_choix_droite():
    """Montre avec des images le tour du joueur a droite"""
    if joueur_droite == 0:
        canevas_droite.create_image(35,110, image = photo_pierre, anchor = tk.NW)   
    elif joueur_droite == 1:
        canevas_droite.create_image(35,110, image = photo_feuille, anchor = tk.NW)
    elif joueur_droite== 2:
        canevas_droite.create_image(35,110, image = photo_ciseaux, anchor = tk.NW)

#fonction pour changer les couleurs des labels
def couleur_gagnant_score():
    """Change la couleur dependant de qui a le plus grand score"""
    if score_joueur_1 > score_joueur_2:
        label_de_score_1.config(bg = "green")
        label_de_score_2.config(bg = "white smoke")
    elif score_joueur_2 > score_joueur_1:
        label_de_score_2.config(bg = "green")
        label_de_score_1.config(bg = "white smoke")

#les boutons peuvent pour l'instant seulement etre activer avec 
# le bouton gauche de la souris
bouton_joueur_gauche0.bind("<Button-1>", evenement_pierre_gauche)
bouton_joueur_gauche1.bind("<Button-1>", evenement_feuille_gauche)
bouton_joueur_gauche2.bind("<Button-1>", evenement_ciseaux_gauche)
bouton_joueur_droite0.bind("<Button-1>", evenement_pierre_droite)
bouton_joueur_droite1.bind("<Button-1>", evenement_feuille_droite)
bouton_joueur_droite2.bind("<Button-1>", evenement_ciseaux_droite)

#tiens compte du resultat
score_joueur_1 = 0
score_joueur_2 = 0

#fonctions qui augmente les scores, change les couleurs des labels, 
# montre les photos et determinent les gagnants
def gagnante_contre_ordi():
    """Determine les gagnants de chaque tour si on est contre un ordinateur"""
    global score_joueur_1
    global score_joueur_2
    evenement_ordinateur()
    #Ce tableau permet de rapidement pouvoir determiner d'une facon efficace le gagnant après chaque tour
    # -1 = egalite, 0 = pierre gagne, 1 = papier gagne, 2 = ciseaux gagne
    tab_test_gagnant = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]] 
    gagnant = tab_test_gagnant[joueur_gauche][ordinateur_aleatoire]
    if gagnant == joueur_gauche:
        score_joueur_1 += 1
        label_de_score_1.config(text= f"Score Joueur 1: {score_joueur_1}")
        reglesdejeu.config(text = "Vous avez gagné")
    elif gagnant == ordinateur_aleatoire:
        score_joueur_2 += 1
        label_de_score_2.config(text= f"Score Joueur 2: {score_joueur_2}")
        reglesdejeu.config(text= "L'ordinateur a gagné")
    elif gagnant == -1: 
        label_de_score_1.config(text= f"Score Joueur 1: {score_joueur_1}")
        label_de_score_2.config(text= f"Score Joueur 2: {score_joueur_2}")
        reglesdejeu.config(text = "Egalité")
    couleur_gagnant_score()
    photos_choix_gauche()
    photos_choix_ordi()

def gagnante_contre_ami():
    """Determine les gagnants de chaque tour si on est contre un joueur"""
    global score_joueur_1
    global score_joueur_2
    tab_test_gagnant = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]] 
    gagnant = tab_test_gagnant[joueur_gauche][joueur_droite]
    if gagnant == joueur_gauche:
        score_joueur_1 += 1
        label_de_score_1.config(text= f"Score Joueur 1: {score_joueur_1}")
        reglesdejeu.config(text = "Joueur 1 a gagné")
    elif gagnant == joueur_droite:
        score_joueur_2 += 1
        label_de_score_2.config(text= f"Score Joueur 2: {score_joueur_2}")
        reglesdejeu.config(text= "Joueur 2 a gagné")
    elif gagnant == -1: 
        label_de_score_1.config(text= f"Score Joueur 1: {score_joueur_1}")
        label_de_score_2.config(text= f"Score Joueur 2: {score_joueur_2}")
        reglesdejeu.config(text = "Egalité")
    reglesdejeu.after(1000, change_text_premier_joueur)
    couleur_gagnant_score()
    photos_choix_gauche()
    photos_choix_droite()

fenetre.mainloop()