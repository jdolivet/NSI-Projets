import pyxel
from fonctions_symboles import dessiner_o, dessiner_x


def choix_joueur_1(prenom: str, case_dict: dict, tour_joueur: str):
    
    choix_joueur = int(input(f"{prenom}, choisissez une case (1 à 9): "))
    assert choix_joueur != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 == 'choisir un nombre'
    

    
    coordinates = { 1: (30, 35), 2: (100, 35), 3: (165, 35),
        4: (30, 100), 5: (100, 100), 6: (165, 100),
        7: (30, 165), 8: (100, 165), 9: (165, 165)}
    
    if choix_joueur in coordinates and case_dict[choix_joueur] == 0:
        x, y = coordinates[choix_joueur]
        dessiner_x(x, y)
        case_dict[choix_joueur] = "X"
    
    else:
        print("Case invalide ou déjà prise. Le tour est passé au prochain.")

    return tour_joueur, case_dict
   


def choix_joueur_2(prenom: str, case_dict: dict, tour_joueur: str):
    
    choix_joueur = int(input(f"{prenom}, choisissez une case (1 à 9): "))
    assert choix_joueur != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 == 'choisir un nombre'
    
    coordinates = { 1: (30, 35), 2: (100, 35), 3: (165, 35),
        4: (30, 100), 5: (100, 100), 6: (165, 100),
        7: (30, 165), 8: (100, 165), 9: (165, 165)}
    
    if choix_joueur in coordinates and case_dict[choix_joueur] == 0:
        x, y = coordinates[choix_joueur]
        dessiner_o(x, y)
        case_dict[choix_joueur] = "O"
    
    else:
        print("Case invalide ou déjà prise. Le tour est passé au prochain.")
        
        
    return tour_joueur, case_dict

