import pygame
import random
import sys

cartas_jogador_imgs = []
pontos_jogador = []
total_jogador = 0
cartas_dealer_imgs = []
pontos_dealer = []
total_dealer = 0
    
pygame.init()
pygame.mixer.init()

# Carregar sons
som1 = pygame.mixer.Sound("buble.mp3")
som2 = pygame.mixer.Sound("MusicaNSI1.mp3")
som3 = pygame.mixer.Sound('Gameover1.mp3')

# Tamanho da tela
tela_larg = 1920
tela_alt = 1080
tela = pygame.display.set_mode((tela_larg, tela_alt))
pygame.display.set_caption("Blackjack")

# Fundo da mesa
fundo = pygame.image.load('Mesa de Poker em Estilo Pixel.png')  
fundo = pygame.transform.scale(fundo, (tela_larg, tela_alt))

# Telas de Vit/Derro
Gameover1 = pygame.image.load('Gameover1.png')
Gameover1 = pygame.transform.scale(Gameover1, (tela_larg, tela_alt))

Gameover2 = pygame.image.load('Gameover2.png')
Gameover2 = pygame.transform.scale(Gameover2, (tela_larg, tela_alt))

Youwin1 = pygame.image.load('Youwin1.png')
Youwin1= pygame.transform.scale(Youwin1, (tela_larg, tela_alt))

matchnul = pygame.image.load('matchnul.png')
matchnul= pygame.transform.scale(matchnul, (tela_larg, tela_alt))

Youwin2 = pygame.image.load('youwin2.png')
Youwin2= pygame.transform.scale(Youwin2, (tela_larg, tela_alt))

# Classe de botão 
class Button:
    def __init__(self, x, y, image, scale):
        largura = image.get_width()
        altura = image.get_height()
        self.image = pygame.transform.scale(image, (int(largura * scale), int(altura * scale)))
        self.rect = pygame.Rect(0, 0, 300, 300)
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        # Desenha a imagem centralizada na área de clique
        surface.blit(self.image, self.image.get_rect(center=self.rect.center))
        return action

# Naipes e valores baseados nos nomes dos arquivos
naipes = ["hearts", "diamonds", "spades", "clubs"]
valores = ["A", "02", "03", "04", "05", "06", "07", "08", "09", "10", "J", "Q", "K"]

def sortear_carta():
    naipe = random.choice(naipes)
    valor = random.choice(valores) 
    carta_jogador_str = valor + naipe
    confirmation_A(pontos_jogador)
    pontos_jogador.append(valor_carta(carta_jogador_str))
    caminho = f"Cards (small)/card_{naipe}_{valor}.png"
    try:
        carta = pygame.image.load(caminho)
        return pygame.transform.scale(carta, (100, 150))
    except:
        print(f"Erro ao carregar: {caminho}")
        return None

def valor_carta(a: str) -> int:
    # On extrait le début jusqu'à ce que ce ne soit plus un chiffre
    valor = ""
    for caractere in a:
        if caractere.isdigit():
            valor += caractere
        else:
            break
    if valor:
        return int(valor)
    elif a[0] == "A":
        return 11
    else:
        return 10  # Pour J, Q, K

def confirmation_A(a):
    '''verifier si le A doit valoire 11 ou 1'''
    total = sum(a)
    for i in range(len(a)):
        if a[i] == 11:
            if total > 21:
                a[i] = 1

def sortear_dealer():
    naipe = random.choice(naipes)
    valor = random.choice(valores) 
    carta_dealer_str = valor + naipe
    confirmation_A(pontos_dealer)
    pontos_dealer.append(valor_carta(carta_dealer_str))
    caminho = f"Cards (small)/card_{naipe}_{valor}.png"
    try:
        carta = pygame.image.load(caminho)
        carta_img = pygame.transform.scale(carta, (100, 150))
        cartas_dealer_imgs.append(carta_img) #ajout au tableau des cartes du dealer
        return carta_img
    except:
        print(f"Erro ao carregar: {caminho}")
        return None
    
def dealer_play():
    while sum(pontos_dealer) < 17:
        sortear_dealer()

# Carregamento das imagens dos botões
botao_hit_img = pygame.image.load("Botao_Hit.png")
botao_fold_img = pygame.image.load("Botao_Fold.png")

# Posicionamento mais proporcional na tela Full HD
botao_hit = Button(600, 850, botao_hit_img, 0.6)
botao_fold = Button(1320, 850, botao_fold_img, 0.6)

# Initialiser la liste des cartes du dealer avec une carte
sortear_dealer()
    
#Deux premières cartes du joueur
for _ in range(2):
    carte = sortear_carta()
    if carte:
        cartas_jogador_imgs.append(carte)
        
fin_jeu = False
# Loop principal
run = True
som2.play()
while run:
    tela.blit(fundo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
            
    # Affiche toutes les cartes du dealer, décalées
    for i, carta_img in enumerate(cartas_dealer_imgs):
        tela.blit(carta_img, (650 + i*110, 250))

    # Affiche toutes les cartes du joueur, décalées
    for i, carta_img in enumerate(cartas_jogador_imgs):
        tela.blit(carta_img, (650 + i*110, 650))
        
    # Botões
    if botao_hit.draw(tela):
        print("HIT clicado")
        nova_carta_img = sortear_carta()
        if nova_carta_img:
            cartas_jogador_imgs.append(nova_carta_img)#ajout au tableau des cartes du joueur   
        som1.play()
    
    if botao_fold.draw(tela) and not fin_jeu:
        print("FOLD clicado")
        dealer_play()
        fin_jeu = True
        som1.play()
        som2.fadeout(2000)
        som3.play(2000)
        
    if fin_jeu:
        
    #Redessine tout avant que le jeu se termine (cartes dealer et joueur)
        tela.blit(fundo, (0, 0))
        for i, carta_img in enumerate(cartas_dealer_imgs):
            tela.blit(carta_img, (650 + i*110, 250))
        for i, carta_img in enumerate(cartas_jogador_imgs):
            tela.blit(carta_img, (650 + i*110, 650))
        
    #Affichage des resultats
            confirmation_A(pontos_jogador)
            confirmation_A(pontos_dealer)
            total_jogador = sum(pontos_jogador)
            total_dealer = sum(pontos_dealer)
    
        if total_jogador > 21:
            tela.blit(Gameover1, (0, 0))  # Jogador estourou
            
        elif total_dealer > total_jogador and total_dealer <= 21:
              tela.blit(Gameover2, (0, 0))  # Dealer venceu
              
        elif total_jogador > total_dealer:
            tela.blit(Youwin1, (0, 0))  # Jogador venceu
            
        elif total_dealer > 21:
            tela.blit(Youwin2,(0,0))
            
        else:
            tela.blit(matchnul,(0,0))

        pygame.display.update()
    pygame.display.update()