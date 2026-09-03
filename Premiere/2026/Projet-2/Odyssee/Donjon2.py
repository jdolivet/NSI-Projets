import pyxel as px
import random
import math
import sys


px.init(320, 240, title="Donjon Fantome")
px.load("musica_game_ulysse.pyxres")
px.playm(4, loop=True)
px.load("map2.pyxres")


#==================VARIABLES========================

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
       "liste_destin" : [list(map(int, file.readline().split())) for _ in range(3)]
}
donjon = [[1 for _ in range(20)] for _ in range(15)]
joueur_x = 1
joueur_y = 1
tresor_x = 0
tresor_y = 0
nb_tresor=0
fantomes = []
jeu_termine = False
victoire = False



#==============================FONCTIONS===============================

def generer_donjon():
    global joueur_x, joueur_y
    global tresor_x, tresor_y
    global fantomes

    for i in range(len(donjon)):
        for j in range(len(donjon[i])):
            if random.randint(0,100) > 25:
                donjon[i][j] = 0
            else:
                donjon[i][j] = 1

    joueur_x = 1
    joueur_y = 1
    donjon[joueur_y][joueur_x] = 0
    trésor()
    for _ in range(15):
        while True:
            gx = random.randint(0, 20 - 1)
            gy = random.randint(0, 15 - 1)
            if donjon[gy][gx] == 0:
                fantomes.append([gx, gy])
                break

def trésor():
    global donjon, tresor_x, tresor_y
    while True:
        tx =random.randint(5, 20 - 2)
        ty =random.randint(3, 15-2)
        if donjon[ty][tx] == 0:
            tresor_x = tx
            tresor_y = ty
            break

def deplacer_joueur(dx, dy):
    global joueur_x, joueur_y

    nx = joueur_x + dx
    ny = joueur_y + dy

    if 0 <= nx < 320 and 0 <= ny < 220:
        try:
            if donjon[ny][nx] == 0:
                joueur_x = nx
                joueur_y = ny
        except IndexError:
            pass
            


def bouger_fantomes():
    global jeu_termine
    if px.btnp(px.KEY_LEFT) or px.btnp(px.KEY_RIGHT) or px.btnp(px.KEY_UP) or px.btnp(px.KEY_DOWN):
        for f in fantomes:
            
            f[0] += random.choice([-1, 0, 1])
            f[1] += random.choice([-1, 0, 1])
            f[0] = max(0, min(320 - 1, f[0]))
            f[1] = max(0, min(220- 1, f[1]))
            if f[0] == joueur_x and f[1] == joueur_y:
                jeu_termine = True


def visible(x, y):
    distance = math.sqrt((x - joueur_x) ** 2 +(y - joueur_y) ** 2)
    return distance <= 4


def retour_map():
    if px.btnp(px.KEY_Q):
        if not victoire and jeu_termine:
            v["points_de_vie"]-=1
            v["argent"]-=nb_tresor*100
        v["argent"]+=nb_tresor*100
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




#========================================UPDATE===============================

def update():
    global victoire, jeu_termine, nb_tresor

    if jeu_termine:
        return

    if px.btnp(px.KEY_LEFT):
        deplacer_joueur(-1, 0)

    if px.btnp(px.KEY_RIGHT):
        deplacer_joueur(1, 0)

    if px.btnp(px.KEY_UP):
        deplacer_joueur(0, -1)

    if px.btnp(px.KEY_DOWN):
        deplacer_joueur(0, 1)

    bouger_fantomes()

    if joueur_x == tresor_x and joueur_y == tresor_y:
        victoire = True
        nb_tresor+=1
        trésor()
        
    retour_map()



#=================================DRAW================================

def draw():
    global victoire
    px.cls(0)

    for y in range(15):
        for x in range(20):

            x1 = x * 16
            y1 = y * 16

            if not visible(x, y):
                px.rect(x1, y1, 16, 16, 0)
                continue
            if donjon[y][x] == 1:
                px.rect(x1, y1, 16, 16, 5)
            else:
                px.rect(x1, y1, 16, 16, 1)
    if visible(tresor_x, tresor_y):
        px.blt(tresor_x * 16 + 2,tresor_y * 16, 1, 16, 16, 16, 16, 13)
    for gx, gy in fantomes:
        if visible(gx, gy):
            px.blt(gx * 16 ,gy * 16 , 1, 32, 16, 16, 16, 13)
    px.blt(joueur_x * 16 ,joueur_y * 16 , 1, 16, 0, 16, 16, 13)
    
    if victoire:
        px.text(55, 55, "TRESOR TROUVE !", 10)
        if px.frame_count % 15 == 0:
            victoire=False
    if jeu_termine:
        if not victoire:
            px.text(50, 55, "UN FANTOME T'A EU, TU AS PERDU TOUT L'ARGENT GAGNE JUSQUE-LA", 8)
            retour_map()


generer_donjon()


px.run(update, draw)