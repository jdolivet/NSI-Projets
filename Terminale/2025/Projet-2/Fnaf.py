import pyxel
import random

LARGEUR = 160
HAUTEUR = 120
FPS = 30

class Five_Nights_At_Python:
    def __init__(self):
        pyxel.init(LARGEUR, HAUTEUR, fps=FPS, title="Five Nights At Pythons")
        pyxel.load("fnaf.pyxres")  # Assurez-vous que le fichier est dans le dossier
        self.reinitialiser()
        pyxel.run(self.update, self.draw)

    def reinitialiser(self):
        self.porte_fermee = False
        self.fin_de_jeu = False
        self.victoire = False
        self.temps_survecu = 0.0
        self.batterie = 100.0  # Batterie en %
        min_y = 20 + 8
        max_y = HAUTEUR - 20 - 8
        self.animatroniques = [
            {"x": 10, "y": random.randint(min_y, max_y), "sprite_x": 0,  "sprite_y": 0, "vitesse": 0.9},
            {"x": 10, "y": random.randint(min_y, max_y), "sprite_x": 16, "sprite_y": 0, "vitesse": 1},
            {"x": 10, "y": random.randint(min_y, max_y), "sprite_x": 32, "sprite_y": 0, "vitesse": 1.5},
        ]

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if self.fin_de_jeu or self.victoire:
            if pyxel.btnp(pyxel.KEY_R):
                self.reinitialiser()
            return

        # Tenter de fermer la porte seulement si la batterie > 0
        if pyxel.btnp(pyxel.KEY_SPACE) and self.batterie > 0:
            self.porte_fermee = not self.porte_fermee

        # Mise à jour du temps survécu en secondes, accéléré 180x (2 min = 6 heures)
        self.temps_survecu += (1 / FPS) * 360

        # Consommation d'énergie si la porte est fermée
        if self.porte_fermee and self.batterie > 0:
            # Perte de 0.1% par frame (~3% par seconde réel)
            self.batterie -= 0.1
            if self.batterie < 0:
                self.batterie = 0
                self.porte_fermee = False  # La porte s'ouvre automatiquement à batterie vide

        porte_x = LARGEUR - 40
        min_y = 20 + 8
        max_y = HAUTEUR - 20 - 8

        for a in self.animatroniques:
            a["x"] += a["vitesse"]

            if a["x"] >= porte_x:
                if self.porte_fermee:
                    a["x"] = 10
                    a["y"] = random.randint(min_y, max_y)
                else:
                    self.fin_de_jeu = True

        # Vérifier si l'heure est arrivée à 6 AM (6 heures = 21600 secondes)
        if self.temps_survecu >= 6 * 60 * 60:
            self.victoire = True

    def draw(self):
        pyxel.cls(0)  # Fundo preto

        if self.fin_de_jeu:
            pyxel.text(LARGEUR // 2 - 45, HAUTEUR // 2, "JUMPSCARE! GAME OVER!", 7)
            pyxel.text(LARGEUR // 2 - 56, HAUTEUR // 2 + 20, "Appuyez sur R pour recommencer", 7)
            return

        if self.victoire:
            pyxel.text(LARGEUR // 2 - 35, HAUTEUR // 2, "FÉLICITATIONS! VOUS AVEZ GAGNÉ!", 7)
            pyxel.text(LARGEUR // 2 - 56, HAUTEUR // 2 + 20, "Appuyez sur R pour rejouer", 7)
            return

        # Couloir
        pyxel.rect(0, 20, LARGEUR, HAUTEUR - 40, 1)
        pyxel.rectb(0, 20, LARGEUR, HAUTEUR - 40, 7)

        # Porte
        porte_x = LARGEUR - 40
        couleur = 8 if self.porte_fermee else 7
        pyxel.line(porte_x, 20, porte_x, HAUTEUR - 20, couleur)
        etat = "FERMEE" if self.porte_fermee else "OUVERTE"
        pyxel.text(porte_x - 40, 10, f"PORTE: {etat}", 7)

        # Joueur (rectangle bleu)
        pyxel.blt(125, 53, 0, 48, 0, 16, 16, 0)

        # Animatroniques
        for a in self.animatroniques:
            pyxel.blt(int(a["x"]) - 8, int(a["y"]) - 8, 0, a["sprite_x"], a["sprite_y"], 16, 16, 0)

        # Barre de batterie
        largeur_barre = 80
        hauteur_barre = 8
        pyxel.rect(5, 25, largeur_barre, hauteur_barre, 7)  # contour blanc
        largeur_remplie = int(largeur_barre * (self.batterie / 100))
        pyxel.rect(5, 25, largeur_remplie, hauteur_barre, 11)  # remplissage bleu clair

        # Affichage de l'heure simulée (12AM à 6AM)
        total_secondes = int(self.temps_survecu)  # temps simulé en secondes
        total_heures = 12 + total_secondes // 3600  # 12AM = 12h
        total_minutes = (total_secondes % 3600) // 60
        if total_heures > 18:
            total_heures = 18
            total_minutes = 0
        heure_affichee = total_heures if total_heures <= 18 else 18
        heure_12h = heure_affichee if heure_affichee <= 12 else heure_affichee - 12
        am_pm = "AM"  # Toujours AM dans le jeu original
        pyxel.text(5, 5, f"Heure: {heure_12h:02d}:{total_minutes:02d} {am_pm}", 7)

        # Instructions
        pyxel.text(5, HAUTEUR - 10, "ESPACE: ouvrir/fermer porte", 7)


if __name__ == "__main__":
    Five_Nights_At_Python()