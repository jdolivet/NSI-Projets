import pyxel
from random import randint, shuffle

class Jeu:
    def __init__(self):
        """
        Initialise le jeu Pyxel et les variables principales.
        - ecran : écran actuel ("menu", "partie", "victoire", "defaite").
        - choix : indice de l’option sélectionnée dans le menu.
        - option_text : options du menu.
        - lancer_partie, plateau_charge : indicateurs d’état de la partie.
        Lance la boucle principale pyxel.run(update, draw).
        """
        pyxel.init(900, 500, title="Jeu")
        self.ecran = "menu" 
        self.couleur = 7
        self.choix = 0
        self.option_text = ["Nouvelle partie","Regle","Quitter"]

        self.lancer_partie = False
        self.plateau_charge = False
        pyxel.run(self.update, self.draw)


    def update(self):
        """
        Fonction principale de mise à jour (logique du jeu).
        Appelle la fonction update correspondant à l’écran actuel :
        - update_menu() si ecran == "menu"
        - update_partie() si ecran == "partie"
        - gestion simple des écrans "victoire" et "defaite" (touche Q).
        """
        if self.ecran == "menu":
            self.update_menu()
        elif self.ecran == "partie":
            self.update_partie()
        elif self.ecran == "regle":
            self.update_regle()
        elif self.ecran == "victoire":
            if pyxel.btnp(pyxel.KEY_Q):
                self.ecran = "menu"
        elif self.ecran == "defaite":
            if pyxel.btnp(pyxel.KEY_Q):
                self.ecran = "menu"
        

    def draw(self):
        """
        Fonction principale d’affichage.
        Appelle la fonction draw correspondant à l’écran actuel :
        - draw_menu(), draw_partie(),draw_regle(), draw_victoire(), draw_defaite().
        """
        if self.ecran == "menu":
            self.draw_menu()
        elif self.ecran == "partie":
            self.draw_partie()
        elif self.ecran == "regle":
            self.draw_regle()
        elif self.ecran == "victoire":
            self.draw_victoire()
        elif self.ecran == "defaite":
            self.draw_defaite()
        

# ---------- MENU -----------------------------------------------------------------------------------------------------------------------------------
    def update_menu(self):
        """
        Gère la logique du menu principal :
        - Flèches haut/bas : changer l’option sélectionnée.
        - ENTRÉE : valider l’option.
          • 0 : lancer une nouvelle partie (écran "partie").
          • 1 : lance les régles(écran "partie").
          • 2 : quitter le jeu.
        """
        if pyxel.btnp(pyxel.KEY_UP):
            self.choix = (self.choix - 1) % len(self.option_text)

        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.choix = (self.choix + 1) % len(self.option_text)

        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.choix == 0:  # Nouvelle partie
                self.ecran = "partie"
                self.lancer_partie = True
                self.initialiser_partie()
            elif self.choix == 1:  # Regle
                self.ecran = "regle"
            elif self.choix == 2:  # Quitter
                pyxel.quit()


    def draw_menu(self):
        """
        Affiche le menu principal :
        - Liste des options (Nouvelle partie, Regle, Quitter).
        - Flèche ">" devant l’option sélectionnée.
        """
        pyxel.cls(0)
        for i in range(len(self.option_text)):
            y = 50 + i * 10  

            if self.choix == i:
                pyxel.text(40, y, ">", 8)
                pyxel.text(50, y, self.option_text[self.choix], 8)
            else:
                pyxel.text(50, y, self.option_text[i], self.couleur) 

   
