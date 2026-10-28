import pyxel
import math

W = 160
H = 120

# ------------------------------------------------
# Paramètres du déplacement
# ------------------------------------------------

move_x = 0
move_y = 0

speed = 0.7
direction = 0

# Distance parcourue sur chaque côté du carré
distance = 18


# ------------------------------------------------
# Création du pavage hexagonal
# ------------------------------------------------

tiles = []

size = 9

for row in range(-7, 8):

    for col in range(-9, 10):

        x = col * size * 1.5

        y = row * size * 1.73

        # Décalage une ligne sur deux
        if row % 2:
            x += size * 0.75

        tiles.append((x, y))

def draw_hexagon(x, y, r, color):

    points = []

    for i in range(6):

        angle = math.pi / 3 * i

        px = int(x + math.cos(angle) * r)
        py = int(y + math.sin(angle) * r)

        points.append((px, py))

    # Triangle fan
    for i in range(1, 5):

        pyxel.tri(
            int(x), int(y),
            points[i][0], points[i][1],
            points[i + 1][0], points[i + 1][1],
            color
        )

    # Dernier triangle
    pyxel.tri(
        int(x), int(y),
        points[5][0], points[5][1],
        points[0][0], points[0][1],
        color
    )

    # Contour
    for i in range(6):

        a = points[i]
        b = points[(i + 1) % 6]

        pyxel.line(
            a[0], a[1],
            b[0], b[1],
            7
        )

# ------------------------------------------------
# Déplacement en carré
# ------------------------------------------------

def update():

    global move_x
    global move_y
    global direction

    if direction == 0:
        # Vers la gauche
        move_x -= speed

        if move_x <= -distance:
            move_x = -distance
            direction = 1

    elif direction == 1:
        # Vers le haut
        move_y -= speed

        if move_y <= -distance:
            move_y = -distance
            direction = 2

    elif direction == 2:
        # Vers la droite
        move_x += speed

        if move_x >= distance:
            move_x = distance
            direction = 3

    elif direction == 3:
        # Vers le bas
        move_y += speed

        if move_y >= distance:
            move_y = distance
            direction = 0



# ------------------------------------------------
# Dessin
# ------------------------------------------------

def draw():

    pyxel.cls(0)

    center_x = W // 2
    center_y = H // 2

    for i, (x, y) in enumerate(tiles):

        # Position du pavage
        px = center_x + x + move_x
        py = center_y + y + move_y

        # Couleurs vives
        colors = [
            8,   # rouge
            9,   # orange
            10,  # jaune
            11,  # vert
            12,  # cyan
            13,  # bleu
            14   # rose
        ]

        color = colors[i % len(colors)]

        draw_hexagon(
            px,
            py,
            size,
            color
        )


# ------------------------------------------------
# PYXEL
# ------------------------------------------------

pyxel.init(
    160,
    120,
    title="Pavage en mouvement"
)

pyxel.run(update, draw)
