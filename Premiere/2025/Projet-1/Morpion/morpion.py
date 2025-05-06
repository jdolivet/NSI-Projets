import pyxel

#  Création de fenêtre

pyxel.init(300, 300, title="Jeu du Morpion")
pyxel.mouse(True)

# Initialisation des variables
croixcommence = 1
rondcommence = 0
ligne1 = [0, 0, 0 ]
ligne2 = [0, 0, 0 ]
ligne3 = [0, 0, 0 ]
matrix = [ligne1, ligne2, ligne3]
clickmatrix = {"c1": 0, "c2": 0, "c3": 0, "c4": 0, "c5": 0, "c6": 0, "c7": 0, "c8": 0, "c9": 0}



# Variables pour régler les couleurs du texte ou bien simplement régler des problèmes pour améliorer la jouabilité (fin, bloc_col1, pas_jouer_au_début, pas_jouer_dans_même_case)

tour = 0

coul_grille = 7
coul_texte = 7
coul_texte1 = 0
coul_texte2 = 2
coul_soulignement = 0
coul_violet2 = 7

fin = 0
bloc_col1 = 0
bloc_croixourond = 0
bloc_grille = 0
pas_jouer_au_début = 0
pas_jouer_dans_même_case = {"case1" : 0, "case2" : 0, "case3" : 0, "case4" : 0, "case5" : 0, "case6" : 0, "case7" : 0, "case8" : 0, "case9" : 0 }


# Limites des cases

case_1 = {"x" : 100,"y" : 100}
case_2 = {"x" : 200,"y" : 100}
case_3 = {"x" : 300,"y" : 100}
case_4 = {"x" : 100,"y" : 200}
case_5 = {"x" : 200,"y" : 200}
case_6 = {"x" : 300,"y" : 200}
case_7 = {"x" : 100,"y" : 300}
case_8 = {"x" : 200,"y" : 300}
case_9 = {"x" : 300,"y" : 300}


# Coordonnées des ronds ( leur x et y sur l'écran )

cor_R1 = {"x" : -50, "y" : -50}
cor_R2 = {"x" : -50, "y" : -50}
cor_R3 = {"x" : -50, "y" : -50}
cor_R4 = {"x" : -50, "y" : -50}
cor_R5 = {"x" : -50, "y" : -50}
cor_R6 = {"x" : -50, "y" : -50}
cor_R7 = {"x" : -50, "y" : -50}
cor_R8 = {"x" : -50, "y" : -50}
cor_R9 = {"x" : -50, "y" : -50}


# Coordonnées des croix ( leur x et y sur l'écran ). Il en faut 8 pour faire deux lignes qui ont besoin de 4 arguments (x1, y1, x2, y2)

cor_C1 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}
cor_C2 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}
cor_C3 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}
cor_C4 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}
cor_C5 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}
cor_C6 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}
cor_C7 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}
cor_C8 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}
cor_C9 = {"x1" : -100, "y1" : -100, "x2" : -100, "y2" : -100, "x3" : -100, "y3" : -100, "x4" : -100, "y4" : -100}


# Définition de chaque rond

def rond1(cor_R1):
    pyxel.circb(cor_R1['x'], cor_R1['y'], 44, 11)

def rond2(cor_R2):
    pyxel.circb(cor_R2['x'], cor_R2['y'], 44, 11)

def rond3(cor_R3):
    pyxel.circb(cor_R3['x'], cor_R3['y'], 44, 11)

def rond4(cor_R4):
    pyxel.circb(cor_R4['x'], cor_R4['y'], 44, 11)

def rond5(cor_R5):
    pyxel.circb(cor_R5['x'], cor_R5['y'], 44, 11)

def rond6(cor_R6):
    pyxel.circb(cor_R6['x'], cor_R6['y'], 44, 11)

def rond7(cor_R7):
    pyxel.circb(cor_R7['x'], cor_R7['y'], 44, 11)

def rond8(cor_R8):
    pyxel.circb(cor_R8['x'], cor_R8['y'], 44, 11)

def rond9(cor_R9):
    pyxel.circb(cor_R9['x'], cor_R9['y'], 44, 11)


# Définition des 8 coordonnées nécessaires pour faire une croix à partir des coordonnées de chacune stockées au-dessus et de leur couleur (rouge).


def croix1(cor_C1):
    pyxel.line(cor_C1['x1'], cor_C1['y1'], cor_C1['x2'], cor_C1['y2'], 8)
    pyxel.line(cor_C1['x3'], cor_C1['y3'], cor_C1['x4'], cor_C1['y4'], 8)

