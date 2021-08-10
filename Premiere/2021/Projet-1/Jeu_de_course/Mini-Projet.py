import pygame
from random import *

voiture_joueur = int(input("Choisisez le nombre de votre voiture: bleu(1); vert(2); blanc(3); rouge(4); jaune(5)"))
voiture_joueur += 469

pygame.init()
janela = pygame.display.set_mode((680, 700))

fundo = pygame.image.load('fundo.png')
fundo2 = pygame.image.load('fundo_2.png')
chegada = pygame.image.load('chegada.png')
gagne = pygame.image.load('Gagné.png')
perdu = pygame.image.load('You_Lose.png')

carro_azul = pygame.image.load('Carro-Azul.png')
carro_amarelo = pygame.image.load('Carro-Amarelo.png')
carro_verde = pygame.image.load('Carro-Verde.png')
carro_branco = pygame.image.load('Carro-Branco.png')
carro_vermelho = pygame.image.load('Carro-Vermelho.png')

bleu = 470
vert = 471
blanc = 472
rouge = 473
jaune = 474

bleu2 = bleu
vert2 = vert
blanc2 = blanc
rouge2 = rouge
jaune2 = jaune

janela_aberta = True

while janela_aberta:

    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    bleu -= randint(2, 10)
    vert -= randint(2, 10)
    blanc -= randint(2, 10)
    rouge -= randint(2, 10)
    jaune -= randint(2, 10)

    janela.blit(fundo, (0, 0))
    janela.blit(chegada, (0, 0))
    janela.blit(carro_azul, (45, bleu))
    janela.blit(carro_amarelo, (600, jaune - 4))
    janela.blit(carro_verde, (180, vert - 1))
    janela.blit(carro_branco, (330, blanc - 2))
    janela.blit(carro_vermelho, (470, rouge - 3))

    print(voiture_joueur)

    if bleu < 70 or vert < 70 or blanc < 70 or rouge < 70 or jaune < 70:
        janela.fill((0, 0, 0))
        if vert < 70 and voiture_joueur == vert2:
            janela.blit(gagne, (130, 300))
        elif vert > 70 and voiture_joueur == vert2:
            janela.blit(perdu, (130, 300))
            vert = 10000
        if bleu < 70 and voiture_joueur == bleu2:
            janela.blit(gagne, (130, 300))
        elif bleu > 70 and voiture_joueur == bleu2:
            janela.blit(perdu, (130, 300))
            bleu = 10000
        if blanc < 70 and voiture_joueur == blanc2:
            janela.blit(gagne, (130, 300))
        elif blanc > 70 and voiture_joueur == blanc2:
            janela.blit(perdu, (130, 300))
            blanc = 10000
        if rouge < 70 and voiture_joueur == rouge2:
            janela.blit(gagne, (130, 300))
        elif rouge > 70 and voiture_joueur == rouge2:
            janela.blit(perdu, (130, 300))
            rouge = 10000
        if jaune < 70 and voiture_joueur == jaune2:
            janela.blit(gagne, (130, 300))
        elif jaune > 70 and voiture_joueur == jaune2:
            janela.blit(perdu, (130, 300))
            jaune = 10000

    pygame.display.update()
pygame.quit()