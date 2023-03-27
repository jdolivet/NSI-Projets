import pyxel, random



minigame = 2
player_x = 64 - 10
player_y = 100 
ennemi_list = []
tir_list = []
score = 0
vie = 3

def player_mouvement(x):
    """Deplace la voiture selon les input du clavier et bloque
    le mouvement selon les limites de la rue"""
    global player_x
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 128 - 10):
            x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0):
            x = x - 2
    return x

def ennemi_creation(ennemi_list):
    """Crée les ennemis dans des endroits définis aléatoirement,
    de couleur et de forme aléatoire, établi par des tableaux ayant les
    coordonnées des sprites dans le banc d'image."""
    if pyxel.frame_count % 40 == 0:
        spawn = random.randint(0, 128 - 10)
        color = [163, 179, 195, 211] #Coordonnées des sprites du banc d'image
        tipe = [17, 33, 49] #Coordonnées des sprites du banc d'image
        couleur = color[random.randint(0, 3)] #Choisi un sprite au hasard
        tipes = tipe[random.randint(0,2)] #Choisi un sprite au hasard
        ennemi_list.append([spawn, 0, tipes, couleur])
        
def ennemi_mouvement(ennemi_list):
    """Déplace les ennemis crées pour allé en direction vers
    le bas/ vers y = 128
    Quand ils dépassent ou rentre en conflit avec le joueur,
    ils sont retirer."""
    global vie
    for ennemi in ennemi_list:
        ennemi[1] += 2
        if ennemi[1] >= 128:
            ennemi_list.remove(ennemi)
            vie -= 1
    return ennemi_list

def colision(tab):
    """Établi que si le joueur se choque contre un ennemi crée,
    il perd une vie."""
    global vie, ennemi_list
    for ennemi in tab:
        if (ennemi[0] <= player_x + 10) and (ennemi[1] <= player_y + 9) and (ennemi[0] + 14 >= player_x)and \
           ( ennemi[1] + 8 >= player_y):
            ennemi_list.remove(ennemi)
            vie -= 1

def tir_creation(tir_list):
    """Crée le tir à partir de la position du joueur."""
    global player_x, player_y
    if pyxel.btnp(pyxel.KEY_SPACE):
        tir_list.append([player_x + 5 , player_y])
        pyxel.playm(1, loop = False)



def tir_mouvement(tir_list):
    """Définir la trajectoire du tir crée vers le haut/jusqu'a y = 0
    à partir de la position du joueur."""
    for tir in tir_list:
        tir[1] -= 3
        if tir[1] <= 0:
            tir_list.remove(tir)
    return tir_list

def tir_colision(tir_list):
    """Detecte si le tir rentre en contact avec un ennemi.
    Si oui, l'ennemi va être retirer."""
    global ennemi_list, score
    for tir in tir_list:
        for ennemi in ennemi_list:
            if (tir[0] <= ennemi[0] + 10) and (tir[1] <= ennemi[1] + 9) and (tir[0] + 4 >= ennemi[0])and \
               ( tir[1] + 5 >= ennemi[1]):
                score += 1
                ennemi_list.remove(ennemi)
                tir_list.remove(tir)
                
def update_score():
    """Fait update du document text dans le fichier Leaderboard
    pour pouvoir préserver le high score du joueur"""
    global score, max_score
    with open("Leaderboard/minigame2.txt", 'r') as fichier:
        text = fichier.read()
        if text == "":
            max_score = 0
        else:   
            max_score = int(text)
        if score > max_score:
            with open("Leaderboard/minigame2.txt", 'w') as fichier:
                fichier.write(str(score))
   
def update2():
    """Met a jour les variables des fonctions et les actualisent
    en temps réel pour que le jeu puisse tourner infinitement ou
    jusqu'a que le jouer sorte du minigame."""
    global player_x, player_y, ennemi_list, vie, minigame, tir_list, score
    minigame = 2
    player_x = player_mouvement(player_x)
    ennemi_creation(ennemi_list)
    ennemi_mouvement(ennemi_list)
    colision(ennemi_list)
    tir_creation(tir_list)
    tir_mouvement(tir_list)
    tir_colision(tir_list)
    update_score()
    if vie == 0:
        ennemi_list = []
        tir_list = []
        player_x = 64 - 10
        player_y = 100 
        if pyxel.btnp(pyxel.KEY_T):
            minigame = 0
            vie = 3
            score = 0
            return minigame

    return minigame
    
def draw2():
    """Permet de mettre les aspects graphiques et animations
    du jeu."""
    global player_x, player_y, ennemi_list, vie, minigame, tir_list, score
    pyxel.cls(0)
    minigame = 2
    if vie == 0:
        pyxel.bltm(0, 0, 4, 0, 1, 128, 128)
        pyxel.text(42, 17, f"{score}", 7)
        pyxel.text(105, 17, f"{max_score}", 7)
        if pyxel.btnp(pyxel.KEY_R):
            vie = 3
            ennemi_list = []
            tir_list = []
            score = 0
            player_x = 64 - 10
            player_y = 100 
        
    
    else:
        pyxel.bltm(0, 0, 2, 0, 1, 128, 128)
        if vie == 3:
            pyxel.blt(player_x, player_y, 0, 3, 163, 10, 9, 6)
        if vie == 2:
            pyxel.blt(player_x, player_y, 0, 3, 195, 10, 9, 6)
        if vie == 1:
            pyxel.blt(player_x, player_y, 0, 3, 211, 10, 9, 6)
        
        pyxel.text(0, 0, f"vie: {vie}", 7)
        pyxel.text(0, 5, f"score: {score}", 7)
        pyxel.text(-4, 10, f" best score: {max_score}", 7)
        for tir in tir_list:
            pyxel.blt(tir[0], tir[1], 0, 2, 242, 4, 5, 6)
        for ennemi in ennemi_list:
            pyxel.blt(ennemi[0], ennemi[1],0, ennemi[2], ennemi[3], 14, 8, 6)