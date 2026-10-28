import pygame
from random import randint, choice


# =====================================================
# == INITIALISATION
# =====================================================

pygame.init()


# =====================================================
# == RÉCUPÉRATION DE LA TAILLE DE L'ÉCRAN
# =====================================================

info = pygame.display.Info()

WIDTH = info.current_w
HEIGHT = info.current_h


# =====================================================
# == FENÊTRE PLEIN ÉCRAN
# =====================================================

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT),
    pygame.FULLSCREEN
)

pygame.display.set_caption(
    "Météores et explosions"
)

clock = pygame.time.Clock()


# =====================================================
# == PALETTE PYXEL -> RGB
# =====================================================

PALETTE = [
    (0, 0, 0),          # 0
    (43, 43, 43),       # 1
    (126, 37, 83),      # 2
    (0, 135, 81),       # 3
    (171, 82, 54),      # 4
    (95, 87, 79),       # 5
    (194, 195, 199),    # 6
    (255, 241, 232),    # 7
    (255, 0, 77),       # 8
    (255, 163, 0),      # 9
    (255, 236, 39),     # 10
    (0, 228, 54),       # 11
    (41, 173, 255),     # 12
    (131, 118, 156),    # 13
    (255, 119, 168),    # 14
    (255, 204, 170)     # 15
]


# =====================================================
# == CLASSE EXPLOSION
# =====================================================

class Explosion:

    def __init__(self, x, y, duree, couleur):

        self.co = x
        self.li = y

        self.duree = duree

        self.diametre = 0

        self.nbRayures = randint(4, 8)

        self.couleurs = (
            [couleur]
            + [
                randint(1, 15)
                for _ in range(self.nbRayures - 2)
            ]
            + [couleur]
        )


# =====================================================
# == CLASSE METEORE
# =====================================================

class Meteore:

    def __init__(
        self,
        x,
        y,
        dx,
        dy,
        dureeVie,
        diametre,
        couleur
    ):

        self.co = x
        self.li = y

        self.dureeVie = dureeVie

        self.diametre = diametre

        self.couleur = couleur

        self.dco = dx
        self.dli = dy


# =====================================================
# == VARIABLES
# =====================================================

meteores = []

explosions = []

frame_count = 0


# =====================================================
# == CREATION D'UN METEORE
# =====================================================

def creationMeteore():

    # Position aléatoire sur tout l'écran
    co = randint(0, WIDTH - 1)
    li = randint(0, HEIGHT - 1)

    # Vitesse
    dco = choice([
        -3, -2, -1,
        1, 2, 3
    ])

    dli = choice([
        -3, -2, -1,
        1, 2, 3
    ])

    # Taille du météore
    diam = randint(5, 10)

    # Couleur
    coul = randint(1, 15)

    # Durée de vie
    dureeVie = randint(75, 150)

    meteores.append(
        Meteore(
            co,
            li,
            dco,
            dli,
            dureeVie,
            diam,
            coul
        )
    )


# =====================================================
# == CREATION DES METEORES
# =====================================================

for _ in range(1000):
    creationMeteore()


# =====================================================
# == DEPLACEMENT DES METEORES
# =====================================================

def deplacementMeteores():

    for m in meteores[:]:

        if (
            0 <= m.co + m.dco < WIDTH
            and
            0 <= m.li + m.dli < HEIGHT
        ):

            m.co += m.dco
            m.li += m.dli

            m.dureeVie -= 1

            # -------------------------------
            # Fin de vie
            # -------------------------------

            if m.dureeVie <= 0:

                meteores.remove(m)

                creationMeteore()

            # -------------------------------
            # Réduction de taille
            # -------------------------------

            elif m.dureeVie < 60:

                m.diametre = 3

            elif m.dureeVie < 90:

                m.diametre = 6

        else:

            meteores.remove(m)

            creationMeteore()


# =====================================================
# == GESTION DES EXPLOSIONS
# =====================================================

def gestionExplosions():

    global explosions

    # Création d'une explosion
    if frame_count % 5 == 0:

        explosions.append(
            Explosion(
                randint(50, WIDTH - 50),
                randint(50, HEIGHT - 50),
                randint(100, 250),
                randint(1, 15)
            )
        )

    # Mise à jour
    for explo in explosions[:]:

        if explo.duree >= explo.diametre:

            # Croissance de l'explosion
            explo.diametre += 5

        else:

            explosions.remove(explo)


# =====================================================
# == UPDATE
# =====================================================

def update():

    deplacementMeteores()

    gestionExplosions()


# =====================================================
# == DRAW
# =====================================================

def draw():

    # Fond noir
    screen.fill(
        PALETTE[0]
    )


    # =================================================
    # == EXPLOSIONS
    # =================================================

    for e in explosions:

        for i in range(e.nbRayures):

            rayon = (
                e.diametre
                + 8 * i
            )

            pygame.draw.circle(
                screen,

                PALETTE[
                    e.couleurs[i]
                ],

                (
                    int(e.co),
                    int(e.li)
                ),

                int(rayon),

                2
            )


    # =================================================
    # == METEORES
    # =================================================

    for m in meteores:

        pygame.draw.circle(
            screen,

            PALETTE[
                m.couleur
            ],

            (
                int(m.co),
                int(m.li)
            ),

            int(m.diametre)
        )


# =====================================================
# == BOUCLE PRINCIPALE
# =====================================================

running = True

while running:

    # -------------------------------------------------
    # ÉVÉNEMENTS
    # -------------------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # ESC permet de quitter le plein écran
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False


    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    update()


    # -------------------------------------------------
    # DRAW
    # -------------------------------------------------

    draw()


    # -------------------------------------------------
    # AFFICHAGE
    # -------------------------------------------------

    pygame.display.flip()


    # -------------------------------------------------
    # COMPTEUR DE FRAMES
    # -------------------------------------------------

    frame_count += 1


    # -------------------------------------------------
    # 60 FPS
    # -------------------------------------------------

    clock.tick(60)


# =====================================================
# == FERMETURE
# =====================================================

pygame.quit()