def croix2(cor_C2):
    pyxel.line(cor_C2['x1'], cor_C2['y1'], cor_C2['x2'], cor_C2['y2'], 8)
    pyxel.line(cor_C2['x3'], cor_C2['y3'], cor_C2['x4'], cor_C2['y4'], 8)

def croix3(cor_C3):
    pyxel.line(cor_C3['x1'], cor_C3['y1'], cor_C3['x2'], cor_C3['y2'], 8)
    pyxel.line(cor_C3['x3'], cor_C3['y3'], cor_C3['x4'], cor_C3['y4'], 8)

def croix4(cor_C4):
    pyxel.line(cor_C4['x1'], cor_C4['y1'], cor_C4['x2'], cor_C4['y2'], 8)
    pyxel.line(cor_C4['x3'], cor_C4['y3'], cor_C4['x4'], cor_C4['y4'], 8)

def croix5(cor_C5):
    pyxel.line(cor_C5['x1'], cor_C5['y1'], cor_C5['x2'], cor_C5['y2'], 8)
    pyxel.line(cor_C5['x3'], cor_C5['y3'], cor_C5['x4'], cor_C5['y4'], 8)

def croix6(cor_C6):
    pyxel.line(cor_C6['x1'], cor_C6['y1'], cor_C6['x2'], cor_C6['y2'], 8)
    pyxel.line(cor_C6['x3'], cor_C6['y3'], cor_C6['x4'], cor_C6['y4'], 8)

def croix7(cor_C7):
    pyxel.line(cor_C7['x1'], cor_C7['y1'], cor_C7['x2'], cor_C7['y2'], 8)
    pyxel.line(cor_C7['x3'], cor_C7['y3'], cor_C7['x4'], cor_C7['y4'], 8)

def croix8(cor_C8):
    pyxel.line(cor_C8['x1'], cor_C8['y1'], cor_C8['x2'], cor_C8['y2'], 8)
    pyxel.line(cor_C8['x3'], cor_C8['y3'], cor_C8['x4'], cor_C8['y4'], 8)

def croix9(cor_C9):
    pyxel.line(cor_C9['x1'], cor_C9['y1'], cor_C9['x2'], cor_C9['y2'], 8)
    pyxel.line(cor_C9['x3'], cor_C9['y3'], cor_C9['x4'], cor_C9['y4'], 8)

# Dessin de la grille

def grille():
    pyxel.rect(98, 4, 2, 288, coul_grille)
    pyxel.rect(198, 4, 2, 288, coul_grille)
    pyxel.rect(4, 96, 288, 2, coul_grille)
    pyxel.rect(4, 196, 288, 2, coul_grille)


# Fonctions pour faire la wincondition


def wincondition(tab, tab2, tab3):
  global fin

  if tab[0] == tab2[0] == tab3[0] == 1 and tab[0] != 0:
      fin = 1
      return 1

  if tab[0] == tab2[0] == tab3[0] == 2 and tab[0] != 0:
      fin = 1
      return 2

  if tab[1] == tab2[1] == tab3[1] == 1 and tab[1] != 0:
      fin = 1
      return 3

  if tab[1] == tab2[1] == tab3[1] == 2 and tab[1] != 0:
      fin = 1
      return 4

  if tab[2] == tab2[2] == tab3[2] == 1 and tab[2] != 0:
      fin = 1
      return 5

  if tab[2] == tab2[2] == tab3[2] == 2 and tab[2] != 0:
      fin = 1
      return 6

  if tab[0] == tab[1] == tab[2] == 1 and tab[0] != 0:
      fin = 1
      return 7

  if tab2[0] == tab2[1] == tab2[2] == 1 and tab2[0] != 0:
      fin = 1
      return 8

  if tab3[0] == tab3[1] == tab3[2] == 1 and tab3[0] != 0:
      fin = 1
      return 9

  if tab[0] == tab[1] == tab[2] == 2 and tab[0] != 0:
      fin = 1
      return 10

  if tab2[0] == tab2[1] == tab2[2] == 2 and tab2[0] != 0:
      fin = 1
      return 11

  if tab3[0] == tab3[1] == tab3[2] == 2 and tab3[0] != 0:
      fin = 1
      return 12

  if tab[0] == tab2[1] == tab3[2] == 1 and tab[0] != 0:
      fin = 1
      return 13

  if tab[0] == tab2[1] == tab3[2] == 2 and tab[0] != 0:
      fin = 1
      return 14

  if tab[2] == tab2[1] == tab3[0] == 1 and tab[2] != 0:
      fin = 1
      return 15

  if tab[2] == tab2[1] == tab3[0] == 2 and tab[2] != 0:
      fin = 1
      return 16


