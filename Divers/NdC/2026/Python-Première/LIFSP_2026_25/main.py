import pyxel as px
import random

"""Bienvenue dans Surnaturêve, dans ce jeu, vous êtes prisonnié de vos propres rêves et vous devez vous en échappé en passant
par le labyrinthe de votre esprit. Malheureusement pour vous les objets qui dans la vie réel ne bougeaient pas cherchent ici
à vous tuer.
Pour vous déplacer, vous devez appuyer sur les touches multidirectionnelles, étant donnée que vous êtes dans votre rêve, vous
pouvez traverser les murs bien que cela vous perturbe mentalement et vous fait perdre des points de précieux point de vie.
Vous gagnez le jeu une fois que vous arrivez au drapeau bien que vos rêves continuent.
Si vous aimez de la bonne musique, écoutez celle de ce jeu !!!!!!

"""





px.init(256,256,"Nuit du code")
px.load("U3.pyxres")
px.playm(0, loop = True)
v={
    "deplac_plaque_ennemi" : [],
    "coord_plaque_ennemi" : [],
    "coord_brique" : [],
    "activation" : 0,
    "scale" : 0,
    "timer" : 0,
    "tourner_plaque" : 0,
    "vitesse_x" : 0,
    "vitesse_y" : 0,
    "x_camera" : 112,
    "y_camera" : 112,
    "vie" : 210,
    "death" : False,
    "v" : False
}
x_perso=112
y_perso=112

def deplacement_camera():
    if (v['vitesse_x'] < 0):
        v['vitesse_x'] += 5
    if (v['vitesse_x'] > 0):
        v['vitesse_x'] -= 5
        
    if (v['vitesse_y'] < 0):
        v['vitesse_y'] += 5
    if (v['vitesse_y'] > 0):
        v['vitesse_y'] -= 5
    
    
    if px.btn(px.KEY_UP):
        if v['vitesse_y'] > -200:
            v['vitesse_y'] -= 10
    if px.btn(px.KEY_DOWN):
        if v['vitesse_y'] < 200:
            v['vitesse_y'] += 10
    if px.btn(px.KEY_RIGHT):
        if v['vitesse_x'] < 200:
            v['vitesse_x'] += 10
    if px.btn(px.KEY_LEFT):
        if v['vitesse_x'] > -200:
            v['vitesse_x'] -= 10
            


def coord_camera():
    if (v['x_camera'] < 256000) and (v['x_camera'] > -1000):
        v['x_camera'] += v['vitesse_x'] / 100
    if (v['y_camera'] < 256000) and (v['y_camera'] > -1000):
        v['y_camera'] += v['vitesse_y'] / 100
    
def creation_ennemi():
    liste_plaque = [[10, 10], [250, 250], [10, 250], [250, 10], [10, 112], [250, 112]]
    a = 0
    if px.frame_count % 60 == 0:
        a = random.randint(1,2)
    if a == 1:
        v['coord_plaque_ennemi'].append([liste_plaque][0][random.randint(0,5)])
        v['deplac_plaque_ennemi'].append([(px.sgn(v['x_camera'] - (v['coord_plaque_ennemi'][-1])[0]) * 5), px.sgn(v['y_camera'] - (v['coord_plaque_ennemi'][-1])[1]) * 5])
        v['timer'] = px.frame_count
    if a == 2:
        liste_brique = [i * 32 for i in range(256//32)]
        for i in range(random.randint(1,10)):
            b = random.randint(0, 7)
            if [b,0] not in v['coord_brique']:
                v['coord_brique'].append([b * 32, 12])

def deplacement_plaque():
    if px.frame_count - v["timer"] > 60:
        for plaque in v['coord_plaque_ennemi']:
            plaque[0] += v['deplac_plaque_ennemi'][v['coord_plaque_ennemi'].index(plaque)][0]
            plaque[1] += v['deplac_plaque_ennemi'][v['coord_plaque_ennemi'].index(plaque)][1]
        
            if (plaque > [256]) or (plaque < [0]):
                v['coord_plaque_ennemi'].remove(plaque)
            
            for plaque in v['coord_plaque_ennemi']:
                plaque[0] -= v['vitesse_x'] / 100
                plaque[1] -= v['vitesse_y'] / 100
        
            
    v['tourner_plaque'] += 10
    
def deplacement_brique():

    for brique in v['coord_brique']:
        brique[1] += 1
        brique[0] -= v['vitesse_x'] / 100
        if brique[1] > 256:
            v['coord_brique'].remove(brique)
            v['activation'] = 0
            
def colision():
    for i in range(2):
        for j in range(124,141):
            if px.pget(j, 124 + (i*16))==0:
                v["vie"]-=1
        for j in range(124,141):
            if px.pget(124+(i*16), j) == 0:
                v["vie"]-=1
                
def death():
    if v["vie"]<=0:
        v["death"]=True
        
def colision_victoire():
    for i in range(2):
        for j in range(124,141):
            if px.pget(j, 124 + (i*16))==4:
                v["v"]=True
        for j in range(124,141):
            if px.pget(124+(i*16), j) == 4:
                v["v"]=True


def update():
    creation_ennemi()
    
    deplacement_plaque()
    
    deplacement_camera()
    
    coord_camera()
    
    deplacement_brique()
    
    colision()
    
    death()
    
    colision_victoire()

def draw():
    global x_perso, y_perso
    px.cls(0)
    px.bltm(0,0,0,v['x_camera'], v['y_camera'],256,256)
    px.blt(124,124,0,16,112,16,16)
    for plaque in v['coord_plaque_ennemi']:
        px.blt(plaque[0], plaque[1], 0, 64, 50, 15, 12, rotate= v['tourner_plaque'])
        
    for brique in v['coord_brique']:
        px.blt(brique[0], brique[1], 0, 80, 16, 16, 16)
    px.text(10,10,f'vie : {v["vie"]}',7)
    
    if v["death"]:
        px.cls(0)
        px.text(124, 124, "Game over :(", 7)
    if v["v"]:
        px.cls(7)
        px.text(124, 124, "Game won :)", 0)
    




px.run(update, draw)