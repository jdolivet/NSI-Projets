import pyxel
import random
import time


# 1.INITIALISATION DU JEU

# ouvre une fenetre 128x128
pyxel.init(256, 256, title="Tetris")
pyxel.load("teste.pyxres")
points = 0

taille_case = 10

speed = 20
prochaine_acceleration = 25

horz = 20 #nombre de lignes
vert = 10 #nombre de colonnes

# Création du tableau du jeu
tab = [[0] * vert for i in range(horz)]

for i in range(len(tab)):
    print(tab[i])

debuttime = time.perf_counter()

mscjoue = 0 #Variable pour savoir si la musique joue déjà



# 2.GESTION DES PIÈCES

def prochaine_piece() -> list:
    """Choisit aléatoirement la prochaine pièce et son numéro."""

    n = random.randint(1,7)

    # Carré O
    if n == 1:
        return [
            [[4,0],[5,0],[4,1],[5,1]], #différentes rotations
            
            [[4,0],[5,0],[4,1],[5,1]],
            
            [[4,0],[5,0],[4,1],[5,1]],
            
            [[4,0],[5,0],[4,1],[5,1]]
        ], 1 # affiche le numéro de la pièce pour savoir quelle pièce est en train d'être utilisée et quelle pièce doit être affichée comme prochaine pièce
    


    # Ligne I
    elif n == 2:
        return [
            [[3,0],[4,0],[5,0],[6,0]],
            
            [[4,0],[4,1],[4,2],[4,3]],
            
            [[3,0],[4,0],[5,0],[6,0]],
            
            [[4,0],[4,1],[4,2],[4,3]]
        ], 2

    # T
    elif n == 3:
        return [
            [[4,0],[3,1],[4,1],[5,1]],

            [[4,0],[4,1],[5,1],[4,2]],

            [[3,1],[4,1],[5,1],[4,2]],

            [[4,0],[3,1],[4,1],[4,2]]
        ], 3

    # L
    elif n == 4:
        return [
            [[4,0],[4,1],[4,2],[5,2]],

            [[3,1],[4,1],[5,1],[3,2]],

            [[3,0],[4,0],[4,1],[4,2]],

            [[5,0],[3,1],[4,1],[5,1]]
        ], 4

    # J
    elif n == 5:
        return [
            [[5,0],[5,1],[5,2],[4,2]],

            [[3,0],[3,1],[4,1],[5,1]],

            [[4,0],[5,0],[4,1],[4,2]],

            [[3,1],[4,1],[5,1],[5,2]]
        ], 5

    # S
    elif n == 6:
        return [
            [[4,0],[5,0],[3,1],[4,1]],

            [[4,0],[4,1],[5,1],[5,2]],

            [[4,1],[5,1],[3,2],[4,2]],

            [[3,0],[3,1],[4,1],[4,2]]
        ], 6

    # Z
    else:
        return [
            [[3,0],[4,0],[4,1],[5,1]],

            [[5,0],[4,1],[5,1],[4,2]],

            [[3,1],[4,1],[4,2],[5,2]],

            [[4,0],[3,1],[4,1],[3,2]]
        ], 7


piece_actuelle, numero_actuel = prochaine_piece()
piece_suivante, numero_suivant = prochaine_piece()

rotation = 0

x_piece = 0
y_piece = 0

gameover = False
menu = False
tutoriel = False
records = False
username = True
nom = ""


# 3.GESTION DU PSEUDO

