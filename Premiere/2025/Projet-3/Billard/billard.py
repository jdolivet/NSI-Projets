import pyxel
import random
import math

def début() -> None:
    
    
    """ Pour initialiser le fenêtre pyxel, et load les ressources du fichier pyxres """
    pyxel.init(800, 535, "Billard", fps = 60)
    pyxel.load("billard_graphiques.pyxres")
    pyxel.mouse(True)
    
    #pyxel.playm(0, loop = True)
    
        
# Corps du code 

# Variables globales principales

x_table = 100
y_table = 40
largeur_table = 600
hauteur_table = 300

long_queue = 256
secondes = 0
force_coup = 0

sprites_boules = [[[16 * i, 0], [16 * i, 16], [16 * i, 32], [16 * i, 48]] for i in range (16)]

en_parametre = False

sons = True
musique = True
couleur_fond = 10

versus_ia = False
versus_joueur = True

peut_commencer_partie = False 

joueur_1 = False
joueur_2 = False

if random.randint(0, 1) == 0:
    joueur_1 = True
else:
    joueur_2 = True
    
action = 0

Jeu_Fini = False

dt = 1/60
mparpixel = 2.54/600
inertie = (2/5) * (0.170) * ((10 * mparpixel) ** 2)
epsilon = 1.5
epsilon2 = 0.01

