import pyxel
import math

pyxel.init(160, 120, title="Pavage rhombitrihexagonal")

# -----------------------------
# VARIABLES
# -----------------------------

ang = 0

# Longueur d'un côté de chaque forme
cot = 10

# Distance entre les centres des hexagones
distance = cot * (1 + math.sqrt(3))


# -----------------------------
# ROTATION
# -----------------------------

def tourner_point(x, y):
    centre_x = pyxel.width / 2
    centre_y = pyxel.height / 2

    cos_a = math.cos(ang)
    sin_a = math.sin(ang)

    nouveau_x = (
        centre_x
        + (x - centre_x) * cos_a
        - (y - centre_y) * sin_a
    )

    nouveau_y = (
        centre_y
        + (x - centre_x) * sin_a
        + (y - centre_y) * cos_a
    )

    return nouveau_x, nouveau_y


# -----------------------------
# DESSIN D'UN POLYGONE
# -----------------------------

def dessiner_polygone(points, couleur):
    
    points_rot = []

    for x, y in points:
        points_rot.append(tourner_point(x, y))

    # On remplit le polygone avec des triangs
    # depuis le premier sommet
    for i in range(1, len(points_rot) - 1):

        x1, y1 = points_rot[0]
        x2, y2 = points_rot[i]
        x3, y3 = points_rot[i + 1]

        pyxel.tri(
            x1, y1,
            x2, y2,
            x3, y3,
            couleur
        )

    # Contour du polygone
    for i in range(len(points_rot)):

        x1, y1 = points_rot[i]
        x2, y2 = points_rot[(i + 1) % len(points_rot)]

        pyxel.line(
            x1, y1,
            x2, y2,
            1
        )


# -----------------------------
# HEXAGONE
# -----------------------------

def dessiner_hexagone(x, y):

    points = []

    # Hexagone régulier
    for i in range(6):

        a = math.radians(30 + i * 60)

        px = x + math.cos(a) * cot
        py = y + math.sin(a) * cot

        points.append((px, py))

    dessiner_polygone(points, 8)


# -----------------------------
# CARRE
# -----------------------------

def dessiner_carre(x1, y1, x2, y2):

    # Vecteur du côté entre les deux centres
    dx = x2 - x1
    dy = y2 - y1

    longueur = math.sqrt(dx * dx + dy * dy)

    ux = dx / longueur
    uy = dy / longueur

    # Vecteur perpendiculaire
    px = -uy
    py = ux

    # Centre du carré
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    # Demi-côté
    demi = cot / 2

    # Les quatre coins
    points = [
        (
            cx - ux * demi - px * demi,
            cy - uy * demi - py * demi
        ),

        (
            cx + ux * demi - px * demi,
            cy + uy * demi - py * demi
        ),

        (
            cx + ux * demi + px * demi,
            cy + uy * demi + py * demi
        ),

        (
            cx - ux * demi + px * demi,
            cy - uy * demi + py * demi
        )
    ]

    dessiner_polygone(points, 12)


# -----------------------------
# TRIang
# -----------------------------

def dessiner_triang(x, y, vers_le_haut):

    hauteur = cot * math.sqrt(3) / 2

    if vers_le_haut:

        points = [
            (x - cot / 2, y - hauteur / 3),
            (x + cot / 2, y - hauteur / 3),
            (x, y + 2 * hauteur / 3)
        ]

    else:

        points = [
            (x - cot / 2, y + hauteur / 3),
            (x + cot / 2, y + hauteur / 3),
            (x, y - 2 * hauteur / 3)
        ]

    dessiner_polygone(points, 11)


# -----------------------------
# CENTRE D'UN HEXAGONE
# -----------------------------

def centre_hexagone(colonne, ligne):

    x = (
        pyxel.width / 2
        + colonne * distance
        + ligne * distance / 2
    )

    y = (
        pyxel.height / 2
        + ligne * distance * math.sqrt(3) / 2
    )

    return x, y


# -----------------------------
# UPDATE
# -----------------------------

def update():

    global ang

    # Rotation façon toupie
    ang += 0.025

    if ang >= 2 * math.pi:
        ang -= 2 * math.pi


# -----------------------------
# DRAW
# -----------------------------

def draw():

    pyxel.cls(0)

    # -------------------------
    # HEXAGONES
    # -------------------------

    for ligne in range(-5, 6):

        for colonne in range(-6, 7):

            x, y = centre_hexagone(colonne, ligne)

            dessiner_hexagone(x, y)


    # -------------------------
    # CARRES
    # -------------------------

    # Chaque hexagone est relié
    # à ses 3 voisins.
    #
    # Les 3 directions suffisent
    # pour ne pas dessiner deux fois
    # le même carré.

    for ligne in range(-5, 6):

        for colonne in range(-6, 7):

            x, y = centre_hexagone(colonne, ligne)

            # Voisin à droite
            x2, y2 = centre_hexagone(
                colonne + 1,
                ligne
            )

            dessiner_carre(x, y, x2, y2)

            # Voisin en haut à droite
            x2, y2 = centre_hexagone(
                colonne,
                ligne + 1
            )

            dessiner_carre(x, y, x2, y2)

            # Voisin en haut à gauche
            x2, y2 = centre_hexagone(
                colonne - 1,
                ligne + 1
            )

            dessiner_carre(x, y, x2, y2)


    # -------------------------
    # TRIangS
    # -------------------------

    # Triangs orientés vers le haut

    for ligne in range(-5, 5):

        for colonne in range(-6, 6):

            x1, y1 = centre_hexagone(
                colonne,
                ligne
            )

            x2, y2 = centre_hexagone(
                colonne + 1,
                ligne
            )

            x3, y3 = centre_hexagone(
                colonne,
                ligne + 1
            )

            # Centre du triang
            cx = (x1 + x2 + x3) / 3
            cy = (y1 + y2 + y3) / 3

            dessiner_triang(
                cx,
                cy,
                True
            )


    # Triangs orientés vers le bas

    for ligne in range(-5, 5):

        for colonne in range(-6, 6):

            x1, y1 = centre_hexagone(
                colonne + 1,
                ligne + 1
            )

            x2, y2 = centre_hexagone(
                colonne,
                ligne + 1
            )

            x3, y3 = centre_hexagone(
                colonne + 1,
                ligne
            )

            # Centre du triang
            cx = (x1 + x2 + x3) / 3
            cy = (y1 + y2 + y3) / 3

            dessiner_triang(
                cx,
                cy,
                False
            )


pyxel.run(update, draw)
