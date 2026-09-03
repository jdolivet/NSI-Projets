import pyxel as px
import random
import sys

px.init(160, 120, title="Attrape les pieces !")
px.load("musica_game_ulysse.pyxres")
px.playm(3, loop=True)
px.load("U3.pyxres")

#===================VARIABLES=========================

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
x = 80
y = 100
score = 0
pieces = []
bombes = []
jeu_termine=False


#=========================FONCTIONS=============================

def deplacement():
    global x
    if px.btn(px.KEY_LEFT):
        x -= 2
    if px.btn(px.KEY_RIGHT):
        x += 2

def création():
    if px.frame_count % 15 == 0:
        pieces.append([random.randint(0, 150), 0])

    if px.frame_count % 25 == 0:
        bombes.append([random.randint(0, 150), 0])
        
def collision():
    global score, jeu_termine
    for bombe in bombes[:]:
        if abs(x - bombe[0]) < 8 and abs(y - bombe[1]) < 8:
            jeu_termine=True
            
    for argent in pieces[:]:
        if abs(x - argent[0]) < 8 and abs(y - argent[1]) < 8:
            score += 1
            pieces.remove(argent)

def retour_map():
    global jeu_termine, score
    if px.btnp(px.KEY_Q):
        if jeu_termine:
            v["points_de_vie"]-=1
            v["argent"]-=score*2
        v["argent"]+=score*2
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





#=================================UPDATE===============================

def update():
    global x, y, score, pieces, bombes, jeu_termine
    
    if jeu_termine:
        return    
    deplacement()
    
    création()

    collision()
    # Mise à jour des positions
    for p in pieces:
        p[1] += 2

    for e in bombes:
        e[1] += 2

    retour_map()



#=============================DRAW========================

def draw():
    px.cls(13)
    
    px.text(5, 5, "Score: " + str(score), 7)

    # joueur
    px.blt(x, y, 0, 16, 112, 16, 16, 1)

    # pièces
    for argent in pieces:
        px.blt(argent[0], argent[1], 0, 0, 0, 16, 16, 1)

    # bombes
    for elt in bombes:
        px.blt(elt[0], elt[1], 0, 16, 0, 16, 16, 1)
    
    if jeu_termine:
        retour_map()
        
        
px.run(update, draw)