def jeufini(ligne1, ligne2, ligne3):

    if wincondition(ligne1, ligne2, ligne3) == 2:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 1:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 3:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 4:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 5:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 6:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 7:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 8:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 9:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 10:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 11:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 12:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 13:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 14:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 15:
        return True
    elif wincondition(ligne1, ligne2, ligne3) == 16:
        return True
    else:
        return False



def clicktomatrix(c1, c2, c3, c4, c5, c6, c7, c8, c9):

    if clickmatrix["c1"] == 1:
        matrix[0][0] = 1
    if clickmatrix["c1"] == 2:
        matrix[0][0] = 2
    if clickmatrix["c2"] == 1:
        matrix[0][1] = 1
    if clickmatrix["c2"] == 2:
        matrix[0][1] = 2
    if clickmatrix["c3"] == 1:
        matrix[0][2] = 1
    if clickmatrix["c3"] == 2:
        matrix[0][2] = 2
    if clickmatrix["c4"] == 1:
        matrix[1][0] = 1
    if clickmatrix["c4"] == 2:
        matrix[1][0] = 2
    if clickmatrix["c5"] == 1:
        matrix[1][1] = 1
    if clickmatrix["c5"] == 2:
        matrix[1][1] = 2
    if clickmatrix["c6"] == 1:
        matrix[1][2] = 1
    if clickmatrix["c6"] == 2:
        matrix[1][2] = 2
    if clickmatrix["c7"] == 1:
        matrix[2][0] = 1
    if clickmatrix["c7"] == 2:
        matrix[2][0] = 2
    if clickmatrix["c8"] == 1:
        matrix[2][1] = 1
    if clickmatrix["c8"] == 2:
        matrix[2][1] = 2
    if clickmatrix["c9"] == 1:
        matrix[2][2] = 1
    if clickmatrix["c9"] == 2:
        matrix[2][2] = 2


# Vérification des entrées pour voir la position de la souris, du click et update des coordonnées des ronds pour les faire apparaitre au bon endroit.
# Chaque rond et croix ont des coordonées qui sont à l'extérieur de l'écran et chacune de ces coordonées va être modifié si il y a un click au bon endroit.
# Les coordonnées des 9 croix et ronds ont été modifiées à la main et ajustées pour apparaitre au bon endroit avec les bonnes dimension avec les fonctions pyxel.line et pyxel.circb.

