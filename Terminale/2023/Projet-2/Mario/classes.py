import pyxel

ennemis = ["goomba", "koopa troopa"]

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        self.mini = True
        if self.mini:
            self.taille = 16
        else:
            self.taille = 37
            
        self.u = 0
        self.v = 0
        self.longueur = 16
            
        self.a = 1 #Animation du mouvement
        self.inverse = False #dessin inverse
        
        self.mort = False
        
        
        self.saut = False
        self.t = 0 # Temps du saut
        
    def mouvement_vertical(self):
        "Mouvement vertical"
        self.y += 2 #Gravite
        
        if self.t > 0:
            self.t -= 1
            self.y -= 4
            if self.t <= 16:
                self.y += 2
        
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP)) and self.saut:
            if self.mini:
                self.u, self.v = 0, 16
            else:
                self.u, self.v = 79, 104
            self.saut = False
            self.t = 48
        
        #Le joueur n'a pas de point d'appuis pour sauter
        self.saut = False
        
        if self.y >= 256:
            self.mort = True
            
    def collision_ennemi(self, entites):
        "Si on touche un ennemi"
        for entite in entites:
            if -16 <= entite.x <= 264 and entite.vivant:
                if ( self.x < entite.x + entite.longueur ) and\
                       ( self.y < entite.y + entite.taille ) and\
                       ( self.x + self.longueur > entite.x) and\
                       ( self.y + self.taille > entite.y):
                    if entite.quoi in ennemis:
                        if self.y + self.taille - 1 <= entite.y + 1:
                            entite.vivant = False
                        else:
                            if not self.mini:
                                self.y -= 20
                                self.grandir()
                            else:
                                self.mort = True
                    else:
                        if self.mini:
                            self.grandir()
                            entites.remove(entite)
                        
    def grandir(self):
        "Joueur grandit"
        if self.mini:
            self.mini = False
            self.taille = 37
            
        elif not self.mini:
            self.mini = True
            self.taille = 16
                    
            
class Bloc:
    def __init__(self, x: int, y: int, u: int, v: int, tangible: bool = True, contenu: list = []):
        self.x = x
        self.y = y
        
        self.u = u
        self.v = v
        
        self.tangible = tangible
        
        self.contenu = contenu
        
        if u == 192 and v == 83:
            self.longueur = 24
            self.taille = 32
        else:
            self.longueur, self.taille = 16, 16
        
    def collision(self, other):
        recul = 0

        if ( self.x < other.x + other.longueur ) and\
           ( self.y < other.y + other.taille ) and\
           ( self.x + 16 > other.x) and\
           ( self.y + 16 > other.y):
            
            if other.y + 15 <= self.y + 1: #Collision supérieure
                if type(other) == Player and self.tangible:
                    other.y -= 2
                    if other.t < 1:
                        other.saut = True
                        if not (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT)):
                            if other.mini:
                                other.u, other.v = 0,0
                            else:
                                other.u, other.v = 14, 32
                elif type(other) != Player:
                    other.y -= 2
                        
                
            elif (self.y + 13) <= other.y <= (self.y + 16): #Collision inférieure
                if type(other) == Player and self.tangible:
                    other.y = self.y + 16
                    other.t = 0
                    
                    if self.u == 32 and self.v == 16 and not other.mini:
                        recul = -9 #il ne s'agit pas d'un recul mais une commande pour enlever ce bloc
                    elif self.u == 48 and self.v == 16:
                        self.u, self.v = 72, 72
                elif type(other) != Player:
                    other.y = self.y + 16
            
            elif other.x <= self.x: #Collision gauche
                if type(other) == Player and self.tangible:
                    recul = 1
                    if self.contenu == ["victoire"]:
                        other.mort = True
                if type(other) != Player:
                    other.collisione()
                
            elif other.x <= (self.x + 16): #Collision droite
                if type(other) == Player and self.tangible:
                    recul = -1
                if type(other) != Player:
                    other.collisione()
            
        return recul
    
class Entite:
    def __init__(self, x: int, y: int, direction: int, quoi: str):
        self.x = x
        self.y = y
        
        if quoi == "goomba":
            
            self.u = 136
            self.v = 0
        
            self.longueur = 16
            self.taille = 16
            
        elif quoi == "koopa troopa":
            self.u = 158
            self.v = 22
            
            self.longueur = 17
            self.taille = 26
            
        elif quoi == "champignon":
            self.u = 144
            self.v = 112
            
            self.longueur = 16
            self.taille = 16
        
        self.quoi = quoi #Ennemi ou objet
        
        self.direction = direction
        self.vivant = True
        self.t = 48
        
    def mouvement(self):
        if self.vivant:
            self.y += 2
            self.x += (0.5 * self.direction)
            if self.quoi == "goomba":
                if self.u == 136:
                    self.u = 152
                elif self.u == 152:
                    self.u = 136
            elif self.quoi == "koopa troopa":
                if self.u == 158:
                    self.u = 190
                elif self.u == 190:
                    self.u = 158
        else:
            if self.quoi == "goomba":
                self.u, self.v = 136, 16
            elif self.quoi == "koopa troopa":
                self.u, self.v = 216, 22
            self.t -= 1
        
    def collisione(self):
        if self.vivant:
            self.direction *= -1
        
        
    