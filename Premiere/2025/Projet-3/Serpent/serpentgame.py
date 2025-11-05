import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")
largeur, hauteur = 1200, 800
écran = pygame.display.set_mode((largeur, hauteur))
horloge = pygame.time.Clock()

# sons
pygame.mixer.init()
son_manger = pygame.mixer.Sound("manger.wav")      # Son quand le serpent mange
son_gameover = pygame.mixer.Sound("gameover.wav")  # Son de fin

# Couleurs
noir = (0, 0, 0)
rouge = (255, 0, 0)
vert = (0, 255, 0)
blanc = (255, 255, 255)

# Paramètres du serpent
taille_carree = 20
vitesse_serpent = 15


def gerer_nourriture():
    nourriture_x = random.randrange(0, largeur - taille_carree, taille_carree)
    nourriture_y = random.randrange(0, hauteur - taille_carree, taille_carree)
    return nourriture_x, nourriture_y


def dessiner_nourriture(taille_carre, nourriture_x, nourriture_y):
    pygame.draw.rect(écran, vert, [nourriture_x, nourriture_y, taille_carree, taille_carree])


def dessiner_serpent(taille, pixels):
    for pixel in pixels:
        pygame.draw.rect(écran, blanc, [pixel[0], pixel[1], taille, taille])


def dessiner_score(score):
    source = pygame.font.SysFont("Helvetica", 25)
    texte = source.render(f"Points: {score}", True, rouge)
    écran.blit(texte, [1, 1])


def selectionner_vitesse(cle):
    if cle == pygame.K_DOWN:
        return 0, taille_carree
    elif cle == pygame.K_UP:
        return 0, -taille_carree
    elif cle == pygame.K_RIGHT:
        return taille_carree, 0
    elif cle == pygame.K_LEFT:
        return -taille_carree, 0
    return 0, 0


def message_fin(score):
    """Affiche l’écran de fin"""
    écran.fill(noir)
    font1 = pygame.font.SysFont("Helvetica", 60)
    font2 = pygame.font.SysFont("Helvetica", 30)
    texte1 = font1.render("GAME OVER", True, rouge)
    texte2 = font2.render(f"Score : {score}", True, blanc)
    texte3 = font2.render("Appuie sur ESPACE pour rejouer ou ESC pour quitter", True, blanc)
    écran.blit(texte1, [largeur // 2 - 150, hauteur // 2 - 100])
    écran.blit(texte2, [largeur // 2 - 50, hauteur // 2 - 40])
    écran.blit(texte3, [largeur // 2 - 300, hauteur // 2 + 20])
    pygame.display.update()


def commencer_jeu():
    fin_programme = False

    while not fin_programme:
        fin_jeu = False
        x = largeur // 2
        y = hauteur // 2
        vitesse_x = 0
        vitesse_y = 0
        taille_serpent = 1
        pixels = []
        nourriture_x, nourriture_y = gerer_nourriture()

        while not fin_jeu:
            écran.fill(noir)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin_jeu = True
                    fin_programme = True
                elif event.type == pygame.KEYDOWN:
                    vitesse_x, vitesse_y = selectionner_vitesse(event.key)

            x += vitesse_x
            y += vitesse_y

            # Collision mur
            if x < 0 or x >= largeur or y < 0 or y >= hauteur:
                son_gameover.play()
                fin_jeu = True

            # Déplacement du serpent
            pixels.append([x, y])
            if len(pixels) > taille_serpent:
                del pixels[0]

            # Collision avec soi-même
            for pixel in pixels[:-1]:
                if pixel == [x, y]:
                    son_gameover.play()
                    fin_jeu = True

            # Dessins
            dessiner_nourriture(taille_carree, nourriture_x, nourriture_y)
            dessiner_serpent(taille_carree, pixels)
            dessiner_score(taille_serpent - 1)
            pygame.display.update()

            # Manger nourriture
            if abs(x - nourriture_x) < taille_carree and abs(y - nourriture_y) < taille_carree:
                son_manger.play()
                nourriture_x, nourriture_y = gerer_nourriture()
                taille_serpent += 1

            horloge.tick(vitesse_serpent)

        # Quand la partie est terminée
        message_fin(taille_serpent - 1)

        # Attente du joueur
        en_attente = True
        while en_attente:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin_programme = True
                    en_attente = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        fin_programme = True
                        en_attente = False
                    elif event.key == pygame.K_SPACE:
                        en_attente = False  # relance une nouvelle partie


commencer_jeu()
pygame.quit()

