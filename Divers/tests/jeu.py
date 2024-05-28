import pyxel, random


pyxel.init(128,128, title="Scuba SAS")
pyxel.load("theme2.pyxres")

player_x = 64
player_y = 100

UPDATE = update
DRAW = draw 

chaves = 0



def mouvement(x, y):
    global player_x, player_y
    if pyxel.btn(pyxel.KEY_D) and x < 120:
        x += 2
    if pyxel.btn(pyxel.KEY_A) and x > 0:
        x -= 2
    if pyxel.btn(pyxel.KEY_S) and y < 120:
        y += 2
    if pyxel.btn(pyxel.KEY_W) and y  > 0:
        y -= 2
    return x, y

def colision():
    global player_x, player_y, UPDATE, DRAW
    if player_x < 20 + 15 and player_y + 15 > 100  and player_x + 15 > 20 and player_y < 100 + 15:
        player_x = 64
        player_y = 100
        UPDATE, DRAW = update1, draw1
    if player_x < 104 + 15 and player_y + 15 > 80  and player_x + 15 > 104 and player_y < 80 + 15:
        player_x = 64
        player_y = 100
        UPDATE, DRAW = update2, draw2
        return player_x, player_y

def win():
    global chaves, UPDATE, DRAW
    if chaves == 2:
        if player_x < 64 + 15 and player_y + 15 > 20  and player_x + 15 > 64 and player_y < 20 + 15:
            UPDATE, DRAW = update8, draw8

def update():
    global player_x, player_y
    player_x, player_y = mouvement(player_x, player_y)
    colision()
    win()
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    global chaves
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 120, 170, 128, 128)
    pyxel.blt(10, 115, 0, 16, 88, 16, 16, 11)
    pyxel.blt(110, 115, 0, 32, 88, 16, 16, 11)
    pyxel.blt(32, 40, 0, 32, 0, 16, 16, 11)
    pyxel.blt(player_x, player_y, 0, 0, 0, 16, 16, 11)
    pyxel.blt(20, 100, 0, 32, 136, 16, 16, 11)
    pyxel.blt(104, 80, 0, 48, 136, 16, 16, 11)
    pyxel.blt(64, 20, 0, 48, 168, 16, 16, 11)
    
#Win
def update8():
    global player_x, player_y
    player_x, player_y = mouvement(player_x, player_y)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw8():
    global chaves
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 120, 170, 128, 128)
    pyxel.text(55, 64, "BRAVO!", 0)
   
### Minigame 1 ###
# Update jogo 1 #
ecout_x = random.randint(0, 124)
ecout_y = 0
aleatorio = random.randint(0, 124)

def randola():
    global aleatorio
    aleatorio = random.randint(0, 124)
    return aleatorio

def mov_ecout(x, y):
    global ecout_y, ecout_x, aleatorio
    y += 1
    if x < aleatorio:
        x += 1
    if x > aleatorio:
        x -= 1
    if x == aleatorio :
        randola()
    return x, y

def colision_ecout() :
    global ecout_x, ecout_y, player_x, player_y, ecout_y,UPDATE, DRAW
    if player_x < ecout_x + 15 and player_y + 15 > ecout_y  and player_x + 15 > ecout_x and player_y < ecout_y + 15:
        player_x = 64
        player_y = 120
        ecout_y = 0
        UPDATE, DRAW = update_w1, draw_w1
        
    if ecout_y == 128 - 4:
        ecout_y = 0
        UPDATE, DRAW = update4, draw4
        
def update1():
    global player_x, player_y, ecout_y, ecout_x
    colision_ecout()
    ecout_x, ecout_y = mov_ecout(ecout_x, ecout_y)
    player_x, player_y = mouvement(player_x, player_y)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw1():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 120, 170, 128, 128)
    pyxel.blt(player_x, player_y, 0, 0, 0, 16, 16, 11)
    pyxel.blt(ecout_x, ecout_y, 0, 48, 16, 16, 16, 11)
    pyxel.blt(100, 30, 0, 32, 56, 20, 22, 11)

# Mapa Game Over

