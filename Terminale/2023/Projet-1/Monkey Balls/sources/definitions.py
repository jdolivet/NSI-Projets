import fonctions_aux, math

class Singe:
    def __init__(self, coord_x, coord_y, type_singe: str):        
        self.range = 30 #Cercle d'attaque
        self.cooldown = 30 #Temps d'attaque
        
        self.longueur = 16
        self.taille = 16
        
        self.x = coord_x - (self.longueur // 2)
        self.y = coord_y - (self.taille // 2)
        
        self.type = type_singe
        self.nb_tirs = 1
        self.percer = 3
        self.degat = 1
        self.ameliorations = [0, 0, 0] #Aucune amelioration
        self.table_ameliorations = [300, 250, 120]
        self.table_a_noms = ["DMG", "CNT", "RNG"]
        
        if type_singe == "Singe":
            self.u = 16
            self.v = 0
            self.prix = 150
            
        elif type_singe == "Super":
            self.u = 64
            self.v = 48
            self.prix = 1000
            self.cooldown = 10
            
        elif type_singe == "Tack":
            self.u = 1
            self.v = 49
            self.prix = 300
            self.longueur = 14
            self.taille = 14
            self.cooldown = 60
            self.percer = 1
            
        elif type_singe == "Bomb":
            self.u = 50
            self.v = 49
            self.prix = 450
            self.degat = 15
            self.percer = 15
            self.longueur = 12
            self.taille = 15
            
    def attaquer(self, u):
        return Dart(self.x, self.y, u.x, u.y, self.range, self.percer, self.degat)
    
    def ameliorer(self, choix: str):
        if self.type == "Singe" or self.type == "Super" or self.type == "Tack" or self.type == "Bomb":
            if choix == "top" and self.ameliorations[0] <= 4:
                self.degat += 2
                self.ameliorations[0] += 1
            elif choix == "mid" and self.ameliorations[1] <= 4:
                self.nb_tirs += 2
                self.ameliorations[1] += 1
            elif choix == "bot" and self.ameliorations[2] <= 4:
                self.range += 10
                self.ameliorations[2] += 1

class Ballon:
    def __init__(self, coord_x, coord_y, nom):        
        self.couleur = nom
        self.elimination = False
        
        #Configuration normales pour les Bloons simples
        self.longueur = 12
        self.taille = 16
        
        self.valeur = 1
        self.vies = 1
        self.v = 16
        
        #Variable pour utiliser pendant le mouvement
        self.tour = 0
        
        if nom == "Rouge":
            self.u = 18
            self.suivant = None
            
        elif nom == "Bleu":
            self.u = 2
            self.suivant = ["Rouge"]
            
        elif nom == "Vert":
            self.u = 34
            self.suivant = ["Bleu"]
            
        elif nom == "Jaune":
            self.u = 50
            self.suivant = ["Vert"]
            
        elif nom == "Rose":
            self.u = 178
            self.suivant = ["Jaune"]
            
        elif nom == "Noir":
            self.u = 114
            self.suivant = ["Rose", "Rose"]
            
        elif nom == "Blanc":
            self.u = 162
            self.suivant = ["Rose", "Rose"]
            
        elif nom == "Violet":
            self.u = 210
            self.suivant = ["Rose", "Rose"]
            
        elif nom == "Zebra":
            self.u = 98
            self.suivant = ["Noir", "Blanc"]
            
        elif nom == "Arc-en-ciel":
            self.u = 82
            self.suivant = ["Zebra", "Zebra"]
            
        elif nom == "Plomb":
            self.u = 194
            self.suivant = ["Noir", "Noir"]
            
        elif nom == "Ceramique":
            self.u = 130
            self.vies = 10
            self.suivant = ["Arc-en-ciel", "Arc-en-ciel"]
            
        elif nom == "Moab":
            self.u = 0
            self.v = 117
            self.vies = 200
            self.suivant = ["Ceramique", "Ceramique", "Ceramique", "Ceramique"]
            self.longueur = 34
            self.taille = 21
            
        elif nom == "Bfb":
            self.u = 114
            self.v = 157
            self.vies = 700
            self.suivant = ["Moab", "Moab", "Moab", "Moab"]
            self.longueur = 32
            self.taille = 21
            
        elif nom == "Zomg":
            self.u = 112
            self.v = 120
            self.vies = 4000
            self.suivant = ["Bfb", "Bfb", "Bfb", "Bfb"]
            self.longueur = 34
            self.taille = 32
            
        elif nom == "Ddt":
            self.u = 80
            self.v = 121
            self.vies = 480
            self.suivant = ["Ceramique", "Ceramique", "Ceramique", "Ceramique"]
            self.longueur = 31
            self.taille = 30
        
        elif nom == "Bad":
            self.u = 0
            self.v = 64
            self.vies = 20000
            self.suivant = ["Zomg", "Zomg", "Ddt", "Ddt", "Ddt"]
            self.longueur = 34
            self.taille = 32
            
        self.x = coord_x - (self.longueur // 2)
        self.y = coord_y - (self.taille // 2)
            
    def check_elimination(self):
        if self.vies <= 0:
            self.elimination = True
            
    def __repr__(self):
        return f"{self.couleur}"
    
class Dart:
    def __init__(self, coord_x, coord_y, trajet_x, trajet_y, range_limite, nb_perce, nb_degat):
        self.depart_x = coord_x
        self.depart_y = coord_y
        
        self.x = coord_x
        self.y = coord_y
        
        self.arrive_x = trajet_x
        self.arrive_y = trajet_y
        
        self.range = range_limite
        self.elimination = False
        
        #Dart 13x5
        self.longueur = 13
        self.taille = 5
        
        #Coordonnées dans l'editeur
        self.u = 16
        self.v = 48
        
        self.percer = nb_perce
        self.degats = nb_degat
        
    def mouvement(self):
        self.x, self.y = fonctions_aux.mouvement((self.depart_x, self.depart_y), (self.arrive_x, self.arrive_y), (self.x, self.y))
        self.correction_angle()
        self.check_elimination()
        
    def check_elimination(self):
        coef_x = self.arrive_x - self.depart_x
        if coef_x > 0 and math.sqrt(fonctions_aux.distance((self.depart_x, self.depart_y), (self.x, self.y))) > self.range:
            self.elimination = True
            
        elif coef_x < 0 and math.sqrt(fonctions_aux.distance((self.depart_x, self.depart_y), (self.x, self.y))) > self.range:
            self.elimination = True
            
        coef_y = self.arrive_y - self.depart_y
        if coef_y > 0 and math.sqrt(fonctions_aux.distance((self.depart_x, self.depart_y), (self.x, self.y))) > self.range:
            self.elimination = True
        
        elif coef_y < 0 and math.sqrt(fonctions_aux.distance((self.depart_x, self.depart_y), (self.x, self.y))) > self.range:
            self.elimination = True
            
        if self.percer <= 0:
            self.elimination = True
            
    def correction_angle(self):
        """On corrige le dart pour aller à la direction attendue"""
        coef_x = self.arrive_x - self.depart_x
        coef_y = self.arrive_y - self.depart_y
        
        if coef_x < 0 and self.longueur > 0:
            self.longueur = -self.longueur

        if coef_y > 0 and self.taille < 0:
            self.taille = -self.taille
            
class Curseur:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.etat = 'vide'
        self.longueur = 1
        self.taille = 1
        
        self.ameliorer = (False, "vide")
        self.singe_choisi = False
        self.super_choisi = False
        self.tack_choisi = False
        self.bomb_choisi = False
        
    def choisirSinge(self, type_singe: str):        
        if type_singe == "Singe":
            self.etat = 'occupé'
            self.singe_choisi = True
            
        if type_singe == "Super":
            self.etat = 'occupé'
            self.super_choisi = True
            
        if type_singe == "Tack":
            self.etat = 'occupé'
            self.tack_choisi = True
            
        if type_singe == "Bomb":
            self.etat = 'occupé'
            self.bomb_choisi = True
            
    def placer(self):
        if self.etat == 'occupé' and self.singe_choisi:
            self.etat = 'vide'
            self.singe_choisi = False
            
            return Singe(self.x, self.y, "Singe")
        
        elif self.etat == "occupé" and self.super_choisi:
            self.etat = "vide"
            self.super_choisi = False
            
            return Singe(self.x, self.y, "Super")
        
        elif self.etat == 'occupé' and self.tack_choisi:
            self.etat = 'vide'
            self.tack_choisi = False
            
            return Singe(self.x, self.y, "Tack")
        
        elif self.etat == 'occupé' and self.bomb_choisi:
            self.etat = 'vide'
            self.bomb_choisi = False
            
            return Singe(self.x, self.y, "Bomb")
            
class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.temps = 0