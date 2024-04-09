import pyxel, definitions, cartes, fonctions_aux, round_tourner, niveaux

class App:
    def __init__(self):
        pyxel.init(256, 128, title="Monkey Balls")
        
        self.jeu = False
        self.difficulte = "En attente"
        self.carte = "En attente"
        self.tutoriel = True
        self.game_over = False
        self.victoire = True
        self.mute = False
        
        self.liste_ballons = []
        self.liste_singes = []
        self.liste_darts = []
        self.liste_explosions = []
        self.curseur = definitions.Curseur()
        self.vie = 100
        self.monnaie = 2000
        self.round = 1
        self.liste_deploiement = niveaux.round_desire(1)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.curseur.x, self.curseur.y = pyxel.mouse_x, pyxel.mouse_y
        
        if not self.jeu:            
            if self.difficulte == "En attente":
                if 24 <= self.curseur.x <= 39 and 70 <= self.curseur.y <= 85 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.difficulte = "Facile"
                    self.vie = 200
                elif 88 <= self.curseur.x <= 103 and 70 <= self.curseur.y <= 85 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.difficulte = "Moyen"
                    self.vie = 150
                elif 152 <= self.curseur.x <= 167 and 70 <= self.curseur.y <= 85 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
                    self.difficulte = "Difficile"
                    self.vie = 100
                elif 216 <= self.curseur.x <= 231 and 70 <= self.curseur.y <= 85 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.difficulte = "CHIMPS"
                    self.vie = 1
                    
            elif self.carte == "En attente":
                if 16 <= self.curseur.x <= 47 and 70 <= self.curseur.y <= 85 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.carte = "1"
                    if not self.tutoriel:
                        self.jeu = True
                elif 80 <= self.curseur.x <= 111 and 70 <= self.curseur.y <= 85 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.carte = "2"
                    if not self.tutoriel:
                        self.jeu = True
                elif 144 <= self.curseur.x <= 175 and 70 <= self.curseur.y <= 85 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.carte = "3"
                    if not self.tutoriel:
                        self.jeu = True
                elif 208 <= self.curseur.x <= 239 and 70 <= self.curseur.y <= 85 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.carte = "4"
                    if not self.tutoriel:
                        self.jeu = True
                        
            elif self.tutoriel:
                if 105 <= self.curseur.x <= 151 and 60 <= self.curseur.y <= 91 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.tutoriel = False
                    self.jeu = True
                    
            elif self.game_over:
                if 105 <= self.curseur.x <= 151 and 60 <= self.curseur.y <= 91 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.game_over = False
                    self.difficulte = "En attente"
                    self.carte = "En attente"
                    self.liste_ballons = []
                    self.liste_singes = []
                    self.liste_darts = []
                    self.liste_explosions = []
                    self.monnaie = 2000
                    self.round = 1
                    self.liste_deploiement = niveaux.round_desire(1)
                    self.curseur.ameliorer = (False, "vide")
                    self.curseur.etat = "vide"
                    self.jeu = False
                    
            elif self.victoire:
                if 105 <= self.curseur.x <= 151 and 60 <= self.curseur.y <= 91 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    self.victoire = False
                    self.difficulte = "En attente"
                    self.carte = "En attente"
                    self.liste_ballons = []
                    self.liste_singes = []
                    self.liste_darts = []
                    self.liste_explosions = []
                    self.monnaie = 2000
                    self.round = 1
                    self.liste_deploiement = niveaux.round_desire(1)
                    self.curseur.ameliorer = (False, "vide")
                    self.curseur.etat = "vide"
                    self.jeu = False
            
        if self.jeu:
            #On coupe le son
            if pyxel.btnp(pyxel.KEY_M):
                if self.mute:
                    self.mute = False
                elif not self.mute:
                    self.mute = True
                
            if self.liste_deploiement != []:
                round_tourner.deploiement(self.liste_ballons, self.carte, self.liste_deploiement)
            elif self.liste_ballons == []:
                self.round += 1
                #Victoire
                if self.round >= 41 and self.difficulte == "Facile":
                    self.jeu = False
                    self.victoire = True
                    
                elif self.round >= 61 and self.difficulte == "Moyen":
                    self.jeu = False
                    self.victoire = True
                    
                elif self.round >= 81 and self.difficulte == "Difficile":
                    self.jeu = False
                    self.victoire = True
                    
                elif self.round >= 101 and self.difficulte == "CHIMPS":
                    self.jeu = False
                    self.victoire = True
                self.liste_deploiement = niveaux.round_desire(self.round)
                        
            #Si le joueur clique sur la case d'achat d'un singe
            if 200 <= self.curseur.x <= 215 and 16 <= self.curseur.y <= 31 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)\
               and self.monnaie >= 150:
                self.curseur.ameliorer = (False, "vide")
                self.curseur.choisirSinge("Singe")
            
            #Même chose pour un super singe
            elif 220 <= self.curseur.x <= 235 and 16 <= self.curseur.y <= 31 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)\
                 and self.monnaie >= 1000:
                self.curseur.ameliorer = (False, "vide")
                self.curseur.choisirSinge("Super")
                
            #Même chose pour un tack shooter
            elif 240 <= self.curseur.x <= 256 and 16 <= self.curseur.y <= 31 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)\
                 and self.monnaie >= 300:
                self.curseur.ameliorer = (False, "vide")
                self.curseur.choisirSinge("Tack")
                
            #Même chose pour une tour de bombe
            elif 200 <= self.curseur.x <= 215 and 40 <= self.curseur.y <= 55 and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)\
                 and self.monnaie >= 450:
                self.curseur.ameliorer = (False, "vide")
                self.curseur.choisirSinge("Bomb")
            
            #On place un singe
            elif self.curseur.etat != 'vide' and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)\
                 and self.curseur.x < 200:
                singe = self.curseur.placer()
                approuve = True
                #On teste si le placement n'est pas sur un singe déjà placé
                for singe_places in self.liste_singes:
                    if fonctions_aux.collision(singe_places, singe):
                        approuve = False
                if approuve:
                    self.liste_singes.append(singe)
                    self.monnaie -= singe.prix
                
            #On fait une amélioration d'un singe,
            #Premiere etape, choix de l'amelioration
            #Il faut qu'un singe soit choisi avant
            elif self.curseur.ameliorer[0] and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                singe = self.curseur.ameliorer[1]
                #Le joueur choisi le chemin du haut
                if 200 <= self.curseur.x <= 215 and 100 <= self.curseur.y <= 115\
                   and self.monnaie >= singe.table_ameliorations[0]:
                    singe.ameliorer("top")
                    if singe.ameliorations[0] <= 4:
                        self.monnaie -= singe.table_ameliorations[0]
                #Le joueur choisi le chemin du milieu
                elif 220 <= self.curseur.x <= 235 and 100 <= self.curseur.y <= 115\
                   and self.monnaie >= singe.table_ameliorations[1]:
                    singe.ameliorer("mid")
                    if singe.ameliorations[1] <= 4:
                        self.monnaie -= singe.table_ameliorations[1]
                #Le joueur choisi le chemin du bas
                elif 240 <= self.curseur.x <= 255 and 100 <= self.curseur.y <= 115\
                   and self.monnaie >= singe.table_ameliorations[2]:
                    singe.ameliorer("bot")
                    if singe.ameliorations[2] <= 4:
                        self.monnaie -= singe.table_ameliorations[2]
                #Pas de choix
                else:
                    self.curseur.ameliorer = (False, "vide")
                    
            #Deuxieme etape, choix d'un singe
            elif self.curseur.etat == 'vide' and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                for singe in self.liste_singes:
                    if fonctions_aux.collision(singe, self.curseur):
                        self.curseur.ameliorer = (True, singe)
                        
            #On fait le deplacement selon la carte choisie
            self.vie -= cartes.cartes_mouv(self.liste_ballons, self.carte)
            #Game over
            if self.vie <= 0:
                self.jeu = False
                self.game_over = True
                            
            #On attaque les ballons
            for singe in self.liste_singes:
                tirs = 0
                for ballon in self.liste_ballons:
                    if fonctions_aux.distance((singe.x, singe.y),(ballon.x, ballon.y)) \
                       <= singe.range**2+singe.range \
                       and pyxel.frame_count % singe.cooldown == 0:
                        if singe.type == "Tack":
                            dart = definitions.Dart(singe.x, singe.y, singe.x, singe.y+singe.range, singe.range, singe.percer, singe.degat)
                            self.liste_darts.append(dart)
                            dart = definitions.Dart(singe.x, singe.y, singe.x, singe.y-singe.range, singe.range, singe.percer, singe.degat)
                            self.liste_darts.append(dart)
                            dart = definitions.Dart(singe.x, singe.y, singe.x-singe.range, singe.y, singe.range, singe.percer, singe.degat)
                            self.liste_darts.append(dart)
                            dart = definitions.Dart(singe.x, singe.y, singe.x+singe.range, singe.y, singe.range, singe.percer, singe.degat)
                            self.liste_darts.append(dart)
                            dart = definitions.Dart(singe.x, singe.y, singe.x+singe.range, singe.y+singe.range, singe.range, singe.percer, singe.degat)
                            self.liste_darts.append(dart)
                            dart = definitions.Dart(singe.x, singe.y, singe.x+singe.range, singe.y-singe.range, singe.range, singe.percer, singe.degat)
                            self.liste_darts.append(dart)
                            dart = definitions.Dart(singe.x, singe.y, singe.x-singe.range, singe.y-singe.range, singe.range, singe.percer, singe.degat)
                            self.liste_darts.append(dart)
                            dart = definitions.Dart(singe.x, singe.y, singe.x-singe.range, singe.y+singe.range, singe.range, singe.percer, singe.degat)
                            self.liste_darts.append(dart)
                            
                            tirs += 1
                        else:
                            dart = singe.attaquer(ballon)
                            self.liste_darts.append(dart)
                            tirs += 1
                    if tirs >= singe.nb_tirs:
                        break #On fait le singe attaquer qu'une fois
            
            #On calcule les degats
            for dart in self.liste_darts:
                dart.mouvement()
                if dart.elimination:
                    self.liste_darts.remove(dart)
                for ballon in self.liste_ballons:
                    if fonctions_aux.collision(dart, ballon):
                        self.monnaie += (ballon.valeur * dart.degats)
                        ballon.vies -= dart.degats
                        dart.percer -= 1
                        if dart.percer <= 0:
                             break
                    ballon.check_elimination()
                    if ballon.elimination:
                        if ballon.suivant is not None:
                            for nouveau_ballon in ballon.suivant:
                                self.liste_ballons.append(definitions.Ballon(ballon.x + (ballon.longueur // 2), ballon.y + (ballon.taille // 2), nouveau_ballon))
                        self.liste_explosions.append(definitions.Explosion(ballon.x, ballon.y))
                        self.liste_ballons.remove(ballon)
                        
                        #On ajoute du son, si le joueur veux
                        if not self.mute:
                            pyxel.playm(0, loop = False)
                        
            #On fait une animation d'explosion
            for explosion in self.liste_explosions:
                explosion.temps += 1
                if explosion.temps >= 12:
                    self.liste_explosions.remove(explosion)
        
    def draw(self):
        pyxel.load("my_resource.pyxres", False, False, False, False)
        
        if not self.jeu:
            if self.difficulte == "En attente":
                pyxel.cls(7)
                pyxel.blt(67, 3, 0, 32, 0, -16, 16, 9)
                pyxel.blt(190, 3, 0, 32, 0, 16, -16, 9)
                
                pyxel.blt(196, 15, 0, 48, 64, 16, 32, 9)
                pyxel.text(212, 32, "Pour jouer:", 0)
                pyxel.text(212, 40, "Clic gauche", 0)
                pyxel.text(110, 5, "MONKEY BALLS", 0)
                pyxel.text(86, 13, "Choisissez une difficulte", 0)
                pyxel.text(2, 122, "Le nombre correspond au nombre de rounds a affronter", 0)
                
                pyxel.text(20, 64, "Facile", 0)
                pyxel.rect(24, 70, 16, 16, 11)
                pyxel.text(28, 75, "40", 0)
                
                pyxel.text(87, 64, "Moyen", 0)
                pyxel.rect(88, 70, 16, 16, 10)
                pyxel.text(92, 75, "60", 0)
                
                pyxel.text(143, 64, "Difficile", 0)
                pyxel.rect(152, 70, 16, 16, 8)
                pyxel.text(156, 75, "80", 0)
                
                pyxel.text(212, 64, "CHIMPS", 0)
                pyxel.rect(216, 70, 16, 16, 2)
                pyxel.text(218, 75, "100", 0)
                
                pyxel.rect(self.curseur.x+1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x-1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y+1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y-1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 6)
                
            elif self.carte == "En attente":
                pyxel.cls(7)
                pyxel.blt(76, 3, 0, 32, 0, -16, 16, 9)
                pyxel.blt(178, 3, 0, 32, 0, 16, -16, 9)
                
                pyxel.blt(196, 15, 0, 48, 64, 16, 32, 9)
                pyxel.text(212, 32, "Pour jouer:", 0)
                pyxel.text(212, 40, "Clic gauche", 0)
                pyxel.text(110, 5, "MONKEY BALLS", 0)
                pyxel.text(95, 13, "Choisissez une carte", 0)
                
                pyxel.blt(16, 70, 0, 48, 104, 32, 16, 9)
                pyxel.blt(80, 70, 0, 48, 120, 32, 16, 9)
                pyxel.blt(144, 70, 0, 48, 136, 32, 16, 9)
                pyxel.blt(208, 70, 0, 80, 104, 32, 16, 9)
                
                pyxel.rect(self.curseur.x+1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x-1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y+1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y-1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 6)
                
            elif self.tutoriel:
                pyxel.cls(11)
                pyxel.rect(90, 0, 87, 20, 7)
                pyxel.blt(90, 3, 0, 32, 0, -16, 16, 9)
                pyxel.blt(160, 3, 0, 32, 0, 16, -16, 9)
                
                pyxel.blt(1, 15, 0, 48, 64, 16, 32, 9)
                pyxel.text(17, 32, "Pour jouer:", 0)
                pyxel.text(17, 40, "Clic gauche", 0)
                pyxel.text(110, 5, "MONKEY BALLS", 0)
                pyxel.text(117, 13, "Tutoriel:", 0)
                
                pyxel.rect(200, 0, 56, 128, 7)
                pyxel.rect(199, 0, 1, 128, 0)
                
                pyxel.rect(104, 60, 48, 32, 3)
                pyxel.rectb(103, 59, 50, 33, 0)
                pyxel.text(105, 74, "Cliquez ici!", 0)
                
                pyxel.rect(200, 100, 16, 16, 0)
                pyxel.text(200, 117, "$???", 0)
                pyxel.rect(220, 100, 16, 16, 0)
                pyxel.text(220, 117, "$???", 0)
                pyxel.rect(240, 100, 16, 16, 0)
                pyxel.text(240, 117, "$???", 0)
                
                pyxel.text(1, 1, f"Vies: VIES", 0)
                pyxel.text(1, 8, f"Round: ROUND", 0)
                pyxel.text(201, 1, f"$:MONNAIE ", 0)
                pyxel.rect(200, 16, 16, 16, 12)
                pyxel.blt(200, 16, 0, 16, 0, 16, 16, 9)
                pyxel.text(201, 8, "Singes ici", 0)
                
                pyxel.text(201, 91, "Ameliorations", 0)
                pyxel.text(1, 122, "Cliquer sur singe pour les ameliorer", 0)
                
                pyxel.text(2, 104, "M pour couper le son", 0)
                pyxel.blt(2, 110, 0, 101, 36, 7, 8, 9)
                pyxel.blt(9, 110, 0, 85, 36, 6, 8, 9)
                
                for i in range(3):
                    for l in range(5):
                            pyxel.rect(213 - (3*l) + (20 * i), 123, 2, 2, 0)
                
                pyxel.rect(self.curseur.x+1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x-1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y+1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y-1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 6)
                
            elif self.game_over:
                pyxel.cls(7)
                pyxel.blt(90, 3, 0, 32, 0, -16, 16, 9)
                pyxel.blt(160, 3, 0, 32, 0, 16, -16, 9)
                
                pyxel.text(110, 5, "MONKEY BALLS", 0)
                pyxel.text(117, 13, "GAME OVER", 0)
                
                pyxel.rect(104, 60, 48, 32, 3)
                pyxel.rectb(103, 59, 50, 33, 0)
                pyxel.text(105, 74, "Rejouez ici!", 0)
                
                pyxel.text(105, 45, f"Mode: {self.difficulte}", 0)
                pyxel.text(105, 52, f"Round: {self.round}", 0)
                
                pyxel.rect(self.curseur.x+1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x-1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y+1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y-1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 6)
                
            elif self.victoire:
                pyxel.cls(7)
                pyxel.blt(90, 3, 0, 32, 0, -16, 16, 9)
                pyxel.blt(160, 3, 0, 32, 0, 16, -16, 9)
                
                pyxel.text(110, 5, "MONKEY BALLS", 0)
                pyxel.text(117, 13, "VICTOIRE", 0)
                
                pyxel.rect(104, 60, 48, 32, 3)
                pyxel.rectb(103, 59, 50, 33, 0)
                pyxel.text(105, 74, "Rejouez ici!", 0)
                
                pyxel.text(105, 45, f"Mode: {self.difficulte}", 0)
                pyxel.text(105, 52, f"Round: {self.round - 1}", 0)
                
                pyxel.rect(self.curseur.x+1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x-1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y+1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y-1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 6)
            
        if self.jeu:
            if self.carte == "1":
                pyxel.bltm(0, 0, 0, 0, 0, 200, 128)
            elif self.carte == "2":
                pyxel.bltm(0, 0, 1, 0, 0, 200, 128)
            elif self.carte == "3":
                pyxel.bltm(0, 0, 2, 0, 0, 200, 128)
            elif self.carte == "4":
                pyxel.bltm(0, 0, 3, 0, 0, 200, 128)
                    
            #Le boutons pour faire des ameliorations
            if self.curseur.ameliorer[0]:
                singe = self.curseur.ameliorer[1]
                pyxel.circ(singe.x + (singe.longueur // 2), singe.y + (singe.taille // 2), singe.range, 3)
                pyxel.circb(singe.x + (singe.longueur // 2), singe.y + (singe.taille // 2), singe.range, 0)
                for singe in self.liste_singes:
                    pyxel.blt(singe.x, singe.y, 0, singe.u, singe.v, singe.longueur, singe.taille, 9)
                for ballon in self.liste_ballons:
                    pyxel.blt(ballon.x, ballon.y, 0, ballon.u, ballon.v, ballon.longueur, ballon.taille, 9)
                for explosion in self.liste_explosions:
                    pyxel.blt(explosion.x, explosion.y, 0, 0, 32, 16, 16, 9)
                for dart in self.liste_darts:
                    pyxel.blt(dart.x, dart.y, 0, dart.u, dart.v, dart.longueur, dart.taille, 9)
                pyxel.rect(200, 0, 56, 128, 7)
                pyxel.rect(199, 0, 1, 128, 0)
                pyxel.text(201, 94, f"{singe.table_a_noms[0]}", 0)
                pyxel.blt(200, 100, 0, 48, 32, 16, 16)
                pyxel.text(200, 117, f"${singe.table_ameliorations[0]}", 0)
                pyxel.text(221, 94, f"{singe.table_a_noms[1]}", 0)
                pyxel.blt(220, 100, 0, 32, 32, 16 , 16)
                pyxel.text(220, 117, f"${singe.table_ameliorations[1]}", 0)
                pyxel.text(241, 94, f"{singe.table_a_noms[2]}", 0)
                pyxel.blt(240, 100, 0, 16, 32, 16, 16)
                pyxel.text(240, 117, f"${singe.table_ameliorations[2]}", 0)
            else:
                #Aucun singe est choisi pour etre ameliore
                for singe in self.liste_singes:
                    pyxel.blt(singe.x, singe.y, 0, singe.u, singe.v, singe.longueur, singe.taille, 9)
                for ballon in self.liste_ballons:
                    pyxel.blt(ballon.x, ballon.y, 0, ballon.u, ballon.v, ballon.longueur, ballon.taille, 9)
                for explosion in self.liste_explosions:
                    pyxel.blt(explosion.x, explosion.y, 0, 0, 32, 16, 16, 9)
                for dart in self.liste_darts:
                    pyxel.blt(dart.x, dart.y, 0, dart.u, dart.v, dart.longueur, dart.taille, 9)
                pyxel.rect(200, 0, 56, 128, 7)
                pyxel.rect(199, 0, 1, 128, 0)
                pyxel.rect(200, 100, 16, 16, 0)
                pyxel.text(200, 117, "$???", 0)
                pyxel.rect(220, 100, 16, 16, 0)
                pyxel.text(220, 117, "$???", 0)
                pyxel.rect(240, 100, 16, 16, 0)
                pyxel.text(240, 117, "$???", 0)
            pyxel.text(201, 1, f"$:{self.monnaie}", 0)
            
            #On dessine le choix d'achat d'un simple singe
            pyxel.rect(200, 16, 16, 16, 12)
            pyxel.blt(200, 16, 0, 16, 0, 16, 16, 9)
            pyxel.text(201, 33, "150", 0)
            
            #On dessine le choix d'achat d'un super singe
            pyxel.rect(220, 16, 16, 16, 5)
            pyxel.blt(220, 16, 0, 64, 48, 16, 16, 9)
            pyxel.text(220, 33, "1000", 0)
            
            #On dessine le choix d'achat d'un tack shooter
            pyxel.rect(240, 16, 16, 16, 12)
            pyxel.blt(241, 17, 0, 1, 49, 14, 14, 9)
            pyxel.text(241, 33, "300", 0)
            
            #On dessine le choix d'achat d'une tour de bombe
            pyxel.rect(200, 40, 16, 16, 5)
            pyxel.blt(202, 41, 0, 50, 49, 12, 15, 9)
            pyxel.text(201, 57, "450", 0)
            
            if self.mute:
                pyxel.blt(2, 119, 0, 101, 36, 7, 8, 9)
            else:
                pyxel.blt(2, 119, 0, 85, 36, 6, 8, 9)
                        
            pyxel.text(1, 1, f"Vies: {self.vie}", 0)
            pyxel.text(1, 8, f"Round: {self.round}", 0)
            
            #On dessine l'etat des ameliorations
            if self.curseur.ameliorer[0]:
                singe = self.curseur.ameliorer[1]
                for i in range(3):
                    for j in range(singe.ameliorations[i]):
                        pyxel.rect(201 + (3*j) + (20 * i), 123, 2, 2, 3)
                    for l in range(5 - singe.ameliorations[i]):
                        pyxel.rect(213 - (3*l) + (20 * i), 123, 2, 2, 0)
            else:
                for i in range(3):
                    for l in range(5):
                            pyxel.rect(213 - (3*l) + (20 * i), 123, 2, 2, 0)
            
            #On dessine en dernier le curseur
            if self.curseur.etat == 'vide':
                pyxel.rect(self.curseur.x+1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x-1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y+1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y-1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 6)
            elif self.curseur.etat != 'vide':
                pyxel.rect(self.curseur.x+1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x-1, self.curseur.y, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y+1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y-1, 1, 1, 0)
                pyxel.rect(self.curseur.x, self.curseur.y, self.curseur.longueur, self.curseur.taille, 8)
        
App()
