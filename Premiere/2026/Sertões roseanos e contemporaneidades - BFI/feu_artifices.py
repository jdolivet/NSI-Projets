import pyxel
from random import randint, choice


class Explosion:
    def __init__(self, x, y, duree, couleur):
        self.co = x
        self.li = y
        self.duree = duree
        self.diametre = 0
        self.nbRayures = randint(3, 7)
        self.couleurs = [couleur] + [randint(1, 15) for i in range(self.nbRayures - 2)] + [couleur]


class Meteore:
    def __init__(self, x, y, dx, dy, dureeVie, diametre, couleur):
        self.co = x
        self.li = y
        self.dureeVie = dureeVie
        self.diametre = diametre
        self.couleur = couleur
        self.dco = dx
        self.dli = dy

    def __repr__(self):
        return f'position: x = {self.co} , y = {self.li}\nvitesse : dx = {self.dco}, dy = {self.dli}'


# =====================================================
# == VARIABLES
# =====================================================

meteores = []

texte = [10, 50]  # li, co

boules = []
for x in range(35, 106, 5):
    boules.append([x, 120])

for y in range(110, 65, -4):
    boules.append([70, y])

boules = boules + [
    [65, 100], [100, 110], [75, 80], [40, 115],
    [60, 95], [95, 105], [65, 75], [70, 70]
]

allumes = [0 for _ in range(len(boules))]

etoile = 1

explosions = []


# =====================================================
# == CREATION DES METEORES
# =====================================================

def creationMeteore():
    co, li = randint(0, 255), randint(0, 127)
    dco = choice([-2, -1, 1, 2])
    dli = choice([-2, -1, 1, 2])
    diam = 3
    coul = randint(1, 15)
    dureeVie = randint(75, 150)

    meteores.append(
        Meteore(co, li, dco, dli, dureeVie, diam, coul)
    )


# Création des 15 météores
for _ in range(200):
    creationMeteore()





# =====================================================
# == DEPLACEMENT DES METEORES
# =====================================================

def deplacementMeteores():
    global meteores

    for m in meteores[:]:

        if 0 <= m.co + m.dco <= 257 and 0 <= m.li + m.dli <= 127:

            m.co += m.dco
            m.li += m.dli
            m.dureeVie -= 1

            if m.dureeVie == 0:
                meteores.remove(m)
                creationMeteore()

            elif m.dureeVie < 60:
                m.diametre = 1

            elif m.dureeVie < 90:
                m.diametre = 2

        else:
            meteores.remove(m)
            creationMeteore()





# =====================================================
# == GESTION DES EXPLOSIONS
# =====================================================

def gestionExplosions():
    global explosions

    if pyxel.frame_count % 10 == 0:
        explosions.append(
            Explosion(
                randint(50, 150),
                randint(50, 150),
                randint(50, 150),
                randint(1, 15)
            )
        )

    for explo in explosions[:]:

        if explo.duree >= explo.diametre:
            explo.diametre += 2

        else:
            explosions.remove(explo)


# =====================================================
# == UPDATE
# =====================================================

def update():
    """Mise à jour des variables."""

    deplacementMeteores()
    gestionExplosions()


# =====================================================
# == DRAW
# =====================================================

def draw():
    """Création et affichage des objets."""

    # Fond noir
    pyxel.cls(0)

    # Dessin des explosions
    for e in explosions:
        for i in range(e.nbRayures):
            pyxel.circb(
                e.co,
                e.li,
                e.diametre + 3 * i,
                e.couleurs[i]
            )

    # Dessin des météores
    for m in meteores:
        pyxel.circ(
            m.co,
            m.li,
            m.diametre,
            m.couleur
        )



# =====================================================
# == LANCEMENT DU PROGRAMME
# =====================================================

pyxel.init(160, 120)

pyxel.run(update, draw)