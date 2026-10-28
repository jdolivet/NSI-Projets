import pyxel
import math
from random import randint

pyxel.init(160, 120, title="Pavage hexagonal adouci")

# -----------------------------
# VARIABLES
# -----------------------------

a = 0

# Longueur du côté des trias
cote = 9

# Centre de l'écran
centre_x = pyxel.width / 2
centre_y = pyxel.height / 2
col1=2
col2=9

# -----------------------------
# ROTATION
# -----------------------------

def tourner(x, y):
    cos_a = math.cos(a)
    sin_a = math.sin(a)

    x2 = (
        centre_x
        + (x - centre_x) * cos_a
        - (y - centre_y) * sin_a
    )

    y2 = (
        centre_y
        + (x - centre_x) * sin_a
        + (y - centre_y) * cos_a
    )

    return x2, y2


# -----------------------------
# POINT DU RESEAU TRIANGULAIRE
# -----------------------------

def point(i, j):
    x = centre_x + cote * (i + j / 2)
    y = centre_y + cote * math.sqrt(3) / 2 * j

    return x, y


# -----------------------------
# POINT SUPPRIME ?
# -----------------------------

def point_supprime(i, j):
    # Le réseau supprimé forme une sous-maille
    # d'indice 7.
    #
    # Les points supprimés sont espacés de sqrt(7)
    # côtés du réseau triangulaire.

    return (
        (3 * i + j) % 7 == 0
        and
        (-i + 2 * j) % 7 == 0
    )


# -----------------------------
# DESSIN D'UN POLYGONE
# -----------------------------

def dessiner_polygone(points, couleur):

    points_rot = []

    for x, y in points:
        points_rot.append(tourner(x, y))

    # Remplissage
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

    # Contour
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

def dessiner_hexagone(i, j):
    global col1
    x, y = point(i, j)

    points = []

    # Les six voisins du sommet supprimé
    voisins = [
        (i + 1, j),
        (i + 1, j - 1),
        (i, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1)
    ]

    for a, b in voisins:
        px, py = point(a, b)
        points.append((px, py))
    
    dessiner_polygone(points, col1)


# -----------------------------
# TRIa
# -----------------------------

def dessiner_tria(i1, j1, i2, j2, i3, j3):
    global col2
    x1, y1 = point(i1, j1)
    x2, y2 = point(i2, j2)
    x3, y3 = point(i3, j3)

    points = [
        (x1, y1),
        (x2, y2),
        (x3, y3)
    ]

    dessiner_polygone(points, col2)

def change_col():
    global col1, col2
    if pyxel.frame_count%25==0:
        col1=randint(1, 7)
    if pyxel.frame_count%15==0:
        col2=randint(8, 15)

# -----------------------------
# UPDATE
# -----------------------------

def update():

    global a

    # Rotation du pavage
    a += 0.025

    if a >= 2 * math.pi:
        a -= 2 * math.pi


# -----------------------------
# DRAW
# -----------------------------

def draw():

    pyxel.cls(0)

    # -------------------------
    # HEXAGONES
    # -------------------------
    change_col()
    for j in range(-12, 13):

        for i in range(-14, 15):

            if point_supprime(i, j):

                dessiner_hexagone(i, j)


    # -------------------------
    # TRIaS
    # -------------------------

    for j in range(-13, 13):

        for i in range(-15, 15):

            # Premier tria
            #
            #       (i,j+1)
            #       /    \
            #      /      \
            # (i,j) ------ (i+1,j)

            a = (i, j)
            b = (i + 1, j)
            c = (i, j + 1)

            if (
                not point_supprime(a[0], a[1])
                and not point_supprime(b[0], b[1])
                and not point_supprime(c[0], c[1])
            ):

                dessiner_tria(
                    a[0], a[1],
                    b[0], b[1],
                    c[0], c[1]
                )


            # Deuxième tria
            #
            # (i+1,j+1) ---- (i,j+1)
            #       \          /
            #        \        /
            #         \      /
            #          (i+1,j)

            a = (i + 1, j + 1)
            b = (i + 1, j)
            c = (i, j + 1)

            if (
                not point_supprime(a[0], a[1])
                and not point_supprime(b[0], b[1])
                and not point_supprime(c[0], c[1])
            ):

                dessiner_tria(
                    a[0], a[1],
                    b[0], b[1],
                    c[0], c[1]
                )


pyxel.run(update, draw)
