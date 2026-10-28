import pyxel
import math

# ============================================================
# PARAMÈTRES
# ============================================================

zorb = 160
plok = 120

mira = 6
vex = 90

qalu = (1 + math.sqrt(5)) / 2
nix = 1 / qalu

blip = 0


# ============================================================
# OUTILS
# ============================================================

def wumbo(a, b):
    return (
        a[0] - b[0],
        a[1] - b[1]
    )


def flarp(a, b):
    return (
        a[0] + b[0],
        a[1] + b[1]
    )


def glorp(a, n):
    return (
        a[0] * n,
        a[1] * n
    )


def sploink(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]

    return math.sqrt(
        dx * dx +
        dy * dy
    )


def wobble(a, b, t):
    return flarp(
        a,
        glorp(
            wumbo(b, a),
            t
        )
    )


# ============================================================
# ROTATION
# ============================================================

def banana(p, theta):

    c = math.cos(theta)
    s = math.sin(theta)

    return (
        p[0] * c - p[1] * s,
        p[0] * s + p[1] * c
    )


# ============================================================
# SUBDIVISION
# ============================================================

def patate(trucs):

    machin = []

    for sorte, a, b, c in trucs:

        if sorte == 0:

            p = wobble(
                a,
                b,
                nix
            )

            machin.append(
                (
                    1,
                    p,
                    c,
                    a
                )
            )

            machin.append(
                (
                    0,
                    c,
                    p,
                    b
                )
            )

        else:

            q = wobble(
                b,
                a,
                nix
            )

            r = wobble(
                b,
                c,
                nix
            )

            machin.append(
                (
                    1,
                    r,
                    c,
                    a
                )
            )

            machin.append(
                (
                    1,
                    q,
                    r,
                    b
                )
            )

            machin.append(
                (
                    0,
                    r,
                    q,
                    a
                )
            )

    return machin


# ============================================================
# GERME
# ============================================================

def cornichon():

    trucs = []

    rayon = 300.0

    for i in range(10):

        alpha = (
            2 * math.pi * i / 10
            - math.pi / 10
        )

        beta = (
            2 * math.pi * i / 10
            + math.pi / 10
        )

        a = (0.0, 0.0)

        b = (
            rayon * math.cos(alpha),
            rayon * math.sin(alpha)
        )

        c = (
            rayon * math.cos(beta),
            rayon * math.sin(beta)
        )

        if i % 2 == 0:
            b, c = c, b

        trucs.append(
            (
                0,
                a,
                b,
                c
            )
        )

    return trucs


# ============================================================
# IDENTIFICATION DES POINTS
# ============================================================

def bidule(p):

    return (
        round(p[0], 6),
        round(p[1], 6)
    )


def machin_bizarre(a, b):

    a = bidule(a)
    b = bidule(b)

    if a < b:
        return (a, b)

    return (b, a)


# ============================================================
# CONSTRUCTION DES LOSANGES
# ============================================================

