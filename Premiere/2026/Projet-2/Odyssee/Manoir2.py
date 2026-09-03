import pyxel as px
import random
import sys



px.init(256,256,"Manoir")
px.load("musica_game_ulysse.pyxres")
px.playm(4, loop=True)
px.load("U3.pyxres")

#=========================VARIABLES============================

with open("donnees.txt", 'r') as file:
    v={
       "argent" : int(file.readline()),
       "points_de_vie" : int(file.readline()),
       "depl" : int(file.readline()),
       "localisation" : list(map(int, file.readline().split())),
       "case1" : int(file.readline()),
       "case2" : int(file.readline()),
       "case3" : int(file.readline()),
       "case4" : int(file.readline()),
       "case5" : int(file.readline()),
       "case6" : int(file.readline()),
       "case7" : int(file.readline()),
       "case8" : int(file.readline()),
       "case9" : int(file.readline()),
       "bateau_x" : int(file.readline()),
       "bateau_y" : int(file.readline()),
       "en_mer" : file.readline()=="True\n",
       "end_of_turn" : file.readline()=="True\n",
       "map1" : [[int(file.readline()) for _ in range(30)] for _ in range(30)],
       "nb_destination" : int(file.readline()),
       "liste_destin" : [list(map(int, file.readline().split())) for _ in range(3)],
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
       "vie" : 278,
       "death" : False,
       "v" : False,
       "pièces" : 100
}
    
x_perso=112
y_perso=112


#======================FONCTIONS==============================

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
        v['deplac_plaque_ennemi'].append([(px.sgn(v['x_camera'] - (v['coord_plaque_ennemi'][-1])[0]) * 5), px.sgn(v['y_camera'] +(v['coord_plaque_ennemi'][-1])[1]) / 5])
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
        brique[1] -= v['vitesse_y'] / 100
        if brique[1] > 256:
            v['coord_brique'].remove(brique)
            v['activation'] = 0
            
def colision():
    for i in range(2):
        for j in range(128,137):
            if px.pget(j, 128 + (i*11)) == 0:
                v["vie"]-=1
        for j in range(128,137):
            if px.pget(128+(i*11), j) == 0:
                v["vie"]-=1
                
def death():
    if v["vie"]<=0:
        v["death"]=True
        
def colision_victoire():
    for i in range(2):
        for j in range(124,141):
            if px.pget(j, 124 + (i*16))==10:
                v["v"]=True
        for j in range(124,141):
            if px.pget(124+(i*16), j) == 10:
                v["v"]=True
                
def retour_map():
    if px.btnp(px.KEY_Q):
        if v["death"]:
            v["points_de_vie"]-=1
        if v["v"]:
            v["argent"]+=100
            v["points_de_vie"]+=1
            if v['x_camera']>900:
                v["argent"]+=100
        with open("donnees.txt", 'w') as file:
            file.write(str(v["argent"]))
            file.write("\n")
            file.write(str(v["points_de_vie"]))
            file.write("\n")
            file.write(str(v["depl"]))
            file.write("\n")
            file.write(str(v["localisation"][0])+" "+str(v["localisation"][1]))
            file.write("\n")
            file.write(str(v["case1"]))
            file.write("\n")
            file.write(str(v["case2"]))
            file.write("\n")
            file.write(str(v["case3"]))
            file.write("\n")
            file.write(str(v["case4"]))
            file.write("\n")
            file.write(str(v["case5"]))
            file.write("\n")
            file.write(str(v["case6"]))
            file.write("\n")
            file.write(str(v["case7"]))
            file.write("\n")
            file.write(str(v["case8"]))
            file.write("\n")
            file.write(str(v["case9"]))
            file.write("\n")
            file.write(str(v["bateau_x"]))
            file.write("\n")
            file.write(str(v["bateau_y"]))
            file.write("\n")
            file.write(str(v["en_mer"]))
            file.write("\n")
            file.write(str(v["end_of_turn"]))
            file.write("\n")
            for ligne in v["map1"]:
                for elt in ligne:
                    file.write(str(elt))
                    file.write("\n")
            file.write(str(v["nb_destination"]))
            file.write("\n")
            for i in range(len(v["liste_destin"])):
                file.write(str(v["liste_destin"][i][0])+" "+str(v["liste_destin"][i][1]))
                file.write("\n")
        sys.exit(7)



#=============================UPDATE==============================

def update():
    creation_ennemi()
    
    deplacement_plaque()
    
    deplacement_camera()
    
    coord_camera()
    
    deplacement_brique()
    
    colision()
    
    death()
    
    colision_victoire()
    
    retour_map()


#=============================DRAW================================

def draw():
    global x_perso, y_perso
    px.cls(0)
    px.bltm(0,0,0,v['x_camera'], v['y_camera'],256,256)
    px.blt(124,124,0,16,112,16,16, colkey = 1)
    for plaque in v['coord_plaque_ennemi']:
        px.blt(plaque[0], plaque[1], 0, 64, 50, 15, 12, rotate= v['tourner_plaque'])
        
    for brique in v['coord_brique']:
        px.blt(brique[0], brique[1], 0, 80, 16, 16, 16)
    px.text(10,10,f'vie : {v["vie"]}',7)
    
    if v["death"]:
        px.cls(0)
        px.text(124, 124, "Game over :(", 7)
        px.text(124, 134, "Tu as perdu 1 point de vie", 7)
    if v["v"]:
        px.cls(7)
        px.text(124, 124, "Game won :)", 0)
        px.text(124, 134, f"Tu as gagne {v['pièces']} pieces d'or", 0)
    if v["v"] and v['x_camera']>900:
        px.cls(7)
        px.text(124, 124, "Game won :)", 0)
        px.text(124, 134, f"Tu as gagne {v['pièces']+100} pieces d'or", 0)
    




px.run(update, draw)