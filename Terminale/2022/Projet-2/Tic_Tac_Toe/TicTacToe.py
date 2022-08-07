import pyxel, random, time

gagnant = None  #Il n'y a pas de gagnant au debut
score_x = 0    #le score des joueurs est une variable globale pour être actualisée tout au long de l'éxécution du code.
score_o = 0
best_score = 0
val_aleatoire = 0
x1 = 0      # x et y sont les coordonées des cases ou le joueur a mis le X ou le O
y1 = 0

def actualise_best_score(): #Fonctio pour actualizer, et afficher le score entre les joueurs
    global best_score, score_x, score_o
    if score_x >= score_o:
        score = score_x
    else:
        score = score_o
    with open('TicTacToe.txt','w+') as fichier:
        texte = fichier.readline()
        if texte == '':
            texte = 0
        if score > int(texte):
            fichier.writelines(str(score))
            best_score = score

class App:
    """Jeu TicTacToe, contient une interface graphique, musique et designs personalisés avec le framework Pyxel.
    
    Jouabilité: Se fait avec le clavier ou la sourie, ou les 2. Choix à critère des joueurs.
    Tip: pour le 1v1, un joueur peut jouer avec clavier pendant que l'autre avec la sourie.
    
    Clavier : flèches du clavier, UP, DOWN, LEFT, RIGHT et appuyer SPACEBAR pour confirmer le tour dans la case choisie.
    Sourie: Left click a la grille pour choisir et Right click pour confirmer le tour dans la case choisie.
    
    Le mode de jeu '1v1' se joue à deux joueurs situées au même ordinateur, avec le joueur X étant toujours le premier a jouer.
    Le choix des joueurs X et O est complètement à critère des joueurs.
    Le mode de jeu 'Humain v Robot' se joue avec un joueur contre l'ordinateur, qui placera le O aléatoirement et sans stratégie aucune à son tour.
    
    Suivez les instructions situées à l'interface pour une meilleure jouabilité.
    Dès que vous êtes au menu de choix, il suffit d'appuiez au bouton contenant un X en face du dessin du mode de jeu,
    soit appuyez 1 pour jouer '1v1' ou 2 pour jouer 'Humain v Robot'
    
    Appuiez N pour arreter la musique et M pour la recommencer à n'importe quel moment.
    
    Appuiez Q en plein jeu pour quitter la partie.
    
    Appuiez Delete pour sortir du jeu.
    """
    
    def __init__(self):
        pyxel.init(53,53, fps = 30) # largeur et longueur de l'interface
        pyxel.load("TicTacToe.pyxres") #Fichier avec musique et dessins personalisés
        self.x = 19 #Position x initiale
        self.y = 19 #Position y initiale
        self.tours = 0 #Nombre d'objets placés dans la partie 
        self.scene = 0 #Definit l'interface d'initialisation du jeu          
        self.tab_o = []  #Initialisations des variables qui mantiennent la grille actualisée
        self.tab_x = []  #quand on place un objet
        self.bouton1 = False
        self.bouton2 = False
        self.mode = None
        self.tab_coord = [[1,1,False],[19,1,False],[37,1,False],[1,19,False],[19,19,False],[37,19,False],[1,37,False],[19,37,False],[37,37,False]] #Coordonnées du tableau du TikTakToe
        pyxel.playm(0,1,True) #musique initialisée
        pyxel.run(self.update, self.draw) #interface du jeu initialisée
    
    def objets_O_deja_places(self):
        #Execute le tableau qui contient les coordonnés ou un O a été placé
        for i in range(len(self.tab_o)):  #et dessine un O dans les coordonnées comprises             
            pyxel.blt(self.tab_o[i][0], self.tab_o[i][1], 0, 17, 0, 15, 15)
    
    def objets_X_deja_places(self):
        #Execute le tableau qui contient les coordonnés ou un X a été placé
        for i in range(len(self.tab_x)): #et dessine un X dans les coordonnées comprises
            pyxel.blt(self.tab_x[i][0], self.tab_x[i][1], 0, 1, 0, 15, 15)
    
    def winner(self, tab):
        global gagnant, score_x, score_o,x1,x2,y1,y2     #Teste si un joueur a gagné la partie.      
        if (1,1) in tab:  
            if (19,1) in tab:
                if (37,1) in tab:    #Teste les différentes combinaisons possibles pour gagner
                    x1,y1 = 0,5
                    if tab is self.tab_x:
                        gagnant = 'X'
                        score_x += 1   #Fonction marche a la fois pour tester si X a gagné
                    if tab is self.tab_o:  #et si O a gagné.
                        gagnant = 'O'  #Doit cependant verifier quel a été le vaincqueur de la partie
                        score_o += 1   #pour augmenter le score du joueur du jeu total.
                    return True
                
            if (19,19) in tab:
                if (37,37) in tab:
                    x1,x2,y1,y2 = 1,52,1,52
                    if tab is self.tab_x:
                        gagnant = 'X'
                        score_x += 1
                    if tab is self.tab_o:
                        gagnant = 'O'
                        score_o += 1
                    return True
                
            if (1,19) in tab:
                if (1, 37) in tab:
                    
                    if tab is self.tab_x:
                        gagnant = 'X'
                        score_x += 1
                    if tab is self.tab_o:
                        gagnant = 'O'
                        score_o += 1
                    return True
                
        if (1, 19) in tab:
            if (19,19) in tab:
                if (37,19) in tab:
                                        
                    if tab is self.tab_x:
                        gagnant = 'X'
                        score_x += 1
                    if tab is self.tab_o:
                        gagnant = 'O'
                        score_o += 1
                    return True
                
        if (1, 37) in tab:
            if (19,37) in tab:
                if (37,37) in tab:
                                        
                    if tab is self.tab_x:
                        gagnant = 'X'
                        score_x += 1
                    if tab is self.tab_o:
                        gagnant = 'O'
                        score_o += 1
                    return True
                
            if (19,19) in tab:
                if (37,1) in tab:
                                        
                    if tab is self.tab_x:
                        gagnant = 'X'
                        score_x += 1
                    if tab is self.tab_o:
                        gagnant = 'O'
                        score_o += 1
                    return True  
      
        if (19,1) in tab:
            if (19,19) in tab:
                if (19,37) in tab:
                                        
                    if tab is self.tab_x:
                        gagnant = 'X'
                        score_x += 1
                    if tab is self.tab_o:
                        gagnant = 'O'
                        score_o += 1
                    return True
                    
        if (37,1) in tab:
            if (37,19) in tab:
                if (37,37) in tab:
                                        
                    if tab is self.tab_x:
                        gagnant = 'X'
                        score_x += 1
                    if tab is self.tab_o:
                        gagnant = 'O'
                        score_o += 1
                    return True
        
        if self.est_egalite():     #En cas d'égalité le jeu s'arrète.
            self.scene = 2  #L'interface n'est plus celle du jeu, mais oui celle du Game Over.          
            return False
        
    def est_egalite(self):   #fonction pour verifier si le jeu termine en egalité
        global gagnant
        return self.grille_pleine() and gagnant == None and self.tours == 9  #Verifications nescessaires pour voir si le jeu a deja fini
    
    def est_vide(self,x, y):     #Fonction pour voir si la case est vide
        for i in range(len(self.tab_coord)):
            if x == self.tab_coord[i][0] and y == self.tab_coord[i][1]:
                if self.tab_coord[i][2] == True:    #Si tab_coord[i][2] == True alors on ne peut pas jouer car la case a deja un X ou O
                    return False
                elif self.tab_coord[i][2] == False:    #Si tab_coord[i][2] == False alors on peut  jouer car la case n'a aucun X ou O
                    self.tab_coord[i][2] = True
                    return True
    
    def grille_pleine(self):   #Fonction pour voir si la grille est  vide, et pouvoir commencer un nouveau jeu
        for i in range(len(self.tab_coord)):
            if self.tab_coord[i][2] is False:    #Parcour entre les glasses
                return False
        return True
        
    def update_debut(self):  #Fonction update utilisée quand au menu initial.
        pyxel.mouse(True) #Affiche le curseur de la sourie pour confort des joueurs.
        if pyxel.btnp(pyxel.KEY_N):   #Arrete la musique
            pyxel.stop(0)
            pyxel.stop(1)
        if pyxel.btnp(pyxel.KEY_M):  #Recommence la musique
            pyxel.playm(0,1,True)
        if pyxel.btnp(pyxel.KEY_RETURN): #Si enter est appuié,
            self.scene = 3 #On passe a l'interface du jeu
        if pyxel.btnp(pyxel.KEY_DELETE):  #Bouton Delete ferme l'interface par complet.
            pyxel.quit()
    
    def update_menu(self):
        if pyxel.btnp(pyxel.KEY_N):   #Arrete la musique
            pyxel.stop(0)
            pyxel.stop(1)
        if pyxel.btnp(pyxel.KEY_M):  #Recommence la musique
            pyxel.playm(0,1,True)
        pyxel.mouse(True)
        if 40 < pyxel.mouse_x < 51 and 12 < pyxel.mouse_y < 23 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_1):
            self.mode = 0
            self.bouton1 = True
            pyxel.playm(2,1,False)
            time.sleep(0.5)
            self.scene = 1
        if 40 < pyxel.mouse_x < 51 and 35 < pyxel.mouse_y < 46 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_2):
            self.mode = 1
            self.bouton2 = True
            pyxel.playm(2,1,False)
            time.sleep(0.5)
            self.scene = 1
        
    def update_jeu(self):   #Fonction update qui est utilisée durant la partie
        if pyxel.btnp(pyxel.KEY_N):   #Arrete la musique
            pyxel.stop(0)
            pyxel.stop(1)
        if pyxel.btnp(pyxel.KEY_M):  #Recommence la musique
            pyxel.playm(0,1,True)
        if pyxel.btnp(pyxel.KEY_DELETE): 
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_Q): #Si touche Q est appuyée au clavier,
            self.scene = 2 #On passe a l'interface du Game Over
            gagnant = None #Dans ce cas il n'y a pas de vaincqueur.
        if pyxel.btnp(pyxel.KEY_RIGHT) and self.x < 34: #Déplace l'objet a droite tant qu'il reste dans la grille.
            self.x += 18
        if pyxel.btnp(pyxel.KEY_LEFT) and self.x > 1:#Déplace l'objet a gauche tant qu'il reste dans la grille.
            self.x -= 18
        if pyxel.btnp(pyxel.KEY_UP) and self.y > 1:#Déplace l'objet en haut tant qu'il reste dans la grille.
            self.y -= 18
        if pyxel.btnp(pyxel.KEY_DOWN) and self.y < 34: #Déplace l'objet en bas tant qu'il reste dans la grille.
            self.y += 18
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
            if self.est_vide(self.x,self.y): #Si le couple de coordonnées ne contient pas déjà un placement d'objet
                if self.tours % 2 == 0: #Le joueur X est toujours le premier a jouer. Il joue aux tours pairs.
                    self.tab_x.append((self.x,self.y)) #Ajoute les coordonnés au tableau de X, de sorte qu'il sera affiché jusqu'à la fin de la partie
                    self.tours += 1 #Augmente les tours après être sûr que le joueur a effectué un placement valide.
                    pyxel.playm(3,0,False)
                    if self.winner(self.tab_x) != None or self.winner(self.tab_o) != None: #teste si X ou O a gagné la partie 
                        print(x1,y1)
                        pyxel.playm(1,1,False)
                        time.sleep(1)
                        self.scene = 2
                elif self.tours % 2 != 0: #Le joueur O est toujours le deuxième a jouer. Il joue aux tours impairs.
                    self.tab_o.append((self.x,self.y))#Ajoute les coordonnés au tableau de O, de sorte qu'il sera affiché jusqu'à la fin de la partie
                    self.tours += 1 #Augmente les tours après être sûr que le joueur a effectué un placement valide  
                    pyxel.playm(3,0,False)
                    if self.winner(self.tab_x) != None or self.winner(self.tab_o) != None: #teste si X ou O a gagné la partie 
                        pyxel.playm(1,1,False)
                        time.sleep(1)
                        self.scene = 2
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 0 < pyxel.mouse_x < 17:
                self.x = 1
            if 17 < pyxel.mouse_x < 37:  #controle avec le mouse le placement du joueur. 
                self.x = 19
            if 37 < pyxel.mouse_x < 53:   #Space pour confirmer est toujours nécéssaire.
                self.x = 37
            if 0 < pyxel.mouse_y < 17:
                self.y = 1
            if 17 < pyxel.mouse_y < 37:
                self.y = 19
            if 37 < pyxel.mouse_y < 53:
                self.y = 37
    
    def update_jeu_ord(self):
        global gagnant, val_aleatoire
        if pyxel.btnp(pyxel.KEY_N):   #Arrete la musique
            pyxel.stop(0)
            pyxel.stop(1)
        if pyxel.btnp(pyxel.KEY_M):  #Recommence la musique
            pyxel.playm(0,1,True)
        if pyxel.btnp(pyxel.KEY_DELETE): 
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_Q): #Si touche Q est appuyée au clavier,
            self.scene = 2 #On passe a l'interface du Game Over
            gagnant = None #Dans ce cas il n'y a pas de vaincqueur.
        if self.tours % 2 == 0:
            if pyxel.btnp(pyxel.KEY_RIGHT) and self.x < 34: #Déplace l'objet a droite tant qu'il reste dans la grille.
                self.x += 18
            if pyxel.btnp(pyxel.KEY_LEFT) and self.x > 1:#Déplace l'objet a gauche tant qu'il reste dans la grille.
                self.x -= 18
            if pyxel.btnp(pyxel.KEY_UP) and self.y > 1:#Déplace l'objet en haut tant qu'il reste dans la grille.
                self.y -= 18
            if pyxel.btnp(pyxel.KEY_DOWN) and self.y < 34: #Déplace l'objet en bas tant qu'il reste dans la grille.
                self.y += 18
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                if 0 < pyxel.mouse_x < 17:
                    self.x = 1
                if 17 < pyxel.mouse_x < 37:  #controle avec le mouse le placement du joueur. 
                    self.x = 19
                if 37 < pyxel.mouse_x < 53:   #Space pour confirmer est toujours nécéssaire.
                    self.x = 37
                if 0 < pyxel.mouse_y < 17:
                    self.y = 1
                if 17 < pyxel.mouse_y < 37:
                    self.y = 19
                if 37 < pyxel.mouse_y < 53:
                    self.y = 37
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
                if self.est_vide(self.x,self.y): #Si le couple de coordonnées ne contient pas déjà un placement d'objet
                    self.tab_x.append((self.x,self.y))
                    self.tours += 1
                    pyxel.playm(3,0,False)
                    if self.winner(self.tab_x) != None or self.winner(self.tab_o) != None: #teste si X ou O a gagné la partie 
                        pyxel.playm(1,1,False)
                        time.sleep(1)
                        self.scene = 2
        if self.tours % 2 != 0: 
            if self.est_vide(self.tab_coord[val_aleatoire][0],self.tab_coord[val_aleatoire][1]) is True:
                time.sleep(0.5)
                self.tours += 1
                self.tab_o.append((self.tab_coord[val_aleatoire][0],self.tab_coord[val_aleatoire][1]))
                pyxel.playm(3,0,False)
                if self.winner(self.tab_x) != None or self.winner(self.tab_o) != None: #teste si X ou O a gagné la partie 
                   pyxel.playm(1,1,False)
                   pyxel.blt(self.tab_coord[val_aleatoire][0], self.tab_coord[val_aleatoire][1], 0, 17, 0, 15, 15)
                   time.sleep(1)
                   self.scene = 2
            val_aleatoire = random.randint(1,8)
        
                        
    def update_fin(self):  #Fonction update utilisée au menu final, de Game Over.
        pyxel.mouse(True)  #Raffiche le curseur de la sourie.
        self.tab_x = []  #Écrase les valeurs du tableau de X en cas d'un prochain tour
        self.tab_o = [] #Écrase les valeurs du tableau de O en cas d'un prochain tour
        self.tours = 0   #Remet les tours a 0
        self.bouton1 = False
        self.bouton2 = False
        if pyxel.btnp(pyxel.KEY_DELETE):     
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_RETURN): #Si la touche Enter est touchée on repart au menu initial
            pyxel.playm(2,1,False)
            time.sleep(0.2)
            self.scene = 0
        if pyxel.btnp(pyxel.KEY_N):
            pyxel.stop(0)
            pyxel.stop(1)              #Mêmes tests que dans update_debut()
        if pyxel.btnp(pyxel.KEY_M):
            pyxel.playm(0,1,True)
        for i in range(len(self.tab_coord)):
            self.tab_coord[i][2] = False
        actualise_best_score()
       
    def draw_debut(self):
        global score_x,score_o, best_score  #prend les variables de score de chaque joueur pour afficher le score
        pyxel.cls(0) #Fond d'écran noir
        pyxel.blt(9, 5, 0, 33, 3, 32, 9)  #Dessine le dessin personalisé du nom du jeu, TicTacToe.
        pyxel.blt(1, 20, 0, 20, 23, 9, 9) #Dessine le dessin personalisé du symbole X
        pyxel.blt(43, 20, 0, 36, 23, 9, 9) #Dessine le dessin personalisé du symbole O
        pyxel.blt(21, 20, 0, 2, 36, 11, 9)#Dessine le dessin personalisé des épées au centre du score
        pyxel.blt(1, 44, 0, 5, 22, 6, 8)
        pyxel.text(15, 22 ,str(score_x), 1)  #Affiche score de X
        pyxel.text(35, 22 ,str(score_o), 1)  #Affiche score de O
        pyxel.text(8, 45 ,str(best_score), 1)
        pyxel.text(1, 35,'Appuiez Enter', random.randint(1,5)) #Couleur généree avant pour que "Appuiez" et "Enter" aient la même couleur    
                
    def draw_menu(self):
        pyxel.cls(0)
        pyxel.text(3,1,'Choix de jeu', random.randint(1,5))
        pyxel.blt(1, 10, 0, 20, 34, 8, 12) #Dessin du nombre 1
        pyxel.blt(11, 11, 0, 2, 36, 11, 9) #epées
        pyxel.blt(24, 10, 0, 20, 34, 8, 12) #Dessin du nombre 1
        pyxel.blt(2, 30, 0, 20, 49, 7, 19) #Dessin de l'humain
        pyxel.blt(11, 35, 0, 2, 36, 11, 9) #epées
        pyxel.blt(24, 30, 0, 0, 49, 13, 19) #Dessin de l'humain
        if not self.bouton1:
            pyxel.blt(40, 12, 0, 34, 35, 11, 11) #bouton 1
        if not self.bouton2: 
            pyxel.blt(40, 35, 0, 34, 35, 11, 11) #bouton 2
        
    def draw_jeu(self):
        global x1,x2,y1,y2
        pyxel.cls(0)  #Fond d'écran noir.
        if pyxel.frame_count % 10 == 5:
            pyxel.pal(2, 0)
        if pyxel.frame_count % 10 == 0:
            pyxel.pal()
        pyxel.rect(0, 17, 53, 1, 13)
        pyxel.rect(0, 35, 53, 1, 13)   #Affiche la grille grise du jeu
        pyxel.rect(17, 0, 1, 53, 13)
        pyxel.rect(35, 0, 1, 53, 13)
        pyxel.rectb(self.x-1, self.y-1,17,17,2)
        if self.tours % 2 == 0:  #Si les tours sont pairs
            pyxel.blt(self.x, self.y, 0, 1, 0, 15, 15)  #à X de jouer. Affiche X.
        if self.tours % 2 != 0:   #Si les tours sont impairs
            pyxel.blt(self.x, self.y, 0, 17, 0, 15, 15) # à O de jouer. Affiche O
        self.objets_O_deja_places()  #Affiche la grille avec les O déjà placé par le joeur.
        self.objets_X_deja_places() #Pareil pour les X
        #pyxel.line(x1,x2,y1,y2,8)
        #pyxel.blt(x1,5,0,0,77,53,5)
        
    def draw_fin(self):
        couleur_aleatoire = random.randint(1,5)  #Genere avant pour que les differents strings dessous ayent la même couleur au même frame.
        pyxel.cls(0) #Fond noir
        pyxel.blt(9, 5, 0, 33, 3, 32, 9) #Affiche le nom du jeu, TicTacToe
        pyxel.text(10, 35,'Game Over', couleur_aleatoire)  #Affiche Game Over
        pyxel.text(1, 47,'Appuiez Enter', couleur_aleatoire) #Affiche Appuiez Enter (pour retourner au menu initial)
        if gagnant == 'X':   #Si le gagnant de la partie est X
            pyxel.blt(22, 20, 0, 20, 18, 9, 14)  #dessine le dessin personalisé de X gagnant
        if gagnant == 'O': #Si le gagnant de la partie est O
            pyxel.blt(22, 20, 0, 36, 18, 9, 14) #dessine le dessin personalisé de O gagnant
        if gagnant == None:  #Si il y a eu égalité
            pyxel.blt(17, 18, 0, 50, 16, 16, 16) #Affiche un drapeau blanc personnalisé
            
    def draw(self):
        if self.scene == 0:   #Si au menu initial,
            self.draw_debut()  #Dessine le menu intial
        elif self.scene == 1:  #Si au menu de jeu,
            self.draw_jeu()
        elif self.scene == 2:  #Si au menu final,
            self.draw_fin()  #Dessine le menu final
        elif self.scene == 3:
            self.draw_menu()
    
    def update(self):
        if self.scene == 0: #Si au menu initial,
            self.update_debut() #execute la fonction update équivalente.
        elif self.scene == 1:#Si au menu de jeu,
            if self.mode == 0:#execute la fonction update équivalente.
                self.update_jeu()
            elif self.mode == 1:
                self.update_jeu_ord()
        elif self.scene == 2: #Si au menu final,
            self.update_fin()#execute la fonction update équivalente.
        elif self.scene == 3:
            self.update_menu()
        
App()  #Execute la class App et donc le jeu.