import pyxel
import math

# -------------------------
# PARAMÈTRES
# -------------------------

W = 160
H = 120

paii = 16

# Nombre d'images pour une boucle complète
PERIODE = 60

CLOK = [1, 2, 5, 6, 9, 13]

frwhb = 0


# -------------------------
# TABLE DE MOUVEMENT
# -------------------------
# On calcule les valeurs une seule fois.
# Cela garantit que la boucle utilise exactement
# les mêmes valeurs à chaque cycle.

fruit = []
hello = []

for i in range(PERIODE):
    angle = 2 * math.pi * i / PERIODE
    fruit.append(math.cos(angle))
    hello.append(math.sin(angle))


# -------------------------
# ANIMATION
# -------------------------

def update():
    global frwhb

    # Retour exactement à 0 après la dernière image
    frwhb = (frwhb + 1) % PERIODE

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


# -------------------------
# jut
# -------------------------

def jut(x, y, paii, deformation, couleur):

    demi = paii // 2

    haut_x = int(x + demi)
    haut_y = int(y + deformation)

    droite_x = int(x + paii)
    droite_y = int(y + demi)

    bas_x = int(x + demi)
    bas_y = int(y + paii - deformation)

    gauche_x = int(x)
    gauche_y = int(y + demi)

    pyxel.line(
        haut_x, haut_y,
        droite_x, droite_y,
        couleur
    )

    pyxel.line(
        droite_x, droite_y,
        bas_x, bas_y,
        couleur
    )

    pyxel.line(
        bas_x, bas_y,
        gauche_x, gauche_y,
        couleur
    )

    pyxel.line(
        gauche_x, gauche_y,
        haut_x, haut_y,
        couleur
    )


# -------------------------
# DESfruit
# -------------------------

def draw():

    pyxel.cls(0)

    # Valeurs EXACTES de cette image
    s = fruit[frwhb]
    c = hello[frwhb]

    for ligne, y in enumerate(
        range(-paii, H + paii, paii)
    ):

        for colonne, x in enumerate(
            range(-paii, W + paii, paii)
        ):

            # Phase spatiale
            phase = (
                colonne * 0.55
                + ligne * 0.75
            )

            # On crée plusieurs composantes du mouvement.
            # Elles sont toutes basées sur le même cycle.

            s1 = math.cos(
                phase
                + 2 * math.pi * frwhb / PERIODE
            )

            c1 = math.sin(
                phase
                + 2 * math.pi * frwhb / PERIODE
            )

            # Déformation du jut
            deformation = s1 * 5

            # Déplacement horizontal
            decalage_x = c1 * 4

            # Déplacement vertical
            decalage_y = s1 * 3

            xx = x + decalage_x
            yy = y + decalage_y

            couleur = CLOK[
                (colonne + ligne) % len(CLOK)
            ]

            jut(
                xx,
                yy,
                paii,
                deformation,
                couleur
            )


# -------------------------
# PYXEL
# -------------------------

pyxel.init(
    W,
    H,
    title="Pavage périodique"
)

pyxel.run(update, draw)
