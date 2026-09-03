import pyxel as px
import sys
from random import randint

px.init(48, 48, "L'Odyssée")
px.load("musica_game_ulysse.pyxres")
px.playm(0, loop=True)
px.load("map2.pyxres")

#Création du map de manière aléatoire
def map_aléatoire():
    for i in range(1,len(v["map1"])-1):
        for j in range(1,len(v["map1"][0])-1):
            if randint(0,1)==1:
                v["map1"][i][j]=randint(1,5)
            else:
                v["map1"][i][j]=0
    v["localisation"]=[round(len(v["map1"])/2), round(len(v["map1"])/2)]
    modifie_map()
                
def modifie_map():
    v["map1"][v["liste_destin"][v["nb_destination"]][0]][v["liste_destin"][v["nb_destination"]][1]]=8
    v["map1"][round(len(v["map1"])/2)][round(len(v["map1"])/2)]=0
    v["map1"][round(len(v["map1"])/2)+1][round(len(v["map1"])/2)]=0
    v["map1"][round(len(v["map1"])/2)-1][round(len(v["map1"])/2)]=0
    v["map1"][round(len(v["map1"])/2)+1][round(len(v["map1"])/2)+1]=2
    v["en_mer"]=True
    



#=============================VARIABLES===================================

try:
    with open("donnees.txt", 'x') as file:
        file.write("200\n")
        file.write("3\n")
        file.write("15\n")
        file.write("10 10\n")
        file.write("6\n")
        file.write("6\n")
        file.write("6\n")
        file.write("6\n")
        file.write("6\n")
        file.write("6\n")
        file.write("6\n")
        file.write("6\n")
        file.write("6\n")
        file.write("16\n")
        file.write("16\n")
        file.write("True\n")
        file.write("False\n")
        for i in range(900):
            file.write("7\n")
        file.write("0\n")
        file.write("27 17\n")
        file.write("25 3\n")
        file.write("3 15\n")
    v={
    "argent" : 200,
    "points_de_vie" : 3,
    "depl" : 15,
    "localisation" : [10,10],
    "case1" : 7,
    "case2" : 7,
    "case3" : 7,
    "case4" : 7,
    "case5" : 7,
    "case6" : 7,
    "case7" : 7,
    "case8" : 7,
    "case9" : 7,
    "bateau_x" : 16,
    "bateau_y" : 16,
    "en_mer" : True,
    "end_of_turn" : False,
    "map1" : [[7 for _ in range(30)] for _ in range(30)],
    "nb_destination" : 0,
    "liste_destin" : [[27, 17], [25, 3], [3, 15]]
    }
    gagné=False
    map_aléatoire()
    
    
except FileExistsError:
    try:
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
        gagné=False
    except ValueError:
            with open("donnees.txt", 'w') as file:
                file.write("200\n")
                file.write("3\n")
                file.write("15\n")
                file.write("10 10\n")
                file.write("6\n")
                file.write("6\n")
                file.write("6\n")
                file.write("6\n")
                file.write("6\n")
                file.write("6\n")
                file.write("6\n")
                file.write("6\n")
                file.write("6\n")
                file.write("16\n")
                file.write("16\n")
                file.write("True\n")
                file.write("False\n")
                for i in range(900):
                    file.write("7\n")
                file.write("0\n")
                file.write("27 17\n")
                file.write("25 3\n")
                file.write("3 15")
            v={
            "argent" : 200,
            "points_de_vie" : 3,
            "depl" : 15,
            "localisation" : [10,10],
            "case1" : 7,
            "case2" : 7,
            "case3" : 7,
            "case4" : 7,
            "case5" : 7,
            "case6" : 7,
            "case7" : 7,
            "case8" : 7,
            "case9" : 7,
            "bateau_x" : 16,
            "bateau_y" : 16,
            "en_mer" : True,
            "end_of_turn" : False,
            "map1" : [[7 for _ in range(30)] for _ in range(30)],
            "nb_destination" : 0,
            "liste_destin" : [[27, 17], [25, 3], [3, 15]]
            }
            gagné=False
            map_aléatoire()




#======================FONCTIONS====================================
def sauvegarde():
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

sauvegarde()
        

#Procédure permettant de savoir quelles sont les cases autour du navire
def cases():
    v["case1"]=v["map1"][v["localisation"][0]-1][v["localisation"][1]-1]
    v["case2"]=v["map1"][v["localisation"][0]-1][v["localisation"][1]]
    v["case3"]=v["map1"][v["localisation"][0]-1][v["localisation"][1]+1]
    v["case4"]=v["map1"][v["localisation"][0]][v["localisation"][1]-1]
    v["case5"]=v["map1"][v["localisation"][0]][v["localisation"][1]+1]
    v["case6"]=v["map1"][v["localisation"][0]+1][v["localisation"][1]-1]
    v["case7"]=v["map1"][v["localisation"][0]+1][v["localisation"][1]]
    v["case8"]=v["map1"][v["localisation"][0]+1][v["localisation"][1]+1]
    v["case9"]=v["map1"][v["localisation"][0]][v["localisation"][1]]


