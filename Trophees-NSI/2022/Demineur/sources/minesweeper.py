# PROJET MINESWEEPWER
import pygame, sys
from random import randint
from time import sleep

pygame.init()
#constantes
#partie graphique
# mainloop qui sert pour tous les jeux sur pygame

def interfaceg():
    """
    Cette fonction sert à créer la fenêtre de Pygame
    """
    case_videv = case_vide()
    h = 0
    for i in range(0, X):
        l = 0
        for j in range(0, Y):
            page.blit(case_videv, (l, h))
            l += LARGEURPX / Y
        h += HAUTEURPX / X
    pygame.display.update() #ceci sert à actualiser la page pygame  
    
def fenetre_pygame():
    """
    La fonction principale du programme: responsable de rassembler et faire tourner
    toutes les fonctions du programme
    """
    global page
    global grille_jeu
    n = input("selectionez un mode de jeu (facile, moyen ou difficile):")
    infos(n) # fonction la plus importante 
    num_mines = mines
    page = pygame.display.set_mode( (LARGEURPX, HAUTEURPX) ) # taille de la grille du jeu
    pygame.display.set_caption('Minesweeper') # Nom de la fenetre pygame
    pygame.display.update()
    grille_complete = grille_mines(grille_vide())
    case_videv = case_vide()
    drapeauv = drapeau()
    grille_jeu = [['.'] * Y for i in range(X)] # grille qui représente l'interface graphique sur python pour fair des calculs
    interfaceg()
    # mainloop qui sert pour tous les jeux sur pygame
    while True:
        """
        Gestionnaire d'évenements:
        conditions de victoire, coordonnées, grille et clics
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # si on appuie sur la croix (boutton d'exit)
                sys.exit()                            
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2] == True: # si on appuie sur le boutton droit de la souris
                # nous permet de prendre les coordonnées de où on a cliqué sur l'interface graphique
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                # transforme ces coordonnées de l'interface graphique en coordonnées de tableau
                colonne_alt = int(mouseY // (HAUTEURPX / X))
                ligne_lar = int(mouseX // (LARGEURPX / Y))
                # boucle if qui nous permet de placer et d'enlever les drapeaux 
                if grille_jeu[colonne_alt][ligne_lar] == 'F': 
                    page.blit(case_videv, (ligne_lar*(LARGEURPX / Y), colonne_alt*(HAUTEURPX / X)))
                    grille_jeu[colonne_alt][ligne_lar] = '.'
                    num_mines += 1
                elif num_mines > 0 and grille_jeu[colonne_alt][ligne_lar] == '.':
                    num_mines -= 1
                    grille_jeu[colonne_alt][ligne_lar] = 'F'
                    page.blit(drapeauv, (ligne_lar*(LARGEURPX / Y), colonne_alt*(HAUTEURPX / X)))
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == True: # si on appuie sur le boutton gauche de la souris
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                colonne_alt = int(mouseY // (HAUTEURPX / X))
                ligne_lar = int(mouseX // (LARGEURPX / Y))
                tab_jeu(grille_complete, colonne_alt, ligne_lar)
            pygame.display.update()
            condition_vitoire(grille_complete) 
    
# début des fonctions du jeu
def tab_jeu(g : list, x : int, y : int) -> None:
    """
    procédure qui controle le jeu
    """
    global tab_images
    bombe_nncliquev = bombe_nnclique()
    drapeau_trompev = drapeau_trompe()
    bombe_cliquev = bombe_clique()
    tab_images = possibles_voisins()
    if grille_jeu[x][y] == '.':
        if g[x][y] == 0:
            voisins = voisinage(g, x, y)
            grille_jeu[x][y] = voisins
            page.blit(tab_images[voisins], (y*(LARGEURPX/Y), x*(HAUTEURPX/X)))
            pygame.display.update()
            clic_recursif(g, x, y)
            pygame.display.update()
        if g[x][y] == 1:
            grille_jeu[x][y] = 'B'
            page.blit(bombe_cliquev, (y*(LARGEURPX/Y), x*(HAUTEURPX/X)))
            pygame.display.update()
            for i in range(len(g)):
                for j in range(len(g[0])):
                    if g[i][j] == 1 and (i, j) != (x, y):
                        grille_jeu[i][j] = 'B'
                        page.blit(bombe_nncliquev,(j*(LARGEURPX/Y), i*(HAUTEURPX/X)))
                    elif g[i][j] == 0 and grille_jeu[i][j] == 'F':
                        page.blit(drapeau_trompev, (j*(LARGEURPX/Y), i*(HAUTEURPX/X)))
            pygame.display.update()
            print("vous avez perdu!")
            sleep(8)
            sys.exit() # arrête le programme
            
              
def grille_mines(g):
    """
    transforme la fonction grille_vide() en mettant des 1 aléatoirement (représentant
    les mines) pour avoir une grille avec des mines
    """
    a = mines
    while a > 0:
        x = randint(0, X-1)
        y = randint(0, Y-1)
        if g[x][y] == 0:
            g[x][y] = 1
            a -= 1
    return g

def grille_vide():
    """
    Procédure créant une grille vide
    """
    return [[0] * Y for i in range(X)]
         
def infos(n):
    """
    Informations sur les tailles référentes aux difficultés
    """
    global mines
    global LARGEURPX
    global HAUTEURPX
    global X
    global Y
    if n == 'facile':
        Y = 10
        X = 8
        HAUTEURPX = 480
        LARGEURPX = 600
        mines = 10
    elif n == 'moyen':
        Y = 18
        X = 14
        HAUTEURPX = 630
        LARGEURPX = 810
        mines = 40
    elif n == 'difficile':
        Y = 24
        X = 20
        HAUTEURPX = 600
        LARGEURPX = 720
        mines = 99
    return [[0] * Y for i in range(X)]
    
def voisinage(tab : list, i : int, j : int) -> int: 
    """
    fonction qui analyse les mines autour de la case cliquée
    renvoyant le nombre de voisins
    """
    nbVoisins = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if 0 <= k < len(tab) and 0 <= l < len(tab[0]):
                if k != i or l != j:
                    nbVoisins += tab[k][l]
    return nbVoisins

def condition_vitoire(g):
    """
    procédure qui regarde si on a gagné
    """
    nb = 0
    for k in range(len(g)):
        for l in range(len(g[0])):
            if g[k][l] == 0 and grille_jeu[k][l] == '.' :
                nb += 1
            else:
                nb += 0
    if nb == 0:
        print('vous avez gagné')
        sleep(5)
        sys.exit() 
    
def clic_recursif(g : list, x : int, y : int) -> None:
    """
    Procédure qui va voir si la case de coordonnées x et y a 0 mines à côté.
    Si elle en a pas, elle va montrer la valeur des cases de son côté.
    Si une de ces cases ouvertes n'a pas de voisins, la fonction va être répétée
    jusqu'à ce qu'il n'y ait aucune case avec 0 mines à côté.
    """
    if voisinage(g, x, y) == 0:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < len(g) and 0 <= j < len(g[0]):
                    if x != i or j != y:
                        voisins = voisinage(g, i, j)
                        if grille_jeu[i][j] == '.' and voisins == 0:
                            grille_jeu[i][j] = voisins
                            clic_recursif(g, i, j)
                        page.blit(tab_images[voisins], (j*(LARGEURPX/Y), i*(HAUTEURPX/X)))
                        grille_jeu[i][j] = voisins

def possibles_voisins():
    """
    les images des numéros utilisés pour le programme
    """
    zero = pygame.image.load('0.png')
    zero_transf = pygame.transform.scale(zero, (LARGEURPX//Y, HAUTEURPX//X))
    un = pygame.image.load('1.png')
    un_transf = pygame.transform.scale(un, (LARGEURPX//Y, HAUTEURPX//X))
    deux = pygame.image.load('2.png')
    deux_transf = pygame.transform.scale(deux, (LARGEURPX//Y, HAUTEURPX//X))
    trois = pygame.image.load('3.png')
    trois_transf = pygame.transform.scale(trois, (LARGEURPX//Y, HAUTEURPX//X))
    quatre = pygame.image.load('4.png')
    quatre_transf = pygame.transform.scale(quatre, (LARGEURPX//Y, HAUTEURPX//X))
    cinq = pygame.image.load('5.png')
    cinq_transf = pygame.transform.scale(cinq, (LARGEURPX//Y, HAUTEURPX//X))
    six = pygame.image.load('6.png')
    six_transf = pygame.transform.scale(six, (LARGEURPX//Y, HAUTEURPX//X))
    sept = pygame.image.load('7.png')
    sept_transf = pygame.transform.scale(sept, (LARGEURPX//Y, HAUTEURPX//X))
    huit = pygame.image.load('8.png')
    huit_transf = pygame.transform.scale(huit, (LARGEURPX//Y, HAUTEURPX//X))
    return (zero_transf, un_transf, deux_transf, trois_transf, quatre_transf, cinq_transf, six_transf, sept_transf, huit_transf)

def case_vide():
    """
    image de la case vide
    """
    case_vide = pygame.image.load('emptyblock.png')
    case_vide_transf = pygame.transform.scale(case_vide, (LARGEURPX//Y, HAUTEURPX//X))
    return case_vide_transf

def drapeau():
    """
    image du drapeau
    """
    drapeau = pygame.image.load('flag.png')
    drapeau_transf = pygame.transform.scale(drapeau, (LARGEURPX//Y, HAUTEURPX//X))
    return drapeau_transf

def bombe_clique():
    """
    image de la bombe quand cliquée
    """
    bomb_clique = pygame.image.load('bomb-at-clicked-block.png')
    bomb_clique_transf = pygame.transform.scale(bomb_clique, (LARGEURPX//Y, HAUTEURPX//X))
    return bomb_clique_transf

def bombe_nnclique():
    """
    image de la bombe non-révélée
    """
    bomb_nnclique = pygame.image.load('unclicked-bomb.png')
    bomb_nnclique_transf = pygame.transform.scale(bomb_nnclique, (LARGEURPX//Y, HAUTEURPX//X))
    return bomb_nnclique_transf

def drapeau_trompe():
    """
    image quand le drapeau a été mal placé quand a perdu
    """
    drapeau_trompe = pygame.image.load('wrong-flag.png')
    drapeau_trompe_transf = pygame.transform.scale(drapeau_trompe, (LARGEURPX//Y, HAUTEURPX//X))
    return drapeau_trompe_transf
    
fenetre_pygame()