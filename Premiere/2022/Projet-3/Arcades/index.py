import pyxel, minigame1, minigame2, minigame3 # les fichiers de chaque minigame

pyxel.init(128, 128, title="Projet Tri3")
 
pyxel.load("final_sprites.pyxres", True, True, True, True) # les graphiques 


#variables initiale

player_x = 64 - 5
player_y = 64 - 12
minigame = -1
position = 0

def player_mouvement(x, y, animation):
    """permet de deplacer le player e de decter si
    il va a gauchge a droite etc... (pour les animations"""
    global position, minigame
    if minigame == 0:
        if pyxel.btn(pyxel.KEY_D):
            if (x < 128 - 9):
                x = x + 2 # se deplacer
                animation = 1 # la position
        if pyxel.btn(pyxel.KEY_A):
            if (x > 0):
                x = x - 2
                animation = 2
        if pyxel.btn(pyxel.KEY_S):
            if (y < 118):
                y = y + 2
                animation = 3
        if pyxel.btn(pyxel.KEY_W):
            if (y > 17):
                y = y - 2
                animation = 4
    return x, y, animation

def colision():
    """ Permet de faire la colision du player et les logo des minigame
    une fois touché, la variable minigame est changé et le player entre dans le minigame"""
    global minigame, player_x, player_y 
    if ( 121 <= player_x + 9 ) and ( 104 <= player_y + 14 ) and ( 121 + 9 >= player_x) and ( 104 + 14 >= player_y):
        minigame = 1
    if ( 25 <= player_x + 9 ) and ( 32 <= player_y + 14 ) and ( 25 + 9 >= player_x) and ( 32 + 14 >= player_y):
        minigame = 2
    if ( 9 <= player_x + 9) and ( 105 <= player_y + 14 ) and ( 9 + 9 >= player_x) and ( 105 + 14 >= player_y):
        minigame = 3

def menu():
    """ Graphique initiale du jeu"""
    global minigame
    if minigame == -1:
        if pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.playm(0, loop = True)
            minigame = -2 # le menu des controle
    return minigame

def controle():
    """ Graphique du controle du jeu"""
    global minigame
    if minigame == -2:
        if pyxel.btnp(pyxel.KEY_SPACE):
            minigame = 0 # la carte
    if pyxel.btn(pyxel.KEY_M):
        pyxel.stop()
    if pyxel.btn(pyxel.KEY_P):
        pyxel.playm(0, loop = True)
            
    return minigame

def update():
    """ Permet de mettre à jour chaque variable et fonction
    pour que le code tourne jusqu'au coilision
    Selon la variable minigame, cette fonction appelle les fonctions update des minigame"""
    global player_x, player_y, minigame, position, play_musique
    colision()
    controle()
    menu()
    player_x, player_y, position = player_mouvement(player_x, player_y, position)
    if minigame == 1:
        pyxel.stop()
        minigame = minigame1.update1() #appelle fonction update de chaque fichier
        if minigame == 0:
            pyxel.playm(0, loop = True)
            player_x = 64 - 5
            player_y = 64 - 12
    if minigame == 2:
        pyxel.stop()
        minigame = minigame2.update2()
        if minigame == 0:
            pyxel.playm(0, loop = True)
            player_x = 64 - 5
            player_y = 64 - 12
    if minigame == 3:
        pyxel.stop()
        minigame = minigame3.update3()
        if minigame == 0:
            pyxel.playm(0, loop = True)
            player_x = 64 - 5
            player_y = 64 - 12

def draw():
    """Permet de dessiner tout le jeu, animation, et la carte
    selon la position du player les sprites sont diférent pour l'animation
    selon la variable minigame,cette fonction apelle la fonction draw des minigame"""
    global position, minigame
    pyxel.cls(0)
    if minigame == -2:
        pyxel.bltm(0, 0, 5, 128, 0, 128, 128) # le menu
        pyxel.text(10, 115, " M pour arreter la musique", 7)
    if minigame == -1:
        pyxel.bltm(0, 0, 5, 0, 0, 128, 128) # le menu des controle
    if minigame == 0:
        pyxel.bltm(0, 0, 0, 0, 1, 128, 128) # la carte 
        if position == 0:
            pyxel.blt(player_x, player_y, 0, 75, 90, 9, 14, 6) # les animations selon la position du personnage
        if position == 1:
            pyxel.blt(player_x, player_y, 0, 91, 90, 9, 14, 6)
        if position == 2:
            pyxel.blt(player_x, player_y, 0, 75, 90, 9, 14, 6)
        if position == 3:
            pyxel.blt(player_x, player_y, 0, 91, 74, 9, 14, 6)
        if position == 4:
            pyxel.blt(player_x, player_y, 0, 75, 74, 9, 14, 6)
    if minigame == 1:
        minigame1.draw1() # appelle la fonction draw de chaque fichier
    if minigame == 2:
        minigame2.draw2()
    if minigame == 3:
        minigame3.draw3()
        
pyxel.run(update, draw)