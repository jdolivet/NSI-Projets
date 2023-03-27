import pyxel, random

# variables initiale

sprite = 0
player_x = 64 - 37.5
player_y = 64 - 6.25
objet_list = []
vie = 1
minigame = 3
score = 0


def taille_ob():
    """ choisi aléatoireent entre 4 options la taille des tubes"""
    global taille, tamanhos
    posb_taille = [6, 22, 38, 54] #les cordonnes pour le fichier du design
    tamanho = [11, 37, 62, 87] # la taille
    true_taille = random.randint(0, 3)
    tamanhos = tamanho[true_taille]
    taille = posb_taille[true_taille]
    return taille, tamanhos

def player_mouvement(y):
    """ le player est toujour en mouveent vers le bas
    cette fonction de permet de lui  faire sauter"""
    global player_y
    if player_y >= 0 + 6.25:
        if pyxel.btnp(pyxel.KEY_SPACE):
            player_y -= 12.5
    return y


def objet_creation(objet_list):
    """ crée les tubes selon les coordonnes et taille de la focntion taille
        l'objet est crée toujours au coin de l'image"""
    global taille, tamanhos
    top = 0 
    bas = 128 - taille
    cord = [top, bas]
    if pyxel.frame_count % 30 == 0:
        spawn = random.randint(0,1)
        objet_list.append([128 - 4, cord[spawn], 81, taille, tamanhos]) #tableau avec toutes les informations du tube
        
def objet_mouvement(objet_list):
    """ tire les objets vers la gauche pour donner l'impression que l'oiseau est en mouvement"""
    global score
    for objet in objet_list:
        objet[0] -= 2.5
        if objet[0] <= 0:
            objet_list.remove(objet) # enleve l'objet une fois qu'il sort de la fenetre
            score += 1 # si l'objet sort de la fenetre le player ganhe 1 point
    return objet_list

def objet_colision(tab):
    """ permet de comparer les cordonnes et faire les colision selon cela
    si l'objet touhe le player, sa vie = 0"""
    global vie, minigame, objet_list, player_x, player_y, score
    for objet in tab:
        if (objet[0] <= player_x + 13) and (objet[1] <= player_y + 9) and (objet[0] + 4 >= player_x)and \
           ( objet[1] + objet[4] >= player_y):
            objet_list = []
            player_x = 64 - 37.5
            player_y = 64 - 6.25
            vie = 0 # le joueur perd
    return tab, vie

def player_colision(y):
    """ Le joueur perd s'il touche le sol"""
    global player_y, player_x, objet_list, minigame, score, vie
    if (player_y >= 128 - 9):
        objet_list = []
        player_x = 64 - 37.5
        player_y = 64 - 6.25
        vie = 0
        
def update_score():
    """ Peret à partir d'un fichier text de sauvegarder les meilleurs score de l'ordinateur"""
    global score, max_score
    with open("Leaderboard/minigame3.txt", 'r') as fichier: #ouvre fichier texte
        text = fichier.read()
        if text == "":
            max_score = 0  #si le fichier est ouvert pour une première fois le meilleur score = 0
        else:   
            max_score = int(text)
        if score > max_score:
            with open("Leaderboard/minigame3.txt", 'w') as fichier: # met a jour le meilleur score
                fichier.write(str(score))

 
def update3():
    """ Permet de mettre à jour chaque variable et fonction
    pour que le code tourne jusqu'au moent ou le player reviendra au menu"""
    global player_y, vie, minigame, objet_list, player_x
    minigame = 3
    player_y += 1.25
    taille_ob()
    player_mouvement(player_y)
    objet_creation(objet_list)
    objet_mouvement(objet_list)
    objet_colision(objet_list)
    player_colision(player_y)
    update_score()
    if vie == 0:
        objet_list = []
        player_x = 64 - 37.5
        player_y = 64 - 6.25
        if pyxel.btnp(pyxel.KEY_T): # menu de Gameover si le player perd il a le choix de revenir au lobby
            vie = 1
            minigame = 0
    return minigame

def draw3():
    """Permet de dessiner tout le jeu, animation, et la carte
    selon la position du player les sprites sont diférent pour l'animation"""
    global sprite, score, max_score, player_y, vie, minigame, objet_list, player_x
    pyxel.cls(0)
    if vie == 0: #menu du gameover
        pyxel.bltm(0, 0, 4, 0, 1, 128, 128) # la carte
        pyxel.text(42, 17, f"{score}", 7)
        pyxel.text(105, 17, f"{max_score}", 7)
        if pyxel.btnp(pyxel.KEY_R): # recommence le jeu si le joueur clique sur R
            vie = 1
            objet_list = []
            player_x = 64 - 37.5
            player_y = 64 - 6.25
            score = 0
         
    else:    
        pyxel.bltm(0, 0, 3, 0, 1, 128, 128)
        pyxel.blt(player_x, player_y, 1, 1, 4, 13, 9,6)
        if pyxel.frame_count % 15 == 0: # animation des ailes du oiseau
            if sprite == 0:
                pyxel.blt(player_x, player_y, 1, 17, 4, 13, 9,6)
            if sprite == 1:
                pyxel.blt(player_x, player_y, 1, 32, 4, 13, 9,6)
            if sprite == 2:
                pyxel.blt(player_x, player_y, 1, 1, 4, 13, 9,6)
                sprite =  -1
            sprite += 1
        pyxel.text(0, 0, f"score: {score}", 7)
        pyxel.text(-4, 5, f" best score: {max_score}", 7)
        for objet in objet_list:
            pyxel.blt(objet[0], objet[1], 1, objet[3], objet[2], 4, objet[4], 6)
