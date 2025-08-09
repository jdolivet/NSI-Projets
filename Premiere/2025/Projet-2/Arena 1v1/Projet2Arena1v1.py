# Version Finale

import pyxel
import random

def init():
    pyxel.init(380, 180, "Arena 1v1", fps = 60, quit_key = pyxel.KEY_Q)
    pyxel.load("2.pyxres")
    pyxel.playm(0, loop = True)


def cpt_frame():
    global cpt
    if pyxel.frame_count % 1 == 0:
        cpt += 1
    if cpt > 30:
        cpt = 0

cpt = 0
accelerationg = 0.5
forcesaut = -7
dsaut = False
nbsaut = 0
fin = False
dir_ninja = 1
dir_skel = 1

x_min_ninja = -1000
x_max_ninja = x_min_ninja + 14
y_min_ninja = -1000
y_min_ninja = y_min_ninja + 14
vy_ninja = 0

x_min_skel = -1100
x_max_skel = x_min_skel + 14
y_min_skel = -1100
y_max_skel = y_min_skel + 14
vy_skel = 0

imgx_skel = 64
imgy_skel = 16
imgX_skel = 15
imgY_skel = 16

imgx_ninja = 0
imgy_ninja = 16
imgX_ninja = 15
imgY_ninja = 16

liste_y = [40, 50, 60, 70]
liste_x = [0, 15, 30, 45, 60]
liste_image_x = [16, 32, 96]
liste_image_y = [0, 32, 96]

col0 = 0
col1 = 0
col2 = 0
col3 = 0
effacer_texte = 0

ninja_vies = 3
skel_vies = 3
projectiles = []
touche_sol = False

def gravite():

    """fourni que le personnage n'est pas sur un support -- attribue une vitesse verticale
        vers le bas constante chaque frame au personnage:
        Autrement dit, instaure une gravite au jeu qui affecte les personnages"""

    global vy_ninja, y_min_ninja, block_spawn_ninja
    global vy_skel, y_min_skel, block_spawn_skel

    if block_spawn_ninja == 1:
        if not colisions_objets_ninja() or pyxel.btn(pyxel.KEY_W):
            vy_ninja += accelerationg
            vy_ninja = min(vy_ninja, 10)
            y_min_ninja += vy_ninja
        else:
            vy_ninja = 0

    if block_spawn_skel == 1:
        if not colisions_objets_skel() or pyxel.btn(pyxel.KEY_UP):
            vy_skel += accelerationg
            vy_skel = min(vy_skel, 10)
            y_min_skel += vy_skel
        else:
            vy_skel = 0

# pour empêcher de pouvoir refaire spawn les personnages en papuyant sur 1, 2, 3 après qu'ils soient apparus.nb_personnes = (int(input())
block_spawn_ninja = 0
block_spawn_skel = 0

# Génération map
liste_y = [148, 132, 116, 100, 84, 68, 52]
liste_x = [0, 16, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 336, 352]
liste_image_x = [0, 16, 32]
liste_image_y = [32, 96]

objet1 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet2 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet3 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet4 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet5 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet6 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet7 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet8 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet9 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet10 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet11 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet12 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet13 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet14 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet15 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet16 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet17 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet18 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet19 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet20 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet21 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]
objet22 = [random.choice(liste_x), random.choice(liste_y), random.choice(liste_image_x), random.choice(liste_image_y)]


objets = [objet1, objet2, objet3, objet4, objet5, objet6, objet7, objet8, objet9, objet10,
          objet11, objet12, objet13, objet14, objet15, objet16, objet17, objet18, objet19, objet20,
          objet21, objet22]

