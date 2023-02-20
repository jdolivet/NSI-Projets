# importe les modules nécessaires pour ce programme
import tkinter as tk
from random import choice

# déclaration des variables
# (elles sont les mêmes dans chaque grande fonction mais peuvent ne pas fonctionner de la même façon)
tours = 1 # variable qui augmente chaque fois qu'un tours est joué
switch = 0 # variable qui sert pour la fonction joueur_contre_machine_difficile
           # qui va aider au programme à répondre aux mouvements du joueur

# variables pour le compteur (score), a est pour les X et b pour les O
a = 0
b = 0

# Création de la première fenêtre qui va nous permettre choisir le mode de jeu
fenetre_debut = tk.Tk()# Création de la fenêtre
fenetre_debut.title("Tic Tac Toe") # Titre de la fenêtre fenêtre

# Création de l'étiquette de cette fenêtre
label = tk.Label(fenetre_debut, text = "Bienvenu(s), choisis(sez) le mode de jeu.")

# Création des boutons qui vont appeler les différents modes de jeu
btn_pvp = tk.Button(fenetre_debut, text = "joueur contre joueur", height = 5, width = 30)
btn_facile = tk.Button(fenetre_debut, text = "joueur contre machine(facile)", height = 5, width = 30)
btn_difficile = tk.Button(fenetre_debut, text = "joueur contre machine(difficile)", height = 5, width = 30)

# Position des boutons et de l'étiquette
label.grid(row = 0, column = 0, columnspan = 3)
btn_pvp.grid(row = 1, column = 0)
btn_facile.grid(row = 1, column = 1)
btn_difficile.grid(row = 1, column = 2)

# Fonction ou un joueur va jouer contre un autre joueur.
def joueur_contre_joueur(event):
    
    def restart_le_compteur(event):
        """ Procédé qui permet de réinitialiser le score(compteur)"""
        global a
        global b
        a = 0
        b = 0
        points_joueur_X["text"] = a
        points_joueur_O["text"] = b
        
    def restart_la_partie(event):
        """ Procédé qui permet de réinitialiser la partie,
            donc le texte des boutons et le nombre de tours"""
        global tours
        case1["text"] = ""
        case2["text"] = " "
        case3["text"] = "  "
        case4["text"] = "   "
        case5["text"] = "    "
        case6["text"] = "     "
        case7["text"] = "      "
        case8["text"] = "       "
        case9["text"] = "        "
        tours = 1
        
