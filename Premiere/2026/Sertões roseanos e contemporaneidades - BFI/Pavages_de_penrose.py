import pyxel
import math

W = 160
H = 120

PHI = (1 + math.sqrt(5)) / 2

angle = 0.0


def lerp(a, b, t):
    return (
        a[0] + (b[0] - a[0]) * t,
        a[1] + (b[1] - a[1]) * t
    )


def rotate(p, a):
    c = math.cos(a)
    s = math.sin(a)

    return (
        p[0] * c - p[1] * s,
        p[0] * s + p[1] * c
    )


def subdivide(triangles):
    result = []

    for typ, A, B, C in triangles:

        if typ == 0:
            P = lerp(A, B, 1 / PHI)

            result.append((0, C, P, B))
            result.append((1, P, C, A))

        else:
            P = lerp(A, B, 1 / PHI)
            Q = lerp(A, C, 1 / PHI)

            result.append((1, Q, P, A))
            result.append((0, Q, C, P))
            result.append((0, P, B, Q))

    return result


def create_penrose():
    triangles = []

    radius = 85

    for i in range(10):

        a1 = i * math.pi / 5
        a2 = (i + 1) * math.pi / 5

        B = (
            math.cos(a1) * radius,
            math.sin(a1) * radius
        )

        C = (
            math.cos(a2) * radius,
            math.sin(a2) * radius
        )

        triangles.append(
            (0, (0, 0), B, C)
        )

    for i in range(6):
        triangles = subdivide(triangles)

    return triangles


triangles = create_penrose()


def update():
    global angle

    angle += 0.015

    if angle >= math.pi * 2:
        angle -= math.pi * 2


def draw():
    pyxel.cls(0)

    center_x = W // 2
    center_y = H // 2

    for typ, A, B, C in triangles:

        A = rotate(A, angle)
        B = rotate(B, angle)
        C = rotate(C, angle)

        ax = int(center_x + A[0])
        ay = int(center_y + A[1])

        bx = int(center_x + B[0])
        by = int(center_y + B[1])

        cx = int(center_x + C[0])
        cy = int(center_y + C[1])

        # Couleurs très vives
        if typ == 0:
            color = 10      # jaune vif
        else:
            color = 14      # rose vif

        pyxel.tri(
            ax, ay,
            bx, by,
            cx, cy,
            color
        )

        # Contours cyan
        pyxel.line(ax, ay, bx, by, 12)
        pyxel.line(bx, by, cx, cy, 12)
        pyxel.line(cx, cy, ax, ay, 12)


pyxel.init(
    160,
    120,
    title="Pavage de Penrose"
)

pyxel.run(update, draw)