def carte():
    global fin

    if fin == False:
        pyxel.blt(objet1[0], objet1[1], 0, objet1[2], objet1[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet2[0], objet2[1], 0, objet2[2], objet2[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet3[0], objet3[1], 0, objet3[2], objet3[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet4[0], objet4[1], 0, objet4[2], objet4[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet5[0], objet5[1], 0, objet5[2], objet5[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet6[0], objet6[1], 0, objet6[2], objet6[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet7[0], objet7[1], 0, objet7[2], objet7[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet8[0], objet8[1], 0, objet8[2], objet8[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet9[0], objet9[1], 0, objet9[2], objet9[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet10[0], objet10[1], 0, objet10[2], objet10[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet11[0], objet11[1], 0, objet11[2], objet11[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet12[0], objet12[1], 0, objet12[2], objet12[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet13[0], objet13[1], 0, objet13[2], objet13[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet14[0], objet14[1], 0, objet14[2], objet14[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet15[0], objet15[1], 0, objet15[2], objet15[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet16[0], objet16[1], 0, objet16[2], objet16[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet17[0], objet17[1], 0, objet17[2], objet17[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet18[0], objet18[1], 0, objet18[2], objet18[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet19[0], objet19[1], 0, objet19[2], objet19[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet20[0], objet20[1], 0, objet20[2], objet20[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet21[0], objet21[1], 0, objet21[2], objet21[3], 16, 16, 2, 0, 1)
        pyxel.blt(objet22[0], objet22[1], 0, objet22[2], objet22[3], 16, 16, 2, 0, 1)

def collision_proj_obj(x, y):
    global projectiles
    global objets
    for i in range(len(objets)):
       obj = objets[i]
       if obj[0] <= x <= obj[0] + 16 and obj[1] <= y <= obj[1] + 16:
          return True
       if y >= 160:
          return True
    return False

def collision_proj_skel(x, y):
    global projectiles
    global x_min_skel, y_min_skel
    if x_min_skel <= x <= x_min_skel + 16 and y_min_skel <= y <= y_min_skel + 16:
        return True
    return False

def collision_proj_ninja(x, y):
    global projectiles
    global x_min_ninja, y_min_ninja
    if x_min_ninja <= x <= x_min_ninja + 16 and y_min_ninja <= y <= y_min_ninja + 16:
        return True
    return False

def tirer_projectiles(x, y, direction, vitesse, perso, grav):
                global vy_ninja, vy_skel
                global projectiles
                vx = vitesse * direction
                if perso == "ninja":
                  vy = vy_ninja/2
                  bounce = 1
                if perso == "skel":
                  vy = vy_skel/2
                  bounce = 0
                projectiles.append([x, y, vx, vy, grav, 1, perso, bounce])

def update_collisions():
    global projectiles
    global ninja_vies
    global skel_vies

    for i in range(len(projectiles)):
        proj = projectiles[i]
        if proj[5] == 0:
            continue

        x = proj[0]
        y = proj[1]

        if collision_proj_obj(x, y):
            if proj[7] == 0:
                proj[2] = -proj[2]
                proj[3] = -proj[3]
                proj[7] += 1
            else:
                projectiles[i][5] = 0
            pyxel.play(2, 9)
            continue

        if collision_proj_skel(x, y) and projectiles[i][6] != "skel":
            projectiles[i][5] = 0
            if  projectiles[i][6] != "skel":
                skel_vies -= 1
            continue

        if collision_proj_ninja(x, y) and projectiles[i][6] != "ninja":
            projectiles[i][5] = 0
            if projectiles [i][6] != "ninja":
                ninja_vies -= 1
            continue

    projectiles = [p for p in projectiles if p[5] == 1]


def update_projectiles():

    for proj in projectiles:
        if proj[5] == 1:
            proj[3] += proj[4]
            proj[0] += proj[2]
            proj[1] += proj[3]

def dessiner_projectiles():
    global projectiles
    for proj in projectiles:
        if proj[5] == 1:
            pyxel.blt(int(proj[0]), int(proj[1]), 0, 53, 100, 6, 6, 2)

# Faire en sorte de générer au moins 6 objets sur le sol
cpt_bloc_sol = 0

for i in range(6):

    for i in range(len(objets)):
        if objets[i][3] == 32:
            cpt_bloc_sol += 1

        if cpt_bloc_sol < 6:
            for i in range(len(objets)):
                if objets[i][3] == 32:
                    objets[i][1] = 148

def texte_début():
    pyxel.text(150, 5, "Deux personnages au choix : ", col0)
    pyxel.text(23, 20, "Click sur 1 pour le squelette, il se joue avec les fleches et attaque !", col1)
    pyxel.text(23, 30, "Click sur 2 pour le ninja, il se joue en WASD et attaque avec la touche E", col2)
    pyxel.rect(0, 164, 380, 16, 5)

def choisir_persos():
    global x_min_skel, x_max_skel, y_min_skel, y_max_skel, x_min_ninja, x_max_ninja, y_min_ninja, y_min_ninja
    global col0, col1, col2
    global effacer_texte
    global block_spawn_ninja, block_spawn_skel

    if effacer_texte < 2:
        if pyxel.btnr(pyxel.KEY_1) and block_spawn_skel != 1:
            x_min_skel = 320
            x_max_skel = 333
            y_min_skel = 148
            y_max_skel = 163
            col1 = 7
            effacer_texte += 1
            block_spawn_skel = 1

        if pyxel.btnr(pyxel.KEY_2) and block_spawn_ninja != 1:
            x_min_ninja = 31
            x_max_ninja = 44
            y_min_ninja = 152
            y_max_ninja = 163
            col2 = 7
            effacer_texte += 1
            block_spawn_ninja = 1

    else:
        col0 = 7
        col1 = 7
        col2 = 7

def affichage_vies():
    global x_min_skel, y_min_skel
    global x_min_ninja, y_min_ninja
    global ninja_vies, skel_vies

    pyxel.trib(5, 178, 110, 178, 110, 165, 0)
    pyxel.text(12, 166, "Vies Ninja", 0)
    pyxel.trib(375, 178, 270, 178, 270, 165, 0)
    pyxel.text(336, 166, "Vies Skel", 0)

    if ninja_vies == 3:
        pyxel.tri(5, 177, 109, 177, 109, 166, 11)
    if ninja_vies == 2:
        pyxel.tri(5, 177, 74, 177, 74, 169, 10)
    if ninja_vies == 1:
        pyxel.tri(5, 177, 38, 177, 38, 173, 8)

    if skel_vies == 3:
        pyxel.tri(375, 177, 271, 177, 271, 166, 11)
    if skel_vies == 2:
        pyxel.tri(375, 177, 306, 177, 306, 169, 10)
    if skel_vies == 1:
        pyxel.tri(375, 177, 341, 177, 341, 173, 8)

def interface_fin():
    global ninja_vies, skel_vies
    global fin

    if ninja_vies == 0:
        pyxel.rect(0, 0, 380, 180, 7)
        fin = True
        pyxel.text(160, 30, "SKELETON WINS !", 0)
        pyxel.text(250, 100, "Click on Q to quit the game", 0)
        if pyxel.frame_count % 15 == 0:
            pyxel.text(250, 130, "EZ WIN", 8)
            pyxel.text(10, 80, " I am the KING of skeleton ", 8)
            pyxel.text(70, 20, "Squelette is the best", 8)
        pyxel.blt(140, 90, 0, imgx_skel, imgy_skel, imgX_skel, imgY_skel, 2, 0, 5)

    if skel_vies == 0:
        pyxel.rect(0, 0, 380, 180, 7)
        fin = True
        pyxel.text(165, 30, "NINJA WINS !", 0)
        pyxel.text(250, 100, "Click on Q to quit the game", 0)
        if pyxel.frame_count % 15 == 0:
            pyxel.text(250, 130, "EZ WIN", 8)
            pyxel.text(30, 80, " I am the G.N.A.T ", 8)
            pyxel.text(70, 20, "Ninja is the best brotha", 8)
        pyxel.blt(140, 90, 0, imgx_ninja, imgy_ninja, imgX_ninja, imgY_ninja, 2, 0, 5)

def colisions_bord_et_sol():
    global x_min_skel, x_min_ninja, y_min_skel, y_min_ninja

    if x_min_skel > 366:
        x_min_skel -= 1
    if x_min_ninja > 366:
        x_min_ninja -= 1
    if x_min_ninja < 0:
        x_min_ninja += 1
    if x_min_skel < 0:
        x_min_skel += 1


    if y_min_skel >= 148:
        y_min_skel = 148

    if y_min_ninja >= 148:
        y_min_ninja = 148

def double_saut():
    global dsaut
    global nbsaut


    if colisions_objets_ninja() == False:
        if bouger_ninja() == "saut":
            nbsaut = 0
    if colisions_objets_ninja() == True:
        nbsaut = 1

    if nbsaut ==1:
        dsaut = True
    if nbsaut == 0:
        dsaut = False


def colisions_objets_ninja():
    global x_min_ninja, x_max_ninja, y_min_ninja, y_max_ninja
    global touche_sol
    global objets

    touche_sol = False

    if 147 <= y_min_ninja <= 149:
        touche_sol = True

    if y_min_ninja + 14 == 162:
        touche_sol = True

    for i in range(len(objets)):
        if objets[i][0] <= x_min_ninja <= objets[i][0] + 15 and objets[i][1] <= y_min_ninja <= objets[i][1] + 1:
            x_min_ninja += 1
        if objets[i][0] <= x_min_ninja + 14 <= objets[i][0] + 15 and objets[i][1] <= y_min_ninja <= objets[i][1] + 1:
            x_min_ninja -= 1
        if objets[i][1] <= y_min_ninja <= objets[i][1] + 16 and objets[i][0] - 11 <= x_min_ninja <= objets[i][0] + 22:
            y_min_ninja += 1
        if objets[i][1] <= y_min_ninja + 14 <= objets[i][1] + 16 and objets[i][0] - 11 <= x_min_ninja <= objets[i][0] + 22:
            y_min_ninja -= 1
            touche_sol = True

    return touche_sol

def colisions_objets_skel():
    global x_min_skel, x_max_skel, y_min_skel, y_max_skel
    global touche_sol
    global objets

    touche_sol = False

    if 147 <= y_min_skel <= 149:
        touche_sol = True

    if y_min_skel + 14 == 162:
        touche_sol = True

    for i in range(len(objets)):
        if objets[i][0] <= x_min_skel <= objets[i][0] + 15 and objets[i][1] <= y_min_skel <= objets[i][1] + 1:
            x_min_skel += 1
        if objets[i][0] <= x_min_skel + 14 <= objets[i][0] + 15 and objets[i][1] <= y_min_skel <= objets[i][1] + 1:
            x_min_skel -= 1
        if objets[i][1] <= y_min_skel <= objets[i][1] + 16 and objets[i][0] - 16 <= x_min_skel <= objets[i][0] + 16:
            y_min_skel += 1
        if objets[i][1] <= y_min_skel + 14 <= objets[i][1] + 16 and objets[i][0] - 16 <= x_min_skel <= objets[i][0] + 16:
            y_min_skel -= 1
            touche_sol = True

    return touche_sol

def bouger_ninja():
    global y_min_ninja, y_max_ninja, x_max_ninja, x_min_ninja
    global imgx_ninja, imgy_ninja, imgX_ninja, imgY_ninja
    global cpt
    global vy_ninja
    global fin
    global dir_ninja

    if pyxel.btn(pyxel.KEY_A):
         x_min_ninja -= 1
         x_max_ninja -= 1
         dir_ninja = -1

         if cpt == 0:
             imgx_ninja = 0
             imgy_ninja = 16
             imgX_ninja = -15
             imgY_ninja = 16
         if cpt == 7:
             imgx_ninja = 16
             imgy_ninja = 16
             imgX_ninja = -15
             imgY_ninja = 16
         if cpt == 14:
             imgx_ninja = 32
             imgy_ninja = 16
             imgX_ninja = -15
             imgY_ninja = 16
         if cpt == 22:
             imgx_ninja = 48
             imgy_ninja = 16
             imgX_ninja = -15
             imgY_ninja = 16

    if pyxel.btn(pyxel.KEY_D):
         x_min_ninja += 1
         x_max_ninja += 1
         dir_ninja = 1

         if cpt == 0:
             imgx_ninja = 0
             imgy_ninja = 16
             imgX_ninja = 15
             imgY_ninja = 16
         if cpt == 7:
             imgx_ninja = 16
             imgy_ninja = 16
             imgX_ninja = 15
             imgY_ninja = 16
         if cpt == 14:
             imgx_ninja = 32
             imgy_ninja = 16
             imgX_ninja = 15
             imgY_ninja = 16
         if cpt == 22:
             imgx_ninja = 48
             imgy_ninja = 16
             imgX_ninja = 15
             imgY_ninja = 16

    if pyxel.btnp(pyxel.KEY_W) and ((colisions_objets_ninja() == True) or dsaut == True):
        pyxel.play(2, 20)
        vy_ninja = forcesaut
        return "saut"

    if fin == False:
        if pyxel.btnp(pyxel.KEY_SPACE) and (pyxel.btn(pyxel.KEY_D) or dir_ninja == 1):
            tirer_projectiles(x_min_ninja, y_min_ninja, 1, 4, "ninja", 0.003)
            pyxel.play(2, 6)

        if pyxel.btnp(pyxel.KEY_SPACE) and (pyxel.btn(pyxel.KEY_A) or dir_ninja == -1):
            tirer_projectiles(x_min_ninja, y_min_ninja, -1, 4, "ninja", 0.003)
            pyxel.play(2, 6)

def bouger_skel():
    global x_min_skel, x_max_skel, y_min_skel, y_max_skel
    global imgx_skel, imgy_skel, imgX_skel, imgY_skel
    global cpt
    global vy_skel
    global fin
    global dir_skel

    if pyxel.btn(pyxel.KEY_LEFT):
         x_min_skel -= 1
         x_max_skel -= 1
         dir_skel = -1

         if cpt == 0:
             imgx_skel = 64
             imgy_skel = 16
             imgX_skel = 15
             imgY_skel = 16
         if cpt == 7:
             imgx_skel = 80
             imgy_skel = 16
             imgX_skel = 15
             imgY_skel = 16
         if cpt == 14:
             imgx_skel = 96
             imgy_skel = 16
             imgX_skel = 15
             imgY_skel = 16
         if cpt == 22:
             imgx_skel = 112
             imgy_skel = 16
             imgX_skel = 15
             imgY_skel = 16

    if pyxel.btn(pyxel.KEY_RIGHT):
         x_min_skel += 1
         x_max_skel += 1
         dir_skel = 1

         if cpt == 0:
             imgx_skel = 64
             imgy_skel = 16
             imgX_skel = -15
             imgY_skel = 16
         if cpt == 7:
             imgx_skel = 80
             imgy_skel = 16
             imgX_skel = -15
             imgY_skel = 16
         if cpt == 14:
             imgx_skel = 96
             imgy_skel = 16
             imgX_skel = -15
             imgY_skel = 16
         if cpt == 22:
             imgx_skel= 112
             imgy_skel = 16
             imgX_skel = -15
             imgY_skel = 16

    if pyxel.btnp(pyxel.KEY_UP) and colisions_objets_skel() == True:
        vy_skel = forcesaut
        pyxel.play(2, 20)

    if fin == False:
        if pyxel.btnp(pyxel.KEY_DOWN) and (pyxel.btn(pyxel.KEY_RIGHT) or dir_skel == 1):
            tirer_projectiles(x_min_skel, y_min_skel, 1, 4, "skel", 0.003 )
            pyxel.play(2, 6)

        if pyxel.btnp(pyxel.KEY_DOWN) and (pyxel.btn(pyxel.KEY_LEFT) or dir_skel == -1):
            tirer_projectiles(x_min_skel, y_min_skel, -1, 4, "skel", 0.003)
            pyxel.play(2, 6)

def update():
    colisions_objets_ninja()
    colisions_objets_skel()
    colisions_bord_et_sol()
    gravite()
    collision_proj_obj
    collision_proj_skel
    collision_proj_ninja
    update_projectiles()
    update_collisions()
    double_saut()
    bouger_ninja()
    bouger_skel()
    cpt_frame()
    choisir_persos()

def draw():
    global x_min_skel, x_max_skel, y_min_skel, y_max_skel, x_min_ninja, x_max_ninja, y_min_ninja
    global fin

    pyxel.cls(7)
    texte_début()
    affichage_vies()
    dessiner_projectiles()
    interface_fin()

    if fin == False:
        if x_min_ninja >= 0 and y_min_ninja >= 0:
            pyxel.blt(x_min_ninja, y_min_ninja, 0, imgx_ninja, imgy_ninja, imgX_ninja, imgY_ninja, 2, 0, 1) # Ninja
        if x_min_skel >= 0 and y_min_skel >= 0:
            pyxel.blt(x_min_skel, y_min_skel, 0, imgx_skel, imgy_skel, -imgX_skel, imgY_skel, 2, 0, 1) # Skeleton

#   Map d'objets aléatorires
    carte()

init()
pyxel.run(update, draw)