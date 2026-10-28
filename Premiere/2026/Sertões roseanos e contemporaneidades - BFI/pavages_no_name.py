import pyxel
import math

pyxel.init(160, 120, title="Pavage de Penrose")

# -----------------------------
# VARIABLES
# -----------------------------

angl = 0

# Nombre de subdivisions
profondeur = 5

# Taille de départ
taille = 50

# Nombre d'or
PHI = (1 + math.sqrt(5)) / 2

centre_x = pyxel.width / 2
centre_y = pyxel.height / 2


# -----------------------------
# ROTATION
# -----------------------------

def tourner(x, y):

    c = math.cos(angl)
    s = math.sin(angl)

    x2 = (
        centre_x
        + (x - centre_x) * c
        - (y - centre_y) * s
    )

    y2 = (
        centre_y
        + (x - centre_x) * s
        + (y - centre_y) * c
    )

    return x2, y2


# -----------------------------
# POINT SUR UN SEGMENT
# -----------------------------

def interpolation(a, b, proportion):

    x = a[0] + (b[0] - a[0]) * proportion
    y = a[1] + (b[1] - a[1]) * proportion

    return (x, y)


# -----------------------------
# DESSIN D'UN TRIangl
# -----------------------------

def triangl(a, b, c, couleur):

    p1 = tourner(a[0], a[1])
    p2 = tourner(b[0], b[1])
    p3 = tourner(c[0], c[1])

    pyxel.tri(
        p1[0], p1[1],
        p2[0], p2[1],
        p3[0], p3[1],
        couleur
    )

    pyxel.line(
        p1[0], p1[1],
        p2[0], p2[1],
        1
    )

    pyxel.line(
        p2[0], p2[1],
        p3[0], p3[1],
        1
    )

    pyxel.line(
        p3[0], p3[1],
        p1[0], p1[1],
        1
    )


# -----------------------------
# SUBDIVISION PENROSE
# -----------------------------

def subdiviser(triangls):

    nouveaux = []

    for triangl_data in triangls:

        a = triangl_data[0]
        b = triangl_data[1]
        c = triangl_data[2]
        type_triangl = triangl_data[3]

        if type_triangl == 0:

            # Triangl aigu

            p = interpolation(a, b, 1 / PHI)
            q = interpolation(a, c, 1 / PHI)

            nouveaux.append(
                (c, q, p, 0)
            )

            nouveaux.append(
                (q, b, p, 1)
            )

            nouveaux.append(
                (b, c, q, 0)
            )

        else:

            # Triangl obtus

            p = interpolation(b, a, 1 / PHI)
            q = interpolation(b, c, 1 / PHI)

            nouveaux.append(
                (p, q, b, 1)
            )

            nouveaux.append(
                (a, p, q, 0)
            )

            nouveaux.append(
                (c, q, p, 0)
            )

            nouveaux.append(
                (a, c, q, 0
            ))

    return nouveaux


# -----------------------------
# CREATION DU PAVAGE
# -----------------------------

def creer_penrose():

    triangls = []

    # On commence avec 10 triangls
    # autour du centre.
    #
    # Cela donne la symétrie d'ordre 10
    # caractéristique de Penrose.

    for i in range(10):

        a1 = 2 * math.pi * i / 10
        a2 = 2 * math.pi * (i + 1) / 10

        centre = (
            centre_x,
            centre_y
        )

        p1 = (
            centre_x + math.cos(a1) * taille,
            centre_y + math.sin(a1) * taille
        )

        p2 = (
            centre_x + math.cos(a2) * taille,
            centre_y + math.sin(a2) * taille
        )

        triangls.append(
            (
                centre,
                p1,
                p2,
                0
            )
        )

    # Subdivisions successives
    for i in range(profondeur):

        triangls = subdiviser(triangls)

    return triangls


# -----------------------------
# CREATION INITIALE
# -----------------------------

triangls = creer_penrose()


# -----------------------------
# UPDATE
# -----------------------------

def update():

    global angl

    # Rotation lente
    angl += 0.015

    if angl >= 2 * math.pi:

        angl -= 2 * math.pi


# -----------------------------
# DRAW
# -----------------------------

def draw():

    pyxel.cls(0)

    for t in triangls:

        a = t[0]
        b = t[1]
        c = t[2]
        type_triangl = t[3]

        if type_triangl == 0:

            triangl(
                a,
                b,
                c,
                9
            )

        else:

            triangl(
                a,
                b,
                c,
                12
            )


pyxel.run(update, draw)
