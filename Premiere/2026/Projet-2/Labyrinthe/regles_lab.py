import pyxel

def draw()->None:
    """affiche les règles du jeu."""

    pyxel.cls(7)

    pyxel.text(63, 4, "REGLES DU JEU", 8)

    pyxel.text(8, 16, "BUT :", 1)
    pyxel.text(8, 26, "Atteindre la sortie des 6 niveaux.", 0)

    pyxel.text(8, 38, "COMMANDES :", 1)
    pyxel.text(8, 48, "Fleche haut    : monter", 0)
    pyxel.text(8, 58, "Fleche bas     : descendre", 0)
    pyxel.text(8, 68, "Fleche gauche  : aller a gauche", 0)
    pyxel.text(8, 78, "Fleche droite  : aller a droite", 0)
    pyxel.text(8, 88, "ESPACE         : recommencer", 0)

    pyxel.text(8, 102, "N1: vision normale / murs sans danger", 3)
    pyxel.text(8, 112, "N2: vision normale / murs qui tuent", 3)
    pyxel.text(8, 122, "N3: vision reduite 2 / murs sans danger", 3)
    pyxel.text(8, 132, "N4: vision reduite 2 / murs qui tuent", 3)
    pyxel.text(8, 142, "N5: vison reduite 1 / murs sans danger", 3)
    pyxel.text(8, 152, "N6: vison reduite 1 / murs qui tuent", 3)
    
    pyxel.text(8, 166, "appuier 1 pour jouer ", 9)