def afficher_nom(lettre: str, position: int) -> None:
    """Affiche une lettre du username à la position donnée grâce au spritesheet.
    Ne renvoie rien car les coordonnées sont directement utilisées par pyxel.blt()
    pour afficher la lettre à l'écran.
    """
    if lettre == "A":
        pyxel.blt(10 + position * 10, 130, 2, 4, 101, 8, 12)
    if lettre == "B":
        pyxel.blt(10 + position * 10, 130, 2, 14, 101, 8, 12)
    if lettre == "C":
        pyxel.blt(10 + position * 10, 130, 2, 24, 101, 8, 12)
    if lettre == "D":
        pyxel.blt(10 + position * 10, 130, 2, 34, 101, 8, 12)
    if lettre == "E":
        pyxel.blt(10 + position * 10, 130, 2, 44, 101, 8, 12)
    if lettre == "F":
        pyxel.blt(10 + position * 10, 130, 2, 54, 101, 8, 12)
    if lettre == "G":
        pyxel.blt(10 + position * 10, 130, 2, 64, 101, 8, 12)
    if lettre == "H":
        pyxel.blt(10 + position * 10, 130, 2, 74, 101, 8, 12)
    if lettre == "I":
        pyxel.blt(10 + position * 10, 130, 2, 84, 101, 8, 12)
    if lettre == "J":
        pyxel.blt(10 + position * 10, 130, 2, 94, 101, 8, 12)
    if lettre == "K":
        pyxel.blt(10 + position * 10, 130, 2, 104, 101, 8, 12)
    if lettre == "L":
        pyxel.blt(10 + position * 10, 130, 2, 114, 101, 8, 12)
    if lettre == "M":
        pyxel.blt(10 + position * 10, 130, 2, 124, 101, 8, 12)
    if lettre == "N":
        pyxel.blt(10 + position * 10, 130, 2, 134, 101, 8, 12)
    if lettre == "O":
        pyxel.blt(10 + position * 10, 130, 2, 144, 101, 8, 12)
    if lettre == "P":
        pyxel.blt(10 + position * 10, 130, 2, 154, 101, 8, 12)
    if lettre == "Q":
        pyxel.blt(10 + position * 10, 130, 2, 164, 101, 8, 12)
    if lettre == "R":
        pyxel.blt(10 + position * 10, 130, 2, 174, 101, 8, 12)
    if lettre == "S":
        pyxel.blt(10 + position * 10, 130, 2, 184, 101, 8, 12)
    if lettre == "T":
        pyxel.blt(10 + position * 10, 130, 2, 194, 101, 8, 12)
    if lettre == "U":
        pyxel.blt(10 + position * 10, 130, 2, 204, 101, 8, 12)
    if lettre == "V":
        pyxel.blt(10 + position * 10, 130, 2, 214, 101, 8, 12)
    if lettre == "W":
        pyxel.blt(10 + position * 10, 130, 2, 224, 101, 8, 12)
    if lettre == "X":
        pyxel.blt(10 + position * 10, 130, 2, 234, 101, 8, 12)
    if lettre == "Y":
        pyxel.blt(10 + position * 10, 130, 2, 244, 101, 8, 12)
    if lettre == "Z":
        pyxel.blt(10 + position * 10, 130, 2, 4, 115, 8, 12)

    if lettre == "1":
        pyxel.blt(10 + position * 10, 130, 2, 14, 115, 8, 12)
    if lettre == "2":
        pyxel.blt(10 + position * 10, 130, 2, 24, 115, 8, 12)
    if lettre == "3":
        pyxel.blt(10 + position * 10, 130, 2, 34, 115, 8, 12)
    if lettre == "4":
        pyxel.blt(10 + position * 10, 130, 2, 44, 115, 8, 12)
    if lettre == "5":
        pyxel.blt(10 + position * 10, 130, 2, 54, 115, 8, 12)
    if lettre == "6":
        pyxel.blt(10 + position * 10, 130, 2, 64, 115, 8, 12)
    if lettre == "7":
        pyxel.blt(10 + position * 10, 130, 2, 74, 115, 8, 12)
    if lettre == "8":
        pyxel.blt(10 + position * 10, 130, 2, 84, 115, 8, 12)
    if lettre == "9":
        pyxel.blt(10 + position * 10, 130, 2, 94, 115, 8, 12)
    if lettre == "0":
        pyxel.blt(10 + position * 10, 130, 2, 104, 115, 8, 12)



# 4.APPARITION ET CHUTE DES PIÈCES

