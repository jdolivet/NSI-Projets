"""
Jeu du serpent (Snake Game) en Pygame.

Ce programme crée un jeu où le joueur contrôle un serpent(en vert) qui grandit
en mangeant de la nourriture(en rouge) apparaissant aléatoirement sur l'écran.
Le joueur doit éviter de heurter les bords de l'écran ou son propre corps.
Le score(en blanc) correspond au nombre de nourritures mangées.

Contrôles :
- Flèches directionnelles : Déplacer le serpen
- Fermer la fenêtre(esc) : Quitter le jeu
"""
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")
largeur, hauteur = 1200, 800
écran = pygame.display.set_mode((largeur, hauteur))
horloge = pygame.time.Clock()

# Couleurs
noir = (0, 0, 0)
vert = (0, 255, 0)
rouge = (255, 0, 0)
blanc = (255, 255, 255)
# Paramètres du serpent
taille_carree = 20
vitesse_serpent = 15

def gerer_nourriture():
    nourriture_x = random.randrange(0, largeur - taille_carree, taille_carree)
    nourriture_y = random.randrange(0, hauteur - taille_carree, taille_carree)
    return nourriture_x, nourriture_y

def dessiner_nourriture(taille_carre, nourriture_x, nourriture_y):
    pygame.draw.rect(écran, rouge, [nourriture_x, nourriture_y, taille_carree, taille_carree])

def dessiner_serpent(taille, pixels):
    for pixel in pixels:
        pygame.draw.rect(écran, vert, [pixel[0], pixel[1], taille, taille])

def dessiner_score(score):
    source = pygame.font.SysFont("Helvetica", 25)
    texte = source.render(f"Points: {score}", True, blanc)
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

def commencer_jeu():
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
            elif event.type == pygame.KEYDOWN:
                vitesse_x, vitesse_y = selectionner_vitesse(event.key)

        x += vitesse_x
        y += vitesse_y

        if x < 0 or x >= largeur or y < 0 or y >= hauteur:
            fin_jeu = True

        pixels.append([x, y])
        if len(pixels) > taille_serpent:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fin_jeu = True

        dessiner_nourriture(taille_carree, nourriture_x, nourriture_y)
        dessiner_serpent(taille_carree, pixels)
        dessiner_score(taille_serpent - 1)
        pygame.display.update()

        if abs(x - nourriture_x) < taille_carree and abs(y - nourriture_y) < taille_carree:
            nourriture_x, nourriture_y = gerer_nourriture()
            taille_serpent += 1

        horloge.tick(vitesse_serpent)

commencer_jeu()
pygame.quit()