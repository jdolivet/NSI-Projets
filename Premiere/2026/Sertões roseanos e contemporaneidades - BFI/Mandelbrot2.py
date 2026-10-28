import pyxel
import math


# =====================================================
# == FENÊTRE
# =====================================================

pyxel.init(
    160,
    120,
    title="Mandelbrot - Deep Zoom"
)


# =====================================================
# == PARAMÈTRES
# =====================================================

zoom = 0.1

# Facteur de zoom
zoom_factor = 0.6

# Nombre initial d'itérations
iterations = 100


# =====================================================
# == PARAMÈTRES DE L'ANIMATION
# =====================================================

# Profondeur maximale du zoom
zoom_max = 35

# Position actuelle dans l'animation
zoom_step = 0

# 1 = zoom
# -1 = dézoom
direction = 1


# =====================================================
# == POINT INTÉRESSANT
# =====================================================

# Seahorse Valley

target_x = -0.74368
target_y = 0.13182590420533


# =====================================================
# == PARAMÈTRES DE LA CAMÉRA
# =====================================================

xAxis = 1 / zoom

yAxis = (
    pyxel.height
    / (pyxel.width * zoom)
)


# Position initiale
xOffset = (
    target_x
    - xAxis / 2
)

yOffset = (
    target_y
    - yAxis / 2
)


# Taille d'un pixel
ratio = (
    xAxis
    / pyxel.width
)


# =====================================================
# == PIXELS
# =====================================================

pixels = []


# =====================================================
# == CALCUL D'UN PIXEL
# =====================================================

def frac(x, y, rat, xOff, yOff, iter):

    # ---------------------------------------------
    # Conversion pixel -> plan complexe
    # ---------------------------------------------

    a = (
        x * rat
        + xOff
    )

    b = (
        y * rat
        + yOff
    )

    ca = a
    cb = b

    n = 0


    # ---------------------------------------------
    # Mandelbrot
    # ---------------------------------------------

    while (
        a * a + b * b < 4
        and n < iter
    ):

        ai = (
            a * a
            - b * b
        )

        bi = (
            2 * a * b
        )

        a = ai + ca
        b = bi + cb

        n += 1


    # ---------------------------------------------
    # Normalisation
    # ---------------------------------------------

    m = n / iter


    # ---------------------------------------------
    # Couleurs
    # ---------------------------------------------

    lin = int(
        255 * m
    ) % 255

    sin = int(
        255
        * (
            -math.cos(math.pi * m)
            + 1
        )
        / 2
    ) % 255

    sqrt = int(
        255 * math.sqrt(m)
    ) % 255

    sqr = int(
        255 * m * m
    ) % 255


    r = sqr
    g = lin
    b = sin


    # ---------------------------------------------
    # RGB -> palette Pyxel
    # ---------------------------------------------

    luminosite = (
        r + g + b
    ) / 3

    couleur = int(
        luminosite
        / 256
        * 16
    )


    if couleur < 0:
        couleur = 0

    if couleur > 15:
        couleur = 15


    return couleur


# =====================================================
# == CALCUL DE L'IMAGE
# =====================================================

def process():

    global pixels

    pixels = []


    for y in range(pyxel.height):

        ligne = []


        for x in range(pyxel.width):

            couleur = frac(
                x,
                y,
                ratio,
                xOffset,
                yOffset,
                iterations
            )

            ligne.append(couleur)


        pixels.append(ligne)


# =====================================================
# == ZOOM AUTOMATIQUE
# =====================================================

def automatic_zoom():

    global ratio
    global xOffset
    global yOffset
    global zoom_step
    global direction


    # ---------------------------------------------
    # Avancer dans l'animation
    # ---------------------------------------------

    zoom_step += direction


    # ---------------------------------------------
    # Arrivé au zoom maximum
    # ---------------------------------------------

    if zoom_step >= zoom_max:

        zoom_step = zoom_max

        # On commence le dézoom
        direction = -1


    # ---------------------------------------------
    # Retour à l'image initiale
    # ---------------------------------------------
# 
    if zoom_step <= 0:
 
         zoom_step = 0

        # On recommence le zoom
         direction = 1


    # ---------------------------------------------
    # Calcul de la nouvelle échelle
    # ---------------------------------------------

    nouveau_ratio = (
        (1 / zoom)
        / pyxel.width
    )


    # ---------------------------------------------
    # Appliquer le zoom autant de fois que
    # nécessaire selon zoom_step
    # ---------------------------------------------

    nouveau_ratio *= (
        zoom_factor ** zoom_step
    )


    # ---------------------------------------------
    # Sécurité
    # ---------------------------------------------

    if nouveau_ratio < 1e-300:

        nouveau_ratio = 1e-300


    ratio = nouveau_ratio


    # ---------------------------------------------
    # Centre de l'écran
    # ---------------------------------------------

    centre_x = (
        pyxel.width / 2
    )

    centre_y = (
        pyxel.height / 2
    )


    # ---------------------------------------------
    # Garder le point intéressant au centre
    # ---------------------------------------------

    xOffset = (
        target_x
        - centre_x * ratio
    )

    yOffset = (
        target_y
        - centre_y * ratio
    )


# =====================================================
# == DESSIN
# =====================================================

def draw():

    pyxel.cls(0)

    for y in range(pyxel.height):

        for x in range(pyxel.width):

            pyxel.pset(
                x,
                y,
                pixels[y][x]
            )


# =====================================================
# == UPDATE
# =====================================================

def update():

    global iterations


    # ---------------------------------------------
    # Zoom / dézoom
    # ---------------------------------------------

    automatic_zoom()


    # ---------------------------------------------
    # Nombre d'itérations
    # ---------------------------------------------

    if ratio < 0.0005:
        iterations = 150

    if ratio < 0.0001:
        iterations = 200

    if ratio < 0.00001:
        iterations = 300

    if ratio < 0.000001:
        iterations = 400

    if ratio < 0.0000001:
        iterations = 500

    if ratio < 0.00000001:
        iterations = 700

    if ratio < 0.000000001:
        iterations = 900


    # ---------------------------------------------
    # Calcul de l'image
    # ---------------------------------------------

    process()


# =====================================================
# == PREMIER CALCUL
# =====================================================

process()


# =====================================================
# == LANCEMENT
# =====================================================

pyxel.run(
    update,
    draw
)