def game_over(tab: list) -> bool:
    """Vérifie si une nouvelle pièce peut apparaître."""

    for x, y in piece_actuelle[rotation]:# On regarde les quatre blocs de la pièce actuelle et vérifie si il une des cases à déjà un 1 
        if tab[y][x] == 1:
            actu_ranking()
            return True

    return False


def spawn_piece(tab: list) -> None:
    """Place la pièce actuelle dans le tableau."""
    
    global x_piece, y_piece

    for bloc in piece_actuelle[rotation]:
    
        x = bloc[0] + x_piece #Pour savoir la position réelle de la pièce on ajoute les coordonnées de base de chaque bloc
        y = bloc[1] + y_piece

        tab[y][x] = 2 # pièce tombe


def nouvelle_piece(tab: list) -> list:
    """Fait apparaître la pièce suivante."""

    global piece_actuelle
    global numero_actuel
    global piece_suivante
    global numero_suivant
    global gameover
    global rotation
    global x_piece
    global y_piece
    global mscjoue
    
    piece_actuelle = piece_suivante # La pièce suivante devient la pièce actuelle
    numero_actuel = numero_suivant

    # On choisit une nouvelle pièce et le numero de la pièce qui deviendra la pièce actuelle
    piece_suivante, numero_suivant = prochaine_piece()
    
    if game_over(tab):
        pyxel.stop()
        gameover = True
        return tab
    
    rotation = 0
    x_piece = 0
    y_piece = 0
    
    spawn_piece(tab)
    return tab


def piece_peut_tomber(tab: list) -> bool:
    """Vérifie si la pièce actuelle peut descendre d'une ligne."""

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 2:
                 # La pièce touche le fond
                if i == len(tab) - 1: 
                    return False
                # Le pièce touche une autre pièce
                if tab[i+1][j] == 1:
                    return False

    return True


def tombe_piece(tab: list) -> list:
    """Fait descendre la pièce actuelle d'une ligne."""

    global y_piece

    if piece_peut_tomber(tab):
        # Efface la pièce
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if tab[i][j] == 2:
                    tab[i][j] = 0

        # Descend d'une ligne
        y_piece += 1

        # Redessine la pièce
        spawn_piece(tab)

        return tab

    else:

        # La pièce ne peut plus descendre, on transforme les 2 en 1
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if tab[i][j] == 2:
                    tab[i][j] = 1

        
        nouvelle_piece(tab) # On fait apparaître une nouvelle pièce

        return tab
        



# 5.DÉPLACEMENTS HORIZONTAUX


def arret_gauche(tab: list) -> bool:
    """Vérifie si la pièce ne peut plus aller vers la gauche."""
    
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 2:
                # Si le bloc est dans la première colonne il ne peut pas aller plus à gauche.
                if j == 0:
                    return True
                # Si la case à gauche contient un bloc la pièce ne peut pas aller vers la gauche
                if tab[i][j - 1] == 1:
                    return True

    return False


def arret_droite(tab: list) -> bool:
    """Vérifie si la pièce ne peut plus aller vers la droite."""

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 2:

                # Si le bloc est dans la dernière colonne il ne peut pas aller plus à droite
                if j == vert - 1:
                    return True

                # Si la case à droite contient un bloc la pièce ne peut pas aller vers la droite
                if tab[i][j + 1] == 1:
                    return True

    return False


def gauche_piece(tab: list) -> list:
    """Déplace la pièce d'une case vers la gauche."""
    
    global x_piece
    
    if arret_gauche(tab) == False:

        # Chaque bloc de la pièce est déplacé d'une colonne vers la gauche
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if tab[i][j] == 2:
                    tab[i][j - 1] = 2
                    tab[i][j] = 0
                    
        x_piece -= 1
        
        spawn_piece(tab)
        
    return tab


def droite_piece(tab: list) -> list:
    """Déplace la pièce actuelle d'une case vers la droite."""
    
    global x_piece
    
    if arret_droite(tab) == False:

        # On parcourt les colonnes de droite vers la gauche car les blocs sont déplacés vers la droite
        for i in range(len(tab)):
            for j in range(len(tab[i])-1, -1, -1):
                if tab[i][j] == 2:
                    tab[i][j + 1] = 2
                    tab[i][j] = 0
                    
        x_piece += 1
        
        spawn_piece(tab)
        
    return tab



