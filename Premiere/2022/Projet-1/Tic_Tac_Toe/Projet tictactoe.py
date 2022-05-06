import random

tab= {'1,1': ' ' , '1,2': ' ' , '1,3': ' ' , #dictionnaire qui attribue une clé (ligne, colonne) à un élément
      '2,1': ' ' , '2,2': ' ' , '2,3': ' ' ,
      '3,1': ' ' , '3,2': ' ' , '3,3': ' ' }
#définition de chaque place du tableau par le nombre de la ligne et de la colonne de la grille
    
def affichage(tab):    #fonction pour afficher le tableau 
    print(tab['1,1'] , '|' , tab['1,2'] , '|' , tab['1,3'])  #première ligne
    print('—————————')  #division entre la ligne 1 et 2
    print(tab['2,1'] , '|' , tab['2,2'] , '|' , tab['2,3'])  #deuxième ligne
    print('—————————')  #division entre la ligne 2 et 3 
    print(tab['3,1'] , '|' , tab['3,2'] , '|' , tab['3,3'])  #troisième ligne

    
def tic_tac_toe():  #fonction principale
    j= random.randint(0, 1)  #choisi au hasard le joueur qui commence
    if j==0:
        symb= "X"
    else:
        symb= "O"
    tour = 0  #nombre de tours 
    for _ in range(len(tab)):
        affichage(tab)
        pos= input(f"Tour de {symb}. Indiquez la ligne puis la colonne (l,c):")  #demande le joueur la position souhaitée et stocke la réponse dans la variable pos
        if tab[pos] == ' ':  #vérifie si la case sélectionnée est vide
            tab[pos] = symb  #change le vide par le symbole 
            tour += 1   #ajoute 1 au tour pour compter le nombre de tours
            
        else:
            print("Celle-ci est déjà remplie. Indiquez une autre place.") #au cas où le joueur saisit une position déjà occupée
            continue
        # Après 5 tours, on vérifie si un des joueurs a fait un point
        if tour >= 5:
            if tab['1,1'] == tab['1,2'] == tab['1,3'] != ' ': # première ligne
                affichage(tab)  
                print(f"Le joueur {symb} a gagné!")  #affiche le gagnant                         
                break  #arrêt de la boucle bouléenne
            elif tab['2,1'] == tab['2,2'] == tab['2,3'] != ' ': # deuxième ligne
                affichage(tab)
                print(f"Le joueur {symb} a gagné!")               
                break    
            elif tab['3,1'] == tab['3,2'] == tab['3,3'] != ' ': # troisième ligne
                affichage(tab)
                print(f"Le joueur {symb} a gagné!")                
                break
            elif tab['1,1'] == tab['2,1'] == tab['3,1'] != ' ': # côté gauche
                affichage(tab)
                print(f"Le joueur {symb} a gagné!")                
                break
            elif tab['1,2'] == tab['2,2'] == tab['3,2'] != ' ': # milieu
                affichage(tab)
                print(f"Le joueur {symb} a gagné!")                
                break
            elif tab['1,3'] == tab['2,3'] == tab['3,3'] != ' ': # côté droit
                affichage(tab)
                print(f"Le joueur {symb} a gagné!")                
                break
            elif tab['1,1'] == tab['2,2'] == tab['3,3'] != ' ': # diagonale 1
                affichage(tab)
                print(f"Le joueur {symb} a gagné!")                
                break
            elif tab['1,3'] == tab['2,2'] == tab['3,1'] != ' ': # diagonale 2
                affichage(tab)
                print(f"Le joueur {symb} a gagné!")                
                break
        if tour == 9: #l'égalité est obligatoire en arrivant au 9ème tour
            affichage(tab)
            print("Égalité")
        
        if symb =='X':  #change le symbole à chaque tour
            symb = 'O'
        else:
            symb = 'X'
      