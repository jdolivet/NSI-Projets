import pyxel
pyxel.init(256, 256, "Nuit du code", quit_key = pyxel.KEY_Q, fps = 60)
pyxel.load("U3.pyxres")

# bougez avec les fleches et sautez avec la fleche en haut
#recuperez la cle et arrivez au coffre pour gagner!



X = 48
Y = 112

epsilon = 1
fps = 60
yfloor = 224
G =1.5
dt = 1/60
speed = 1.5
forcesaut = -50
position = [8, 224]
vitesse = [0, 0]
lastjump = 0
dbjumpcd = 100
frame = 0
cle = False
trouve = False
objet_1 = [80, 224, -16, 16]
objet_2 = [96, 208, -16, 16]
objet_3 = [112, 192, -16, 16]
objet_4 = [128, 192, -16, 16]
objet_5 = [144, 176, -16, 16]
objet_6 = [160, 176, -16, 16]
objet_7 = [136, 160, -16, 16]
objet_8 = [122, 160, -16, 16]
objet_9 = [72, 160, -16, 16]
objet_10 = [56, 160, -16, 16]
objet_11 = [0, 150, -16, 16]


def colision_objet_1():
    global position
    global objet_1
    
    if objet_1[0] - 1 < position[0] + 13 < objet_1[0] + 4 and objet_1[1] + 3 < position[1] + 6 < objet_1[1] + 16:
        position[0] -= 2
        

    if objet_1[1] - 17 < position[1] < objet_1[1] - 15 and objet_1[0] < position[0] + 13 < objet_1[0] + 19:
        position[1] -= 2
        
        
    if objet_2[0] - 1 < position[0] + 13 < objet_2[0] + 4 and objet_2[1] + 3 < position[1] + 6 < objet_2[1] + 16:
        position[0] -= 2
        

    if objet_2[1] - 17 < position[1] < objet_2[1] - 15 and objet_2[0] < position[0] + 13 < objet_2[0] + 19:
        position[1] -= 2
        
    if objet_3[0] - 1 < position[0] + 13 < objet_3[0] + 4 and objet_3[1] + 3 < position[1] + 6 < objet_3[1] + 16:
        position[0] -= 2
        

    if objet_3[1] - 17 < position[1] < objet_3[1] - 15 and objet_3[0] < position[0] + 13 < objet_3[0] + 19:
        position[1] -= 2


    if objet_4[0] - 1 < position[0] + 13 < objet_4[0] + 4 and objet_4[1] + 3 < position[1] + 6 < objet_4[1] + 16:
        position[0] -= 2
        

    if objet_4[1] - 17 < position[1] < objet_4[1] - 15 and objet_4[0] < position[0] + 13 < objet_4[0] + 19:
        position[1] -= 2

    if objet_5[0] - 1 < position[0] + 13 < objet_5[0] + 4 and objet_5[1] + 3 < position[1] + 6 < objet_5[1] + 16:
        position[0] -= 2
        

    if objet_5[1] - 17 < position[1] < objet_5[1] - 15 and objet_5[0] < position[0] + 13 < objet_5[0] + 19:
        position[1] -= 2
        
    if objet_6[0] - 1 < position[0] + 13 < objet_6[0] + 4 and objet_6[1] + 3 < position[1] + 6 < objet_6[1] + 16:
        position[0] -= 2
        

    if objet_6[1] - 17 < position[1] < objet_6[1] - 15 and objet_6[0] < position[0] + 13 < objet_6[0] + 19:
        position[1] -= 2
    
       
    if objet_7[0] - 1 < position[0] + 13 < objet_7[0] + 4 and objet_7[1] + 3 < position[1] + 6 < objet_7[1] + 16:
        position[0] -= 2
        

    if objet_7[1] - 17 < position[1] < objet_7[1] - 15 and objet_7[0] < position[0] + 13 < objet_7[0] + 19:
        position[1] -= 2
    
       
    if objet_8[0] - 1 < position[0] + 13 < objet_8[0] + 4 and objet_8[1] + 3 < position[1] + 6 < objet_8[1] + 16:
        position[0] -= 2
        

    if objet_8[1] - 17 < position[1] < objet_8[1] - 15 and objet_8[0] < position[0] + 13 < objet_8[0] + 19:
        position[1] -= 2
        
        
       
    if objet_9[0] - 1 < position[0] + 13 < objet_9[0] + 4 and objet_9[1] + 3 < position[1] + 6 < objet_9[1] + 16:
        position[0] -= 2
        

    if objet_9[1] - 17 < position[1] < objet_9[1] - 15 and objet_9[0] < position[0] + 13 < objet_9[0] + 19:
        position[1] -= 2
        
       
    if objet_10[0] - 1 < position[0] + 13 < objet_10[0] + 4 and objet_10[1] + 3 < position[1] + 6 < objet_10[1] + 16:
        position[0] -= 2
        

    if objet_10[1] - 17 < position[1] < objet_10[1] - 15 and objet_10[0] < position[0] + 13 < objet_10[0] + 19:
        position[1] -= 2
        
    
       
    if objet_11[0] - 1 < position[0] + 13 < objet_11[0] + 4 and objet_11[1] + 3 < position[1] + 6 < objet_11[1] + 16:
        position[0] -= 2
        

    if objet_11[1] - 17 < position[1] < objet_11[1] - 15 and objet_11[0] < position[0] + 13 < objet_11[0] + 19:
        position[1] -= 2


