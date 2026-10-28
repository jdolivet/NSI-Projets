import pyxel
import math

W = 160
H = 120

# =========================================================
# ANIMATION
# =========================================================

an = 0.0
rayon_x = 18
rayon_y = 10
speed = 0.025
SIDE = 7.0
DX = SIDE * 1.5
DY = SIDE * math.sqrt(3)
DODEC_COLORS = [
    8,   # rouge
    9,   # orange
    10,  # jaune
    11,  # vert
    12,  # cyan
    13,  # bleu
    14   # rose
]
TRI_COLORS = [
    10,
    12,
    14,
    9,
    11,
    13
]


# =========================================================
# HEXAGONES DE BASE
# =========================================================

hexagons = []

for row in range(-14, 15):

    for col in range(-15, 16):

        x = col * DX
        y = row * DY

        if row % 2:
            x += DX / 2

        hexagons.append((x, y))


# =========================================================
# SOMMETS UNIQUES
#
# Chaque sommet de l'ancien pavage hexagonal devient
# le centre d'un trian après troncature.
# =========================================================

vertices = {}


def hex_vertices(cx, cy):

    result = []

    for i in range(6):

        a = i * math.pi / 3

        result.append((
            cx + math.cos(a) * SIDE,
            cy + math.sin(a) * SIDE
        ))

    return result


for hx, hy in hexagons:

    points = hex_vertices(hx, hy)

    for p in points:

        key = (
            round(p[0], 5),
            round(p[1], 5)
        )

        vertices[key] = p


# =========================================================
# DODÉCAGONES
#
# Chaque hexagone est tronqué à 1/3 de ses arêtes.
#
# Les 6 coins deviennent donc 12 sommets.
# =========================================================

dodecagons = []

for hx, hy in hexagons:

    v = hex_vertices(hx, hy)

    polygon = []

    for i in range(6):

        a = v[i]
        b = v[(i + 1) % 6]

        # 1/3 depuis A
        p1 = (
            a[0] * 2 / 3 + b[0] / 3,
            a[1] * 2 / 3 + b[1] / 3
        )

        # 1/3 depuis B
        p2 = (
            a[0] / 3 + b[0] * 2 / 3,
            a[1] / 3 + b[1] * 2 / 3
        )

        polygon.append(p1)
        polygon.append(p2)

    dodecagons.append(polygon)


# =========================================================
# TRIanS
#
# Autour de chaque ancien sommet hexagonal, les trois
# points de coupe forment exactement un trian.
# =========================================================

trians = []

for key, vertex in vertices.items():

    vx, vy = vertex

    points = []

    # Recherche des trois points situés à 1/3 de distance
    # du sommet vers les centres des hexagones voisins.
    #
    # Les six directions possibles sont examinées.

    for hx, hy in hexagons:

        dx = hx - vx
        dy = hy - vy

        dist = math.sqrt(dx * dx + dy * dy)

        if dist > 0 and dist < SIDE * 1.01:

            px = vx + dx * (1 / 3)
            py = vy + dy * (1 / 3)

            points.append((px, py))


    # Dans certains cas les coordonnées sont légèrement
    # différentes à cause des flottants.
    #
    # On garde uniquement les trois points du trian.

    if len(points) >= 3:

        # Tri des points autour du sommet

        points.sort(
            key=lambda p: math.atan2(
                p[1] - vy,
                p[0] - vx
            )
        )

        # Les trois premiers correspondent aux trois
        # hexagones qui se rencontrent au sommet.

        trian = [
            points[0],
            points[1],
            points[2]
        ]

        trians.append(trian)


# =========================================================
# DESSIN POLYGONE
# =========================================================

def draw_polygon(points, color):

    if len(points) < 3:
        return

    # Centre du polygone

    cx = 0
    cy = 0

    for x, y in points:

        cx += x
        cy += y

    cx /= len(points)
    cy /= len(points)

    # Trian fan

    for i in range(len(points)):

        a = points[i]
        b = points[(i + 1) % len(points)]

        pyxel.tri(
            int(cx),
            int(cy),
            int(a[0]),
            int(a[1]),
            int(b[0]),
            int(b[1]),
            color
        )


# =========================================================
# AUTO-RÉFÉRENCE
#
# On ajoute de petits motifs à l'intérieur des grands
# dodécagones.
#
# Ils suivent exactement le même mouvement.
# =========================================================

def draw_inner_pattern(points, color1, color2):

    if len(points) != 12:
        return

    cx = 0
    cy = 0

    for x, y in points:

        cx += x
        cy += y

    cx /= 12
    cy /= 12

    # Petit hexagone intérieur

    r = 2.1

    inner = []

    for i in range(6):

        a = i * math.pi / 3

        inner.append((
            cx + math.cos(a) * r,
            cy + math.sin(a) * r
        ))

    draw_polygon(
        inner,
        color1
    )

    # Petit trian intérieur

    r2 = 0.9

    trian = []

    for i in range(3):

        a = -math.pi / 2 + i * math.pi * 2 / 3

        trian.append((
            cx + math.cos(a) * r2,
            cy + math.sin(a) * r2
        ))

    draw_polygon(
        trian,
        color2
    )


# =========================================================
# UPDATE
# =========================================================

def update():

    global an

    an += speed

    if an >= math.pi * 2:
        an -= math.pi * 2


# =========================================================
# DRAW
# =========================================================

def draw():

    pyxel.cls(0)

    # ---------------------------------------------
    # Déplacement elliptique
    # ---------------------------------------------

    offset_x = math.cos(an) * rayon_x
    offset_y = math.sin(an) * rayon_y

    center_x = W / 2
    center_y = H / 2


    # ---------------------------------------------
    # DODÉCAGONES
    # ---------------------------------------------

    for i, polygon in enumerate(dodecagons):

        moved = []

        for x, y in polygon:

            moved.append((
                center_x + x + offset_x,
                center_y + y + offset_y
            ))

        color = DODEC_COLORS[
            i % len(DODEC_COLORS)
        ]

        draw_polygon(
            moved,
            color
        )

        # Motif récursif / auto-référent
        #
        # Il est volontairement petit afin que la
        # géométrie principale reste lisible.

        inner1 = DODEC_COLORS[
            (i + 3) % len(DODEC_COLORS)
        ]

        inner2 = DODEC_COLORS[
            (i + 5) % len(DODEC_COLORS)
        ]

        draw_inner_pattern(
            moved,
            inner1,
            inner2
        )


    # ---------------------------------------------
    # TRIanS
    # ---------------------------------------------

    for i, trian in enumerate(trians):

        moved = []

        for x, y in trian:

            moved.append((
                center_x + x + offset_x,
                center_y + y + offset_y
            ))

        color = TRI_COLORS[
            i % len(TRI_COLORS)
        ]

        draw_polygon(
            moved,
            color
        )


# =========================================================
# PYXEL
# =========================================================

pyxel.init(
    160,
    120,
    title="Pavage 3.12.12 Auto-Referent"
)

pyxel.run(update, draw)