balle1 = {"pos": [500, (2 * y_table + 105)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 1, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle2 = {"pos": [516, (2 * y_table + 105 - 9)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 2, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle3 = {"pos": [516, (2 * y_table + 105 + 9)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 3, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle4 = {"pos": [532, (2 * y_table + 105 - 18)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 4, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle5 = {"pos": [532, (2 * y_table + 105)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 8, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle6 = {"pos": [532, (2 * y_table + 105 + 18)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 6, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle7 = {"pos": [548, (2 * y_table + 105 - 27)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 7, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle8 = {"pos": [548, (2 * y_table + 105 - 9)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 5, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle9 = {"pos": [548, (2 * y_table + 105 + 9)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 9, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle10 = {"pos": [548, (2 * y_table + 105 + 27)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 10, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle11 = {"pos": [564, (2 * y_table + 105 - 36)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 11, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle12 = {"pos": [564, (2 * y_table + 105 - 18)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 12, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle13 = {"pos": [564, (2 * y_table + 105)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 12, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle14 = {"pos": [564, (2 * y_table + 105 + 18)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 14, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balle15 = {"pos": [564, (2 * y_table + 105 + 36)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 15, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}
balleb = {"pos": [200, (2 * y_table + 105)], "vitesse": [0, 0], "acc": [0, 0], "forces": [ ], "m": 0.170, "r": 8,  "couleur": 0, "vitesse_angulaire": 0, "acceleration_angulaire": 0, "torque": [], "i": inertie, "dedans": False}

balles = [balleb, balle1, balle2, balle3, balle4, balle5, balle6, balle7, balle8, balle9, balle10, balle11, balle12, balle13,
          balle14, balle15]

boules_in_j1 = []
boules_in_j2 = []

coup_fait_j1 = False
coup_fait_j2 = False

coup_jouer_j1 = {"force" : 0, "direction": 0, "position" : [0, 0], "angle" : 0}
coup_jouer_j2 = {"force" : 0, "direction": 0, "position" : [0, 0], "angle" : 0}


#Fonctions Vecteurs

def add(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]

def soustraire(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1]]

def mul(v, k):
    return [v[0]*k, v[1]*k]

def div(v, k):
    return [v[0]/k, v[1]/k]

def norme(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def normal(v):
    return [v[0]/norme(v), v[1]/norme(v)] if norme(v) != 0 else [0,0]

def scalaire(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def distance(v1, v2):
    return norme(soustraire(v1, v2))

def projection(v, u):
    return mul(norme(u), scalaire(v, norme(u)))

#Physique

def physique():
    
    collisions_toutes_les_balles()
    collision_mur()
    collision_mur_rotation()

    resistance_air()
    friction()
    torque_roulement()
    frottement_rotationel()
    effect_magnus()

    updates_physique()
    updates_rotation()

    limite_vitesse()
    

def friction():
    global mparpixel
    global balles
    global epsilon
    for balle in balles:
        if norme(balle["vitesse"]) >= epsilon:
            direction = normal(balle["vitesse"])
            poids = balle["m"] * 9.81
            coeff_friction = 0.03

            vfriction = [-direction[0] * poids * coeff_friction, -direction[1] * poids * coeff_friction]
            balle["forces"].append(vfriction)


def updates_physique():
    global balles
    global dt
    global mparpixel
    global sprites_boules
    for balle in balles:
        sommeforces = [0, 0]
        for vecteur in balle["forces"]:
            sommeforces[0] += vecteur[0]
            sommeforces[1] += vecteur[1]
        balle["acc"][0] = sommeforces[0] / balle["m"] / mparpixel
        balle["acc"][1] = sommeforces[1] / balle["m"] / mparpixel

        balle["vitesse"][0] += balle["acc"][0] * dt
        balle["vitesse"][1] += balle["acc"][1] * dt

        balle["pos"][0] += balle["vitesse"][0] * dt   
        balle["pos"][1] += balle["vitesse"][1] * dt

        balle["forces"].clear()

def collisionballes(idobj1, idobj2):
    global balles, dt, mparpixel, sons

    b1 = balles[idobj1]
    b2 = balles[idobj2]

    delta = soustraire(b2["pos"], b1["pos"])
    dist = norme(delta)
    rsum = b1["r"] + b2["r"]
    if dist >= rsum:
        return

    direction = normal(delta)
    pen = rsum - dist
    if pen > 0:
        corr = mul(direction, pen * 0.7 + 0.01)
        b1["pos"] = soustraire(b1["pos"], corr)
        b2["pos"] = add(b2["pos"], corr)

    vrel = soustraire(b1["vitesse"], b2["vitesse"])
    vn = scalaire(vrel, direction)
    if vn >= 2:
        return

    vnm = vn * mparpixel
    e = 0.8
    j = (-(1 + e) * vnm / (1.0 / b1["m"] + 1.0 / b2["m"])) + 0
    
    if sons:
        pyxel.play(0, 0)
    F = div(mul(direction, j), dt)
    b1["forces"].append(F)
    b2["forces"].append(mul(F, -1))

    pen = rsum - dist
    if pen > 0:
        corr = mul(direction, pen * 0.5 + 0.01)
        b1["pos"] = soustraire(b1["pos"], corr)
        b2["pos"] = add(b2["pos"], corr)

def collision_mur():
    global dt
    global balles
    global mparpixel
    global x_table, y_table, hauteur_table, largeur_table
    x_min = x_table + 7
    x_max = x_table + largeur_table - 7
    y_min = y_table + 7
    y_max = y_table + hauteur_table - 14
    coeff_elasticite = 0.93
    for balle in balles:
        r = balle["r"]
        pos = balle["pos"]
        m = balle["m"]
        vel = balle["vitesse"]

        if pos[0] - r < x_min and y_min <= pos[1] - r <= y_max:
            n = [1, 0]
            vitesse = vel[0]*n[0] + vel[1]*n[1]
            if vitesse < 0:
                vitesse = vitesse * mparpixel
                impulsion = -(1 + coeff_elasticite) * m * vitesse
                vforce = [impulsion * n[0] / dt, impulsion * n[1] / dt]
                balle["forces"].append(vforce)
            pos[0] = x_min + r


        if pos[0] + r > x_max and y_min <= pos[1] - r <= y_max:
            n = [-1, 0]
            vitesse = vel[0]*n[0] + vel[1]*n[1]
            if vitesse < 0:
                vitesse = vitesse * mparpixel
                impulsion = -(1 + coeff_elasticite) * m * vitesse
                vforce = [impulsion * n[0] / dt, impulsion * n[1] / dt]
                balle["forces"].append(vforce)
            pos[0] = x_max - r


        if pos[1] - r < y_min:
            n = [0, 1]
            vitesse = vel[0]*n[0] + vel[1]*n[1]
            if vitesse < 0:
                vitesse = vitesse * mparpixel
                impulsion = -(1 + coeff_elasticite) * m * vitesse
                vforce = [impulsion * n[0] / dt, impulsion * n[1] / dt]
                balle["forces"].append(vforce)
            pos[1] = y_min + r


        if pos[1] + r > y_max: 
            n = [0, -1]
            vitesse = vel[0]*n[0] + vel[1]*n[1]
            if vitesse < 0:
                vitesse = vitesse * mparpixel
                impulsion = -(1 + coeff_elasticite) * m * vitesse
                vforce = [impulsion * n[0] / dt, impulsion * n[1] / dt]
                balle["forces"].append(vforce)
            pos[1] = y_max - r
            


def resistance_air():
    global balles
    global mparpixel
    global epsilon
    coeff_frottement = 0.0003
    for balle in balles:
        if norme(balle["vitesse"]) > epsilon:
            direction = normal(balle["vitesse"])
            vitesse = norme(balle["vitesse"]) * mparpixel
            force = -coeff_frottement * vitesse**2
            vforce = mul(direction, force)
            balle["forces"].append(vforce)



def updates_rotation():
    global balles
    global dt
    global mparpixel
    for balle in balles:
        sommetorque = 0
        for t in balle["torque"]:
            sommetorque += t

        balle["acceleration_angulaire"] = sommetorque / balle["i"]
        balle["vitesse_angulaire"] += balle["acceleration_angulaire"] * dt
        balle["torque"].clear()

def frottement_rotationel():
    global balles
    global epsilon2
    coeff_frottement = 0.001
    for balle in balles:
        if abs(balle["vitesse_angulaire"]) > epsilon2:
            torque = -coeff_frottement * balle["vitesse_angulaire"]
            balle["torque"].append(torque)


def torque_roulement():
    global balles
    global dt
    global mparpixel
    coeff_frottement = 0.02

    for balle in balles:
        vitesse = norme(balle["vitesse"])
        vitesse_lineaire = vitesse * mparpixel
        if vitesse_lineaire == 0:
            continue

        rayonm = balle["r"] * mparpixel
        vitesse_roulement = abs(balle["vitesse_angulaire"]) * rayonm

        diff_vitesse = vitesse_lineaire - vitesse_roulement
        direction = normal(balle["vitesse"])
        force = -coeff_frottement * balle["m"] * 9.81 * (-1 if diff_vitesse < 0 else 1)
        vforce  = [direction[0] * force, direction[1] * force]


        balle["forces"].append(vforce)

        force_rotation = -force * rayonm
        balle["torque"].append(force_rotation)



def collision_mur_rotation():
    global dt, balles, mparpixel
    global x_table, largeur_table, y_table, hauteur_table
    
    x_min = x_table
    x_max = x_table + largeur_table

    y_min = y_table
    y_max = y_table + hauteur_table
    coeff_spin = 0.02

    for balle in balles:
        pos = balle["pos"]
        vitesse = balle["vitesse"]
        m = balle["m"]
        i = balle["i"]
        r = balle["r"] * mparpixel

        if pos[0] - balle["r"] < x_min:
            normale = [1, 0]
        elif pos[0] + balle["r"] > x_max:
            normale = [-1, 0]
        elif pos[1] - balle["r"] < y_min:
            normale = [0, 1]
        elif pos[1] + balle["r"] > y_max:
            normale = [0, -1]
        else:
            continue
        vnormale = scalaire(vitesse, normale)
        vtangente = soustraire(vitesse, mul(normale, vnormale))
        normevt = norme(vtangente) * mparpixel

        if normevt > 0:
            tangente = normal(vtangente)
            vsurface = balle["vitesse_angulaire"] * r
            diff_tangent = normevt - vsurface

            force = -coeff_spin * m * 9.81 * (-1 if diff_tangent < 0 else 1)
            vforce = mul(tangente, force)
            balle["forces"].append(vforce)

            forcetorque= -force * r
            balle["torque"].append(forcetorque)




def effect_magnus():
    global mparpixel
    global epsilon
    coeff_magnus = 0.001
    for balle in balles:
        if norme(balle["vitesse"]) > epsilon:
            v = norme(balle["vitesse"])
            vnormal = normal(balle["vitesse"])
            if v == 0:
                continue
            force = [-coeff_magnus * balle["vitesse_angulaire"] * vnormal[1], coeff_magnus * balle["vitesse_angulaire"] * vnormal[0]]
            balle["forces"].append(force)

def collision_balles_rotation(id1, id2):
    global balles
    global dt
    global mparpixel

    coeff_frottement_balles = 0.02

    balle1 = balles[id1]
    balle2 = balles[id2]

    pos1 = balle1["pos"]
    pos2 = balle2["pos"]
    r1 = balle1["r"] * mparpixel
    r2 = balle2["r"] * mparpixel

    if distance(pos1, pos2) > (balle1["r"] + balle2["r"]):
        return

    normale = normal(soustraire(pos2, pos1))
    tangente = [-normale[1], normale[0]]

    vitesse_relative = soustraire(balle1["vitesse"], balle2["vitesse"])
    vitesse_tangentielle = scalaire(vitesse_relative, tangente) * mparpixel

    vspin1 = balle1["vitesse_angulaire"] * r1
    vspin2 = balle2["vitesse_angulaire"] * r2

    vitesse_contact = vitesse_tangentielle + (vspin1 - vspin2)

    if abs(vitesse_contact) < 1e-5:
        return

    signe = (1 if vitesse_contact > 0 else -1)
    masse_effective = (balle1["m"] * balle2["m"]) / (balle1["m"] + balle2["m"])
    impulsion_tangentielle = -coeff_frottement_balles * masse_effective * 9.81 * signe

    force_tangentielle = impulsion_tangentielle / dt
    vecteur_force_tangentielle = [tangente[0]*force_tangentielle, tangente[1]*force_tangentielle]


    balle1["forces"].append(vecteur_force_tangentielle)
    balle2["forces"].append([-vecteur_force_tangentielle[0], -vecteur_force_tangentielle[1]])


    balle1["torque"].append(-force_tangentielle * r1)
    balle2["torque"].append(force_tangentielle * r2)


def coup_j1(balle, coup_jouer_j1):
    global mparpixel, balles, action

    m = balle["m"]
    r = balle["r"] * mparpixel
    i = balle["i"]
    force = coup_jouer_j1["force"]
    normale = normal(coup_jouer_j1["direction"])
    offset = mul(coup_jouer_j1["position"], mparpixel)
    angle = coup_jouer_j1["angle"]
    impulsen = force
    
    F = mul(normale, impulsen)
    

    balle["forces"].append(F)

def coup_j2(balle, coup_jouer_j2):
    global mparpixel, balles, action

    m = balle["m"]
    r = balle["r"] * mparpixel
    i = balle["i"]
    force = coup_jouer_j2["force"]
    normale = normal(coup_jouer_j2["direction"])
    offset = mul(coup_jouer_j2["position"], mparpixel)
    angle = coup_jouer_j2["angle"]

    impulsen = force
    F = mul(normale, impulsen)

    balle["forces"].append(F)
    
    

def limite_vitesse():
    global balles
    global epsilon, epsilon2
    for balle in balles:
        if abs(norme(balle["vitesse"])) <= epsilon:
            balle["vitesse"] = mul(balle["vitesse"], 0)
        if balle["vitesse_angulaire"] <= epsilon2:
            balle["vitesse_angulaire"] = 0
            
            
            
def collisions_toutes_les_balles():
    global balles
    for i in range(len(balles)):
        for j in range(i + 1, len(balles)):
            collisionballes(i, j)
            collision_balles_rotation(i, j)

# ------------------------------------------------------------------------------------------------------- #
# -----------------------------   Partie sur les différents menus du jeu    ----------------------------- # 
# ------------------------------------------------------------------------------------------------------- #


def parametres() -> None:
    """ Fonction qui permet de gérer les paramètres de jeu """
    global Jeu_Fini, en_parametre, sons, musique, couleur_fond
    
    pyxel.blt(10, 10, 0, 7, 83, 56, 56, 8, 0, 1)
    
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 10 < pyxel.mouse_x < 66 and 10 < pyxel.mouse_y < 66:
        en_parametre = True
        
    if en_parametre:
        
        pyxel.rect(0, 0, 800, 535, 0)
        pyxel.circ(400, 250, 200, 12)
        pyxel.circb(400, 250, 201, 7)
        
        pyxel.blt(30, 490, 0, 11, 152, 17, 17, 13, 0, 3)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 10 < pyxel.mouse_x < 70 and 460 < pyxel.mouse_y < 530:
            en_parametre = False
        
        pyxel.text(310, 150, "SONS : ", 0)
        pyxel.blt(340, 137, 0, 80, 80, 26, 26, 13)
        pyxel.blt(380, 137, 0, 107, 80, 26, 26, 13)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 340 < pyxel.mouse_x < 366 and 137 < pyxel.mouse_y < 163:
            sons = False
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 380 < pyxel.mouse_x < 406 and 137 < pyxel.mouse_y < 163:
            sons = True
        if not sons:
            pyxel.blt(344, 115, 0, 39, 152, 17, 17, 13)
        else:
            pyxel.blt(384, 115, 0, 39, 152, 17, 17, 13)
        
        pyxel.text(295, 250, "MUSIQUE : ", 0)
        pyxel.blt(340, 237, 0, 80, 80, 26, 26, 13)
        pyxel.blt(380, 237, 0, 107, 80, 26, 26, 13)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 340 < pyxel.mouse_x < 366 and 237 < pyxel.mouse_y < 263:
            musique = False
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 380 < pyxel.mouse_x < 406 and 237 < pyxel.mouse_y < 263:
            musique = True
        if not musique:
            pyxel.blt(344, 215, 0, 39, 152, 17, 17, 13)
        else:
            pyxel.blt(384, 215, 0, 39, 152, 17, 17, 13)
            
    
    
        pyxel.text(265, 340, "COULEUR_DE_FOND : ", 0)
        pyxel.blt(340, 337, 0, 136, 84, 32, 8)
        pyxel.blt(380, 337, 0, 136, 96, 32, 8)
        pyxel.blt(420, 337, 0, 136, 108, 32, 8)
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 340 < pyxel.mouse_x < 372 and 337 < pyxel.mouse_y < 345:
            couleur_fond = 10
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 380 < pyxel.mouse_x < 412 and 337 < pyxel.mouse_y < 345:
            couleur_fond = 9
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 420 < pyxel.mouse_x < 452 and 337 < pyxel.mouse_y < 345:
            couleur_fond = 11
        
        if couleur_fond == 10:
            pyxel.blt(348, 315, 0, 39, 152, 17, 17, 13)
        elif couleur_fond == 9:
            pyxel.blt(388, 315, 0, 39, 152, 17, 17, 13)
        elif couleur_fond == 11:
            pyxel.blt(428, 315, 0, 39, 152, 17, 17, 13)
        
    
def menu_initial() -> bool:
    """ Affiche le menu initial avant d'afficher le billard """
    global peut_commencer_partie
    
    interface_init()
    règles()
    commencer()
    
    return peut_commencer_partie
    
def interface_init() -> None:
    """ Dessine le décor du menu de base """ 
    
    pyxel.cls(6)
    pyxel.text(150, 60, "Voici le tant attendu BILLARD : Pour profiter pleinement de notre jeu, mettez la fenetre en grand ecran.", 0)
    
def règles() -> None:
    """ Affiche le texte pour les règles des jeux """
    
    pyxel.text(150, 100, "Le but du jeu est de faire rentrer en premier 7 boules et enfin la noire.", 0)
    pyxel.text(150, 115, "Si vous commencez par faire entrer une boule pleine, vous devrez mettre les pleines et vice-versa", 0)
    pyxel.text(150, 130, "Vous jouerez contre une intelligence artificielle ou simplement contre qqln d'autre.", 0)
    pyxel.text(150, 160, "Comment jouer a ce billard, telle est la question : ", 0)
    pyxel.text(150, 175, " - Appuyez en premier sur la boule blanche", 0)
    pyxel.text(150, 190, " - Choisissez l'angle et la force de votre tir dans la boule blanche afin de reussir vos coups", 0)
    pyxel.text(150, 215, "Il y aura une jauge pour la force du tir, et vous appuirez autour d'une boule pour décider l'angle", 0)
    pyxel.text(250, 245, "Choisissez le mode de jeu que vous souhaitez : ", 0)
    pyxel.blt(235, 285, 0, 79, 117, 30, 22, 13, 0, 2)
    pyxel.blt(420, 285, 0, 80, 149, 30, 22, 13, 0, 2)
    pyxel.text(150, 420, "PS : Vous pouvez aussi modifier les paramètres du jeu, vous pouvez retirer la musique, retirer les sons et choisir une autre couleur de sol pour le billard", 0)
        

def commencer() -> None:
    """ Fonction qui update le jeu si le joueur veut commencer la partie """
    global peut_commencer_partie
    
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 235 < pyxel.mouse_x < 257 and 285 < pyxel.mouse_y < 298:
    
        versus_joueur = True
        peut_commencer_partie = True
    
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 420 < pyxel.mouse_x < 442 and 285 < pyxel.mouse_y < 298:
        vesus_ia = True
        peut_commencer_partie = True
    
    
def menu_fin() -> None:
    """ Affiche le menu de fin, enregistre les scores et les données de la partie, demande au joueur si il veut recommencer """
    
    global Jeu_Fini, comptage_boules, boules_in_j1, boules_in_j2
    
    if Jeu_Fini:
        pyxel.cls(12)
        
        if len(boules_in_j1) > len(boules_in_j2):
            pyxel.text(200, 100, " Joueur_1 a gagné ", 0)
        if len(boules_in_j1) == len(boules_in_j2):
            pyxel.text(200, 100, " C'est l'égalité ", 0)
        if len(boules_in_j1) < len(boules_in_j2):
            pyxel.text(200, 100, " Joueur_2 a gagné ", 0)
        
        pyxel.text(150, 400, "La partie est terminée, vous pouvez recommencer le script pour refaire une partie, bonne chance, (il faut beaucoup s'entrainer)", 0)
        
    
    

# ------------------------------------------------------------------------------------------------------ #
# -----------------------------  Partie graphique du billard et des queues ----------------------------- # 
# ------------------------------------------------------------------------------------------------------ #

def billard() -> None:
    """ Dessine la table de billard en entier avec tous les détails """
    
    global x_table, y_table, largeur_table, hauteur_table
    
    tapis_billard(x_table, y_table, largeur_table, hauteur_table)
    trous_billard(x_table, y_table, largeur_table, hauteur_table)
    détails_lignes_billard(x_table, y_table, largeur_table, hauteur_table)
    détails_bords_billard(x_table, y_table, largeur_table, hauteur_table)
    queues()
    boules()
    
def tapis_billard(x_table: int, y_table: int, largeur_table: int, hauteur_table: int) -> None:
    """ Dessine la corps du billard """

    pyxel.rect(x_table, y_table, largeur_table, hauteur_table, 5)
    
def trous_billard(x_table: int, y_table: int, largeur_table: int, hauteur_table: int) -> None:
    """ Dessine les trous de la table avec leurs contours en blanc """
    
    # Trous dans les coins en haut 
    pyxel.circ(x_table, y_table, 10, 0)
    pyxel.circb(x_table, y_table, 11, 7)
    pyxel.circ(x_table + largeur_table, y_table, 10, 0)
    pyxel.circb(x_table + largeur_table, y_table, 11, 7)

    # Trous dans les coins en bas """
    pyxel.circ(x_table, y_table + hauteur_table, 10, 0)
    pyxel.circb(x_table, y_table + hauteur_table, 11, 7)
    pyxel.circ(x_table + largeur_table, y_table + hauteur_table, 10, 0)
    pyxel.circb(x_table + largeur_table, y_table + hauteur_table, 11, 7)
    
    # Trous au milieu 
    pyxel.circ(x_table + largeur_table // 2, y_table - 6, 10, 0)
    pyxel.circb(x_table + largeur_table // 2, y_table - 6, 11, 7)
    pyxel.circ(x_table + largeur_table // 2, y_table + hauteur_table + 6, 10, 0)
    pyxel.circb(x_table + largeur_table // 2, y_table + hauteur_table + 6, 11, 7)


def détails_bords_billard(x_table: int, y_table: int, largeur_table: int, hauteur_table: int) -> None:
    """ Dessine les détails des côtés de la table de billard """
    
    # Tour table
    pyxel.line(x_table - 22, y_table - 22, x_table - 22, y_table + hauteur_table + 22, 7)
    pyxel.line(x_table - 22, y_table + hauteur_table + 22, x_table + largeur_table + 22, y_table + hauteur_table + 22, 7)
    pyxel.line(x_table + largeur_table + 22, y_table + hauteur_table + 22, x_table + largeur_table + 22, y_table - 22, 7)
    pyxel.line(x_table + largeur_table + 22, y_table - 22, x_table - 22, y_table - 22, 7)
    
    # Délimitations parties pour fill
    pyxel.line(x_table + 18, y_table - 21, x_table + 18, y_table - 1, 13)
    pyxel.line(x_table - 21, y_table + 18, x_table - 1, y_table + 18, 13)
    pyxel.fill(x_table + 9, y_table - 10, 13)
    
    pyxel.line(x_table + largeur_table - 18, y_table - 21, x_table + largeur_table - 18, y_table - 1, 13)
    pyxel.line(x_table + largeur_table + 21, y_table + 18, x_table + largeur_table + 1, y_table + 18, 13)
    pyxel.fill(x_table + largeur_table - 13, y_table + - 13, 13)
    
    pyxel.line(x_table + largeur_table + 21, y_table + hauteur_table - 18, x_table + largeur_table + 1, y_table + hauteur_table - 18, 13)
    pyxel.line(x_table + largeur_table - 18, y_table + hauteur_table + 21, x_table + largeur_table - 18, y_table + hauteur_table + 1, 13)
    pyxel.fill(x_table + largeur_table + 11, y_table + hauteur_table - 8, 13)
    
    pyxel.line(x_table + 18, y_table + hauteur_table + 21, x_table + 18, y_table + hauteur_table + 1, 13)
    pyxel.line(x_table - 21, y_table + hauteur_table - 18, x_table + 1, y_table + hauteur_table - 18, 13)
    pyxel.fill(x_table + 9, y_table + hauteur_table + 10, 13)
    
    
    pyxel.line(x_table + largeur_table // 2 - 18, y_table - 21, x_table + largeur_table // 2 - 18, y_table - 1, 13)
    pyxel.line(x_table + largeur_table // 2 + 18, y_table - 21, x_table + largeur_table // 2 + 18, y_table - 1, 13)
    pyxel.fill(x_table + largeur_table // 2 - 13, y_table - 18, 13)
    
    pyxel.line(x_table + largeur_table // 2 - 18, y_table + hauteur_table + 21, x_table + largeur_table // 2 - 18, y_table + hauteur_table + 1, 13)
    pyxel.line(x_table + largeur_table // 2 + 18, y_table + hauteur_table + 21, x_table + largeur_table // 2 + 18, y_table + hauteur_table + 1, 13)
    pyxel.fill(x_table + largeur_table // 2 + 10, y_table + hauteur_table + 15, 13)
               
    # Côtés en bois du billard
    pyxel.fill(x_table + 40, y_table - 7, 4)
    pyxel.fill(x_table + largeur_table // 2 + 30, y_table - 7, 4)
    pyxel.fill(x_table - 10, y_table + 60, 4)
    pyxel.fill(x_table + largeur_table // 2 + 30, y_table + hauteur_table + 7, 4)
    pyxel.fill(x_table + 40, y_table + hauteur_table + 10, 4)
    pyxel.fill(x_table + largeur_table + 10, y_table + 40, 4)
    
    # Détails boulons billard
    for i in range(6):
        pyxel.circ((x_table * i) + 150, y_table - 10, 4, 13)
        pyxel.circb((x_table * i) + 150, y_table - 10, 4, 7)
        
    for i in range(6):
        pyxel.circ((x_table * i) + 150, y_table + hauteur_table + 11, 4, 13)
        pyxel.circb((x_table * i) + 150, y_table + hauteur_table + 11, 4, 7)
        
    for i in range(3):
        pyxel.circ(x_table - 11, (y_table * 2 * i) + 110, 4, 13)
        pyxel.circb(x_table - 11, (y_table * 2 *i) + 110, 4, 7)
        
    for i in range(3):
        pyxel.circ(x_table + largeur_table + 11, (y_table * 2 * i) + 100, 4, 13)
        pyxel.circb(x_table + largeur_table + 11, (y_table * 2 * i) + 100, 4, 7)
        
def détails_lignes_billard(x_table: int, y_table: int, largeur_table: int, hauteur_table: int) -> None:
    """ Dessine les détails des lignes du billard """
    
    # Lignes fines blanches horizontales
    pyxel.line(x_table + 11, y_table, x_table - 11 + largeur_table // 2, y_table, 7)
    pyxel.line(x_table + 11 + largeur_table // 2, y_table, x_table + largeur_table - 11, y_table, 7)
    pyxel.line(x_table + 11, y_table + hauteur_table, x_table - 11 + largeur_table // 2, y_table + hauteur_table, 7)
    pyxel.line(x_table + 11 + largeur_table // 2, y_table + hauteur_table, x_table + largeur_table - 11, y_table + hauteur_table, 7)
    
    # Lignes fines blanches verticales
    pyxel.line(x_table, y_table + 11, x_table, y_table + hauteur_table - 11, 7)
    pyxel.line(x_table + largeur_table, y_table + 11, x_table + largeur_table, y_table + hauteur_table - 11, 7)
    
    # Lignes noires horizontales d'épaisseur 2 ( pyxel.rect permet cela, recangle de height = 2 en fait)
    pyxel.rect(x_table + 19, y_table + 7, largeur_table // 2 - 29 , 2, 0)
    pyxel.rect(x_table + largeur_table // 2 + 11, y_table + 7, largeur_table // 2 - 29, 2, 0)
    pyxel.rect(x_table + 19, y_table + hauteur_table - 8, largeur_table // 2 - 29, 2, 0)
    pyxel.rect(x_table + largeur_table // 2 + 11, y_table + hauteur_table - 8, largeur_table // 2 - 29, 2, 0)
    
    # Lignes noires verticales d'épaisseur 2
    pyxel.rect(x_table + 7, y_table + 18, 2, hauteur_table - 36, 0)
    pyxel.rect(x_table + largeur_table - 8, y_table + 18, 2, hauteur_table - 36, 0)
    
    # Intersections entre les lignes noires (x2 pour plus d'épaisseur) et les côtés des trous
   
    pyxel.line(x_table + 18, y_table + 7, x_table + 11, y_table, 0)
    pyxel.line(x_table + 18, y_table + 8, x_table + 11, y_table + 1, 0)
    pyxel.line(x_table + 7, y_table + 18, x_table, y_table + 11, 0)
    pyxel.line(x_table + 8, y_table + 18, x_table + 1, y_table + 11, 0)
    
    pyxel.line(x_table + largeur_table - 18, y_table + 7, x_table + largeur_table - 11, y_table, 0)
    pyxel.line(x_table + largeur_table - 18, y_table + 8, x_table + largeur_table - 11, y_table + 1, 0)
    pyxel.line(x_table + largeur_table - 7, y_table + 18, x_table + largeur_table, y_table + 11, 0)
    pyxel.line(x_table + largeur_table - 8, y_table + 18, x_table + largeur_table - 1, y_table + 11, 0)
    
    pyxel.line(x_table + 18, y_table + hauteur_table - 7, x_table + 11, y_table + hauteur_table, 0)
    pyxel.line(x_table + 18, y_table + hauteur_table - 8, x_table + 11, y_table + hauteur_table - 1, 0) 
    pyxel.line(x_table + 7, y_table + hauteur_table - 18, x_table, y_table + hauteur_table - 11, 0)
    pyxel.line(x_table + 8, y_table + hauteur_table - 18, x_table + 1, y_table + hauteur_table - 11, 0)
    
    pyxel.line(x_table + largeur_table - 7, y_table + hauteur_table - 18, x_table + largeur_table, y_table + hauteur_table - 11, 0)
    pyxel.line(x_table + largeur_table - 8, y_table + hauteur_table - 18, x_table + largeur_table - 1, y_table + hauteur_table - 11, 0)
    pyxel.line(x_table + largeur_table - 18, y_table + hauteur_table - 7, x_table + largeur_table - 11, y_table + hauteur_table, 0)
    pyxel.line(x_table + largeur_table - 18, y_table + hauteur_table - 8, x_table + largeur_table - 11, y_table + hauteur_table - 1, 0)
    
    pyxel.line(x_table + largeur_table // 2 - 11, y_table + 7, x_table + largeur_table // 2 - 10, y_table, 0)
    pyxel.line(x_table + largeur_table // 2 + 11, y_table + 7, x_table + largeur_table // 2 + 10, y_table, 0)
    
    pyxel.line(x_table + largeur_table // 2 - 11, y_table + hauteur_table - 7, x_table + largeur_table // 2 -10, y_table + hauteur_table, 0)
    pyxel.line(x_table + largeur_table // 2 + 11, y_table + hauteur_table - 7, x_table + largeur_table // 2 + 10, y_table + hauteur_table, 0)

def queues() -> None:
    """ Fonction pour répresenter les queues graphiquement """
    global joueur_1, joueur_2
    
    if not joueur_1:
        pyxel.blt(x_table + 540, y_table + hauteur_table // 2, 0, 0, 70, 256, 4, 13, 270)
    
    if not joueur_2:
        pyxel.blt(x_table + 560, y_table + hauteur_table // 2, 0, 0, 70, 256, 4, 13, 270)
    
    
    
# ------------------------------------------------------------------------------------------------------------ #
# -----------------------------  Partie graphique de la représentaion des boules ----------------------------- # 
# ------------------------------------------------------------------------------------------------------------ #



def boules() -> None:
    """ Fonction pour représenter les boules graphiquement """
    global sprites_boules, balles
    
    # Boules de couleurs, pleines ou rayées allant de 1 à 15
        
    if balle1["dedans"] == False:
        pyxel.blt(balle1["pos"][0], balle1["pos"][1], 0, sprites_boules[0][0][0], sprites_boules[0][0][1], 16, 16, 13) 
    
    if balle2["dedans"] == False:
        pyxel.blt(balle2["pos"][0], balle2["pos"][1], 0, sprites_boules[1][0][0], sprites_boules[1][0][1], 16, 16, 13)
    if balle3["dedans"] == False:
        pyxel.blt(balle3["pos"][0], balle3["pos"][1], 0, sprites_boules[2][0][0], sprites_boules[2][0][1], 16, 16, 13)
     
    if balle4["dedans"] == False:
        pyxel.blt(balle4["pos"][0], balle4["pos"][1], 0, sprites_boules[3][0][0], sprites_boules[3][0][1], 16, 16, 13)
    if balle5["dedans"] == False:
        pyxel.blt(balle5["pos"][0], balle5["pos"][1], 0, sprites_boules[7][0][0], sprites_boules[7][0][1], 16, 16, 13)
    if balle6["dedans"] == False:
        pyxel.blt(balle6["pos"][0], balle6["pos"][1], 0, sprites_boules[5][0][0], sprites_boules[5][0][1], 16, 16, 13)
     
    if balle7["dedans"] == False:
        pyxel.blt(balle7["pos"][0], balle7["pos"][1], 0, sprites_boules[6][0][0], sprites_boules[6][0][1], 16, 16, 13)
    if balle8["dedans"] == False:
        pyxel.blt(balle8["pos"][0], balle8["pos"][1], 0, sprites_boules[4][0][0], sprites_boules[4][0][1], 16, 16, 13)
    if balle9["dedans"] == False:
        pyxel.blt(balle9["pos"][0], balle9["pos"][1], 0, sprites_boules[8][0][0], sprites_boules[8][0][1], 16, 16, 13)
    if balle10["dedans"] == False:
        pyxel.blt(balle10["pos"][0], balle10["pos"][1], 0, sprites_boules[9][0][0], sprites_boules[9][0][1], 16, 16, 13)
     
    if balle11["dedans"] == False:
        pyxel.blt(balle11["pos"][0], balle11["pos"][1], 0, sprites_boules[10][0][0], sprites_boules[10][0][1], 16, 16, 13)
    if balle12["dedans"] == False:
        pyxel.blt(balle12["pos"][0], balle12["pos"][1], 0, sprites_boules[11][0][0], sprites_boules[11][0][1], 16, 16, 13)
    if balle13["dedans"] == False:
        pyxel.blt(balle13["pos"][0], balle13["pos"][1], 0, sprites_boules[12][0][0], sprites_boules[12][0][1], 16, 16, 13)
    if balle14["dedans"] == False:
        pyxel.blt(balle14["pos"][0], balle14["pos"][1], 0, sprites_boules[13][0][0], sprites_boules[13][0][1], 16, 16, 13)
    if balle15["dedans"] == False:
        pyxel.blt(balle15["pos"][0], balle15["pos"][1], 0, sprites_boules[14][0][0], sprites_boules[14][0][1], 16, 16, 13)
     
    if balleb["dedans"] == False:
        pyxel.blt(balleb["pos"][0], balleb["pos"][1], 0, sprites_boules[15][0][0], sprites_boules[15][0][1], 16, 16, 13)


def règles_partie() -> None:
    """ Fais en sorte que les vraies règles du billard américain sont respéctées """
    global balles, joueur_1, joueur_2, action, Jeu_Fini, boules_in
    
    if balleb["dedans"] == True:
        balleb["pos"][0] = 200
        balleb["pos"][1] = 185
        balleb["vitesse"][0] = 0
        balleb["vitesse"][1] = 0
        balleb["dedans"] = False
    
    
    if joueur_1 and balle5["dedans"] == True:
        if balle1["dedans"] == False or balle2["dedans"] == False or balle3["dedans"] == False or balle4["dedans"] == False or balle5["dedans"] == False \
           or balle6["dedans"] == False or balle7["dedans"] == False or balle9["dedans"] == False or balle10["dedans"] == False or balle11["dedans"] == False \
           or balle12["dedans"] == False or balle13["dedans"] == False or balle14["dedans"] == False or balle15["dedans"] == False:
            
            print("Perdu joueur_1, la balle noire est rentrée avant la fin de notre partie")
            Jeu_Fini = True
        
    if joueur_2 and balle5["dedans"] == True:
        if balle1["dedans"] == False or balle2["dedans"] == False or balle3["dedans"] == False or balle4["dedans"] == False or balle5["dedans"] == False \
           or balle6["dedans"] == False or balle7["dedans"] == False or balle9["dedans"] == False or balle10["dedans"] == False or balle11["dedans"] == False \
           or balle12["dedans"] == False or balle13["dedans"] == False or balle14["dedans"] == False or balle15["dedans"] == False:
        
            print("Perdu joueur_2, la balle noire est rentrée avant la fin de notre partie")
            Jeu_Fini = True


def comptage_boules() -> None:
    """ Fonction qui permet de savoir quelles boules sont entrées grâçe à qui """
    global boules_in_j1, boules_in_j2, balles, joueur_1, joueur_2
    
    for balle in balles:
        if balle["dedans"] == True and not balle.get("déja_comptee", False):
            if joueur_1:
                boules_in_j1.append(balle["couleur"])
            if joueur_2:
                boules_in_j2.append(balle["couleur"])  
            balle["déja_comptee"] = True
    print(boules_in_j1, boules_in_j2)

def menu_jeu() -> None:
    """ Fonction des interfaces pendant le jeu """
    global couleur_fond, joueur_1, joueur_2, en_parametre
    
    pyxel.cls(couleur_fond)
    règles_partie()
    if not en_parametre:
        billard()
    if joueur_1 and not en_parametre:
        interface_joueur1()
    if joueur_2 and not en_parametre:
        interface_joueur2()
    dedans()
    
def interface_joueur1() -> None:
    """ Fonction qui permet au joueur1 d'interagir avec l'écran pour pouvoir jouer au billard """
    global balles, secondes, action, joueur_1, joueur_2, coup_jouer_j1, coup_fait_j1
        
    if action == 0:
        pyxel.text(100, 400, "Votre tour, appuyez sur la boule blanche", 0)
        
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and (balleb["pos"][0] < pyxel.mouse_x < balleb["pos"][0] + 16) and \
    (balleb["pos"][1] < pyxel.mouse_y < balleb["pos"][1] + 16):
        action = 1
        secondes = 0  
    
    if action == 1:
        angle_j1()
        
    if action == 2:
        cpt_time()
        if secondes > 1:
            jauge_j1()
        
    if action == 3:
        cpt_time()
        if secondes > 3:  
            animation_queue()
            if not coup_fait_j1:
                coup_j1(balleb, coup_jouer_j1)
                coup_fait_j1 = True
                resultat()
            
    if action == 4:
        secondes = 0
        coup_fait_j1 = False  
        joueur_1 = False
        joueur_2 = True
        action = 0
        

def interface_joueur2() -> None:
    """ Fonction qui permet au joueur2 d'interagir avec l'écran pour pouvoir jouer au billard """
    global balles, secondes, action, joueur_1, joueur_2, coup_jouer_j2, coup_fait_j2
    
    if action == 0:
        pyxel.text(500, 400, "Votre tour, appuyez sur la boule blanche :", 0)
        
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and (balleb["pos"][0] < pyxel.mouse_x < balleb["pos"][0] + 16) and \
    (balleb["pos"][1] < pyxel.mouse_y < balleb["pos"][1] + 16):
        action = 1
        secondes = 0 
    
    if action == 1:
        angle_j2()
        
    if action == 2:
        cpt_time()
        if secondes > 1:
            jauge_j2()
        
    if action == 3:
        cpt_time()
        if secondes > 3:  
            animation_queue()
            if not coup_fait_j2:
                coup_j2(balleb, coup_jouer_j2)
                coup_fait_j2 = True
                resultat()
            
    if action == 4:
        secondes = 0
        coup_fait_j2 = False
        joueur_1 = True
        joueur_2 = False
        action = 0
    
    
def angle_to_vecteur(angle) -> list:
    """ Convertit l'angle en vecteur """
    
    anglerad = math.radians(angle)
    
    x = math.cos(anglerad)
    y = math.sin(anglerad)
    
    return [x, y]


def angle_j1() -> None:
    """ Représentation graphique pour choisir l'angle du tir """
    global action, angle_tir, coup_jouer_j1
        
    pyxel.text(25, 410, "Cliquez autour de la boule pour choisir l'angle de tir", 0)
    pyxel.blt(200, 470, 0, 240, 0, 16, 16, 13, 0, 5)
    
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 430 < pyxel.mouse_y < 510 and 160 < pyxel.mouse_x < 240:
        
        centre_x = 208  
        centre_y = 478  

        distance_x = pyxel.mouse_x - centre_x
        distance_y = pyxel.mouse_y - centre_y
        
        angle_tir = (math.degrees(math.atan2(distance_y, distance_x)) + 180) % 360
        
        coup_jouer_j1["direction"] = angle_to_vecteur(angle_tir)
            
        action = 2
                
def angle_j2() -> None:  
    """ Représentation graphique pour choisir l'angle du tir """
    global action, angle_tir, coup_jouer_j2

    pyxel.text(430, 410, "Cliquez autour de la boule pour choisir l'angle de tir", 0)
    pyxel.blt(515, 470, 0, 240, 0, 16, 16, 13, 0, 5)
    
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and 430 < pyxel.mouse_y < 510 and 480 < pyxel.mouse_x < 560:
        
        centre_x = 523 
        centre_y = 478  
        
        distance_x = pyxel.mouse_x - centre_x
        distance_y = pyxel.mouse_y - centre_y
        
        angle_tir = (math.degrees(math.atan2(distance_y, distance_x)) + 180) % 360
        
        coup_jouer_j2["direction"] = angle_to_vecteur(angle_tir)
        
        action = 2
    
def jauge_j1() -> None:
    """ Représentation graphique pour choisir la force du tir """
    global action, coup_jouer_j1
    
    pyxel.trib(100, 500, 375, 500, 375, 449, 0)
    pyxel.tri(100, 499, 192, 499, 192, 483, 11)
    pyxel.tri(192, 499, 283, 499, 283, 466, 9)
    pyxel.tri(192, 499, 192, 483, 283, 466, 9)
    pyxel.tri(283, 499, 374, 499, 374, 450, 8)
    pyxel.tri(283, 499, 283, 466, 374, 450, 8)
    
    pyxel.text(95, 505, "0", 0)
    pyxel.text(187, 505, "20", 0)
    pyxel.text(278, 505, "40", 0)
    pyxel.text(369, 505, "60", 0)
    
    pyxel.text(100, 430, "Maintenant, choisissez la puissance qui va de 1 a 60", 0)
    
    for i in range(59):
        pyxel.line(100 + i * 4.75, 500, 100 + i * 4.75, 497, 0)
    
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 100 + i * 4.75 < pyxel.mouse_x < 100 + (i + 1) * 4.75 and 440 < pyxel.mouse_y < 510:
                coup_jouer_j1["force"] = i
                
                action = 3
                
        
def jauge_j2() -> None:
    """ Représentation graphique pour choisir la force du tir """
    global action, coup_jouer_j2
    
    pyxel.trib(420, 500, 695, 500, 420, 449, 0)
    pyxel.tri(695, 499, 603, 499, 603, 483, 11)
    pyxel.tri(603, 499, 511, 499, 511, 466, 9)
    pyxel.tri(603, 499, 603, 483, 511, 466, 9)
    pyxel.tri(511, 499, 421, 499, 421, 450, 8)
    pyxel.tri(511, 499, 511, 467, 421, 450, 8)
    
    pyxel.text(691, 505, "0", 0)
    pyxel.text(599, 505, "20", 0)
    pyxel.text(507, 505, "40", 0)
    pyxel.text(417, 505, "60", 0)
    
    pyxel.text(400, 430, "Maintenant, choisissez la puissance qui va de 1 a 60", 0)
    
    for i in range(59):
        pyxel.line(695 - i * 4.75, 500, 695 - i * 4.75, 497, 0)
        
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and 695 - ( i + 1) * 4.75 < pyxel.mouse_x < 695 - i * 4.75 and 440 < pyxel.mouse_y < 510:
            coup_jouer_j2["force"] = i
            
            action = 3



def animation_queue() -> None:
    """ Fonction qui fait l'animation de la queue de billard """
    global balles, action, balleb, long_queue, angle_tir
    
    centre_x = balleb["pos"][0] + 8  
    centre_y = balleb["pos"][1] + 8
    
    angle_rad = math.radians(angle_tir)
    
    queue_x = centre_x - math.cos(angle_rad) * long_queue
    queue_y = centre_y - math.sin(angle_rad) * long_queue
    
    pyxel.blt(queue_x, queue_y, 0, 0, 70, 256, 4, 13, angle_tir)
    
def resultat() -> None:
    """ Fontion permettant de constater si les balles ne bougent plus et qu'on peut passer au prochain coup. """
    global balles, action, coup_jouer_j1, coup_jouer_j2
    
    for balle in balles:
        if not balle["vitesse"][0] == 0 and balle["vitesse"][1] == 0:
            action = 3
            
        action = 4
        

def cpt_time() -> None:
    """ Fonction qui va servir à délimiter le temps de chaque action """
    global secondes
    
    if pyxel.frame_count % 60 == 0:
        secondes += 1
        
    return secondes


def dedans() -> None:
    """ Fonction qui détermine si les boules sont rentrées dans les trous """
    global balles
    
    for balle in balles:
        if x_table < balle["pos"][0] < x_table + 25 and y_table < balle["pos"][1] < y_table + 25 \
           or x_table + largeur_table - 25 < balle["pos"][0] + 8 < x_table + largeur_table and y_table < balle["pos"][1] + 8 < y_table + 25 \
           or x_table < balle["pos"][1] < x_table + 25 and y_table + hauteur_table - 25 < balle["pos"][1] + 16 < y_table + hauteur_table \
           or x_table + largeur_table - 25 < balle["pos"][0] < x_table + largeur_table and y_table + hauteur_table - 25 < balle["pos"][0] < y_table + hauteur_table \
           or x_table + largeur_table // 2 - 12 < balle["pos"][0] < x_table + largeur_table // 2 + 12 and y_table + 20 < balle["pos"][0] < y_table \
           or x_table + largeur_table // 2 - 12 < balle["pos"][0] + 8 < x_table + largeur_table // 2 + 12 and y_table + hauteur_table - 20 < balle["pos"][0] + 8 < y_table + hauteur_table:
            balle["dedans"] = True
            
            
def condition_fin() -> bool:
    """ Fonction qui vérifie si la partie est terminée """
    
    global balles, Jeu_Fini
    
    for balle in balles:
        if balle["dedans"] == False:
            return Jeu_Fini
        Jeu_Fini = True
        
    return Jeu_Fini


def update() -> None:
    """ Fonction principale pour appeler toutes les fonctions qui à chaque frame update l'état actuel du jeu """
    parametres()
    physique()
    menu_initial()
    menu_jeu()
    menu_fin()
    
def draw() -> None:
    """ Fonction principale pour appeler toutes les fonctions qui à chaque frame update l'état graphique du jeu """
    global joueur_1, joueur_2
    
    if not peut_commencer_partie:
        menu_initial()
        parametres()
        
    if peut_commencer_partie:
        menu_jeu()
        parametres()
        
    if Jeu_Fini:
        menu_fin()
        parametres()
        
début(), pyxel.run(update, draw)
