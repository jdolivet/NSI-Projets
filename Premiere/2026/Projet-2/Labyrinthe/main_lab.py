import pyxel
import regles_lab
import jeux_lab


ecran_regles = True


def update() -> None:
    """Gère le passage entre les règles et le jeu."""

    global ecran_regles

    if ecran_regles:
        if pyxel.btnp(pyxel.KEY_1):
            ecran_regles = False
            jeux_lab.charger()
    else:
        jeux_lab.update()


def draw() -> None:
    """Affiche les règles ou le jeu."""

    if ecran_regles:
        regles_lab.draw()
    else:
        jeux_lab.draw()


pyxel.init(176, 176, title="Labyrinthe")

pyxel.run(update, draw)