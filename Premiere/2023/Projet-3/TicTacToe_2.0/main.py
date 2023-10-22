import pyxel

pyxel.init(200, 200)

from choix_joueur import choix_joueur_1, choix_joueur_2
from grille import dessiner_grille
from victoire import victoire


joueur_1 = input("Joueur 1, veuillez entrer votre nom : ")
joueur_2 = input("Joueur 2, veuillez entrer votre nom : ")


print(f"{joueur_1} sera X et {joueur_2} sera O.\n")

case_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
tour_joueur = "X"

def update():
    global tour_joueur, case_dict, joueur_1, joueur_2
    
    if tour_joueur == "X":
        choix_joueur_1(joueur_1, case_dict, tour_joueur)
            
        if victoire(case_dict, tour_joueur) == True:
            print(f"{joueur_1} a gagné!")
            pyxel.quit()
        
        tour_joueur = "O"
    
    elif tour_joueur == "O":
        choix_joueur_2(joueur_2, case_dict, tour_joueur)
        
        if victoire(case_dict, tour_joueur) == True:
            print(f"{joueur_2} a gagné!")
            pyxel.quit()
        
        tour_joueur = "X"


def draw():
    dessiner_grille()

pyxel.run(draw, update)
