import definitions, pyxel

def deploiement(liste_ballons: list, carte_choisie: str, liste_deploiement: list):
    """Envoie tous les ballons d'un round"""
    if carte_choisie != "En attente":
        if carte_choisie == "1":
            debut = (-17, 60)
        elif carte_choisie == "2":
            debut = (-17, 95)
        elif carte_choisie == "3":
            debut = (152, -17)
        elif carte_choisie == "4":
            debut = (-17, 60)
            
        if pyxel.frame_count % 15 == 0:
            liste_ballons.append(definitions.Ballon(debut[0], debut[1], liste_deploiement[0]))
            liste_deploiement.remove(liste_deploiement[0])
            


    