def cle():
    global cle
    if objet_11[0] - 1 < position[0] + 13 < objet_11[0] + 4 and objet_11[1] + 3 < position[1] + 6 < objet_11[1] + 16:
        cle = True


def cpt_frame():
    global frame
    frame += 1
    return frame 

def addvitesse():
    global position, vitesse
    position[1] += vitesse[1] * dt
    
def gravite(G):
    global position, yfloor, vitesse
    if position[1] < yfloor:
        position[1] += G

def floor():
    global yfloor, epsilon, position, vitesse
    
    if yfloor + epsilon >= position[1] >= yfloor - epsilon:
        vitesse[1] = 0
        position[1] = yfloor
        return True
        
        
def walk():
    global yfloor, epsilon, position, vitesse, speed, X, Y
    if pyxel.btn(pyxel.KEY_RIGHT):
        position[0] += speed
        if pyxel.frame_count % 4 > 0:
            X = 48
            Y = 112
        else:
            X = 48
            Y = 128
    else:
        X = 48
        Y = 112
        
    if pyxel.btn(pyxel.KEY_LEFT):
        position[0] -= speed
        if pyxel.frame_count % 4 > 0:
            X = 0
            Y = 112
        else:
            X = 0
            Y = 128
            
def jump():
    global lastjump, dbjumpcd, vitesse, forcesaut, position
    if ((225>= position[1] >= 223) or (cpt_frame() >= lastjump + dbjumpcd)) and pyxel.btn(pyxel.KEY_UP):
        position[1] += forcesaut
        lastjump = cpt_frame()




def decor_1():
    global position, objets_1
    global X, Y, trouve
    pyxel.bltm(0, 0, 0, 0, 0, 256, 256)
    pyxel.blt(position[0], position[1], 0, X, Y, 16, 16, 1)
    if trouve == False:
        pyxel.blt(96, 224, 0, 112, 16, 16, 16)
    


def end():
    global cle, trouve
    if cle == True and objet_1[0]  + 15 < position[0] + 13 < objet_1[0] + 19 and objet_1[1] + 3 < position[1] + 6 < objet_1[1] + 16:
        trouve = True
        
def texte_fin():
    global trouve
    if trouve == True:
        pyxel.text(130, 230, "Bravo !", 7)

    
def deplacement():
    #addvitesse()
    gravite(G)
    floor()
    walk()
    jump()

    
def update():
    global cle
    cpt_frame()
    decor_1()
    deplacement()
    cle()
    colision_objet_1()
    cle()
    end()
    texte_fin()
    #print(position)
    #print(vitesse)
    #print(floor())
    #print(colision(objets_1))
    pass


def draw():
    pass

pyxel.run(update, draw)