# 6.GESTION DES LIGNES ET DU SCORE


def ligne_remplie(tab: list, l: int) -> bool:
    """Teste si la ligne l est remplie et renvoie un booléen."""

    for i in range(vert):
        if tab[l][i] != 1:
            return False

    return True


def test_lignes(tab: list) -> int | None:
    """Teste si une ligne est remplie.
    Renvoie son numéro ou None."""

    for i in range(horz):
        if ligne_remplie(tab, i):
            return i

    return None


def remplace_ligne(tab: list) -> list:
    """Supprime une ligne remplie et fait descendre les autres.
    Voit le nombre de lignes remplacées et ajoute les points gagnés."""

    global points

    ligne = test_lignes(tab)
    nblignerem = 0

    if ligne == None:
        return tab

    while ligne != None:

        # Toutes les lignes situées au-dessus de la ligne supprimée tombe d'une ligne
        for i in range(ligne, 0, -1):

            # On évite ainsi que deux lignes utilisent la même liste.
            tab[i] = tab[i - 1][:]

        # La première ligne devient vide.
        tab[0] = [0] * vert

        # On cherche à nouveau une ligne remplie ce qui permet de supprimer plusieurs lignes d'un coup
        ligne = test_lignes(tab)

        nblignerem += 1

    # Score avec le nombre de ligne suprimées
    if nblignerem == 1:
        points += 100
    elif nblignerem == 2:
        points += 300
    elif nblignerem == 3:
        points += 500
    else:
        points += 800

    return tab



# 7.ROTATION

def rotation_possible(tab: list) -> bool:
    """Vérifie si la rotation est possible."""

    for x, y in piece_actuelle[rotation]:

        # On ajoute la position actuelle de la pièce aux coordonnées de chaque bloc
        x = x + x_piece
        y = y + y_piece

        # Vérifie que la pièce ne sort pas à gauche ou à droite.
        if x < 0 or x >= vert:
            return False

        # Vérifie que la pièce ne sort pas du terrain verticalement.
        if y < 0 or y >= horz:
            return False

        # Vérifie que la nouvelle position de rotation ne rencontre pas une autre pièce
        if tab[y][x] == 1:
            return False

    return True


def tourne_piece(tab: list) -> list:
    """Tourne la pièce actuelle"""

    global rotation# On garde la rotation actuelle car elle sera utilisée si la nouvelle rotation est impossible
    
    ancienne_rotation = rotation

    # On enlève la pièce actuelle du tableau avant de tester sa nouvelle rotation
    for i in range(horz):
        for j in range(vert):
            if tab[i][j] == 2:
                tab[i][j] = 0

    # On passe à la rotation suivante
    rotation += 1
    
    # Si la rotation passe de 4 elle revient à la première et sa recommence
    if rotation == 4:
        rotation = 0

    # On vérifie si la nouvelle rotation est possible.
    if rotation_possible(tab):
        spawn_piece(tab)

    else:

        # Si la rotation est impossible on revient à l'ancienne rotation.
        rotation = ancienne_rotation
        spawn_piece(tab)
        
    return tab

# 8. GESTION DU RANKING