def update4():
    global player_x, player_y 
    player_x, player_y = mouvement(player_x, player_y)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
        
def draw4():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 120, 170, 128, 128)
    pyxel.text(45, 54, "GAME OVER", 0)
    pyxel.text(40, 74, "press SPACE", 0)
    pyxel.text(45, 84, "to restart", 0)
    
# Mapa win 1 / jogo 1

key_x = 64
key_y = 64

def colision_key():
    global player_x, player_y, chaves,UPDATE, DRAW
    if player_x < key_x + 12 and player_y + key_y  and player_x + 15 > ecout_x and player_y < key_y + 12:
        player_x = 64
        player_y = 100
        chaves += 1
        UPDATE, DRAW = update, draw
    
def update_w1():
    global player_x, player_y
    player_x, player_y = mouvement(player_x, player_y)
    colision_key()
        
def draw_w1():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 120, 170, 128, 128)
    pyxel.blt(player_x, player_y, 0, 0, 0, 16, 16, 11)
    pyxel.blt(64, 64 , 0, 32, 16, 16, 16, 11)
    
### Minigame2 ###
    
ennemi1_x = 25
ennemi1_y = 25
ennemi2_x = 63
ennemi2_y = 25
ennemi3_x = 100
ennemi3_y = 25
projetil_y = 25
projetil_x = 150
couleur = 2

tab_ennemi = [ennemi1_x, ennemi2_x, ennemi3_x]
rav = random.randint(0,2)

conteur = 0

def mov_projetil():
    global projetil_y, projetil_x
    projetil_y += 3
    return projetil_y

def key():
    global conteur, couleur,UPDATE, DRAW
    if conteur == 12:
        UPDATE, DRAW = update_w1, draw_w1
        
def colision_mancha():
    global projetil_y, projetil_x, player_x, player_y,UPDATE, DRAW
    if player_x < projetil_x + 15 and player_y + 15 > projetil_y  and player_x + 15 > projetil_x and player_y < projetil_y + 15:
        UPDATE, DRAW = update7, draw7
    
def colision_projetil():
    global projetil_y, projetil_x, rav, tab_ennemi, conteur
    if projetil_y > 126 :
        tab_ennemi = [ennemi1_x, ennemi2_x, ennemi3_x]
        rav = random.randint(0,2)
        projetil_x = tab_ennemi[rav]
        projetil_y = 25


def mouvement2(x, y):
    global player_x, player_y, conteur
    if pyxel.btnp(pyxel.KEY_D) and x < 120:
        x += 40
        conteur += 1
    if pyxel.btnp(pyxel.KEY_A) and x > 0:
        x -= 40
        conteur += 1
    y = player_y
    return x, y

def update2():
    global player_x, player_y, projetil_x, projetil_y
    key()
    mov_projetil()
    colision_mancha()
    colision_projetil()
    player_x, player_y = mouvement2(player_x, player_y)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw2():
    global projetil_y, projetil_x, couleur
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 120, 170, 128, 128)
    pyxel.blt(player_x, player_y, 0, 0, 0, 16, 16, 11)
    pyxel.blt(ennemi1_x, ennemi1_y, 0, 0, 72, 16, 16, 11)
    pyxel.blt(ennemi2_x, ennemi2_y, 0, 0, 72, 16, 16, 11)
    pyxel.blt(ennemi3_x, ennemi3_y, 0, 0, 72, 16, 16, 11)
    pyxel.blt(projetil_x, projetil_y, 0, 0, 152, 16, 16, 11)
    

# Mapa Game Over

def update7():
    global player_x, player_y,UPDATE, DRAW
    player_x, player_y = mouvement(player_x, player_y)
    if pyxel.btnp(pyxel.KEY_SPACE):
        UPDATE, DRAW = update, draw
        
def draw7():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 120, 170, 128, 128)
    pyxel.text(45, 54, "GAME OVER", 0)
    pyxel.text(40, 74, "press SPACE", 0)
    pyxel.text(45, 84, "to restart", 0)


pyxel.run(UPDATE, DRAW)