def clic():
    global gagné
    if px.btnp(px.MOUSE_BUTTON_LEFT):
        v["depl"]-=1
        v["end_of_turn"]=False
        cases()
        sauvegarde()
    #Puzzle
        if v["case9"]==2:
            sys.exit(-1)
            
    #Shop
        if v["case9"]==5:
            sys.exit(5)

    #Manoir
        if v["case9"]==4:
            sys.exit(4)

    #Donjon
        if v["case9"]==3:
            sys.exit(3)

    #Île au trésor
        if v["case9"]==1:
            sys.exit(2)
  
     #Île drapeau
        if v["case9"]==8:
            v["map1"][v["liste_destin"][v["nb_destination"]][0]][v["liste_destin"][v["nb_destination"]][1]]=0
            v["nb_destination"]+=1
            if v["nb_destination"]==3:
                gagné=True
                sys.exit(8)
            v["depl"]+=15
            modifie_map()
            
        

#Déplacement
def deplacement():
    if v["depl"]==0:
        v["end_of_turn"]=True
        v["en_mer"]=False
        v["depl"]=16
        map_aléatoire()
        
    if v["localisation"][0] > 1:
        if px.btnp(px.MOUSE_BUTTON_LEFT) and (px.mouse_x>=0 and px.mouse_x<=15):
            for i in range(16):
                v["bateau_x"]-=1
            v["localisation"][0] -= 1
            v["bateau_x"]=16
    if v["localisation"][0] < (len(v["map1"])-2):
        if px.btnp(px.MOUSE_BUTTON_LEFT) and (px.mouse_x>=31 and px.mouse_x<=47):
            for i in range(16):
                v["bateau_x"]+=1
            v["localisation"][0] += 1
            v["bateau_x"]=16
    if v["localisation"][1] < len(v["map1"])-2:
        if px.btnp(px.MOUSE_BUTTON_LEFT) and (px.mouse_y>=31 and px.mouse_y<=47):
            for i in range(16):
                v["bateau_y"]+=1
            v["localisation"][1] += 1
            v["bateau_y"]=16
    if v["localisation"][1] > 1:
        if px.btnp(px.MOUSE_BUTTON_LEFT) and (px.mouse_y>=0 and px.mouse_y<=15):
            for i in range(16):
                v["bateau_y"]-=1
            v["localisation"][1] -= 1
            v["bateau_y"]=16

def regles():
    if px.btnp(px.KEY_R):
        sys.exit(6)
        
#======================UPDATE===========================
def update():
    global gagné
    
    if v["points_de_vie"]<=0:
        return
    
    if gagné:
        return
    
    regles()
    
    cases()
    
    deplacement()
    
    clic()
    
#=======================DRAW============================    
def draw():
    global gagné
    if v["points_de_vie"]<=0:
        px.cls(0)
        px.text(7, 20, "GAME OVER", 7)
        with open("donnees.txt", 'w') as file:
            file.write("")     
        return
    if gagné:
        px.cls(0)
        px.text(7, 20, "You won", 11)
        return
        
    if v["en_mer"]:
        #Cases
        px.blt(0,0,0,16*v["case1"],16*v["case1"],16,16)
        px.blt(0,16,0,16*v["case2"],16*v["case2"],16,16)
        px.blt(0,32,0,16*v["case3"],16*v["case3"],16,16)
        px.blt(16,0,0,16*v["case4"],16*v["case4"],16,16)
        px.blt(16,32,0,16*v["case5"],16*v["case5"],16,16)
        px.blt(32,0,0,16*v["case6"],16*v["case6"],16,16)
        px.blt(32,16,0,16*v["case7"],16*v["case7"],16,16)
        px.blt(32,32,0,16*v["case8"],16*v["case8"],16,16)
        px.blt(16,16,0,16*v["case9"],16*v["case9"],16,16)
        #bateau
        px.blt(v["bateau_x"],v["bateau_y"],0,96,96,16,16,12)
        #nb_case_qui_manque
        for i in range(len(str(v["depl"]))):
            px.blt(6**i,0,0,16+8*(int(str(v["depl"])[i])),0,8,8,0)
    if v["end_of_turn"]:
        px.cls(1)
        px.text(1,10,"back in time",0)
        px.text(9,20,"Continue",7)
        px.rectb(7,18,35,10,7)
        px.blt(16,32,0,0,32,16,16,0)
        v["nb_destination"]=0
        modifie_map()
    #mouse
    px.blt(px.mouse_x-7,px.mouse_y-6,0,0,16,16,16,0)
    
        

px.run(update, draw)