def actu_ranking() -> None:
    """Procédure qui actualise les fichier .txt: ponct_records.txt et nom_records.txt avec les nouveux rankings"""
    pos = 0
    global points
    global nom
    with open("ponct_records.txt", 'r', encoding='utf-8') as rank: #Lis les ponctuations et définit la position du joueur
        
        for i in range(10):
            ponctuation = ""
            pointact = rank.readline()
        
            for lettre in pointact:
                if lettre != '\\' and lettre != 'n':
                    ponctuation = ponctuation + lettre
                    
            ponctuation = int(ponctuation)
            if points <= ponctuation:
                pos += 1
        print(pos)
       
    if pos < 10:
        
        nvl_ligne = str(points) + "\n"
        with open("ponct_records.txt", "r", encoding="utf-8") as rank:
            lignes = rank.readlines()
        
        print(lignes)
        lignes.insert(pos, nvl_ligne) #insère ne nouveau nombre de points dans la bonne place
        lignes.pop(10) #efface la 11ème ligne
        print(lignes)

        with open("ponct_records.txt", "w", encoding="utf-8") as rank: #Réécris le nouveau ranking
            rank.writelines(lignes)
            
            
        nvl_ligne = nom + "\n"
        with open("nom_records.txt", "r", encoding="utf-8") as rank:
            lignes = rank.readlines()
        print(lignes)

        lignes.insert(pos, nvl_ligne) #insère ne nouveau nom dans la bonne place
        lignes.pop(10) #efface la 11ème ligne
        print(lignes)
        
        with open("nom_records.txt", "w", encoding="utf-8") as rank: #Réécris le nouveau ranking
            rank.writelines(lignes)
            
def print_ranking() -> None:
    """Affiche le ranking dans la partie du menu ranking"""
    for i in range(10):
        pyxel.text(50, 60 + 15*i, f"{i+1}." , 7)

    with open("nom_records.txt", "r", encoding="utf-8") as rank:
        lignes = rank.readlines()
        for nb in range(len(lignes)):
            pyxel.text(80, 60 + 15*nb, lignes[nb] , 7)
        
    with open("ponct_records.txt", "r", encoding="utf-8") as rank:
        lignes = rank.readlines()
        for nb in range(len(lignes)):
            pyxel.text(180, 60 + 15*nb, lignes[nb] , 7)


# 9.RÉINITIALISATION ET BOUCLE DU JEU

def reset_game() -> None:
    """Réinitialise les données de la partie."""

    global tab
    global points
    global speed
    global prochaine_acceleration
    global debuttime
    global fintime
    global gameover
    global rotation
    global x_piece, y_piece
    global piece_actuelle, numero_actuel
    global piece_suivante, numero_suivant

    # Réinitialiser le terrain
    tab = [[0] * vert for _ in range(horz)]

    # Réinitialiser le score
    points = 0

    # Réinitialiser la vitesse
    speed = 20
    prochaine_acceleration = 25

    # Réinitialiser le temps
    debuttime = time.perf_counter()
    fintime = debuttime

    # Réinitialiser la position de la pièce
    rotation = 0
    x_piece = 0
    y_piece = 0

    # Nouvelles pièces
    piece_actuelle, numero_actuel = prochaine_piece()
    piece_suivante, numero_suivant = prochaine_piece()

    # Faire apparaître la première pièce
    spawn_piece(tab)

    gameover = False