#-----------REGLE---------------------------------------------------------------------------------------------------------------------------------- 
    def update_regle(self):
        """Gère l'écran des règles :
        - Q : revenir au menu.
        """
        if pyxel.btnp(pyxel.KEY_Q):
            self.ecran = "menu"

    def draw_regle(self):
        """Affiche l'écran des règles du jeu.
        Reprend le texte fourni, découpé en sections lisibles.
        """
        pyxel.cls(0)
        
        pyxel.text(60, 10, "REGLES DU JEU", 10)

        # Objectif
        pyxel.text(50, 40, "Objectif :", 7)
        pyxel.text(50, 50, "- Decouvrir la solution secrete composee de 3 cartes :", 7)
        pyxel.text(70, 60, "un personnage, une arme et une piece.", 7)
        pyxel.text(70, 70, "Ces 3 cartes forment la solution et sont mises", 7)
        pyxel.text(70, 80, "de cote au debut de la partie.", 7)

        # Début de partie
        pyxel.text(50, 100, "Debut de partie :", 7)
        pyxel.text(50, 110, "- 3 cartes (personnage, arme, piece) sont tirees", 7)
        pyxel.text(70, 120, "au hasard pour former la solution.", 7)
        pyxel.text(50, 130, "- Les autres cartes sont melangees et distribuees", 7)
        pyxel.text(70, 140, "aux joueurs.", 7)
        pyxel.text(50, 150, "- Le joueur humain est le pion Blanc ;", 7)
        pyxel.text(70, 160, "les autres pions sont des bots.", 7)

        # Phases principales
        pyxel.text(50, 180, "Phases principales :", 7)

        pyxel.text(50, 195, "ATTENTE_DE :", 7)
        pyxel.text(70, 205, "- ESPACE : lancer les des", 7)
        pyxel.text(90, 215, "(somme = nb de cases a parcourir).", 7)
        pyxel.text(70, 225, "- A : ouvrir une accusation", 7)
        pyxel.text(90, 235, "(choisir personnage, arme, piece).", 7)

        pyxel.text(50, 250, "DEPLACEMENT :", 7)
        pyxel.text(70, 260, "- Fleches : deplacer le pion case par case.", 7)
        pyxel.text(70, 270, "- E : si le pion est devant une porte,", 7)
        pyxel.text(90, 280, "ouvrir une suggestion", 7)
        pyxel.text(110, 290, "(la piece est imposee par la porte).", 7)

        pyxel.text(50, 305, "SUGGESTION :", 7)
        pyxel.text(70, 315, "- Le joueur choisit un personnage et une arme", 7)
        pyxel.text(90, 325, "(la piece est deja determinee par la porte).", 7)
        pyxel.text(70, 335, "- Les autres joueurs doivent, si possible,", 7)
        pyxel.text(90, 345, "montrer une carte qui contredit la suggestion.", 7)

        pyxel.text(50, 360, "FIN_SUGGESTION :", 7)
        pyxel.text(70, 370, "- Affiche la suggestion et la carte montree", 7)
        pyxel.text(90, 380, "(ou l'absence de carte).", 7)
        pyxel.text(70, 390, "- ESPACE : terminer la suggestion", 7)
        pyxel.text(90, 400, "et passer a FIN_TOUR.", 7)

        pyxel.text(50, 415, "FIN_TOUR :", 7)
        pyxel.text(70, 425, "- ESPACE : passer le tour au joueur suivant.", 7)

        pyxel.text(450, 40, "ACCUSATION :", 7)
        pyxel.text(470, 50, "- Le joueur choisit successivement", 7)
        pyxel.text(490, 60, "un personnage, une arme, puis une piece", 7)
        pyxel.text(490, 70, "parmi toutes les cartes.", 7)
        pyxel.text(470, 80, "- Si l'accusation correspond exactement", 7)
        pyxel.text(490, 90, "a la solution : ecran VICTOIRE.", 7)
        pyxel.text(470, 100, "- Sinon : ecran PERDU avec affichage", 7)
        pyxel.text(490, 110, "de la solution.", 7)

        # Fin de partie
        pyxel.text(450, 130, "Fin de partie :", 7)
        pyxel.text(450, 140, "- Victoire : accusation exacte = solution.", 7)
        pyxel.text(450, 150, "- Defaite : accusation fausse.", 7)
        pyxel.text(450, 160, "- Q : revenir au menu depuis n'importe", 7)
        pyxel.text(470, 170, "quel ecran de fin.", 7)

        pyxel.text(450, 190, "Appuyez sur Q pour revenir au menu", 7)

        

