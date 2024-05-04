import pyxel
import random

def app_draw():
    
# monte l'écran avec l'oiseau, les obstacles et le score du jeu
    
 global app_obstacleX, app_intervalleY, ecran_larg, ecran_alt, fin_du_jeu
 global obstacle_larg, intervalle_alt, score
 
 pyxel.cls(12)  #  remplit l'écran avec la couleur 12 = bleu
 
 # dessine les obstacles sur l’écran
 max=len(app_obstacleX)
 for i in range(0, max):
     
      # prendre le x de l’obstacle et le y du intervalle
      obstacle_x=app_obstacleX[i]
      intervalle_y=app_intervalleY[i]

      # partie supérieure de l'obstacle, de la ligne 0 jusqu'au début de l'intervalle
      pyxel.rect(obstacle_x, 0, obstacle_larg, intervalle_y, 14) # couleur 14 = rose
 
      # partie inférieure de l'obstacle (de la fin de l'intervalle jusqu'à la fin de l'écran)
      pyxel.rect(obstacle_x, intervalle_y+intervalle_alt, obstacle_larg, ecran_alt, 14)


 # dessine l’oiseaux sur l’écran
# pyxel.rect(bird_x, bird_y, bird_larg, bird_alt, bird_cor)
 pyxel.blt(bird_x, bird_y,0,0,0,bird_larg, bird_alt)


 # écris le score du jeu sur l'écran (colonne 5, ligne 4)
 pyxel.text(12, 4, f"Score du jeu: {score}", 0) # couleur 0 = noir
 
 
 if fin_du_jeu:
    pyxel.cls(12)  # remplit l'écran avec la couleur 12 = bleu
    pyxel.text(12, 12, f"Score du jeu = {score}", 0) # couleur 8 = noir
    if score <= 10:
          pyxel.text(12, 45, "Decevant!", 0)  # 0=noir, col 5 lin 45
          intervalle_alt=60
    elif score<=20:
          pyxel.text(12, 45, "Pas mal", 0)  # 0=noir, col 5 lin 45
          intervalle_alt=40
    else:
          pyxel.text(12, 45, "Tres bien!", 0)  # 0=noir, col 5 lin 45
          intervalle_alt=30
          
    pyxel.text(12, 55, 'Tape "r" pour recommencer', 0)  # col 5, lin 55



def app_update():
    
 global fin_du_jeu, frame_count, app_obstacleX, app_intervalleY
 global ecran_alt, intervalle_alt, ecran_larg
 global bird_x, bird_y, bird_larg, obstacle_larg, score
 
 # si la touche 'r' a été pressée, fait recommencer le jeu
 if pyxel.btnp(pyxel.KEY_R):
       fin_du_jeu = False
       pyxel.cls(12)  # rémplit l’écran avec la couleur 12 = bleu
       pyxel.text(12, 12, f"Score du jeu = {score}", 0) # couleur 8 = noir
       frame_count = 0
       score=0
       app_obstacleX=[] # nettoie la liste avec x des obstacles
       app_intervalle_Y=[] # nettoie la liste y avec des intervalles

 #si le jeu n'est pas encore terminé
 if fin_du_jeu==False:
     
       frame_count = frame_count + 1

       # anime l'oiseau
       bird_update()

       # toutes les 60 frames, crée un nouvel obstacle
       if frame_count % 60 == 0:  # si le compteur de frames est un multiple de 60
            # crée un nouvel obstacle
            intervalle_y = random.randint(16, ecran_alt - 16 - intervalle_alt)
            app_obstacleX.append(ecran_larg)
            app_intervalleY.append(intervalle_y)

       # anime tous les obstacles de la liste
       max=len(app_obstacleX)-1
       for i in range(0, max):
           
            # fait avancer l'obstacle d'un pas vers la gauche
            app_obstacleX[i] = app_obstacleX[i] -1.5                               
            
            # si l'oiseau entre en collision avec l'obstacle, fin de jeu
            obstacle_x= app_obstacleX[i]
            intervalle_y = app_intervalleY[i]
            test1= bird_x + bird_larg > obstacle_x
            test2= bird_x < obstacle_x + obstacle_larg
            test3= bird_y < intervalle_y
            test4= bird_y + bird_alt > intervalle_y + intervalle_alt
            if (test1 and test2 and (test3 or test4)):
                 fin_du_jeu = True

       # supprime les obstacles vaincus et met à jour le score
       newX=[]
       newY=[]
       max=len(app_obstacleX)
       #  crée une nouvelle liste d'obstacles et d'intervalle
       for i in range(0, max):
          if app_obstacleX[i] >0:
             newX.append(app_obstacleX[i])
             newY.append(app_intervalleY[i])
          else: # pour chaque obstacle vaincu
             score=score+1 # ajoute un point au score
       app_obstacleX=newX
       app_intervalleY=newY


def bird_update():
    
 global bird_pasY, gravite, bird_y, impulsion
 

 # anime l'oiseau en vertical
 # la gravité tire vers le bas et le passoY tire vers le haut
 bird_pasY = bird_pasY + gravite
 bird_y = bird_y + bird_pasY
 
 # si arrivé au sol, retourne en haut de l'écran
 if bird_y > ecran_alt:
     bird_pasY=0
     bird_y=0

 #  si la touche espace a été pressée, donne un coup de pouce vers le haut
 if pyxel.btnp(pyxel.KEY_SPACE):
       bird_pasY = impulsion

#    fin des définitions de fonctions ####################################
       
#   Ici commence le programme      

# démarre le pyxel
ecran_larg = 160
ecran_alt = 120
pyxel.init(ecran_larg, ecran_alt, title="Flappy Bird, par Manuela et Claire")
# chargement des images et des sons
pyxel.load("my_resource.pyxres", False, False, False, False)

pyxel.playm(0, loop=True) #Lancement de la musique



# Place l'oiseau exactement au milieu de l'écran
bird_couleur=11       # vert
bird_larg = 16
bird_alt = 16
bird_x = (ecran_larg // 2 - bird_larg // 2)
bird_y = (ecran_alt // 2 - bird_alt // 2)
bird_pasY = 0   # le pas sera la somme de la gravité avec l'impulsion
gravite = 0.1    # tire l'oiseau vers le bas
impulsion = -1.0    # tire l'oiseau vers le haut (barre d'espace)


# listes d'obstacles et intervalles correspondants
# (toutes les 80 images, le programme génère un nouvel obstacle)
app_obstacleX = []       # colonne où se trouve l'obstacle
app_intervalleY =[]         # ligne où commence l'intervalle
obstacle_larg = 20   #  largeur de l'obstacle
intervalle_alt = 40     # hauteur de l'intervalle (espace d'évasion pour l'oiseau)


score = 0         # chaque obstacle vaincu compte un point
fin_du_jeu = False
frame_count = 0



# loop infinit du pyxel
pyxel.run(app_update, app_draw)