def update() -> None:
    """Met à jour l'état du jeu à chaque image."""

    global speed
    global tab
    global prochaine_acceleration
    global menu
    global tutoriel
    global records
    global mscjoue
    global username
    global nom
    global debuttime
    
               
    if gameover == False:
        
        if username:
            if len(nom) < 25:
                if pyxel.btnp(pyxel.KEY_A):
                    nom += "A"

                if pyxel.btnp(pyxel.KEY_B):
                    nom += "B"

                if pyxel.btnp(pyxel.KEY_C):
                    nom += "C"

                if pyxel.btnp(pyxel.KEY_D):
                    nom += "D"

                if pyxel.btnp(pyxel.KEY_E):
                    nom += "E"

                if pyxel.btnp(pyxel.KEY_F):
                    nom += "F"

                if pyxel.btnp(pyxel.KEY_G):
                    nom += "G"

                if pyxel.btnp(pyxel.KEY_H):
                    nom += "H"

                if pyxel.btnp(pyxel.KEY_I):
                    nom += "I"

                if pyxel.btnp(pyxel.KEY_J):
                    nom += "J"

                if pyxel.btnp(pyxel.KEY_K):
                    nom += "K"

                if pyxel.btnp(pyxel.KEY_L):
                    nom += "L"

                if pyxel.btnp(pyxel.KEY_M):
                    nom += "M"

                if pyxel.btnp(pyxel.KEY_N):
                    nom += "N"

                if pyxel.btnp(pyxel.KEY_O):
                    nom += "O"

                if pyxel.btnp(pyxel.KEY_P):
                    nom += "P"

                if pyxel.btnp(pyxel.KEY_Q):
                    nom += "Q"

                if pyxel.btnp(pyxel.KEY_R):
                    nom += "R"

                if pyxel.btnp(pyxel.KEY_S):
                    nom += "S"

                if pyxel.btnp(pyxel.KEY_T):
                    nom += "T"

                if pyxel.btnp(pyxel.KEY_U):
                    nom += "U"

                if pyxel.btnp(pyxel.KEY_V):
                    nom += "V"

                if pyxel.btnp(pyxel.KEY_W):
                    nom += "W"

                if pyxel.btnp(pyxel.KEY_X):
                    nom += "X"

                if pyxel.btnp(pyxel.KEY_Y):
                    nom += "Y"

                if pyxel.btnp(pyxel.KEY_Z):
                    nom += "Z"

                if pyxel.btnp(pyxel.KEY_0):
                    nom += "1"

                if pyxel.btnp(pyxel.KEY_1):
                    nom += "2"

                if pyxel.btnp(pyxel.KEY_2):
                    nom += "3"

                if pyxel.btnp(pyxel.KEY_3):
                    nom += "4"

                if pyxel.btnp(pyxel.KEY_4):
                    nom += "5"

                if pyxel.btnp(pyxel.KEY_5):
                    nom += "6"

                if pyxel.btnp(pyxel.KEY_6):
                    nom += "7"

                if pyxel.btnp(pyxel.KEY_7):
                    nom += "8"

                if pyxel.btnp(pyxel.KEY_8):
                    nom += "9"

                if pyxel.btnp(pyxel.KEY_9):
                    nom += "0"

                if pyxel.btnp(pyxel.KEY_SPACE):
                    nom += " "
                    
                if pyxel.btnp(pyxel.KEY_BACKSPACE):
                    nom = nom[0:-1]
                    
                if pyxel.btnp(pyxel.KEY_RETURN):
                    menu = True
                    username = False

            else:
                if pyxel.btnp(pyxel.KEY_BACKSPACE):
                    nom = nom[0:-1]
                
    
        elif menu:
            if mscjoue == 0:
                pyxel.playm(2, loop = True)
                mscjoue = 1
            
            if pyxel.btnp(pyxel.KEY_M):
                if mscjoue == 1:
                    pyxel.stop()
                    mscjoue = 2
                else:
                    mscjoue = 0
                    
            if pyxel.btnp(pyxel.KEY_RETURN):
                pyxel.stop()
                debuttime = time.perf_counter()
                menu = False
                
            if pyxel.btnp(pyxel.KEY_T):
                menu = False
                tutoriel = True
                
            if pyxel.btnp(pyxel.KEY_R):
                menu = False
                records = True
                
            if pyxel.btnp(pyxel.KEY_ESCAPE):
                pyxel.quit()
        
        elif tutoriel:
            if pyxel.btnp(pyxel.KEY_B):
                tutoriel = False
                menu = True
                
        elif records:
            if pyxel.btnp(pyxel.KEY_B):
                records = False
                menu = True
            
        else:
            if mscjoue == 1:
                pyxel.playm(1, loop = True)
                mscjoue = 0

            if mscjoue == 2:
                pyxel.stop()
                
            if pyxel.btnp(pyxel.KEY_LEFT, 10, 3):
                tab = gauche_piece(tab)
        
            if pyxel.btnp(pyxel.KEY_RIGHT, 10, 3):
                tab = droite_piece(tab)
            
            if pyxel.btnp(pyxel.KEY_UP):
                tab = tourne_piece(tab)
            
            if pyxel.btn(pyxel.KEY_DOWN):
                # Quand la touche bas est appuyée ont augmente la vitesse de la pièce ce qui permet de la faire tomber rapidement
                vitesse = 2
            
            else:
                vitesse = speed

            # frame_count augmente à chaque image.
            if pyxel.frame_count % vitesse == 0:
                tab = tombe_piece(tab)
    
            tab = remplace_ligne(tab)
    
            fintime = time.perf_counter()

            # Toutes les 25 secondes, speed diminue.
            if fintime - debuttime > prochaine_acceleration and speed > 3:
                speed -= 1

                # On prépare le prochain moment où la vitesse augmentera.
                prochaine_acceleration += 25
        
    else:
                
        if mscjoue == 0:
            pyxel.playm(0, loop = True)
            mscjoue = 1
                
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_B):
            pyxel.stop()
            mscjoue = 2
            menu = True
            reset_game()
                
    



