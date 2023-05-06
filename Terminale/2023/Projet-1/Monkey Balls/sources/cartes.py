from definitions import Ballon

def cartes_mouv(tab: list, type_carte):
    """Fait avancer dans le parcours de la première carte
    les elements de tab."""
    vie_perdue = 0
    for elt in tab:           
        if type_carte == "1":
            if -17 - (elt.longueur // 2) <= elt.x <= 151 - (elt.longueur // 2) and elt.y == 60 - (elt.taille // 2)\
               and elt.tour == 0:
                elt.x += 1
            elif elt.x == 88 - (elt.longueur // 2) and 14 - (elt.taille // 2) <= elt.y <= 117 - (elt.taille // 2) \
                 and elt.tour == 1:
                elt.y += 1
            elif elt.x == 152 - (elt.longueur // 2) and 15 - (elt.taille // 2) <= elt.y <= 60 - (elt.taille // 2):
                elt.y -= 1
                elt.tour = 1
            elif 89 - (elt.longueur // 2) <= elt.x <= 152 - (elt.longueur // 2) and elt.y == 14 - (elt.taille // 2):
                elt.x -= 1
            elif 24 - (elt.longueur // 2) <= elt.x <= 88 - (elt.longueur // 2) and elt.y == 118 - (elt.taille // 2):
                elt.x -= 1
            elif elt.x == 23 - (elt.longueur // 2) and 85 - (elt.taille // 2) <= elt.y <= 118 - (elt.taille // 2):
                elt.y -= 1
                elt.tour = 2
            elif 23 - (elt.longueur // 2) <= elt.x <= 183 - (elt.longueur // 2) and elt.y == 84 - (elt.taille // 2)\
                 and elt.tour == 2:
                elt.x += 1
            elif elt.x == 184 - (elt.longueur // 2) and 84 - (elt.taille // 2) <= elt.y <= 128 + (elt.taille // 2):
                elt.y += 1               
            elif elt.y < 128 + elt.taille:
                vie_perdue += elt.vies
                if elt.suivant is not None:
                    for nouveau_ballon in elt.suivant:
                        tab.append(Ballon(elt.x + (elt.longueur // 2), elt.y + (elt.taille // 2), nouveau_ballon))
                tab.remove(elt)
                
        elif type_carte == "2":
            #print(elt.x + (elt.longueur // 2), elt.y + (elt.taille // 2))
            if -17 - (elt.longueur // 2) <= elt.x <= 6 - (elt.longueur // 2) and elt.y == 95 - (elt.taille // 2):
                elt.x += 1
            elif 7 - (elt.longueur // 2) <= elt.x <= 44 - (elt.longueur // 2) and 22 - (elt.taille // 2) <= elt.y <= 95 - (elt.taille // 2):
                elt.x += 0.5
                elt.y -= 1
            elif 44 - (elt.longueur // 2) <= elt.x <= 153 - (elt.longueur // 2) and elt.y == 21 - (elt.taille // 2):
                elt.x += 1
            elif 109 - (elt.longueur // 2) <= elt.x <= 154 - (elt.longueur // 2) and 21 - (elt.taille // 2) <= elt.y <= 110 - (elt.taille // 2):
                elt.x -= 0.5
                elt.y += 1
            elif  49 - (elt.longueur // 2) <= elt.x <= 109 - (elt.longueur // 2) and elt.y == 111 - (elt.taille // 2):
                elt.x -= 1
            elif elt.x == 48 - (elt.longueur // 2) and 111 - (elt.taille // 2) <= elt.y <= 128 + (elt.taille // 2):
                elt.y += 1
            elif elt.y < 128 + elt.taille:
                vie_perdue += elt.vies
                if elt.suivant is not None:
                    for nouveau_ballon in elt.suivant:
                        tab.append(Ballon(elt.x + (elt.longueur // 2), elt.y + (elt.taille // 2), nouveau_ballon))
                tab.remove(elt)
                
        elif type_carte == "3":
            if elt.x == 152 - (elt.longueur // 2) and -17 - (elt.taille // 2) <= elt.y <= 47 - (elt.taille // 2):
                elt.y += 1
            elif  120 - (elt.longueur // 2) <= elt.x <= 152 - (elt.longueur // 2) and elt.y == 48 - (elt.taille // 2):
                elt.x -= 1
            elif 69 - (elt.longueur // 2) <= elt.x <= 119 - (elt.longueur // 2) and 23 - (elt.taille // 2) <= elt.y <= 48 - (elt.taille // 2):
                elt.x -= 1
                elt.y -= 0.5
            elif  18 - (elt.longueur // 2) <= elt.x <= 68 - (elt.longueur // 2) and elt.y == 22.5 - (elt.taille // 2):
                elt.x -= 1
            elif elt.x == 17 - (elt.longueur // 2) and 22.5 - (elt.taille // 2) <= elt.y <= 85 - (elt.taille // 2):
                elt.y += 1
            elif 17 - (elt.longueur // 2) <= elt.x <= 60 - (elt.longueur // 2) and 85.5 - (elt.taille // 2) <= elt.y <= 107 - (elt.taille // 2):
                elt.x += 1
                elt.y += 0.5
            elif  60.5 - (elt.longueur // 2) <= elt.x <= 103 - (elt.longueur // 2) and elt.y == 107.5 - (elt.taille // 2):
                elt.x += 1
            elif elt.x == 104 - (elt.longueur // 2) and 85.5 - (elt.taille // 2) <= elt.y <= 107.5 - (elt.taille // 2):
                elt.y -= 1
            elif  43 - (elt.longueur // 2) <= elt.x <= 104 - (elt.longueur // 2) and elt.y == 84.5 - (elt.taille // 2):
                elt.x -= 1
            elif elt.x == 42 - (elt.longueur // 2) and 45.5 - (elt.taille // 2) <= elt.y <= 84.5 - (elt.taille // 2):
                elt.y -= 1
            elif  42 - (elt.longueur // 2) <= elt.x <= 58 - (elt.longueur // 2) and elt.y == 44.5 - (elt.taille // 2):
                elt.x += 1
            elif 58 - (elt.longueur // 2) <= elt.x <= 110 - (elt.longueur // 2) and 44.5 - (elt.taille // 2) <= elt.y <= 70.5 - (elt.taille // 2):
                elt.x += 1
                elt.y += 0.5
            elif 111 - (elt.longueur // 2) <= elt.x <= 143 - (elt.longueur // 2) and elt.y == 70.5 - (elt.taille // 2):
                elt.x += 1
            elif elt.x == 144 - (elt.longueur // 2) and 70.5 - (elt.taille // 2) <= elt.y <= 128 + (elt.taille // 2):
                elt.y += 1
            elif elt.y < 128 + elt.taille:
                vie_perdue += elt.vies
                if elt.suivant is not None:
                    for nouveau_ballon in elt.suivant:
                        tab.append(Ballon(elt.x + (elt.longueur // 2), elt.y + (elt.taille // 2), nouveau_ballon))
                tab.remove(elt)
                
        elif type_carte == "4":
            #print(elt.x + (elt.longueur // 2), elt.y + (elt.taille // 2))
            if -17 - (elt.longueur // 2) <= elt.x <= 46 - (elt.longueur // 2) and elt.y == 60 - (elt.taille // 2):
                elt.x += 1
            elif elt.x == 47 - (elt.longueur // 2) and 15 - (elt.taille // 2) <= elt.y <= 60 + (elt.taille // 2):
                elt.y -= 1
            elif 47 - (elt.longueur // 2) <= elt.x <= 95 - (elt.longueur // 2) and elt.y == 14 - (elt.taille // 2):
                elt.x += 1
            elif elt.x == 96 - (elt.longueur // 2) and 14 - (elt.taille // 2) <= elt.y <= 93 + (elt.taille // 2):
                elt.y += 1
            elif 96 - (elt.longueur // 2) <= elt.x <= 143 - (elt.longueur // 2) and elt.y <= 126 - (elt.taille // 2):
                elt.x += 1 #ici
            elif elt.x == 144 - (elt.longueur // 2) and 40 - (elt.taille // 2) <= elt.y <= 110 + (elt.taille // 2):
                elt.y -= 1
            elif 40 - (elt.longueur // 2) <= elt.x <= 200 + (elt.longueur // 2) and elt.y == 39 - (elt.taille // 2):
                elt.x += 1
            elif elt.x < 200 + elt.longueur:
                vie_perdue += elt.vies
                if elt.suivant is not None:
                    for nouveau_ballon in elt.suivant:
                        tab.append(Ballon(elt.x + (elt.longueur // 2), elt.y + (elt.taille // 2), nouveau_ballon))
                tab.remove(elt)
    return vie_perdue