# Neuf procédés, une pour chaque bouton,
# On va vérifier si la case cliquée est vide,
# si elle est vide on va voir si il faut mettre X ou O,
# cela en regardant le reste de tours/2.
# Si ce résultat est différent de 0, alors on va mettre X,
# si le résultat est égal à 0, on va mettre O.
# On va aussi ajouter 1 à la variable tours, enlever le texte de l'étiquette qui_gagne.
# Finalement, appeler la fonction check(), pour voir si on à un gagnant, si on a une égalité
# ou s'il faut continuer.
    def clique1(event):
        global tours
        if case1["text"] == "":
            if tours % 2 != 0:
                case1["text"] = "X"
            else:
                case1["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
        
    def clique2(event):
        global tours
        if case2["text"] == " ":
            if tours % 2 != 0:
                case2["text"] = "X"
            else:
                case2["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
        
    def clique3(event):
        global tours
        if case3["text"] == "  ":
            if tours % 2 != 0:
                case3["text"] = "X"
            else:
                case3["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
            
    def clique4(event):
        global tours
        if case4["text"] == "   ":
            if tours % 2 != 0:
                case4["text"] = "X"
            else:
                case4["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
        
    def clique5(event):
        global tours
        if case5["text"] == "    ":
            if tours % 2 != 0:
                case5["text"] = "X"
            else:
                case5["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
        
    def clique6(event):
        global tours
        if case6["text"] == "     ":
            if tours % 2 != 0:
                case6["text"] = "X"
            else:
                case6["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
        
    def clique7(event):
        global tours
        if case7["text"] == "      ":
            if tours % 2 != 0:
                case7["text"] = "X"
            else:
                case7["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
        
    def clique8(event):
        global tours
        if case8["text"] == "       ":
            if tours % 2 != 0:
                case8["text"] = "X"
            else:
                case8["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
        
    def clique9(event):
        global tours
        if case9["text"] == "        ":
            if tours % 2 != 0:
                case9["text"] = "X"
            else:
                case9["text"] = "O"
            tours += 1
        qui_gagne["text"] = ""
        check()
        
    def check():
        """ Procédé qui vérifie si on a un gagnant, une égalitée, ou s'il faut continuer.
            Pour verifier si quelqu'un a gagné, on regarde si dans les 3 lignes verticales,
            3 horizontales et 2 diagonales, les 3 cases formant chaque ligne ont la même valeur.
            Si elles ont la même valeur, on va regarder si cette ligne est formée de X ou de O.
            Indépendément de qui gagne, le compteur va changer et l'étiquette qui_gagne pour qu'il dise qui a gagné,
            et utiliser la fonction restart_la_partie pour pouvoir jouer une autre partie.
            Si il y a égalité, tours doit être égal à 10 et donc qui_gagne va écrire "Égalité"
            et on va devoir cliquer sur le bouton restart_partie pour jouer une autre partie.
            Si rien de l'antérieur passe, la partie va continuer.""" 
        global a
        global b
        global tours
        if case1["text"] == case2["text"] == case3["text"] or case1["text"] == case4["text"] == case7["text"] or case1["text"] == case5["text"] == case9["text"] :
            if case1["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case1["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
        if case4["text"] == case5["text"] == case6["text"] or case2["text"] == case5["text"] == case8["text"] or case3["text"] == case5["text"] == case7["text"]:
            if case5["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case5["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
        if case7["text"] == case8["text"] == case9["text"] or case3["text"] == case6["text"] == case9["text"]:
            if case9["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case9["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
        elif tours == 10:
            qui_gagne["text"] = "Égalité!"
            tours = 1
    # Fermeture de la fenetre de choix du jeu      
    fenetre_debut.destroy()
    # Création de la fenêtre ou l'on va jouer
    jeu = tk.Tk()
    # Titre de la page
    jeu.title("Tic Tac Toe")
    # Création des étiquettes de la page
        # Etiquettes qui indiquent qui est chaque joueur
    joueurX = tk.Label(jeu, text = "Joueur 1 (X)", height = 5, width = 10, font = 20)
    joueurO = tk.Label(jeu, text = "Joueur 2 (O)", height = 5, width = 10, font = 20)
        # Etiquettes qui forment le compteur(score)
    points_joueur_X = tk.Label(jeu, text = a, font = 10)
    points_joueur_O = tk.Label(jeu, text = b, font = 10)
        # Etiquette qui est le tiret du compteur
    compteur = tk.Label(jeu, text = "-", font = 5)
        # Etiquette qui va dire qui à gagné ou s'il y a égalité
    qui_gagne = tk.Label(jeu, text = "", font = 10)
    
    # Boutons qui vont être utilisés pour jouer        
    case1 = tk.Button(jeu, text = "", bg="lightblue", height = 5, width = 10,font = 20)
    case2 = tk.Button(jeu, text = " ", bg="lightblue", height = 5, width = 10,font = 20)
    case3 = tk.Button(jeu, text = "  ", bg="lightblue", height = 5, width = 10,font = 20)
    case4 = tk.Button(jeu, text = "   ", bg="lightblue", height = 5, width = 10,font = 20)
    case5 = tk.Button(jeu, text = "    ", bg="lightblue", height = 5, width = 10,font = 20)
    case6 = tk.Button(jeu, text = "     ", bg="lightblue", height = 5, width = 10,font = 20)
    case7 = tk.Button(jeu, text = "      ", bg="lightblue", height = 5, width = 10,font = 20)
    case8 = tk.Button(jeu, text = "       ", bg="lightblue", height = 5, width = 10,font = 20)
    case9 = tk.Button(jeu, text = "        ", bg="lightblue", height = 5, width = 10,font = 20)
    restart_compteur = tk.Button(jeu, text = "restart compteur")
    restart_partie = tk.Button(jeu, text = "restart partie")
    
    # Positions des boutons et des étiquettes
    joueurX.grid(row = 0, column = 0)
    joueurO.grid(row = 0, column = 2)
    points_joueur_X.grid(row = 1, column = 0)
    points_joueur_O.grid(row = 1, column = 2)
    compteur.grid(row = 1, column = 1)
    qui_gagne.grid(row = 6, column = 0, columnspan = 3)
    case1.grid(row = 2, column = 0)
    case2.grid(row = 2, column = 1)
    case3.grid(row = 2, column = 2)
    case4.grid(row = 3, column = 0)
    case5.grid(row = 3, column = 1)
    case6.grid(row = 3, column = 2)
    case7.grid(row = 4, column = 0)
    case8.grid(row = 4, column = 1)
    case9.grid(row = 4, column = 2)
    restart_partie.grid( row = 5, column = 2)
    restart_compteur.grid( row = 5, column = 1)
    
    # Quelle fonction va activer chaque bouton
    case1.bind("<Button-1>", clique1)
    case2.bind("<Button-1>", clique2)
    case3.bind("<Button-1>", clique3)
    case4.bind("<Button-1>", clique4)
    case5.bind("<Button-1>", clique5)
    case6.bind("<Button-1>", clique6)
    case7.bind("<Button-1>", clique7)
    case8.bind("<Button-1>", clique8)
    case9.bind("<Button-1>", clique9)
    restart_partie.bind("<Button-1>", restart_la_partie)
    restart_compteur.bind("<Button-1>", restart_le_compteur)
    
#Fonction ou le joueur va jouer contre la machine, il va etre très dur de gagner.
def joueur_contre_machine_difficile(event):
    def machine_difficile():
        """ Procédé qui va nous permettre a la machine comment le tableau
            est situé puis efféctuer le meilleur mouvement possible"""
        global switch
        # On crée un tableau pour mieux étudier la positions des X et O,
        # si dans un case il y a un X, dans le tableau il y aura un 1
        # si dans un case il y a un O, dans le tableau il y aura un 3.
        tab = [[0] * 3 for i in range(3)]
        if case1["text"] == "X":
            tab[0][0] = 1
        if case1["text"] == "O":
            tab[0][0] = 3
        if case2["text"] == "X":
            tab[0][1] = 1
        if case2["text"] == "O":
            tab[0][1] = 3
        if case3["text"] == "X":
            tab[0][2] = 1
        if case3["text"] == "O":
            tab[0][2] = 3
        if case4["text"] == "X":
            tab[1][0] = 1
        if case4["text"] == "O":
            tab[1][0] = 3
        if case5["text"] == "X":
            tab[1][1] = 1
        if case5["text"] == "O":
            tab[1][1] = 3
        if case6["text"] == "X":
            tab[1][2] = 1
        if case6["text"] == "O":
            tab[1][2] = 3
        if case7["text"] == "X":
            tab[2][0] = 1
        if case7["text"] == "O":
            tab[2][0] = 3
        if case8["text"] == "X":
            tab[2][1] = 1
        if case8["text"] == "O":
            tab[2][1] = 3
        if case9["text"] == "X":
            tab[2][2] = 1
        if case9["text"] == "O":
            tab[2][2] = 3

        
        # Ces conditions regardent si dans une ligne( verticale, horizontale ou diagonale)
        # il y a une possibilité de bloquer la victoire du joueur(X),
        # ou s'l y a une possibilité de victoire de l'ordinateur(O).
        
        # Ici le tableau crée avant est utilisé dans toutes les conditions au dessous.
        # Si la somme d'une ligne est égale a 2, cela veut dire qu'il y a deux X dans cette ligne,
        # On cherche donc quelle est la case vide de cette ligne, pour bloquer la victoire du joueur.
        # Le cas contraire, c'est-à-dire que qu'une ligne est égale 6, cela veut qu'il y a deux O dans la ligne,
        # on cherche alors quelle est la case vide de la ligne pour mettre le O et gagner la partie.
        
        if tab[0][0] + tab[0][1] + tab[0][2] == 2 or tab[0][0] + tab[0][1] + tab[0][2] == 6:
            if case1["text"] == "":
                case1["text"] = "O"
                
            elif case2["text"] == " ":
                case2["text"] = "O"
                
            elif case3["text"] == "  ":
                case3["text"] = "O"
   
        elif tab[1][0] + tab[1][1] + tab[1][2] == 2 or tab[1][0] + tab[1][1] + tab[1][2] == 6:
            if case4["text"] == "   ":
                case4["text"] = "O"
                
            elif case5["text"] == "    ":
                case5["text"] = "O"
                
            elif case6["text"] == "     ":
                case6["text"] = "O"

        elif tab[2][0] + tab[2][1] + tab[2][2] == 2 or tab[2][0] + tab[2][1] + tab[2][2] == 6:
            if case7["text"] == "      ":
                case7["text"] = "O"
                
            elif case8["text"] == "       ":
                case8["text"] = "O"
                
            elif case9["text"] == "        ":
                case9["text"] = "O"

        elif tab[0][0] + tab[1][0] + tab[2][0] == 2 or tab[0][0] + tab[1][0] + tab[2][0] == 6:
            if case1["text"] == "":
                case1["text"] = "O"
                
            elif case4["text"] == "   ":
                case4["text"] = "O"
                
            elif case7["text"] == "      ":
                case7["text"] = "O"

        elif tab[0][1] + tab[1][1] + tab[2][1] == 2 or tab[0][1] + tab[1][1] + tab[2][1] == 6:
            if case2["text"] == " ":
                case2["text"] = "O"
                
            elif case5["text"] == "    ":
                case5["text"] = "O"
                
            elif case8["text"] == "       ":
                case8["text"] = "O"

        elif tab[0][2] + tab[1][2] + tab[2][2] == 2 or tab[0][2] + tab[1][2] + tab[2][2] == 6:
            if case3["text"] == "  ":
                case3["text"] = "O"
                
            elif case6["text"] == "     ":
                case6["text"] = "O"
                
            elif case9["text"] == "        ":
                case9["text"] = "O"
                
        elif tab[0][0] + tab[1][1] + tab[2][2] == 2 or tab[0][0] + tab[1][1] + tab[2][2] == 6:
            if case1["text"] == "":
                case1["text"] = "O"
                
            elif case5["text"] == "    ":
                case5["text"] = "O"
                
            elif case9["text"] == "        ":
                case9["text"] = "O"

        elif tab[0][2] + tab[1][1] + tab[2][0] == 2 or tab[0][2] + tab[1][1] + tab[2][0] == 6:
            if case3["text"] == "  ":
                case3["text"] = "O"
                
            elif case5["text"] == "    ":
                case5["text"] = "O"
                
            elif case7["text"] == "      ":
                case7["text"] = "O"
        # Ici commancent les cas particuliers
        # Le premier est que si la case5, c'est-à-dire, celle du milieu est vide, l'ordinateur va jouer au milieu
        # Ceci est dû a ce que si on a le contrôle du milieu on a moins possibilités de perdre.
        elif case5["text"] == "    ":
            case5["text"] = "O"
        
        elif tab[2][0] == tab[0][2] == 1 and tab[1][1] == 3 and case2["text"] == " ":
            case2["text"] = "O"

        elif tab[2][1] == tab[0][2] == 1 and tab[1][1] == 3 and case9["text"] == "        ":
            case9["text"] = "O"

        elif tab[0][0] == tab[2][1] == 1 and tab[1][1] == 3 and case7["text"] == "      ":
            case7["text"] = "O"

        elif tab[2][0] == tab[1][2] == 1 and tab[1][1] == 3 and case9["text"] == "        ":
            case9["text"] = "O"

        elif tab[1][2] == tab[2][1] == 1 and tab[1][1] == 3 and case9["text"] == "        ":
            case9["text"] = "O"
        
        elif tab[1][1] == tab[2][2] == 1 and tab[0][0] == 3 and case3["text"] == "  ":
            case3["text"] = "O"
        
        # Si aucune des conditions au dessus est vraie, l'ordinateur va jouer de la suivante façon.
        # si la case 1 es vide, alors il va le placer à la case 1, si elle est pleine il va jouer à la suivante,
        # à la case 2, et ainsi de suite. Dû a ce système il y a les cas particuliers au-dessus.
        else:                   
            if case1["text"] == "":
                case1["text"] = "O"
            elif case2["text"] == " ":
                case2["text"] = "O"
            elif case3["text"] == "  ":
                case3["text"] = "O"
            elif case4["text"] == "   ":
                case4["text"] = "O"
            elif case5["text"] == "    ":
                case5["text"] = "O"
            elif case6["text"] == "     ":
                case6["text"] = "O"
            elif case7["text"] == "      ":
                case7["text"] = "O"
            elif case8["text"] == "       ":
                case8["text"] = "O"
            elif case9["text"] == "        ":
                case9["text"] = "O"
                
    def restart_le_compteur(event):
        """ Procédé qui permet de réinitialiser le score(compteur)"""
        global a
        global b
        a = 0
        b = 0
        points_joueur_X["text"] = a
        points_joueur_O["text"] = b
        
    def restart_la_partie(event):
        """ Procédé qui permet de réinitialiser la partie,
            donc le texte des boutons et le nombre de tours"""
        global tours
        case1["text"] = ""
        case2["text"] = " "
        case3["text"] = "  "
        case4["text"] = "   "
        case5["text"] = "    "
        case6["text"] = "     "
        case7["text"] = "      "
        case8["text"] = "       "
        case9["text"] = "        "
        tours = 1
# Neuf procédés, une pour chaque bouton,
# On va enlever le texte de l'étiquette qui_gagne.
# On va vérifier si la case cliquée est vide,
# si elle est vide, le texte de cette case sera X et
# on va executer la fonction machine_difficile pour voir ou l'ordinateur va jouer en réponse
# On va aussi ajouter 1 à la variable tours.
# Finalement, appeler la fonction check(), pour voir si on à un gagnant, si on a une égalité
# ou s'il faut continuer.
    def clique1(event):
        global tours
        qui_gagne["text"] = ""
        if case1["text"] == "":
            case1["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def clique2(event):
        global tours
        qui_gagne["text"] = ""
        if case2["text"] == " ":
            case2["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def clique3(event):
        global tours
        qui_gagne["text"] = ""
        if case3["text"] == "  ":
            case3["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def clique4(event):
        global tours
        qui_gagne["text"] = ""
        if case4["text"] == "   ":
            case4["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def clique5(event):
        global tours
        qui_gagne["text"] = ""
        if case5["text"] == "    ":
            case5["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def clique6(event):
        global tours
        qui_gagne["text"] = ""
        if case6["text"] == "     ":
            case6["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def clique7(event):
        global tours
        qui_gagne["text"] = ""
        if case7["text"] == "      ":
            case7["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def clique8(event):
        global tours
        qui_gagne["text"] = ""
        if case8["text"] == "       ":
            case8["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def clique9(event):
        global tours
        qui_gagne["text"] = ""
        if case9["text"] == "        ":
            case9["text"] = "X"
            tours += 1
        machine_difficile()
        check()
    def check():
        """ Procédé qui vérifie si on a un gagnant, une égalitée, ou s'il faut continuer.
            Pour verifier si quelqu'un a gagné, on regarde si dans les 3 lignes verticales,
            3 horizontales et 2 diagonales, les 3 cases formant chaque ligne ont la même valeur.
            Si elles ont la même valeur, on va regarder si cette ligne est formée de X ou de O.
            Indépendément de qui gagne, le compteur va changer et l'étiquette qui_gagne pour qu'il dise qui a gagné,
            et utiliser la fonction restart_la_partie pour pouvoir jouer une autre partie.
            Si il y a égalité, tours doit être égal à 10 et donc qui_gagne va écrire "Égalité"
            et on va devoir cliquer sur le bouton restart_partie pour jouer une autre partie.
            Si rien de l'antérieur passe, la partie va continuer.""" 
        global a
        global b
        global tours
        if case1["text"] == case2["text"] == case3["text"] or case1["text"] == case4["text"] == case7["text"] or case1["text"] == case5["text"] == case9["text"]:
            if case1["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case1["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
            tours = 1
                
        if case4["text"] == case5["text"] == case6["text"] or case2["text"] == case5["text"] == case8["text"] or case3["text"] == case5["text"] == case7["text"]:
            if case5["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case5["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
            tours = 1
        
        if case7["text"] == case8["text"] == case9["text"] or case3["text"] == case6["text"] == case9["text"]:
            if case9["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case9["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
            tours = 1
        if tours == 6:
            qui_gagne["text"] = "Égalité"
    # Fermeture de la fenetre de choix du jeu      
    fenetre_debut.destroy()
    # Création de la fenêtre ou l'on va jouer
    jeu = tk.Tk()
    # Titre de la page
    jeu.title("Tic Tac Toe")
    # Création des étiquettes de la page
        # Etiquettes qui indiquent qui est chaque joueur
    joueurX = tk.Label(jeu, text = "Joueur 1 (X)", height = 5, width = 10, font = 20)
    joueurO = tk.Label(jeu, text = "Joueur 2 (O)", height = 5, width = 10, font = 20)
        # Etiquettes qui forment le compteur(score)
    points_joueur_X = tk.Label(jeu, text = a, font = 10)
    points_joueur_O = tk.Label(jeu, text = b, font = 10)
        # Etiquette qui est le tiret du compteur
    compteur = tk.Label(jeu, text = "-", font = 5)
        # Etiquette qui va dire qui à gagné ou s'il y a égalité
    qui_gagne = tk.Label(jeu, text = "", font = 10)
    
    # Boutons qui vont être utilisés pour jouer        
    case1 = tk.Button(jeu, text = "", bg="lightblue", height = 5, width = 10,font = 20)
    case2 = tk.Button(jeu, text = " ", bg="lightblue", height = 5, width = 10,font = 20)
    case3 = tk.Button(jeu, text = "  ", bg="lightblue", height = 5, width = 10,font = 20)
    case4 = tk.Button(jeu, text = "   ", bg="lightblue", height = 5, width = 10,font = 20)
    case5 = tk.Button(jeu, text = "    ", bg="lightblue", height = 5, width = 10,font = 20)
    case6 = tk.Button(jeu, text = "     ", bg="lightblue", height = 5, width = 10,font = 20)
    case7 = tk.Button(jeu, text = "      ", bg="lightblue", height = 5, width = 10,font = 20)
    case8 = tk.Button(jeu, text = "       ", bg="lightblue", height = 5, width = 10,font = 20)
    case9 = tk.Button(jeu, text = "        ", bg="lightblue", height = 5, width = 10,font = 20)
    restart_compteur = tk.Button(jeu, text = "restart compteur")
    restart_partie = tk.Button(jeu, text = "restart partie")
    
    # Positions des boutons et des étiquettes
    joueurX.grid(row = 0, column = 0)
    joueurO.grid(row = 0, column = 2)
    points_joueur_X.grid(row = 1, column = 0)
    points_joueur_O.grid(row = 1, column = 2)
    compteur.grid(row = 1, column = 1)
    qui_gagne.grid(row = 6, column = 0, columnspan = 3)
    case1.grid(row = 2, column = 0)
    case2.grid(row = 2, column = 1)
    case3.grid(row = 2, column = 2)
    case4.grid(row = 3, column = 0)
    case5.grid(row = 3, column = 1)
    case6.grid(row = 3, column = 2)
    case7.grid(row = 4, column = 0)
    case8.grid(row = 4, column = 1)
    case9.grid(row = 4, column = 2)
    restart_partie.grid( row = 5, column = 2)
    restart_compteur.grid( row = 5, column = 1)
    
    # Quelle fonction va activer chaque bouton
    case1.bind("<Button-1>", clique1)
    case2.bind("<Button-1>", clique2)
    case3.bind("<Button-1>", clique3)
    case4.bind("<Button-1>", clique4)
    case5.bind("<Button-1>", clique5)
    case6.bind("<Button-1>", clique6)
    case7.bind("<Button-1>", clique7)
    case8.bind("<Button-1>", clique8)
    case9.bind("<Button-1>", clique9)
    restart_partie.bind("<Button-1>", restart_la_partie)
    restart_compteur.bind("<Button-1>", restart_le_compteur)
    
def joueur_contre_machine_facile(event):
    
    def restart_le_compteur(event):
        """ Procédé qui permet de réinitialiser le score(compteur)"""
        global a
        global b
        a = 0
        b = 0
        points_joueur_X["text"] = a
        points_joueur_O["text"] = b
        
    def restart_la_partie(event):
        """ Procédé qui permet de réinitialiser la partie,
            donc le texte des boutons et le nombre de tours"""
        global tours
        case1["text"] = ""
        case2["text"] = " "
        case3["text"] = "  "
        case4["text"] = "   "
        case5["text"] = "    "
        case6["text"] = "     "
        case7["text"] = "      "
        case8["text"] = "       "
        case9["text"] = "        "
        tours = 1
        
# Neuf procédés, une pour chaque bouton,
# On crée un tableau avec les cases possibles qui vont plus tard êtres tirées au hasard
# (Pour des raisons logiques,
# chaque tableau dans chaque procédé est différent pour éviter remplacer la case cliquée)
# On va vérifier si la case cliquée est vide,
# si elle est vide, le texte de cette case sera X et
# on va tirer au hasard une case pour voir où l'ordinateur va jouer.
# Si cette case est dejà occupée, il va tirer au hasard jusqu'à trouver une case vide
# (Pour des raisons logiques, chaque tableau
# On va enlever le texte de l'étiquette qui_gagne.
# Finalement, appeler la fonction check(), pour voir si on à un gagnant, si on a une égalité
# ou s'il faut continuer.

    def clique1(event):
        global tours
        cases = [case2, case3, case4, case5, case6, case7, case8, case9]
        if case1["text"] == "":
            case1["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
        
    def clique2(event):
        global tours
        cases = [case1, case3, case4, case5, case6, case7, case8, case9]
        if case2["text"] == " ":
            case2["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
        
    def clique3(event):
        global tours
        cases = [case1, case2, case4, case5, case6, case7, case8, case9]
        if case3["text"] == "  ":
            case3["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
        
    def clique4(event):
        global tours
        cases = [case1, case2, case3, case5, case6, case7, case8, case9]
        if case4["text"] == "   ":
            case4["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
        
    def clique5(event):
        global tours
        cases = [case1, case2, case3, case4, case6, case7, case8, case9]
        if case5["text"] == "    ":
            case5["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
        
    def clique6(event):
        global tours
        cases = [case1, case2, case3, case4, case5, case7, case8, case9]
        if case6["text"] == "     ":
            case6["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
        
    def clique7(event):
        global tours
        cases = [case1, case2, case3, case4, case5, case6, case8, case9]
        if case7["text"] == "      ":
            case7["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
        
    def clique8(event):
        global tours
        cases = [case1, case2, case3, case4, case5, case6, case7, case9]
        if case8["text"] == "       ":
            case8["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
        
    def clique9(event):
        global tours
        cases = [case1, case2, case3, case4, case5, case6, case7, case8]
        if case9["text"] == "        ":
            case9["text"] = "X"
            tours += 1
            variable_while = 1
            while variable_while == 1 and tours < 6:
                case_aleatoire = choice(cases)
                if case_aleatoire["text"] != "X" and case_aleatoire["text"] != "O":
                    case_aleatoire["text"] = "O"
                    variable_while = 0
        qui_gagne["text"] = ""
        check()
    
    def check():
        """ Procédé qui vérifie si on a un gagnant, une égalitée, ou s'il faut continuer.
            Pour verifier si quelqu'un a gagné, on regarde si dans les 3 lignes verticales,
            3 horizontales et 2 diagonales, les 3 cases formant chaque ligne ont la même valeur.
            Si elles ont la même valeur, on va regarder si cette ligne est formée de X ou de O.
            Indépendément de qui gagne, le compteur va changer et l'étiquette qui_gagne pour qu'il dise qui a gagné,
            et utiliser la fonction restart_la_partie pour pouvoir jouer une autre partie.
            Si il y a égalité, tours doit être égal à 10 et donc qui_gagne va écrire "Égalité"
            et on va devoir cliquer sur le bouton restart_partie pour jouer une autre partie.
            Si rien de l'antérieur passe, la partie va continuer."""
        global a
        global b
        global tours
        if case1["text"] == case2["text"] == case3["text"] or case1["text"] == case4["text"] == case7["text"] or case1["text"] == case5["text"] == case9["text"] :
            if case1["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case1["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
        if case4["text"] == case5["text"] == case6["text"] or case2["text"] == case5["text"] == case8["text"] or case3["text"] == case5["text"] == case7["text"]:
            if case5["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case5["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
        if case7["text"] == case8["text"] == case9["text"] or case3["text"] == case6["text"] == case9["text"]:
            if case9["text"] == "X":
                qui_gagne["text"] = "Joueur 1 (X) a gagné!"
                a += 1
                points_joueur_X["text"] = a
            elif case9["text"] == "O":
                qui_gagne["text"] = "Joueur 2 (0) a gagné!"
                b += 1
                points_joueur_O["text"] = b
            restart_la_partie(event)
        elif tours == 6:
            qui_gagne["text"] = "Égalité!"
            tours = 1
            
    # Fermeture de la fenetre de choix du jeu      
    fenetre_debut.destroy()
    # Création de la fenêtre ou l'on va jouer
    jeu = tk.Tk()
    # Titre de la page
    jeu.title("Tic Tac Toe")
    # Création des étiquettes de la page
        # Etiquettes qui indiquent qui est chaque joueur
    joueurX = tk.Label(jeu, text = "Joueur 1 (X)", height = 5, width = 10, font = 20)
    joueurO = tk.Label(jeu, text = "Joueur 2 (O)", height = 5, width = 10, font = 20)
        # Etiquettes qui forment le compteur(score)
    points_joueur_X = tk.Label(jeu, text = a, font = 10)
    points_joueur_O = tk.Label(jeu, text = b, font = 10)
        # Etiquette qui est le tiret du compteur
    compteur = tk.Label(jeu, text = "-", font = 5)
        # Etiquette qui va dire qui à gagné ou s'il y a égalité
    qui_gagne = tk.Label(jeu, text = "", font = 10)
    
    # Boutons qui vont être utilisés pour jouer        
    case1 = tk.Button(jeu, text = "", bg="lightblue", height = 5, width = 10,font = 20)
    case2 = tk.Button(jeu, text = " ", bg="lightblue", height = 5, width = 10,font = 20)
    case3 = tk.Button(jeu, text = "  ", bg="lightblue", height = 5, width = 10,font = 20)
    case4 = tk.Button(jeu, text = "   ", bg="lightblue", height = 5, width = 10,font = 20)
    case5 = tk.Button(jeu, text = "    ", bg="lightblue", height = 5, width = 10,font = 20)
    case6 = tk.Button(jeu, text = "     ", bg="lightblue", height = 5, width = 10,font = 20)
    case7 = tk.Button(jeu, text = "      ", bg="lightblue", height = 5, width = 10,font = 20)
    case8 = tk.Button(jeu, text = "       ", bg="lightblue", height = 5, width = 10,font = 20)
    case9 = tk.Button(jeu, text = "        ", bg="lightblue", height = 5, width = 10,font = 20)
    restart_compteur = tk.Button(jeu, text = "restart compteur")
    restart_partie = tk.Button(jeu, text = "restart partie")
    
    # Positions des boutons et des étiquettes
    joueurX.grid(row = 0, column = 0)
    joueurO.grid(row = 0, column = 2)
    points_joueur_X.grid(row = 1, column = 0)
    points_joueur_O.grid(row = 1, column = 2)
    compteur.grid(row = 1, column = 1)
    qui_gagne.grid(row = 6, column = 0, columnspan = 3)
    case1.grid(row = 2, column = 0)
    case2.grid(row = 2, column = 1)
    case3.grid(row = 2, column = 2)
    case4.grid(row = 3, column = 0)
    case5.grid(row = 3, column = 1)
    case6.grid(row = 3, column = 2)
    case7.grid(row = 4, column = 0)
    case8.grid(row = 4, column = 1)
    case9.grid(row = 4, column = 2)
    restart_partie.grid( row = 5, column = 2)
    restart_compteur.grid( row = 5, column = 1)
    
    # Quelle fonction va activer chaque bouton
    case1.bind("<Button-1>", clique1)
    case2.bind("<Button-1>", clique2)
    case3.bind("<Button-1>", clique3)
    case4.bind("<Button-1>", clique4)
    case5.bind("<Button-1>", clique5)
    case6.bind("<Button-1>", clique6)
    case7.bind("<Button-1>", clique7)
    case8.bind("<Button-1>", clique8)
    case9.bind("<Button-1>", clique9)
    restart_partie.bind("<Button-1>", restart_la_partie)
    restart_compteur.bind("<Button-1>", restart_le_compteur)

# Les fonctions que vont activer les boutons de la première fenêtre
btn_pvp.bind("<Button-1>", joueur_contre_joueur)
btn_difficile.bind("<Button-1>", joueur_contre_machine_difficile)
btn_facile.bind("<Button-1>", joueur_contre_machine_facile)