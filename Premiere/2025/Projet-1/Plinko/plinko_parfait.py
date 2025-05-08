import pyxel
import random

class PlinkoParfait:
    def __init__(self):
        pyxel.init(200, 250, title="PLINKO PARFAIT", fps=60)
        self.billes = []
        self.argent = 1000
        self.mise = 25
        self.piquets = []
        self.creer_piquets_denses()
        self.multiplicateurs = [10, 5, 2, 0.5, 0.2, 0.5, 2, 5, 10]  # Symétrique
        pyxel.run(self.mettre_a_jour, self.dessiner)

    def creer_piquets_denses(self):
        """Crée des piquets très rapprochés"""
        for y in range(30, 170, 12):  # Espacement vertical 
            decalage = 6 if (y//12) % 2 else 0
            for x in range(decalage, 200, 12):  # Espacement horizontal 
                self.piquets.append((x, y))

    def lancer_bille(self):
        if self.argent >= self.mise and len(self.billes) < 8:
            self.argent -= self.mise
            x = 100 + (random.random() - 0.5) * 10
            self.billes.append([x, 20, 0, 0])  # x, y, vx, vy

    def appliquer_physique(self, bille):
        x, y, vx, vy = bille
          
        # Physique allégée
        vy += 0.1  # Gravité 
        vx *= 0.98  # Frottement
        vy *= 0.98
        
        # Collisions avec piquets
        for px, py in self.piquets:
            dx = x - px
            dy = y - py
            if dx*dx + dy*dy < 16:  # Distance^2 < 4^2
                vx += dx * 0.08
                vy += dy * 0.08
        
        # Bordures
        if x < 5 or x > 195:
            vx = -vx * 0.7
        
        return [x + vx, y + vy, vx, vy]

    def mettre_a_jour(self):
        # Contrôles
        if pyxel.btnp(pyxel.KEY_UP) and self.mise + 5 <= self.argent:
            self.mise += 5
        if pyxel.btnp(pyxel.KEY_DOWN) and self.mise > 5:
            self.mise -= 5
        
        if pyxel.btn(pyxel.KEY_SPACE) and pyxel.frame_count % 5 == 0:
            self.lancer_bille()
        
        # Mise à jour physique
        self.billes = [self.appliquer_physique(b) for b in self.billes if b[1] < 230]
        
        # Vérifier les gains
        for i, (x, y, _, _) in enumerate(self.billes):
            if y >= 180:
                zone = min(int(x / (200/9)), 8)  # 9 zones
                self.argent += int(self.mise * self.multiplicateurs[zone])
                self.billes.pop(i)
                break

    def dessiner(self):
        pyxel.cls(0)
        
        # Piquets (denses)
        for x, y in self.piquets:
            pyxel.circ(x, y, 2, 8)
        
        # Billes (blanches)
        for x, y, _, _ in self.billes:
            pyxel.circ(x, y, 2, 7)
        
        # Zones de gain (symétriques)
        largeur_zone = 200 / len(self.multiplicateurs)
        couleurs = [9, 8, 7, 6, 5, 6, 7, 8, 9]  # Dégradé symétrique
        for i, (mult, col) in enumerate(zip(self.multiplicateurs, couleurs)):
            pyxel.rect(i*largeur_zone, 180, largeur_zone, 40, col)
            pyxel.text(i*largeur_zone+5, 190, f"x{mult}", 0)
        
        # Interface
        pyxel.text(10, 10, f"ARGENT: ${self.argent}", 7)
        pyxel.text(10, 20, f"MISE: ${self.mise} (▲/▼ +5)", 7)
        pyxel.text(10, 220, "ESPACE: LANCER", 7)
        pyxel.text(10, 230, "▲/▼: MODIFIER MISE", 7) 

PlinkoParfait()