# ---------- PARTIE -------------------------------------------------------------------------------------------------------------------------------

    def initialiser_partie(self):
        """
        Initialise une nouvelle partie :
        - Charge le tilemap du plateau.
        - Définit les listes de personnages, armes et pièces.
        - Crée les joueurs (pions) avec leurs positions et attributs.
        - Génère la solution secrète (3 cartes).
        - Construit le paquet de cartes restantes et les distribue.
        - Initialise les zones interdites, les portes et les pièces.
        - Met en place les variables de jeu (phase, dés, déplacement, etc.).
        """
        pyxel.load("plateau.pyxres")
     
        self.plateau_charge = True

      
        
        self.personnage = ["Blanc","Rouge","Vert","Violet","Jaune","Bleu"]
        self.arme = ["Poignard", "Revolver", "Chandelier", "Corde", "Matraque", "Clef anglaise"]
        self.piece = ["Cuisine", "Bibliothèque", "Salon", "Salle à manger", "Bureau", "Hall", "Billard", "Veranda", "Salle de bal"]


        self.joueurs = [
        {"nom": "Blanc","x": 402,"y": 41,"img": 1,"u": 32,"v": 208,"w": 15,"h": 30, "cartes": [], "humain": True},
        {"nom": "Rouge", "x": 370,"y": 425,"img": 1,"u": 32,"v": 48,"w": 15,"h": 30, "cartes": [], "humain": False},
        {"nom": "Vert", "x": 482,"y": 41,"img": 1,"u": 32,"v": 80,"w": 15,"h": 30, "cartes": [], "humain": False},
        {"nom": "Violet", "x": 626,"y": 345,"img": 1,"u": 32,"v": 144,"w": 15,"h": 30, "cartes": [], "humain": False},
        {"nom": "Jaune", "x": 258,"y": 313,"img": 1,"u": 32,"v": 110,"w": 15,"h": 32, "cartes": [], "humain": False},
        {"nom": "Bleu", "x": 626,"y": 137,"img": 1,"u": 32,"v": 176,"w": 15,"h": 30, "cartes": [], "humain": False}
        ]

        self.liste_choix = [
        "Blanc","Rouge","Vert","Violet","Jaune","Bleu",
        "Poignard", "Revolver", "Chandelier", "Corde", "Matraque", "Clef anglaise",
        "Cuisine", "Bibliothèque", "Salon", "Salle à manger", "Bureau", "Hall","Billard", "Veranda", "Salle de bal"
        ]

        # Taille d'une case (en pixels)
        self.taille_case = 16

        # Résultat du dés
        self.resultat_de_un = 0
        self.resultat_de_deux = 0
        self.deplacement = 0

        self.joueur_actuel = 0

        self.saisie_texte = ""          # texte en cours de saisie
        self.saisie_valide = False      # devient True quand le joueur a validé
        self.suggestion_en_cours = None
        self.accusation_en_cours = {
            "personnage": None,
            "arme": None,
            "piece": None
            }


        self.phase = "ATTENTE_DE"
        self.cases_parcourues = 0
        
        #Avoir la solution
        self.solution = [
        ("personnage", self.personnage[randint(0, 5)]),
        ("arme",       self.arme[randint(0, 5)]),
        ("piece",      self.piece[randint(0, 8)]),
        ]

      
        # Pour mélanger les cartes afin de les distribue aux joueurs
        ens = set()
        
        for per in self.personnage:
            ens.add(("personnage", per))
        for ar in self.arme:
            ens.add(("arme", ar))
        for piece in self.piece:
            ens.add(("piece", piece))
        
        ens.remove(self.solution[0])
        ens.remove(self.solution[1])
        ens.remove(self.solution[2])


        self.cartes = list(ens)   
        shuffle(self.cartes)

        self.choix_possibles = []
        i = 0
        for c in self.liste_choix:
                est_dans_solution = False
                for sol in self.solution:
                    if c == sol[1]:  # sol[1] = nom de la carte solution
                        est_dans_solution = True
                        break
                if not est_dans_solution:
                    self.choix_possibles = self.choix_possibles + [c]
                    i += 1

        self.nb_joueurs = 6
        cartes_par_joueur = 3

        self.mains = [0] * self.nb_joueurs

        for j in range(self.nb_joueurs):
            debut = j * cartes_par_joueur
            fin = debut + cartes_par_joueur
            # crée une sous-liste de 3 cartes
            self.joueurs[j]["cartes"] = self.cartes[debut:fin]

        self.humain = 0

        #délimatation du plateau
        self.zones_interdites = [
        # (x_min, x_max, y_min, y_max)
        (0, 242, 0, 500),
        (0, 900, 0, 41),
        (642, 900, 0, 500),
        (0, 900, 440, 500),
        ]

        self.zones_porte =  {
            "Cuisine": [(322, 153)],
            "Salle de bal": [(402, 153), (482, 153)],
            "Veranda":[(562, 121)],
            "Billard": [(546, 185), (578, 169)],
            "Bibliothèque": [(530, 297), (578, 265)],
            "Bureau": [(530, 377)],
            "Hall": [(482, 361), (434, 329), (450, 329)],
            "Salon": [(354, 345)],
            "Salle à manger": [(354, 281), (370, 329)],
        
        
            }

        self.zones_pieces = {
            "Cuisine": [(258, 338, 57, 137)],
            "Salle de bal": [(386, 498, 73, 153),],
            "Veranda": [(546, 626, 57, 105), (562, 626, 121, 121),],
            "Billard": [(546, 626, 169, 233)],
            "Bibliothèque": [(546, 626, 265, 329), (530, 530, 281, 313),],
            "Bureau": [(530, 610, 377, 425)],
            "Hall": [(402, 482, 329, 425)],
            "Salon": [(258, 345, 354, 409)],
            "Salle à manger": [(258, 370, 201, 281), (258, 322, 185, 185),],
        
        
            }

        




    def case_est_valide(self, x, y):
        """
        Vérifie si une case (x, y) est valide pour le déplacement :
        - Doit être dans les limites du plateau.
        - Ne doit pas appartenir à une zone interdite.
        - Ne doit pas être à l’intérieur d’une pièce.
        Retourne True si la case est valide, False sinon.
        """
        if x < 0 or y < 0:
            return False
        

        for (xmin, xmax, ymin, ymax) in self.zones_interdites:
            if xmin <= x <= xmax and ymin <= y <= ymax:
                return False
        for nom_piece, zones in self.zones_pieces.items():
            for (xmin, xmax, ymin, ymax) in zones:
                if xmin <= x <= xmax and ymin <= y <= ymax:
                    return False

        return True

    def piece_dans_laquelle_est(self, joueur):
        """
        Retourne le nom de la pièce dans laquelle se trouve le joueur.
        Si le joueur n’est dans aucune pièce, retourne None.
        """
        for nom_piece, zones in self.zones_pieces.items():
            x = joueur["x"]
            y = joueur["y"]
            for (xmin, xmax, ymin, ymax) in zones:
                if xmin <= x <= xmax and ymin <= y <= ymax:
                    return nom_piece  # ou True si tu veux juste un booléen
        return None
        
 

    def est_dans_piece(self, joueur):
        """
        Retourne True si le joueur est dans une pièce, False sinon.
        """
        for nom_piece, zones in self.zones_pieces.items():
            x = joueur["x"]
            y = joueur["y"]
            for (xmin, xmax, ymin, ymax) in zones:
                if xmin <= x <= xmax and ymin <= y <= ymax:
                    return True
                    
        return False

    def est_sur_une_porte(self, joueur):
        """
        Retourne le nom de la pièce associée si le joueur est exactement
        sur une case de porte, sinon retourne None.
        """
        x = joueur["x"]
        y = joueur["y"]
        for nom_piece, portes in self.zones_porte.items():
            for (xp, yp) in portes:
                if x == xp and y == yp:
                    return nom_piece  # retourne le nom de la pièce associée
        return None

    def porte_proche(self, joueur):
        """
        Renvoie le nom de la pièce si le joueur est à côté d’une porte, 
        sinon retourne None.
        """
        x = joueur["x"]
        y = joueur["y"]
        for nom_piece, portes in self.zones_porte.items():
            for (xp, yp) in portes:
                if abs(x - xp) + abs(y - yp) <= self.taille_case:
                    return nom_piece
        return None


        

    def deplacement_des_pions(self, joueur):
        """
        Déplace automatiquement un pion non humain (bot) :
        - Choisit une direction aléatoire (haut, bas, gauche, droite).
        - Déplace le pion d’une case si la case est valide.
        - Incrémente cases_parcourues.
        Ne fait rien si cases_parcourues >= deplacement.
        """
        if self.cases_parcourues >= self.deplacement:
            return

        direction = randint(0, 3)

        if direction == 0: #droite
            nouvelle_x = joueur["x"] + self.taille_case
            nouvelle_y = joueur["y"]
        elif direction == 1: #gauche

            nouvelle_x = joueur["x"]
            nouvelle_y = joueur["y"] - self.taille_case
        elif direction == 2:#bas
            nouvelle_x = joueur["x"]
            nouvelle_y = joueur["y"] + self.taille_case
        elif direction == 3:# haut
            nouvelle_x = joueur["x"] -  self.taille_case
            nouvelle_y = joueur["y"]

        if self.case_est_valide(nouvelle_x, nouvelle_y):
            joueur["x"] = nouvelle_x
            joueur["y"] = nouvelle_y
            self.cases_parcourues += 1

    def update_suggestion(self):
        """
        Gère la phase de suggestion :
        - Le joueur choisit un personnage et une arme parmi les choix_possibles
          (la pièce est déjà imposée par la porte).
        - Utilise les touches a, b, c, ... pour sélectionner un élément.
        - Passe ensuite à la phase "REFUTATION".
        """
        for i in range(len(self.choix_possibles)):
            code_touche = pyxel.KEY_A + i
            if pyxel.btnp(code_touche):
                choix = self.choix_possibles[i]  # élément correspondant à la touche

                if choix in self.personnage:
                    self.suggestion_en_cours["personnage"] = choix
                elif choix in self.arme:
                    self.suggestion_en_cours["arme"] = choix
                   

                # passer à la phase suivante
                self.phase = "REFUTATION"  # ou "FIN_SUGGESTION"
                return

    def update_accusation(self):
        """
        Gère la phase d’accusation :
        - Le joueur choisit successivement un personnage, une arme, puis
          une pièce parmi toutes les cartes (liste_choix).
        - Utilise les touches a, b, c, ... pour sélectionner un élément.
        - Quand les 3 choix sont faits, compare l’accusation à la solution :
          • Si égale : écran "victoire".
          • Sinon : écran "defaite".
        """
        for i in range(len(self.liste_choix)):
            code_touche = pyxel.KEY_A + i
            if pyxel.btnp(code_touche):
                choix = self.liste_choix[i]

            # 1. Remplir personnage si pas encore rempli
                if self.accusation_en_cours["personnage"] is None:
                    if choix in self.personnage:
                        self.accusation_en_cours["personnage"] = choix
                        return  # on attend le prochain choix

            # 2. Remplir arme si personnage déjà choisi
                elif self.accusation_en_cours["arme"] is None:
                    if choix in self.arme:
                        self.accusation_en_cours["arme"] = choix
                        return

            # 3. Remplir pièce si personnage et arme déjà choisis
                elif self.accusation_en_cours["piece"] is None:
                    if choix in self.piece:
                        self.accusation_en_cours["piece"] = choix

            # 4. Si les 3 sont remplis, on vérifie
                if (self.accusation_en_cours["personnage"] is not None and
                    self.accusation_en_cours["arme"] is not None and
                    self.accusation_en_cours["piece"] is not None):

                    acc = [
                        ("personnage", self.accusation_en_cours["personnage"]),
                        ("arme",       self.accusation_en_cours["arme"]),
                        ("piece",      self.accusation_en_cours["piece"]),
                        ]

                    if acc == self.solution:
                        self.ecran = "victoire"
                    else:
                        self.ecran = "defaite"

                return
    
    def update_partie(self):
        """
         Gère la logique principale de la partie :
        - Q : revenir au menu.
        - Phases :
          • ATTENTE_DE : lancer les dés (ESPACE) ou ouvrir une accusation (A).
          • DEPLACEMENT : déplacer le pion (flèches) et ouvrir une suggestion
            avec E si devant une porte.
          • SUGGESTION, REFUTATION, FIN_SUGGESTION : gérer l’enquête.
          • ACCUSATION : appeler update_accusation().
          • FIN_TOUR : passer au joueur suivant.
        """
       
        if pyxel.btnp(pyxel.KEY_Q):
            self.ecran = "menu"  # revenir au menu
        
        joueur = self.joueurs[self.joueur_actuel]

        if self.phase == "ATTENTE_DE":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.resultat_de_un = randint(1, 6)
                self.resultat_de_deux = randint(1, 6)
                self.deplacement = self.resultat_de_un + self.resultat_de_deux
                self.phase = "DEPLACEMENT"

            # Lancer une accusation avec la touche A
            if pyxel.btnp(pyxel.KEY_A):
                self.phase = "ACCUSATION"
                self.accusation_en_cours = {
                    "personnage": None,
                    "arme": None,
                    "piece": None
                    }

        elif self.phase == "DEPLACEMENT":
            if self.cases_parcourues >= self.deplacement:
                piece = self.est_sur_une_porte(joueur)
                if piece is not None:
            # Le joueur est sur une porte donc on lance la suggestion
                    self.suggestion_en_cours = {
                        "piece": piece,
                        "personnage": None,
                        "arme": None
                    }
                    self.phase = "SUGGESTION"
                else:
                    self.phase = "FIN_TOUR"
                return

        


            if joueur["humain"]:

                if pyxel.btnp(pyxel.KEY_RIGHT):
                    nouvelle_x = joueur["x"] + self.taille_case
                    nouvelle_y = joueur["y"]
                    if self.case_est_valide(nouvelle_x, nouvelle_y):
                        joueur["x"] = nouvelle_x
                        joueur["y"] = nouvelle_y
                        self.cases_parcourues += 1
                        
                elif pyxel.btnp(pyxel.KEY_LEFT):
                    nouvelle_x = joueur["x"] - self.taille_case
                    nouvelle_y = joueur["y"]
                    if self.case_est_valide(nouvelle_x, nouvelle_y):
                        joueur["x"] = nouvelle_x
                        joueur["y"] = nouvelle_y
                        self.cases_parcourues += 1

                elif pyxel.btnp(pyxel.KEY_UP):
                    nouvelle_x = joueur["x"]
                    nouvelle_y = joueur["y"] - self.taille_case  
                    if self.case_est_valide(nouvelle_x, nouvelle_y):
                        joueur["x"] = nouvelle_x
                        joueur["y"] = nouvelle_y
                        self.cases_parcourues += 1
                        
                elif pyxel.btnp(pyxel.KEY_DOWN):
                    nouvelle_x = joueur["x"]
                    nouvelle_y = joueur["y"] + self.taille_case 
                    if self.case_est_valide(nouvelle_x, nouvelle_y):
                        joueur["x"] = nouvelle_x
                        joueur["y"] = nouvelle_y
                        self.cases_parcourues += 1 

                if pyxel.btnp(pyxel.KEY_E):
                    piece = self.porte_proche(joueur)
                    if piece is not None:
                        self.suggestion_en_cours = {
                            "piece": piece,
                            "personnage": None,
                            "arme": None
                            }
                        self.phase = "SUGGESTION"
                         # on sort directement, le tour reste en SUGGESTION
                        return

            else:
        # Déplacement automatique des autres pions
                self.deplacement_des_pions(joueur)

        # Fin du déplacement (seulement si on n'est pas déjà passé en SUGGESTION)
            if self.cases_parcourues >= self.deplacement:
                self.phase = "FIN_TOUR"
                return 
            
        elif self.phase == "SUGGESTION":
            self.update_suggestion()

        elif self.phase == "REFUTATION":
            carte_montree = None
            for j in self.joueurs:
                if j["nom"] == "Blanc": # on ne regarde pas les cartes de Blanc comme on les connait déjà
                    continue
                for c in j["cartes"]:
                    if c in [
                ("personnage", self.suggestion_en_cours["personnage"]),
                ("arme", self.suggestion_en_cours["arme"]),
                ("piece", self.suggestion_en_cours["piece"])]:
                        carte_montree = c
                        joueur_qui_montre = j
                        break
                if carte_montree:
                    break
            self.carte_montree = carte_montree
            self.joueur_qui_montre = joueur_qui_montre
            self.phase = "FIN_SUGGESTION"

        elif self.phase == "FIN_SUGGESTION":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.phase = "FIN_TOUR"

        elif self.phase == "ACCUSATION":
            self.update_accusation()


        elif self.phase == "FIN_TOUR":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.resultat_de_un = 0
                self.resultat_de_deux = 0
                self.deplacement = 0
                self.cases_parcourues = 0
                self.phase = "ATTENTE_DE"

                if self.joueur_actuel == 5:
                    self.joueur_actuel = 0
                else: 
                    self.joueur_actuel = self.joueur_actuel + 1


            
        

                

    def draw_partie(self):
        """
        Affiche l’écran de jeu pendant la partie :
        - Plateau (tilemap).
        - Pions de tous les joueurs.
        - Affichages selon la phase (suggestion, accusation, etc.).
        - Informations : dés, déplacement, phase, position, tour, cartes du Blanc.
        - Bloc « INFOS / AIDE » avec les raccourcis clavier.
        """
        pyxel.cls(0)
        joueur_blanc = None
        for j in self.joueurs:
            if j["nom"] == "Blanc":
                joueur_blanc = j
                break

        if self.plateau_charge:
            pyxel.bltm((900 - 384)//2, (500 - 408)//2, 0, 0, 0, 384, 408)
        joueur = self.joueurs[self.joueur_actuel]

        if self.phase == "SUGGESTION":
            self.draw_suggestion()
        elif self.phase == "FIN_SUGGESTION":
            self.draw_fin_suggestion()
        elif self.phase == "ACCUSATION":
            self.draw_accusation()
        #Personnages
        for elt in self.joueurs:
            pyxel.blt(elt["x"],elt["y"],elt["img"],elt["u"],elt["v"],elt["w"],elt["h"],colkey=0)

      
        
        if joueur_blanc is not None:
            pyxel.text(5, 5, f"Cartes: {joueur_blanc['cartes']}", 7)
        pyxel.text(5, 15, f"De1: {self.resultat_de_un}", 7)
        pyxel.text(5, 25, f"De2: {self.resultat_de_deux}", 7)
        pyxel.text(5, 35, f"Deplacement: {self.deplacement}", 7)
        pyxel.text(5, 45, f"Phase: {self.phase}", 7)
        pyxel.text(5, 55, f"Cases: {self.cases_parcourues}/{self.deplacement}", 7)
        pyxel.text(5, 65, f'X: {joueur["x"]}', 7)
        pyxel.text(5, 75, f'Y: {joueur["y"]}', 7)
        nom_actuel = self.joueurs[self.joueur_actuel]["nom"]
        pyxel.text(5, 85, f"Tour: {nom_actuel}", 7)
   
        

        # Informations / Aide
        pyxel.text(5, 250, "INFOS / AIDE :", 7)
        pyxel.text(5, 260, "Pendant la phase ATTENTE_DE :", 7)
        pyxel.text(5, 270, "  -ESPACE : lancer les dés", 7)
        pyxel.text(5, 280, "  -A : ouvrir une accusation", 7)
        pyxel.text(5, 290, "Pendant la phase DEPLACEMENT :", 7)
        pyxel.text(5, 300, "  -Fleches : deplacer le pion", 7)
        pyxel.text(5, 310, "  -E : suggestion (devant une porte)", 7)
        pyxel.text(5, 320, "Pendant la phase FIN_TOUR :", 7)
        pyxel.text(5, 330, "  -ESPACE plusieurs fois : lancer passer le tour", 7)
        pyxel.text(5, 340, "Q : menu", 7)


       

    def draw_suggestion(self):
        """
        Affiche l’écran de suggestion :
        - Titre "SUGGESTION".
        - Liste des choix possibles (personnages, armes, pièces hors solution).
        - Indication des touches a, b, c, ...
        """
        if self.phase != "SUGGESTION":
            return

        pyxel.text(700, 95, "SUGGESTION", 7)
        pyxel.text(700, 105, "Choisissez un element:", 7)
        y = 120
        for i, choix in enumerate(self.choix_possibles):
            lettre = chr(ord('a') + i)  # a, b, c, ...
            pyxel.text(700, y, f"{lettre}. {choix}", 7)
            y += 10
        pyxel.text(650, y + 5, "Appuyez sur a/b/c... pour choisir une des suggestion suivante", 7)

    def draw_fin_suggestion(self):
        """
        Affiche le résultat de la suggestion :
        - Suggestion effectuée (personnage / arme / pièce).
        - Carte montrée par un autre joueur, ou message si aucune carte.
        - Indication pour appuyer sur ESPACE pour continuer.
        """
        if self.phase == "FIN_SUGGESTION":
            pyxel.text(700, 95, "RESULTAT DE LA SUGGESTION", 7)
            
            s = self.suggestion_en_cours
            pyxel.text(700, 115, f"Suggestion : {s['personnage']} / {s['arme']} / {s['piece']}", 7)
            
            if self.carte_montree is not None and self.joueur_qui_montre is not None:
                type_c, nom_c = self.carte_montree
                nom_j = self.joueur_qui_montre["nom"]
                pyxel.text(700, 130, f"Le joueur {nom_j} montre : {type_c} - {nom_c}", 7)
            else:
                pyxel.text(700, 145, "Aucun joueur ne peut montrer de carte.", 7)
            pyxel.text(700, 160, "Appuyez sur ESPACE pour continuer", 7)

    def draw_accusation(self):
        """
        Affiche l’écran d’accusation :
        - Titre "ACCUSATION".
        - Liste de tous les choix (personnages, armes, pièces).
        - Indication des touches a, b, c, ...
        - Récapitulatif de l’accusation en cours (personnage, arme, pièce).
        """
        if self.phase != "ACCUSATION":
            return
        pyxel.text(700, 95, "ACCUSATION", 7)
        pyxel.text(700, 105, "Choisissez un element:", 7)
        y = 120
        for i, choix in enumerate(self.liste_choix):
            lettre = chr(ord('a') + i)
            pyxel.text(700, y, f"{lettre}. {choix}", 7)
            y += 10

        pyxel.text(650, y + 5, "Appuyez sur a/b/c... pour accuser", 7)
        a = self.accusation_en_cours
        pyxel.text(100, 180, "Accusation en cours :", 7)
        pyxel.text(100, 190, f"Personnage: {a['personnage']}", 7)
        pyxel.text(100, 200, f"Arme: {a['arme']}", 7)
        pyxel.text(100, 210, f"Piece: {a['piece']}", 7)

    def draw_victoire(self):
        """
        Affiche l’écran de victoire :
        - Message "VICTOIRE".
        - Indication que le joueur a trouvé la bonne solution.
        - Rappel pour appuyer sur Q pour revenir au menu.
        """
        pyxel.cls(0)
        pyxel.text(350, 200, "VICTOIRE", 10)
        pyxel.text(250, 220, "Vous avez trouvé la bonne solution !", 7)
        pyxel.text(250, 240, "Appuyez sur Q pour revenir au menu", 7)

    def draw_defaite(self):
        """
        Affiche l’écran de défaite :
        - Message "PERDU".
        - Indication que ce n’était pas la bonne solution.
        - Affichage détaillé de la solution (personnage, arme, pièce).
        - Rappel pour appuyer sur Q pour revenir au menu.
        """
        pyxel.cls(0)
        pyxel.text(350, 200, "PERDU", 8)
        pyxel.text(250, 220, "Ce n'était pas la bonne solution.", 7)
        # Afficher la solution
        pyxel.text(250, 250, "La solution etait :", 7)
        sol = self.solution
        pyxel.text(250, 265, f"Personnage: {sol[0][1]}", 7)
        pyxel.text(250, 280, f"Arme: {sol[1][1]}", 7)
        pyxel.text(250, 295, f"Piece: {sol[2][1]}", 7)

        pyxel.text(250, 320, "Appuyez sur Q pour revenir au menu", 7)
        

Jeu()