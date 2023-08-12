from random import randint
import pyxel

#Création de la fenètre
TITLE = "Space Invaders"
WIDTH = 224
HEIGHT = 256
pyxel.init(WIDTH, HEIGHT, title=TITLE)
pyxel.load("ressource.pyxres")

Alien_Speed = 31
score = 0
lives = 3


direction = 0 #Défini la direction que les invaseurs bougent
game_over = 0 #Vérifie si tu as perdu le jeux
damage_indicator = 0 #Indique si tu as perdu une vie
ship = [102,230] 

#Tableaux vides qui vont contenir les coordonnées des tirs
ship_bullets = []
alien_bullets = []

cooldown = 0 #limite les tirs du défenseur

#Coordonnée du premier invaseur
x = 26
y = 24

#Tableau qui va contenir les coordonnées des invaseurs
aliens = [[[0] * 2 for _ in range(8)] for i in range(5)]
#Compte le nombre d'invaseurs restant
aliens_alive = 40    

def draw():  
    if game_over == 1:
        pyxel.cls(0)
        pyxel.text(30,128, "You have failed to defend Earth! GAME OVER!", 7)
        pyxel.text(100,135, f"SCORE : {score}", 7)
        
    if game_over == 0:
        pyxel.cls(0)
        pyxel.text(4,4, f"SCORE : {score}", 7)
        pyxel.text(180,4, f"LIVES : {lives}", 7)
        
#Coordonnées du défenseur
        x_ship = ship[0]
        y_ship = ship[1]
        
#Dessine le défenseur, vérifiant si tu as perdu une vie et si oui, fait cligner le défenseur
        if damage_indicator % 2 == 0:
            pyxel.blt(x_ship, y_ship,0,0,0,25,18,0)
        else:
            pyxel.blt(x_ship, y_ship,1,0,0,20,13,0)
#Dessine la ligne représentant la Terre    
        pyxel.rect(5, 230,210,1,9)
        
#Dessine les tirs des invaseurs et du défenseur
        if len(ship_bullets) > 0:
            for i in range (len(ship_bullets)):
                pyxel.rect(ship_bullets[i][0], ship_bullets[i][1], 1, 4, 7)
        if len(alien_bullets) > 0:
            for v in range (len(alien_bullets)):
                pyxel.rect(alien_bullets[v][0], alien_bullets[v][1], 1, 4, 4)
        
#Dessine les invaseurs
        y_aliens = y
        for a in range(len(aliens)):
            x_aliens = x
            for b in range(len(aliens[0])):
                for c in range(2):
                    if aliens [a][b] != [50,1000]: #Vérifie si l'invaseur est encore vivant
                        aliens[a][b] = [x_aliens, y_aliens]
                pyxel.blt(aliens[a][b][0], aliens[a][b][1],2,0,0,22,13,0)
                x_aliens += 18
            y_aliens+= 24
                          

def update():
    global damage_indicator
    global direction
    global Alien_Speed
    global aliens
    global x
    global y
    global cooldown
    global score
    global aliens_alive
    global game_over
    global lives
    
    if game_over == 0:
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()
#Permet de se déplacer et de tirer avec le défenseur    
        if pyxel.btn(pyxel.KEY_RIGHT) and ship[0] < 211:
            ship[0] += 2
        if pyxel.btn(pyxel.KEY_LEFT) and ship[0] > 0:
            ship[0] -= 2
        if pyxel.btn(pyxel.KEY_SPACE) and cooldown == 0:
            ship_bullets.append([ship[0] + 16, 236]) #Addicione la coordonnée du nouveaux tir dans le tableau
            cooldown = 20
          
#Fait bouger les tirs du défenseur  
        for j in range (len(ship_bullets)):
            ship_bullets[j][1] -= 5
        
#Fait tirer les invaseurs
        if pyxel.frame_count % Alien_Speed == 0:    
            for w in range (len(aliens)):
                for n in range (len(aliens[0])):
                    if randint(1,80) == 80:
                        alien_bullets.append([aliens[w][n][0]+6, aliens[w][n][1] + 13])
            
#Fait bouger les invaseurs, vérifiant si ils sont arrivées a la limite de l'écran
    #Si oui, change leur direction et leur fait déscendre
            if direction == 0:
                for s in range(len(aliens)):
                    if max(aliens[s]) < [190,0]:
                        x = x + 5
                        break
                for s in range(len(aliens)):
                    if max(aliens[s]) >= [190,0]:
                        direction = 1
                        y += 10
                        break
            if direction == 1:
                for q in range(len(aliens)):
                    if min(aliens[q]) > [0,0]:
                        x = x - 5
                        break
                for q in range(len(aliens)):
                    if min(aliens[q]) <= [0,0]:
                        direction = 0
                        y += 10
                        break
#Met fin au clignotement du défenseur                    
        if damage_indicator > 0:
            damage_indicator -= 1

#Fait bouger les tirs des invaseurs
        for z in range (len(alien_bullets)):
            alien_bullets[z][1] += 3

#Réduit le temps de recharge de tirer jusqu'à pouvoir tirer à nouveau
        if cooldown > 0:
            cooldown -= 1

#Vérifie si un tir a touché un invaseur et si oui, augmente le score et enlève ce tir et invaseur de l'écran
        for k in range(len(ship_bullets)):
            for l in range(len(aliens)):
                for m in range(len(aliens[0])):
                    if ship_bullets[k][0] > (aliens[l][m][0]) + 8 and ship_bullets[k][0] < (aliens[l][m][0]) + 23:
                        if ship_bullets[k][1] > (aliens[l][m][1]) - 1 and ship_bullets[k][1] < (aliens[l][m][1]) + 14:
                            #Je voulais utiliser del(), mais je ne suis pas parvenu a la fair fonctionner avec le reste du code.
                                #Donc j'envoie le tir et l'invaseur hors de l'écran.
                            aliens[l][m]= [50,1000]
                            score += 30
                            ship_bullets[k] = [1000, 1000]
                            aliens_alive -=1
        
#Vérifie si un tir des invaseurs a touché le défenseur. Si oui, retire 1 vie et fait le défenseur clignoter
        for h in range(len(alien_bullets)):
            if alien_bullets[h][0] > (ship[0]) + 10 and alien_bullets[h][0] < (ship[0]) + 25:
                if alien_bullets[h][1] > (ship[1]) - 1 and alien_bullets[h][1] < (ship[1]) + 13:
                    lives -= 1
                    damage_indicator = 5
                    alien_bullets[h] = [1000, 1000]
        
#Vérifie si les conditions d'un game over sont accomplies:
        #Vérifie si les invaseurs ont franchi la ligne désignant la Terre
        for t in range (len(aliens)):
            for u in range (len(aliens[0])):
                if aliens[t][u][1] >=220 and aliens[t][u][1] < 1000 :
                    game_over = 1
                    break
        #Vérifie si il reste des vies au joueur
        if lives == 0:
            game_over = 1

#Vérifie si il y a enocre des invaseurs. Sinon, crée une nouvelle vague d'envahisseurs et augmente leur vitesse.
        if aliens_alive == 0:
            x = 26
            y = 24
            aliens = [[[0] * 2 for _ in range(8)] for i in range(5)]
            aliens_alive = 40
            if Alien_Speed > 1:
                Alien_Speed -= 3 

pyxel.run(draw,update)