# 10.AFFICHAGE

def draw():
    """Affiche le jeu dans la fenêtre Pyxel."""
    pyxel.cls(1)

    # largeur = colonnes, hauteur = lignes
    largeur_terrain = vert * taille_case
    hauteur_terrain = horz * taille_case

    # pour placer le terrain au milieu, on doit savoir ou c'est le milieu
    x_terrain = (256 - largeur_terrain) // 2
    y_terrain = (256 - hauteur_terrain) // 2

    # contour du "terrain"
    # pyxel.rectb = seulement la borde du rectangle
    # pyxel.rect(x, y, largeur, hauteur, couleur)
    pyxel.rectb(x_terrain, y_terrain, largeur_terrain, hauteur_terrain, 7)
    
    # quadrillages
    for y in range(horz):
        for x in range(vert):
            pyxel.rectb(x_terrain + x * taille_case,
                        y_terrain + y * taille_case,
                        taille_case, taille_case, 13)
    
    # affichage des points
    pyxel.text(20, 30, "POINTS", 7)
    pyxel.text(20, 40, f"{points}", 7)
              
    temps = int(time.perf_counter() - debuttime)
    minutes = temps // 60
    secondes = temps % 60
    pyxel.text(20, 60, "TEMPS", 7)
    pyxel.text(20, 70, f"{minutes}:{secondes}s", 7)
    
    
    # affichage de la prochaine pièce
    pyxel.text(x_terrain + largeur_terrain + 6, 30, "PIECE SUIVANTE", 7)
    
    
    for y in range(horz):
        for x in range(vert):
            if tab[y][x] == 2:

                # bloc de la pièce actuellement en train de tomber
                pyxel.rect(x_terrain + x * taille_case,
                           y_terrain + y * taille_case,
                           taille_case, taille_case, 9)

    for y in range(horz):
        for x in range(vert):
            if tab[y][x] == 1:

                # bloc d'une pièce déjà posée.
                pyxel.rect(x_terrain + x * taille_case,
                           y_terrain + y * taille_case,
                           taille_case, taille_case, 8)

    # cadre de la prochaine pièce
    pyxel.rectb(x_terrain + largeur_terrain + 3, 45, 70, 75, 7)

    #print(numero_suivant)
    
    if numero_suivant == 1:
        pyxel.blt(x_terrain + largeur_terrain + 21, 65, 0, 7, 7, 33, 33)
        
    if numero_suivant == 2:
        pyxel.blt(x_terrain + largeur_terrain + 5, 70, 0, 7, 47, 65, 17)
        
    if numero_suivant == 3:
        pyxel.blt(x_terrain + largeur_terrain + 12, 62, 0, 15, 71, 49, 33)
        
    if numero_suivant == 4:
        pyxel.blt(x_terrain + largeur_terrain + 20, 60, 0, 7, 111, 33, 49)
        
    if numero_suivant == 5:
        pyxel.blt(x_terrain + largeur_terrain + 21, 57, 0, 55, 111, 33, 49)
    
    if numero_suivant == 6:
        pyxel.blt(x_terrain + largeur_terrain + 13, 65, 0, 7, 175, 49, 33)
        
    if numero_suivant == 7:
        pyxel.blt(x_terrain + largeur_terrain + 13, 65, 0, 71, 175, 49, 33)
    
    if gameover:
        pyxel.cls(1) # efface la fenetre avec la couleur 1 (bleu foncé)
        pyxel.blt(100, 80, 2, 4, 12, 45, 35)
        pyxel.text(50, 200, "APPUIE SUR 'ESC' pour quitter", 7)
        pyxel.text(50, 180, "APPUIE SUR 'B' POUR REVENIR AU MENU", 7)
        pyxel.text(90, 150, f"TOTAL POINTS : {points}", 10)
        
        

    if username:
        pyxel.cls(0)
        pyxel.text(80, 50, "Saisissez votre username", 7)
        pyxel.text(30, 70, "Seulement les lettres et les chiffres fonctionnent.", 7)
        pyxel.text(50, 200, "Appuyez sur 'Enter' pour continuer.", 7)

        for position in range(len(nom)):
            afficher_nom(nom[position], position)

        if len(nom) >= 25:
            pyxel.text(30, 100,
                       "USERNAME TROP LONG ! EFFACEZ UN CARACTÈRE POUR CONTINUER",
                       8)
                
    if menu:
        pyxel.cls(1)

        if mscjoue == 1:
            pyxel.blt(230, 230, 2, 0, 56, 16, 16)
        else:
            pyxel.blt(230, 230, 2, 0, 72, 16, 16)

        pyxel.blt(15, 30, 1, 7, 7, 233, 65)
        pyxel.blt(30, 150, 1, 20, 93, 55, 11)
        pyxel.text(30, 170, "CLIQUE R", 0)
        pyxel.blt(110, 150, 1, 23, 117, 63, 11)
        pyxel.text(110, 170, "CLIQUE T", 14)
        pyxel.blt(190, 150, 1, 28, 136, 40 , 15)
        pyxel.text(190, 170, "CLIQUE 'ENTER'", 7)
        pyxel.text(20, 230, "CLIQUE 'M' COUPER LE SON ", 7)
        pyxel.text(20, 240, "CLIQUE 'ESC' POUR QUITTER", 7)
        
    if records:
        pyxel.cls(1)
        pyxel.text(50, 230, "APPUIE SUR 'B' POUR REVENIR AU MENU", 7)
        print_ranking()
                
    if tutoriel:
        pyxel.cls(1)
        pyxel.blt(15, 30, 1, 7, 7, 233, 65)
        
        pyxel.blt(30, 120, 1, 28, 165, 72, 11 )
        pyxel.text(5, 135, "Empile les pieces pour", 7)
        pyxel.text(5, 143, "former des lignes completes.", 7)
        pyxel.text(5, 151, "Chaque ligne complete disparait ", 7)
        pyxel.text(5, 159, "Plus tu survis longtemps,", 7)
        pyxel.text(5, 167, "plus la vitesse du jeu augmente.", 7)
        pyxel.text(5, 175, "Essaie d'obtenir le meilleur", 7)
        pyxel.text(5, 183, "score possible !", 7)
        
        pyxel.line(135, 120, 135, 190, 4)
        
        pyxel.blt(140, 120, 1, 28, 189, 72, 11)
        pyxel.blt(150, 140, 1, 36, 212, 10, 8)
        pyxel.text(160, 140, " : DEPLACER A GAUCHE ", 7)
        pyxel.blt(150, 155, 1, 47, 212, 10, 8)
        pyxel.text(160, 155, " : DEPLACER A DROITE ", 7)
        pyxel.blt(150, 170, 1, 42, 227, 9, 10)
        pyxel.text(160, 170, " : TOURNER", 7)
        pyxel.blt(150, 185, 1, 42, 246, 9, 10)
        pyxel.text(160, 185, " : DESCENDRE PLUS VITE", 7)
        
        pyxel.text(50, 230, "APPUIE SUR 'B' POUR REVENIR AU MENU", 7)
            
        
pyxel.run(update, draw)
