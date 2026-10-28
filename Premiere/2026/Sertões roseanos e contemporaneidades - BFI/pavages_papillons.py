import pyxel
import math

W = 160
H = 120

# ------------------------------------------------
# Papillons
#
# [x, y, angle, vitesse, taille]
# ------------------------------------------------

butterflies = [
    [20, 25, 0.0,  0.020, 0.42],
    [50, 25, 1.0, -0.017, 0.42],
    [80, 25, 2.0,  0.022, 0.42],
    [110, 25, 3.0, -0.019, 0.42],
    [140, 25, 4.0,  0.018, 0.42],

    [35, 52, 0.5, -0.021, 0.42],
    [65, 52, 1.5,  0.018, 0.42],
    [95, 52, 2.5, -0.020, 0.42],
    [125, 52, 3.5,  0.021, 0.42],

    [20, 79, 1.0,  0.019, 0.42],
    [50, 79, 2.0, -0.022, 0.42],
    [80, 79, 3.0,  0.020, 0.42],
    [110, 79, 4.0, -0.018, 0.42],
    [140, 79, 5.0,  0.021, 0.42],

    [35, 106, 0.3, -0.019, 0.42],
    [65, 106, 1.3,  0.022, 0.42],
    [95, 106, 2.3, -0.020, 0.42],
    [125, 106, 3.3,  0.018, 0.42]
]


# ------------------------------------------------
# Rotation d'un point
# ------------------------------------------------

def rotate(x, y, angle, scale):

    x *= scale
    y *= scale

    c = math.cos(angle)
    s = math.sin(angle)

    return (
        x * c - y * s,
        x * s + y * c
    )


# ------------------------------------------------
# Dessin d'un papillon
# ------------------------------------------------

def draw_butterfly(cx, cy, angle, scale):

    def point(x, y):

        rx, ry = rotate(
            x,
            y,
            angle,
            scale
        )

        return (
            int(cx + rx),
            int(cy + ry)
        )


    # --------------------------------------------
    # Ailes
    # --------------------------------------------

    wing_left = [
        (-3, -2),
        (-18, -18),
        (-38, -27),
        (-45, -15),
        (-40, 2),
        (-25, 10),
        (-8, 7)
    ]

    wing_right = [
        (3, -2),
        (18, -18),
        (38, -27),
        (45, -15),
        (40, 2),
        (25, 10),
        (8, 7)
    ]


    # Aile gauche
    p = [point(x, y) for x, y in wing_left]

    for i in range(1, len(p) - 1):

        pyxel.tri(
            p[0][0], p[0][1],
            p[i][0], p[i][1],
            p[i + 1][0], p[i + 1][1],
            14
        )


    # Aile droite
    p = [point(x, y) for x, y in wing_right]

    for i in range(1, len(p) - 1):

        pyxel.tri(
            p[0][0], p[0][1],
            p[i][0], p[i][1],
            p[i + 1][0], p[i + 1][1],
            10
        )


    # --------------------------------------------
    # Motifs
    # --------------------------------------------

    motifs = [
        (-27, -15, 8),
        (-35, -5, 9),
        (-20, 1, 12),

        (27, -15, 13),
        (35, -5, 11),
        (20, 1, 12)
    ]

    for x, y, color in motifs:

        px, py = point(x, y)

        pyxel.circ(
            px,
            py,
            max(1, int(4 * scale)),
            color
        )


    # --------------------------------------------
    # Corps
    # --------------------------------------------

    body = [
        (0, -15),
        (3, -8),
        (3, 8),
        (0, 16),
        (-3, 8),
        (-3, -8)
    ]

    p = [point(x, y) for x, y in body]

    for i in range(1, len(p) - 1):

        pyxel.tri(
            p[0][0], p[0][1],
            p[i][0], p[i][1],
            p[i + 1][0], p[i + 1][1],
            7
        )


    # --------------------------------------------
    # Tête
    # --------------------------------------------

    hx, hy = point(0, -18)

    pyxel.circ(
        hx,
        hy,
        max(2, int(4 * scale)),
        8
    )


    # --------------------------------------------
    # Antennes
    # --------------------------------------------

    a1 = point(-2, -20)
    a2 = point(-9, -27)

    b1 = point(2, -20)
    b2 = point(9, -27)

    pyxel.line(
        a1[0], a1[1],
        a2[0], a2[1],
        12
    )

    pyxel.line(
        b1[0], b1[1],
        b2[0], b2[1],
        12
    )


# ------------------------------------------------
# Lignes géométriques
# ------------------------------------------------

def draw_geometry():

    # On relie les centres selon la grille.
    #
    # Cela crée des triangles et des losanges
    # très réguliers entre les papillons.

    lines = [
        # horizontales
        (0, 1), (1, 2), (2, 3), (3, 4),
        (5, 6), (6, 7), (7, 8),
        (9, 10), (10, 11), (11, 12), (12, 13),
        (14, 15), (15, 16), (16, 17),

        # diagonales
        (0, 5), (1, 5), (1, 6),
        (2, 6), (2, 7),
        (3, 7), (3, 8),
        (4, 8),

        (5, 9), (5, 10),
        (6, 10), (6, 11),
        (7, 11), (7, 12),
        (8, 12), (8, 13),

        (9, 14), (10, 14),
        (10, 15), (11, 15),
        (11, 16), (12, 16),
        (12, 17), (13, 17)
    ]


    for n, (a, b) in enumerate(lines):

        x1 = int(butterflies[a][0])
        y1 = int(butterflies[a][1])

        x2 = int(butterflies[b][0])
        y2 = int(butterflies[b][1])

        # Plusieurs couleurs géométriques
        colors = [1, 5, 6, 12]

        color = colors[n % len(colors)]

        pyxel.line(
            x1, y1,
            x2, y2,
            color
        )


# ------------------------------------------------
# UPDATE
# ------------------------------------------------

def update():

    for butterfly in butterflies:

        butterfly[2] += butterfly[3]

        if butterfly[2] > math.pi * 2:
            butterfly[2] -= math.pi * 2

        if butterfly[2] < -math.pi * 2:
            butterfly[2] += math.pi * 2


# ------------------------------------------------
# DRAW
# ------------------------------------------------

def draw():

    pyxel.cls(0)

    # Géométrie en arrière-plan
    draw_geometry()

    # Papillons par-dessus
    for butterfly in butterflies:

        x = butterfly[0]
        y = butterfly[1]
        angle = butterfly[2]
        scale = butterfly[4]

        draw_butterfly(
            x,
            y,
            angle,
            scale
        )


# ------------------------------------------------
# PYXEL
# ------------------------------------------------

pyxel.init(
    160,
    120,
    title="Papillons géométriques"
)

pyxel.run(update, draw)
