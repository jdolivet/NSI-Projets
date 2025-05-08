import pyxel
import random

pyxel.init(128, 128, title="Space Game")

# Position du joueur
joueur_x = 60
joueur_y = 60

# Constantes
MAX_PROJECTILES = 50
MAX_ADVERSAIRES = 30
MAX_BOUMS = 20

# Vies
nb_vies = 4

# Tableaux fixes
projectiles = [[-1, -1] for _ in range(MAX_PROJECTILES)]
adversaires = [[-1, -1] for _ in range(MAX_ADVERSAIRES)]
boums = [[-1, -1, 0] for _ in range(MAX_BOUMS)]  # x, y, compteur

def deplacer_joueur(x, y):
    if pyxel.btn(pyxel.KEY_D) and x < 120:
        x += 1
    if pyxel.btn(pyxel.KEY_A) and x > 0:
        x -= 1
    if pyxel.btn(pyxel.KEY_S) and y < 120:
        y += 1
    if pyxel.btn(pyxel.KEY_W) and y > 0:
        y -= 1
    return x, y

def tirer(x, y):
    if pyxel.btnr(pyxel.KEY_SPACE):
        for p in projectiles:
            if p[1] == -1:  # spot libre
                p[0] = x + 4
                p[1] = y - 4
                break

def bouger_projectiles():
    for p in projectiles:
        if p[1] != -1:
            p[1] -= 1
            if p[1] < -4:
                p[1] = -1  # désactivation

def spawn_adversaires():
    if pyxel.frame_count % 30 == 0:
        for a in adversaires:
            if a[1] == -1:
                a[0] = random.randint(0, 120)
                a[1] = 0
                break

def bouger_adversaires():
    for a in adversaires:
        if a[1] != -1:
            a[1] += 1
            if a[1] > 128:
                a[1] = -1

def collision_joueur(x, y, vies):
    for a in adversaires:
        if a[1] != -1:
            if a[0] < x + 8 and a[0] + 8 > x and a[1] < y + 8 and a[1] + 8 > y:
                a[1] = -1
                creer_explosion(x, y)
                vies -= 1
    return vies

def collision_tirs():
    for e in adversaires:
        if e[1] == -1:
            continue
        for t in projectiles:
            if t[1] == -1:
                continue
            if e[0] <= t[0] <= e[0] + 8 and e[1] <= t[1] <= e[1] + 8:
                creer_explosion(e[0], e[1])
                e[1] = -1
                t[1] = -1
                break

def creer_explosion(x, y):
    for b in boums:
        if b[2] == 0:
            b[0] = x
            b[1] = y
            b[2] = 1
            break

def animer_explosions():
    for b in boums:
        if b[2] > 0:
            b[2] += 1
            if b[2] > 12:
                b[2] = 0

def update():
    global joueur_x, joueur_y, nb_vies
    joueur_x, joueur_y = deplacer_joueur(joueur_x, joueur_y)
    tirer(joueur_x, joueur_y)
    bouger_projectiles()
    spawn_adversaires()
    bouger_adversaires()
    collision_tirs()
    nb_vies = collision_joueur(joueur_x, joueur_y, nb_vies)
    animer_explosions()

def draw():
    pyxel.cls(0)
    if nb_vies > 0:
        pyxel.text(5, 5, f"VIES: {nb_vies}", 7)
        pyxel.rect(joueur_x, joueur_y, 8, 8, 9)
        for p in projectiles:
            if p[1] != -1:
                pyxel.rect(p[0], p[1], 1, 4, 11)
        for e in adversaires:
            if e[1] != -1:
                pyxel.rect(e[0], e[1], 8, 8, 8)
        for b in boums:
            if b[2] > 0:
                pyxel.circb(b[0] + 4, b[1] + 4, (b[2] // 4) * 2, 7 + b[2] % 3)
    else:
        pyxel.text(45, 60, "GAME OVER", 7)

pyxel.run(update, draw)
