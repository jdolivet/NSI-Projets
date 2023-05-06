from turtle import *
from projet_grille import grille
from circle_model import O
from x_model import X

q_fois_x = 0
q_fois_o = 0
case1 = 0
case2 = 0
case3 = 0
case4 = 0
case5 = 0
case6 = 0
case7 = 0
case8 = 0
case9 = 0

# Demander aux joueurs de saisir leur nom
joueur_1 = input("Joueur 1, veuillez entrer votre nom : ")
joueur_2 = input("Joueur 2, veuillez entrer votre nom : ")

# Attribuer les symboles "X" et "O"
joueur1_symb = "X"
joueur2_symb = "O"

print(f"{joueur_1} sera {joueur1_symb} et {joueur_2} sera {joueur2_symb}.\n")

grille()

def horizontale_o():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9
    if case1 == 2 and case2 == 2 and case3 == 2:
        return True
    elif case4 == 2 and case5 == 2 and case6 == 2:
        return True
    elif case7 == 2 and case8 == 2 and case9 == 2:
        return True 

def verticale_o():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9
    if case1 == 2 and case4 == 2 and case7 == 2:
        return True
    elif case2 == 2 and case5 == 2 and case8 == 2:
        return True
    elif case3 == 2 and case6 == 2 and case9 == 2:
        return True

def diagonale_o():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9
    if case1 == 2 and case5 == 2 and case9 == 2:
        return True
    elif case3 == 2 and case5 == 2 and case7 == 2:
        return True
        
def horizontale_x():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9
    if case1 == 1 and case2 == 1 and case3 == 1:
        return True
    elif case4 == 1 and case5 == 1 and case6 == 1:
        return True
    elif case7 == 1 and case8 == 1 and case9 == 1:
        return True 

def verticale_x():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9
    if case1 == 1 and case4 == 1 and case7 == 1:
        return True
    elif case2 == 1 and case5 == 1 and case8 == 1:
        return True
    elif case3 == 1 and case6 == 1 and case9 == 1:
        return True

def diagonale_x():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9
    if case1 == 1 and case5 == 1 and case9 == 1:
        return True
    elif case3 == 1 and case5 == 1 and case7 == 1:
        return True

def partie_x():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9, joueur_1
    choix_joueur = int(input(f"{joueur_1}, choisissez une case (1 à 9): "))
    if choix_joueur == 1:
        X(-200,150)
        case1 = 1
        return case1
    if choix_joueur == 2:
        X(-25,150)
        case2 = 1
        return case2
    if choix_joueur == 3:
        X(150,150)
        case3 = 1
        return case3
    if choix_joueur == 4:
        X(-200,-5)
        case4 = 1
        return case4
    if choix_joueur == 5:
        X(-25,-5)
        case5 = 1
        return case5
    if choix_joueur == 6:
        X(150,-5)
        case6 = 1
        return case6
    if choix_joueur == 7:
        X(150,-150)
        case7 = 1
        return case6
    if choix_joueur == 8:
        X(-25,-150)
        case8 = 1
        return case8
    if choix_joueur == 9:
        X(-200,-150)
        case9 = 1
        return case9

def partie_o():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9, joueur_2
    choix_joueur = int(input(f"{joueur_2}, choisissez une case (1 à 9): "))
    if choix_joueur == 1:
        O(-185,150)
        case1 = 2
        return case1
    if choix_joueur == 2:
        O(-10,150)
        case2 = 2
        return case2
    if choix_joueur == 3:
        O(175,150)
        case3 = 2
        return case3
    if choix_joueur == 4:
        O(-185,-5)
        case4 = 2
        return case4
    if choix_joueur == 5:
        O(-10,-5)
        case5 = 2
        return case5
    if choix_joueur == 6:
        O(175,-5)
        case6 = 2
        return case6
    if choix_joueur == 7:
        O(175,-175)
        case7 = 2
    if choix_joueur == 8:
        O(-10,-175)
        case8 = 2
        return case8
    if choix_joueur == 9:
        O(-185,-175)
        case9 = 2
        return case9

for i in range(9):
    partie_x()
    q_fois_x += 1
    if horizontale_x() == True:
        print(f"{joueur_1} a gagné, éxécutez le jeu à nouveau afin de rejouer")
        break
    if verticale_x() == True:
        print(f"{joueur_1} a gagné, éxécutez le jeu à nouveau afin de rejouer")
        break
    if diagonale_x() == True:
        print(f"{joueur_1} a gagné, éxécutez le jeu à nouveau afin de rejouer")
        break
    while q_fois_x > q_fois_o:
        partie_o()
        q_fois_o += 1
        if horizontale_o() == True:
            print(f"{joueur_2} a gagné, éxécutez le jeu à nouveau afin de rejouer")
            break 
        if verticale_o() == True:
            print(f"{joueur_2} a gagné, éxécutez le jeu à nouveau afin de rejouer")
            break
        if diagonale_o() == True:
            print(f"{joueur_2} a gagné, éxécutez le jeu à nouveau afin de rejouer")
            break
    
    if case1 != 0 and case2 != 0 and case3 != 0 and case4 != 0 and case5 != 0 and case6 != 0 and case7 != 0 and case8 != 0 and case9 != 0:
            print("Match Nul")
            


