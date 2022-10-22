import pyxel, random

#pyxel.init(128, 128, title="Projet sas")
#pyxel.load("final_sprites.pyxres", True, True, False, False)

minigame = 1
player_x = 64 - 5
player_y = 100
objet_list = []
score = 0
couleur = 0
vitesse = 2
vie = 1

def player_mouvement(x, y):
    """Deplace la voiture selon les input du clavier et bloque
    le mouvement selon les limites de la rue"""
    global player_x
    if pyxel.btnp(pyxel.KEY_D):
        if (x < 64 - 8 + 25.6):
            x = x + 25.6
    if pyxel.btnp(pyxel.KEY_A):
        if (x > 64 + 8 - 25.6):
            x = x - 25.6
    return x, y

def objet_creation(objet_list):
    """Crée les obstacles dans les 3 endroits définis aléatoirement,
    de couleur et de forme aléatoire, établi par des tableaux ayant les
    coordonnées des sprites dans le banc d'image."""
    global couleur
    gauche = 64 - 4 - 25.6
    droite = 64 + 25.6 - 4 
    mid = 64 - 4
    cord = [gauche, mid, droite]
    color = [81, 97, 113] #Coordonnées des sprites du banc d'image
    tipe = [20, 36, 52] #Coordonnées des sprites du banc d'image
    couleur = color[random.randint(0, 2)] #Choisi un sprite au hasard
    tipes = tipe[random.randint(0,2)] #Choisi un sprite au hasard
    if pyxel.frame_count % 30 == 0:
        spawn = random.randint(0,2)
        objet_list.append([cord[spawn], 8, couleur, tipes])

def objet_mouvement(objet_list):
    """Déplace les objets crée pour allé en direction vers
    le bas/ vers y = 128
    Quand ils dépassent ou rentre en conflit avec le joueur,
    ils sont retirer."""
    global score, vitesse
    if pyxel.frame_count % 60 == 0: #Augmente la vitesse à chaque 2
        vitesse += 0.2
    for objet in objet_list:
        objet[1] += vitesse
        if objet[1] >= 128:
            objet_list.remove(objet)
            score += 1
    return objet_list
    
def colision(tab):
    """Établi que si le joueur se choque contre un objet crée,
    il perd la vie et le jeu retourne à la vitesse et objet_list
    originale"""
    global vie, minigame, objet_list, score, vitesse
    for objet in tab:
        if (objet[0] <= player_x + 8) and (objet[1] <= player_y + 13) and (objet[0] + 8 >= player_x)and \
           ( objet[1] + 13 >= player_y):
            vie = 0
            objet_list = []
            vitesse = 1
    return tab, vie

def update_score():
    """Fait update du document text dans le fichier Leaderboard
    pour pouvoir préserver le high score du joueur"""
    global score, max_score
    with open("Leaderboard/minigame1.txt", 'r') as fichier:
        text = fichier.read()
        if text == "":
            max_score = 0
        else:   
            max_score = int(text)
        if score > max_score:
            with open("Leaderboard/minigame1.txt", 'w') as fichier:
                fichier.write(str(score))

                
def update1():
    """Met a jour les variables des fonctions et les actualisent
    en temps réel pour que le jeu puisse tourner infinitement ou
    jusqu'a que le jouer sorte du minigame."""
    global player_x, player_y, objet_list, vie, minigame, couleur
    minigame = 1
    objet_creation(objet_list)
    objet_mouvement(objet_list)
    colision(objet_list)
    update_score()
    player_x, player_y = player_mouvement(player_x, player_y)
    if vie == 0:
        objet_list = []
        vitesse = 1
        player_x = 64 - 5
        player_y = 100
        if pyxel.btnp(pyxel.KEY_T):
            vie = 1
            score = 0
            objet_list = []
            vitesse = 1
            minigame = 0
            player_x = 64 - 5
            player_y = 100
            return minigame
    return minigame

def draw1():
    """Permet de mettre les aspects graphiques et animations
    du jeu."""
    global vie, score, minigame, player_x, player_y, objet_list
    pyxel.cls(0)
    minigame = 1
    if vie == 0:
        pyxel.bltm(0, 0, 4, 0, 1, 128, 128) #Le menu de game over
        pyxel.text(42, 17, f"{score}", 7)
        pyxel.text(105, 17, f"{max_score}", 7)
        if pyxel.btnp(pyxel.KEY_R):
            vie = 1
            objet_list = []
            score = 0
            player_x = 64 - 5
            player_y = 100
            vitesse = 2
        
        

    else:
        pyxel.bltm(0, 0, 1, 0, 1, 128, 128) #La carte du jeu
        pyxel.blt(player_x, player_y, 0, 4, 82, 8, 13,6) #Le graphique du personnage
        pyxel.text(0, 0, f"score: {score}", 7)
        pyxel.text(-4, 5, f" best score: {max_score}", 7)
        for objet in objet_list:
            pyxel.blt(objet[0], objet[1], 0, objet[3], objet[2], 8, 13, 6)
    return minigame