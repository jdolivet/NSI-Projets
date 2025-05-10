# Jeux d'hasard

# On importe les modules randint et pyxel pour faire la partie visuelle
import pyxel as px
from random import randint

# Taille définit pour la fenêtre (pris dans le site PYXEL vue en classe)
# Taille de la fenetre 128x128 pixels
px.init(128, 128, title = "Casino du Tigre")
px.mouse(True) #Faire que la souris soit visible

# Création des cases
x_nombre1 = 10
y_nombre1 = 40

x_nombre2 = 45
y_nombre2 = 40

x_nombre3 = 80
y_nombre3 = 40

# Position des cases
cases = [
    {"x": 10, "y": 40, "val": 0},
    {"x": 45, "y": 40, "val": 0},
    {"x": 80, "y": 40, "val": 0}
]

#GOD MODE - Essentiellement pour des Tests
GOD_MODE = False

# Définir argents
argent = randint(150, 200)

#Définie si la variable argent à déjà été modifié ou pas
argent_update = False

# Définir le changement des nombres
jackpot = 0

# Définie le blockage du jeu pour ne pas avoirs de 'spam'
block = True

# Définie la fin du jeu par le game_over, le jeut fini s'il est = True
game_over = False

# Définie l'index du jackpot comme 0 pour commencer au début des cases
jackpot_index = 0

#Fonction de reset du jeu
def reset_game():
    """Renvoie la reinitialisation du jeu pour recommencer
    une nouvelle partie."""
    global argent, jackpot, jackpot_index, block, argent_update, game_over, GOD_MODE
    
    # Reset le jeu au début
    argent = randint(150, 200)
    jackpot = 0
    block = True
    argent_update = False
    game_over = False
    GOD_MODE = False
    for c in cases:
        c["val"] = 0

# Animation de suspense entre les tirages
def tirage_avec_suspense(index):
    for _ in range(10):
        cases[index]["val"] = randint(1, 7) # Tirage des valeurs
        px.cls(0)
        draw() # Appelle la function draw pour faire les dessins
        px.flip()
        l = 0
        for _ in range(1_000_000): # Temps de suspense sans le module time
            l += 1
    cases[index]["val"] = randint(1, 7) # Autre tirage des valeurs

# Quelques combinaisons possibles et leurs valeurs
def eval_combinaison():
    global argent
    valeurs = [c["val"] for c in cases]

    # Liste pour les combinaisons et leurs valeurs
    if valeurs.count(7) == 3: # 7
        argent += 1000  
    elif valeurs.count(5) == 3: # BAR
        argent += 300  
    elif valeurs.count(6) == 3: # Étoile
        argent += 200  
    elif valeurs.count(4) == 3: # Cloche
        argent += 120  
    elif valeurs.count(3) == 3: # Pastèque
        argent += 90   
    elif valeurs.count(2) == 3: # Citron
        argent += 60   
    elif valeurs.count(1) == 3: # Cerise
        argent += 30   
    elif valeurs.count(7) == 2: # deux 7
        argent += 200
    elif valeurs.count(7) == 1: # Jackpot
        argent += 90
    else:
        #Cumulation des pertes
        perte = 0
        for v in valeurs:
            if v == 1:
                perte += 50  # Cerise
            elif v == 2:
                perte += 40  # Citron
            elif v == 3:
                perte += 30  # Pastèque
        argent -= perte

# Chargement des images
px.load("Sprites.pyxres")

# =========================================================
# == UPDATE
# =========================================================
def update():
    """mise à jour des variables (30 fois pra secondes)"""
    global block, argent, argent_update, game_over, GOD_MODE, jackpot_index
    
    # Activation du mode Dieu pour essentiellement des Tests 
    if px.btnp(px.KEY_G):
        GOD_MODE = True
    
    # Tester le mode de victoire et de perte du jeu
    if GOD_MODE:
        if px.btnp(px.KEY_Z):
            argent = -1000
        if px.btnp(px.KEY_X):
            argent = 1000
    
    # Fim du jeu
    if game_over:
        if px.btnp(px.KEY_R):
            reset_game()

    # Reinicilaise je jeu
    if px.btnp(px.KEY_R):
        reset_game()
    
    # Reinicialise par button
    if px.btnp(px.MOUSE_BUTTON_LEFT):
        if 7 <= px.mouse_x <= 30 and 110 < px.mouse_y <= 122:
            reset_game()

    # Fait un tirage au sort
    if px.btnp(px.MOUSE_BUTTON_LEFT):
        if 48 <= px.mouse_x <= 70 and 105 < px.mouse_y <= 122:
            if jackpot_index < 3:
                tirage_avec_suspense(jackpot_index)
                jackpot_index += 1
                block = False
    
    # Fait un tirage au sort
    elif px.btnp(px.KEY_SPACE) and jackpot_index < 3:
        tirage_avec_suspense(jackpot_index)
        jackpot_index += 1
        block = False

    # Débloque pour le prochain tirage
    if px.btnp(px.MOUSE_BUTTON_RIGHT):
        for c in cases:
            c["val"] = 0
        jackpot_index = 0
        block = True
        argent_update = False
    
    # Vérifie si les 3 cases sont remplis ou pas dans leurs valeurs, calcule les combinaisons obtenue
    # et enfim actualise l'argent
    if not argent_update and all(c["val"] != 0 for c in cases):
        eval_combinaison()
        argent_update = True

# =========================================================
# == DRAW
# =========================================================
def draw():
    """Renvoie la partie graphique de notre jeu"""
    global game_over
    px.cls(0)

    # Renvoie les 3 cases blanches où les dessins von être mis et révèle celui qui à été choisis.
    for c in cases:
        px.rect(c["x"], c["y"], 32, 48, 7)
        if 1 <= c["val"] <= 7:
            sprite_y = (c["val"] - 1) * 48 # Renvoie les cases des sprites choisis par l'ordonné
            px.blt(c["x"], c["y"], 0, 0, sprite_y, 32, 48, 0)
            
    # Les cases blanches de reset et de tirage au sort
    px.rect(7, 105, 30, 15, 7)
    px.text(10, 110, "RESET", 0)
    px.rect(48, 105, 30, 15, 7)
    px.text(50, 110, "TIRER", 0)
    
    #Text de l'argent
    px.text(35, 20, f"Argent: {argent}", 10)
    
    # Écran de défaite
    if argent <= -200:
        px.cls(0)
        px.text(40, 50, "- GAME OVER -", 8)
        px.text(22, 70, "Appuie sur R pour rejouer", 7)
        game_over = True
        
    #Écran de victoire
    elif argent >= 500:
        px.cls(0)
        px.text(20, 50, "- VOUS ÊTES RICHE ! -", 10)
        px.text(22, 70, "Appuie sur R pour rejouer", 7)
        game_over = True

# Execution du code
px.run(update, draw)