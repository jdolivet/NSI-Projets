from random import randint
import pyxel

#Création de la fenètre
TITLE = "LE PROF"
WIDTH = 230
HEIGHT = 260
pyxel.init(WIDTH, HEIGHT, title=TITLE)

#Création du fichier qui va contenir les highscores
with open("highscore.txt", 'a+') as f: #Nous voulions utiliser une seule instance de "with open", mais pour une raison ou... 
    pass                           # ...une autre, 'a+' croyait que le fichier était toujours vide donc le code ne marchait pas
with open("highscore.txt", 'r') as f:
    if f.readline() == '':
        with open("highscore.txt", 'w') as a:
            a.write('0')

increase_score = True #Défini si le score augmente
game_over = False
game_speed = 31
score = 0 
lives = 1
danger = 0
countdown = 7 #Permet au prof de se retourner progréssivement
faster = 0
high_score = 0
powerup = False #Indique si un powerup est actif
powers = 0 #Indique quel powerup est actif
charging = 0 #Indique si le powerup a été obtenu ou combien il reste pour l'obtenir
bonus_score = 0 
expire = 0 #Indique si le joueur n'as pas activé le powerup a temps et le fait disparaitre
ik_prevention = False #Empeche au joueur de mourrir instantanément independament de son nombre de vies

def draw():
    if game_over == True:
        pyxel.cls(0)
        pyxel.text(15,128,"Le prof vous a vu utilisant le telephone! GAME OVER!", 7)
        pyxel.text(100,135, f"SCORE : {score}", 7)
        pyxel.text(90,142, f"HIGH SCORE : {high_score}", 7)
        pyxel.text(75, 156, "Press space to restart", 7)
    
    if game_over == False:
        pyxel.cls(12)
        pyxel.text(4,4, f"SCORE : {score}", 7)
        if bonus_score > 0:
             pyxel.text(4,4, f"SCORE : {score} (x2)", 7) #Indique au joueur s'il ganhe plus de points
        pyxel.text(4,12, f"LIVES : {lives}", 7)
        
        #Dessine le téléphone
        if increase_score == True:
                pyxel.rect(100,185,40,70,13)
                pyxel.rect(100,185,40,5,0)
                pyxel.rect(100,185,5,70,0)
                pyxel.rect(140,185,5,70,0)
                pyxel.rect(100,250,45,10,0)
                pyxel.rect(120,255,6,6,13)
        
        #Dessine le prof
        pyxel.rect(100,50,30,70,15)
        pyxel.rect(100,80,30,70,6)
        if danger == 0:
            pyxel.rect(100,50,30,70,15)
            pyxel.rect(100,80,30,70,6)
        if danger == 1:
            pyxel.rect(105,60,5,5,0)
        if danger == 2:
            pyxel.rect(105,60,5,5,0)
            pyxel.rect(120,60,5,5,0) 

        
        #Dessine les powerups
        if powerup == True:
            if powers == 1:
                pyxel.text(180,4, f"BONUS LIFE", 7)
            if powers == 2:
                pyxel.text(180,4, f"BONUS SCORE", 7)
            if powers == 3:
                pyxel.text(180,4, f"SLOWDOWN", 7)
            #Dessine la bar de charge du powerup
            if charging < 80:
                pyxel.rect(180,12,5,1,9)
            if charging < 60:
                pyxel.rect(187,12,5,1,9)
            if charging < 40:
                pyxel.rect(194,12,5,1,9)
            if charging < 20:
                pyxel.rect(201,12,5,1,9)
            if charging < 1:
                pyxel.rect(208,12,5,1,9)

def update():
    global game_speed
    global score
    global game_over
    global lives
    global increase_score
    global countdown
    global danger
    global faster
    global high_score
    global powerup
    global powers
    global charging
    global bonus_score
    global expire
    global ik_prevention
    
    if game_over == False:
        
        bonus_score -= 1 #Permet au powerup "Bonus Score" de finir
        
        #Augmente le score
        if increase_score == True:
            score += 1
            faster+= 1
            #Si le powerup "Bonus Score" est actif, double le score obtenu
            if bonus_score > 0:
                score +=1

        #Accélère le jeu
        if faster == 100 and game_speed > 1:
            game_speed -= 1
            faster = 0
        
        #Controles
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_SPACE):
            increase_score = False
        else:
            increase_score = True
        
        #Controle le prof
        if pyxel.frame_count % game_speed == 0 and score > 100:        
            if danger != 0:
                countdown -= 1
           #Détermine si le le prof commence se retourne   
            if danger == 0 and randint(1,10) == 10:
                danger = 1
            if countdown == 5:
                danger = 2
            if countdown == 0:
                danger = 0
                countdown = 7
                ik_prevention = False
        
        #Détermine si un powerup est activé et en selectionne un
        if powerup == False and randint(1,400) == 400:
            powerup = True
            charging = 100
            powers = randint(1,3)           
        
        #Permet au powerup d'expiré si le joueur ne l'obtient pas à temps
        if powerup == True:
            expire +=1
        if expire == 160:
            powerup = False
            powers = 0
            charging = 0
            expire = 0
        
        #Permet au joueur d'obtenir le powerup
        if increase_score == True and charging > 0:
            charging -= 1
        if charging < 1:
            if powers == 1:
                lives +=1
                powerup = False
                powers = 0
                expire = 0
            if powers == 2:
                bonus_score = 200
                powerup = False
                powers = 0
                expire = 0
            if powers == 3:
                game_speed += 9
                powerup = False
                powers = 0
                expire = 0                
            
            #Fait que si un joueur est en train d'obtenir des points quand le prof le regarde, il perd une vie
            if danger== 2 and increase_score == True and ik_prevention == False:
                lives -= 1
                ik_prevention = True
        
        #Vérifie si le jeu est perdu et vérifie si un nouveau highscore fut obtenu
        if lives == 0:
            game_over = True
            with open("highscore.txt", 'r') as f:
                previous_score = int(f.readline())
            if score > previous_score:
                with open("highscore.txt", 'w+') as f:
                    f.write(f"{score}")
            with open("highscore.txt", 'r') as f:    
                high_score = int(f.readline())
    
    #Permet au joueur de recommencer le jeu
    if game_over == True:
        if pyxel.btn(pyxel.KEY_SPACE):
                increase_score = True 
                game_over = False
                game_speed = 31
                score = 0
                lives = 1 
                danger = 0
                countdown = 7
                faster = 0
                high_score = 0
                powerup = False 
                powers = 0
                charging = 0
                bonus_score = 0
                expire = 0
                ik_prevention = False


pyxel.run(update,draw)