def vérifier_entrée():
    global tour
    global pas_jouer_au_début                                                                                     # importation des variables tour et pas_jouer_au_début
    global bloc_col1
    global bloc_croixourond
    global bloc_grille
    if pas_jouer_au_début == 1:                                                                                   # changement de cette varaible à 1 pour pouvoir permettre de jouer après les deux premières pages car our faire affciher la grille en appuyant sur S on augmente aussi cette varaible et donc remplit la condtiton ce qui nous permet de lire les input à parti de ce moment-là.
        bloc_col1 = 1
        bloc_croixourond = 1
        bloc_grille = 1
        if pyxel.mouse_x < case_1['x'] and pyxel.mouse_y < case_1['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):    # pour chaque case dont les coordonnées sont délimitées par leurs limites définies au-dessus ; il y a une vérification de la position de la souris et du click.
            pas_jouer_dans_même_case['case1'] += 1                                                                # la variable pas_jouer_dans_même_case initialement à 0, j'augmente la valeur de celle-ci pour permettre de ne pas jouer deans la même case deux fois car sinon la variable n'est pas égale à 1 si on lui ajoute 1 à chauqe fois et donc cela ne vas pas dessiner les croix ou les ronds.
            if pas_jouer_dans_même_case['case1'] == 1:
                  tour += 1                                                                                       # changement de la valeur de tour pour la rendre paire ou impaire.
                  if tour % 2 == 0:                                                                               # si tour est pair alors ça dessine une croix, si tour est impair ça dessine une croix.
                      cor_R1['x'] = 50                                                                          # changement des valeurs de x et y pour dessiner correctement le rond avec la fonction pyxel.circb(x, y, rayon, couleur)                                          .
                      cor_R1['y'] = 50
                      clickmatrix["c1"] = 2
                  else:
                      cor_C1['x1'] = 8                                                                            # La fonction pyxel.line a 5 arguments, x1, y1, x2, Y2.
                      cor_C1['y1'] = 8                                                                            # Sachant que pour faire une croix on a besoin de deux lignes, alors les 8 valeurs permettant de dessiner les criox sont ajustées.
                      cor_C1['x2'] = 92
                      cor_C1['y2'] = 92
                      cor_C1['x3'] = 92
                      cor_C1['y3'] = 8
                      cor_C1['x4'] = 8
                      cor_C1['y4'] = 92
                      clickmatrix["c1"] = 1
            else:
                pass                                                                                              # La fonction pass() pour ne rien faire si il n'y a pas de click.
        if case_1['x'] < pyxel.mouse_x < case_2['x'] and pyxel.mouse_y < case_2['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pas_jouer_dans_même_case['case2'] += 1
            if pas_jouer_dans_même_case['case2'] == 1:
                tour += 1
                if tour % 2 == 0:
                    cor_R2['x'] = 150
                    cor_R2['y'] = 50
                    clickmatrix["c2"] = 2

                else:
                    cor_C2['x1'] = 108
                    cor_C2['y1'] = 8
                    cor_C2['x2'] = 192
                    cor_C2['y2'] = 92
                    cor_C2['x3'] = 192
                    cor_C2['y3'] = 8
                    cor_C2['x4'] = 108
                    cor_C2['y4'] = 92
                    clickmatrix["c2"] = 1
            else:
                pass
        if case_2['x'] < pyxel.mouse_x < case_3['x'] and pyxel.mouse_y < case_3['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pas_jouer_dans_même_case['case3'] += 1
            if pas_jouer_dans_même_case['case3'] == 1:
                tour += 1
                if tour % 2 == 0:
                    cor_R3['x'] = 250
                    cor_R3['y'] = 50
                    clickmatrix["c3"] = 2
                else:
                    cor_C3['x1'] = 208
                    cor_C3['y1'] = 8
                    cor_C3['x2'] = 292
                    cor_C3['y2'] = 92
                    cor_C3['x3'] = 292
                    cor_C3['y3'] = 8
                    cor_C3['x4'] = 208
                    cor_C3['y4'] = 92
                    clickmatrix["c3"] = 1
            else:
                pass

        if pyxel.mouse_x < case_4['x'] and case_1['y'] < pyxel.mouse_y < case_4['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pas_jouer_dans_même_case['case4'] += 1
            if pas_jouer_dans_même_case['case4'] == 1:
                tour += 1
                if tour % 2 == 0:
                    cor_R4['x'] = 50
                    cor_R4['y'] = 150
                    clickmatrix["c4"] = 2
                else:
                    cor_C4['x1'] = 8
                    cor_C4['y1'] = 108
                    cor_C4['x2'] = 92
                    cor_C4['y2'] = 192
                    cor_C4['x3'] = 92
                    cor_C4['y3'] = 108
                    cor_C4['x4'] = 8
                    cor_C4['y4'] = 192
                    clickmatrix["c4"] = 1
            else:
                pass

        if case_4['x'] < pyxel.mouse_x < case_5['x'] and case_2['y'] < pyxel.mouse_y < case_5['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pas_jouer_dans_même_case['case5'] += 1
            if pas_jouer_dans_même_case['case5'] == 1:
                tour += 1
                if tour % 2 == 0:
                    cor_R5['x'] = 150
                    cor_R5['y'] = 150
                    clickmatrix["c5"] = 2
                else:
                    cor_C5['x1'] = 108
                    cor_C5['y1'] = 108
                    cor_C5['x2'] = 192
                    cor_C5['y2'] = 192
                    cor_C5['x3'] = 192
                    cor_C5['y3'] = 108
                    cor_C5['x4'] = 108
                    cor_C5['y4'] = 192
                    clickmatrix["c5"] = 1
            else:
                pass

        if case_5['x'] < pyxel.mouse_x < case_6['x'] and case_3['y'] < pyxel.mouse_y < case_6['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pas_jouer_dans_même_case['case6'] += 1
            if pas_jouer_dans_même_case['case6'] == 1:
                tour += 1
                if tour % 2 == 0:
                    cor_R6['x'] = 250
                    cor_R6['y'] = 150
                    clickmatrix["c6"] = 2
                else:
                    cor_C6['x1'] = 208
                    cor_C6['y1'] = 108
                    cor_C6['x2'] = 292
                    cor_C6['y2'] = 192
                    cor_C6['x3'] = 292
                    cor_C6['y3'] = 108
                    cor_C6['x4'] = 208
                    cor_C6['y4'] = 192
                    clickmatrix["c6"] = 1
            else:
                pass

        if pyxel.mouse_x < case_7['x'] and case_4['y'] < pyxel.mouse_y < case_7['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pas_jouer_dans_même_case['case7'] += 1
            if pas_jouer_dans_même_case['case7'] == 1:
                tour += 1
                if tour % 2 == 0:
                    cor_R7['x'] = 50
                    cor_R7['y'] = 250
                    clickmatrix["c7"] = 2
                else:
                    cor_C7['x1'] = 8
                    cor_C7['y1'] = 208
                    cor_C7['x2'] = 92
                    cor_C7['y2'] = 292
                    cor_C7['x3'] = 92
                    cor_C7['y3'] = 208
                    cor_C7['x4'] = 8
                    cor_C7['y4'] = 292
                    clickmatrix["c7"] = 1
            else:
                pass

        if case_7['x'] < pyxel.mouse_x < case_8['x'] and case_5['y'] < pyxel.mouse_y < case_8['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pas_jouer_dans_même_case['case8'] += 1
            if pas_jouer_dans_même_case['case8'] == 1:
                tour += 1
                if tour % 2 == 0:
                    cor_R8['x'] = 150
                    cor_R8['y'] = 250
                    clickmatrix["c8"] = 2
                else:
                    cor_C8['x1'] = 108
                    cor_C8['y1'] = 208
                    cor_C8['x2'] = 192
                    cor_C8['y2'] = 292
                    cor_C8['x3'] = 192
                    cor_C8['y3'] = 208
                    cor_C8['x4'] = 108
                    cor_C8['y4'] = 292
                    clickmatrix["c8"] = 1
            else:
                pass

        if case_8['x'] < pyxel.mouse_x < case_9['x'] and case_6['y'] < pyxel.mouse_y < case_9['y'] and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pas_jouer_dans_même_case['case9'] += 1
            if pas_jouer_dans_même_case['case9'] == 1:
                tour += 1
                if tour % 2 == 0:
                    cor_R9['x'] = 250
                    cor_R9['y'] = 250
                    clickmatrix["c9"] = 2
                else:
                    cor_C9['x1'] = 208
                    cor_C9['y1'] = 208
                    cor_C9['x2'] = 292
                    cor_C9['y2'] = 292
                    cor_C9['x3'] = 292
                    cor_C9['y3'] = 208
                    cor_C9['x4'] = 208
                    cor_C9['y4'] = 292
                    clickmatrix["c9"] = 1
            else:
                pass


# Fonction pour quitter l'écran

def sortir():
    if pyxel.btn(pyxel.KEY_A):
        pyxel.quit()



# S'il y a match nul

def match_nul(wincondition, cor_C1, cor_C2, cor_C3, cor_C4, cor_C5, cor_C6, cor_C7, cor_C8, cor_C9, cor_R1, cor_R2, cor_R3, cor_R4, cor_R5, cor_R6, cor_R7, cor_R8, cor_R9):
    global tour
    global coul_grille
    global rondcommence
    global croixcommence
    global fin
    
# Déplacement de toutes les coordonnées des cercles pour les bouger hors de l'écran

    if fin == 0:
        if rondcommence == 1 and tour == 10 or croixcommence == 1 and tour == 9:
            
            cor_R1['x'] = -50
            cor_R1['y'] = -50
            cor_C1['x1'] = -8
            cor_C1['y1'] = -8
            cor_C1['x2'] = -92
            cor_C1['y2'] = -92
            cor_C1['x3'] = -92
            cor_C1['y3'] = -8
            cor_C1['x4'] = -8
            cor_C1['y4'] = -92

            cor_R2['x'] = -150
            cor_R2['y'] = -50
            cor_C2['x1'] = -108
            cor_C2['y1'] = -8
            cor_C2['x2'] = -192
            cor_C2['y2'] = -92
            cor_C2['x3'] = -192
            cor_C2['y3'] = -8
            cor_C2['x4'] = -108
            cor_C2['y4'] = -92

            cor_R3['x'] = -250
            cor_R3['y'] = -50
            cor_C3['x1'] = -208
            cor_C3['y1'] = -8
            cor_C3['x2'] = -292
            cor_C3['y2'] = -92
            cor_C3['x3'] = -292
            cor_C3['y3'] = -8
            cor_C3['x4'] = -208
            cor_C3['y4'] = -92

            cor_R4['x'] = -50
            cor_R4['y'] = -150
            cor_C4['x1'] = -8
            cor_C4['y1'] = -108
            cor_C4['x2'] = -92
            cor_C4['y2'] = -192
            cor_C4['x3'] = -92
            cor_C4['y3'] = -108
            cor_C4['x4'] = -8
            cor_C4['y4'] = -192

            cor_R5['x'] = -150
            cor_R5['y'] = -150
            cor_C5['x1'] = -108
            cor_C5['y1'] = -108
            cor_C5['x2'] = -192
            cor_C5['y2'] = -192
            cor_C5['x3'] = -192
            cor_C5['y3'] = -108
            cor_C5['x4'] = -108
            cor_C5['y4'] = -192

            cor_R6['x'] = -250
            cor_R6['y'] = -150
            cor_C6['x1'] = -208
            cor_C6['y1'] = -108
            cor_C6['x2'] = -292
            cor_C6['y2'] = -192
            cor_C6['x3'] = -292
            cor_C6['y3'] = -108
            cor_C6['x4'] = -208
            cor_C6['y4'] = -192

            cor_R7['x'] = -50
            cor_R7['y'] = -250
            cor_C7['x1'] = -8
            cor_C7['y1'] = -208
            cor_C7['x2'] = -92
            cor_C7['y2'] = -292
            cor_C7['x3'] = -92
            cor_C7['y3'] = -208
            cor_C7['x4'] = -8
            cor_C7['y4'] = -292

            cor_R8['x'] = -150
            cor_R8['y'] = -250
            cor_C8['x1'] = -108
            cor_C8['y1'] = -208
            cor_C8['x2'] = -192
            cor_C8['y2'] = -292
            cor_C8['x3'] = -192
            cor_C8['y3'] = -208
            cor_C8['x4'] = -108
            cor_C8['y4'] = -292

            cor_R9['x'] = -250
            cor_R9['y'] = -250
            cor_C9['x1'] = -208
            cor_C9['y1'] = -208
            cor_C9['x2'] = -292
            cor_C9['y2'] = -292
            cor_C9['x3'] = -292
            cor_C9['y3'] = -208
            cor_C9['x4'] = -208
            cor_C9['y4'] = -292

    #  Ecrire le match nul

            coul_grille = 7
            pyxel.text(90, 100, "Dommage ! C'est un match nul :(", 0)
            pyxel.text(90, 150, "Appuyez sur A pour quitter", 0)



# Définir les premières pages de texte, jusqu'à la vérification des entrées de la souris pour commencer le jeu.


def debut():
    global croixcommence
    global rondcommence
    global tour                  # variable pour choisir le tour dans le début du jeu
    global bloc_col1
    global coul_texte            # {
    global coul_grille           #
    global coul_texte2           #  variables importées du script global avec la fonction global pour gérer l'apparition et la désapirition du texte
    global coul_soulignement     #
    global coul_texte1           #
    global coul_violet2          # }
    global bloc_croixourond
    global pas_jouer_au_début    # variable créée pour ne pas pouvoir faire apparaitre des ronds et croix en appuyant avec la souris au début.
    global fin
    pyxel.cls(7)
# Instructions permettant d'écrire le texte

    pyxel.text(120, 40, "JEU DU MORPION", coul_texte1)
    pyxel.line(115, 48, 180, 48, coul_soulignement)
    pyxel.text(16, 75, "Bonjour et Bienvenue sur notre plateau de jeu !", coul_texte2)
    pyxel.text(34, 90, "Aujourd'hui nous avons au programme le  :  'jeu du morpion'.", coul_texte1)
    pyxel.text(16, 130, " Veuillez cliquer sur la touche 'R' pour lire les regles du jeu", coul_texte2)

    pyxel.text(120, 30, " REGLES DU JEU ", coul_texte)
    pyxel.line(115, 38, 180, 38, coul_texte)
    pyxel.text(45, 60, "1. Vous devez placer troix croix ou 3  ronds", coul_texte)
    pyxel.text(45, 70, "  de sorte qu'ils forment une ligne de 3 que ce  ", coul_texte)
    pyxel.text(45, 80, "   soit verticalement, horizontalement ou en diagonale.", coul_texte)
    pyxel.text(45,105, "2. Vous jouez chacun votre tour en faisant click gauche", coul_texte)
    pyxel.text(45, 115,"  sur une des cases de la grille.", coul_texte)
    pyxel.text(45, 140,"3. Maintenant que vous savez tout, choisissez qui", coul_texte)
    pyxel.text(45, 150,"   qui va commencer, les croix ou les  ronds :", coul_texte)
    pyxel.text(45, 160,"  appuyez sur la touche '1' pour les croix", coul_texte)
    pyxel.text(45, 170,"  et sur la touche '2' pour les ronds", coul_texte)
    pyxel.text(53, 220,"Amusez-vous bien ! :)", coul_texte)
    pyxel.text(40, 185, "Appuyez sur la touche 'S' pour commencer la partie", coul_violet2)
    pyxel.text(15, 250, " NB : ", coul_violet2)

    pyxel.text(40, 250, "Appuyez sur la touche 'A' a tout moment pour quitter la fenetre", coul_texte)

    if pyxel.btn(pyxel.KEY_1) and bloc_croixourond == 0:
        tour = 0
        croixcommence = 1
        pyxel.text(178, 220, "Croix commence", coul_texte)

    if pyxel.btn(pyxel.KEY_2) and bloc_croixourond == 0:
        tour = 1
        rondcommence = 1
        croixcommence = 0
        pyxel.text(181, 220, "Rond commence", coul_texte)


# Bouton R pour lire les règles et faire apparaitre le texte

    if pyxel.btn(pyxel.KEY_R) and bloc_col1 == 0:
        coul_texte = 0
        coul_texte1 = 7
        coul_texte2 = 7
        coul_soulignement = 7
        coul_violet2 = 2


# Bouton S pour cacher le texte et montrer la grille

    if pyxel.btn(pyxel.KEY_S) and fin == 0:
        coul_grille = 0
        coul_texte = 7
        coul_violet2 = 7
        pas_jouer_au_début = 1



# Interface après la partie, win or draw

def interface_fin(wincondition):
    global pas_jouer_au_début
    global coul_grille
    if jeufini(ligne1, ligne2, ligne3):

# Pour ne plus pouvoir bouger les ronds et croix

        pas_jouer_au_début = 2

# Déplacement de tous les ronds et croix de la grille au dehors du cadre

        cor_R1['x'] = -50
        cor_R1['y'] = -50
        cor_C1['x1'] = -8
        cor_C1['y1'] = -8
        cor_C1['x2'] = -92
        cor_C1['y2'] = -92
        cor_C1['x3'] = -92
        cor_C1['y3'] = -8
        cor_C1['x4'] = -8
        cor_C1['y4'] = -92

        cor_R2['x'] = -150
        cor_R2['y'] = -50
        cor_C2['x1'] = -108
        cor_C2['y1'] = -8
        cor_C2['x2'] = -192
        cor_C2['y2'] = -92
        cor_C2['x3'] = -192
        cor_C2['y3'] = -8
        cor_C2['x4'] = -108
        cor_C2['y4'] = -92

        cor_R3['x'] = -250
        cor_R3['y'] = -50
        cor_C3['x1'] = -208
        cor_C3['y1'] = -8
        cor_C3['x2'] = -292
        cor_C3['y2'] = -92
        cor_C3['x3'] = -292
        cor_C3['y3'] = -8
        cor_C3['x4'] = -208
        cor_C3['y4'] = -92

        cor_R4['x'] = -50
        cor_R4['y'] = -150
        cor_C4['x1'] = -8
        cor_C4['y1'] = -108
        cor_C4['x2'] = -92
        cor_C4['y2'] = -192
        cor_C4['x3'] = -92
        cor_C4['y3'] = -108
        cor_C4['x4'] = -8
        cor_C4['y4'] = -192

        cor_R5['x'] = -150
        cor_R5['y'] = -150
        cor_C5['x1'] = -108
        cor_C5['y1'] = -108
        cor_C5['x2'] = -192
        cor_C5['y2'] = -192
        cor_C5['x3'] = -192
        cor_C5['y3'] = -108
        cor_C5['x4'] = -108
        cor_C5['y4'] = -192

        cor_R6['x'] = -250
        cor_R6['y'] = -150
        cor_C6['x1'] = -208
        cor_C6['y1'] = -108
        cor_C6['x2'] = -292
        cor_C6['y2'] = -192
        cor_C6['x3'] = -292
        cor_C6['y3'] = -108
        cor_C6['x4'] = -208
        cor_C6['y4'] = -192

        cor_R7['x'] = -50
        cor_R7['y'] = -250
        cor_C7['x1'] = -8
        cor_C7['y1'] = -208
        cor_C7['x2'] = -92
        cor_C7['y2'] = -292
        cor_C7['x3'] = -92
        cor_C7['y3'] = -208
        cor_C7['x4'] = -8
        cor_C7['y4'] = -292

        cor_R8['x'] = -150
        cor_R8['y'] = -250
        cor_C8['x1'] = -108
        cor_C8['y1'] = -208
        cor_C8['x2'] = -192
        cor_C8['y2'] = -292
        cor_C8['x3'] = -192
        cor_C8['y3'] = -208
        cor_C8['x4'] = -108
        cor_C8['y4'] = -292

        cor_R9['x'] = -250
        cor_R9['y'] = -250
        cor_C9['x1'] = -208
        cor_C9['y1'] = -208
        cor_C9['x2'] = -292
        cor_C9['y2'] = -292
        cor_C9['x3'] = -292
        cor_C9['y3'] = -208
        cor_C9['x4'] = -208
        cor_C9['y4'] = -292


# Animation quand les ronds gagnent la partie

        if tour % 2 == 0:
            pyxel.text(100, 60, "Bravo ! Victoire des ronds ! ", 0)
            if pyxel.frame_count % 20 > 1:
                pyxel.circb(90, 150, 30, 11)
            if pyxel.frame_count % 20 > 6:
                pyxel.circb(160, 150, 30, 11)
            if pyxel.frame_count % 20 > 11:
                pyxel.circb(230, 150, 30, 11)
            if pyxel.frame_count % 20 > 11:
                pyxel.line(45, 150, 270, 150, 11)
            coul_grille = 7


# Animation quand les croix gagnent la partie.

        if tour % 2 == 1:
            pyxel.text(100, 60, "Bravo ! Victoire des croix ! ", 0)
            if pyxel.frame_count % 20 > 1:
                pyxel.line(60, 120, 110, 170, 8)
                pyxel.line(110, 120, 60, 170, 8)
            if pyxel.frame_count % 20 > 6:
                pyxel.line(130, 120, 180, 170, 8)
                pyxel.line(180, 120, 130, 170, 8)
            if pyxel.frame_count % 20 > 11:
                pyxel.line(200, 120, 250, 170, 8)
                pyxel.line(250, 120, 200, 170, 8)
            if pyxel.frame_count % 20 > 11:
                pyxel.line(45, 145, 260, 145, 8)

            coul_grille = 7

        pyxel.text(85, 250, "Appuyez sur A pour quitter la fentre.", 0)


# Update pour vérifier chaque frame si il y a une entrée

def update():
    debut()
    vérifier_entrée()
    clicktomatrix(clickmatrix["c1"], clickmatrix["c2"], clickmatrix["c3"], clickmatrix["c4"], clickmatrix["c5"], clickmatrix["c6"], clickmatrix["c7"], clickmatrix["c8"], clickmatrix["c9"])
    wincondition(ligne1, ligne2, ligne3)
    jeufini(ligne1, ligne2, ligne3)
    interface_fin(wincondition)
    sortir()
    match_nul(wincondition, cor_C1, cor_C2, cor_C3, cor_C4, cor_C5, cor_C6, cor_C7, cor_C8, cor_C9, cor_R1, cor_R2, cor_R3, cor_R4, cor_R5, cor_R6, cor_R7, cor_R8, cor_R9)


# Draw pour tout ce qui va être dessiné

def draw():
    pyxel.cls(7)
    debut()
    grille()
    jeufini(ligne1, ligne2, ligne3)
    wincondition(ligne1, ligne2, ligne3)
    interface_fin(wincondition)
    match_nul(wincondition, cor_C1, cor_C2, cor_C3, cor_C4, cor_C5, cor_C6, cor_C7, cor_C8, cor_C9, cor_R1, cor_R2, cor_R3, cor_R4, cor_R5, cor_R6, cor_R7, cor_R8, cor_R9)
    rond1(cor_R1)
    rond2(cor_R2)
    rond3(cor_R3)
    rond4(cor_R4)
    rond5(cor_R5)
    rond6(cor_R6)
    rond7(cor_R7)
    rond8(cor_R8)
    rond9(cor_R9)
    croix1(cor_C1)
    croix2(cor_C2)
    croix3(cor_C3)
    croix4(cor_C4)
    croix5(cor_C5)
    croix6(cor_C6)
    croix7(cor_C7)
    croix8(cor_C8)
    croix9(cor_C9)


pyxel.run(update, draw)