def schmilblick(trucs):

    bazar = {}

    for i, (sorte, a, b, c) in enumerate(trucs):

        machin = [a, b, c]

        for j in range(3):

            p = machin[j]
            q = machin[(j + 1) % 3]

            cle = machin_bizarre(
                p,
                q
            )

            if cle not in bazar:
                bazar[cle] = []

            bazar[cle].append(i)

    tuiles = []
    poubelle = set()

    for indices in bazar.values():

        if len(indices) != 2:
            continue

        i1, i2 = indices

        if i1 in poubelle or i2 in poubelle:
            continue

        _, a1, b1, c1 = trucs[i1]
        _, a2, b2, c2 = trucs[i2]

        sac = [a1, b1, c1]
        sac2 = [a2, b2, c2]

        commun = []

        for p in sac:
            for q in sac2:

                if bidule(p) == bidule(q):
                    commun.append(p)

        if len(commun) != 2:
            continue

        reste1 = None
        reste2 = None

        for p in sac:

            if (
                bidule(p) != bidule(commun[0])
                and
                bidule(p) != bidule(commun[1])
            ):
                reste1 = p

        for p in sac2:

            if (
                bidule(p) != bidule(commun[0])
                and
                bidule(p) != bidule(commun[1])
            ):
                reste2 = p

        if reste1 is None or reste2 is None:
            continue

        points = [
            commun[0],
            commun[1],
            reste1,
            reste2
        ]

        centre = (
            sum(p[0] for p in points) / 4,
            sum(p[1] for p in points) / 4
        )

        points.sort(
            key=lambda p:
            math.atan2(
                p[1] - centre[1],
                p[0] - centre[0]
            )
        )

        d1 = sploink(
            points[0],
            points[2]
        )

        d2 = sploink(
            points[1],
            points[3]
        )

        cote = (
            sploink(points[0], points[1])
            +
            sploink(points[1], points[2])
            +
            sploink(points[2], points[3])
            +
            sploink(points[3], points[0])
        ) / 4

        grosse = max(d1, d2)

        if grosse / cote > 1.5:
            sorte = 1
        else:
            sorte = 0

        tuiles.append(
            (
                points,
                sorte,
                centre
            )
        )

        poubelle.add(i1)
        poubelle.add(i2)

    return tuiles


# ============================================================
# CONSTRUCTION
# ============================================================

trucs = cornichon()

for _ in range(mira):
    trucs = patate(trucs)

tuiles = schmilblick(trucs)


# ============================================================
# TRANSFORMATION
# ============================================================

def teleportation(p, theta, zoom):

    p = banana(
        p,
        theta
    )

    return (
        int(zorb / 2 + p[0] * zoom),
        int(plok / 2 + p[1] * zoom)
    )


# ============================================================
# PALETTE
# ============================================================

arc_en_ciel = [
    1,
    5,
    6,
    13,
    9,
    10,
    2
]


# ============================================================
# DÉGRADÉ
# ============================================================

def truc_chose(x, y, phase, sorte):

    rayon = math.sqrt(
        x * x +
        y * y
    )

    angle = math.atan2(
        y,
        x
    )

    vague = (
        rayon * 0.045
        - phase
        + angle * 1.5
    )

    patate_chaude = (
        math.sin(vague)
        + 1
    ) * 0.5

    if sorte == 1:
        patate_chaude += 0.18

    numero = int(
        patate_chaude
        * len(arc_en_ciel)
    )

    numero %= len(arc_en_ciel)

    return arc_en_ciel[numero]


# ============================================================
# UPDATE
# ============================================================

def update():

    global blip

    blip = (
        blip + 1
    ) % vex

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


# ============================================================
# DRAW
# ============================================================

def draw():

    pyxel.cls(0)

    phase = (
        2 * math.pi
        * blip
        / vex
    )

    theta = (
        math.sin(phase)
        * 0.035
    )

    zoom = (
        0.48
        + math.sin(phase)
        * 0.012
    )

    for points, sorte, centre in tuiles:

        couleur = truc_chose(
            centre[0],
            centre[1],
            phase,
            sorte
        )

        p = []

        for point in points:

            p.append(
                teleportation(
                    point,
                    theta,
                    zoom
                )
            )

        pyxel.tri(
            p[0][0], p[0][1],
            p[1][0], p[1][1],
            p[2][0], p[2][1],
            couleur
        )

        pyxel.tri(
            p[0][0], p[0][1],
            p[2][0], p[2][1],
            p[3][0], p[3][1],
            couleur
        )

        for i in range(4):

            a = p[i]
            b = p[(i + 1) % 4]

            pyxel.line(
                a[0],
                a[1],
                b[0],
                b[1],
                0
            )


# ============================================================
# LANCEMENT
# ============================================================

pyxel.init(
    zorb,
    plok,
    title="Penrose"
)

pyxel.run(
    update,
    draw
)
