import pygame
import random
import sys

# função que acha o recorde no arquivo
def recorde() -> int:
    try:
        with open("score.txt", "r") as arquivo:
            scores = [int(linha.strip()) for linha in arquivo if linha.strip().isdigit()]
            return max(scores) if scores else 0
    except FileNotFoundError:
        return 0

# Carrega o fundo
imagem_fundo = pygame.image.load("background.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (1200, 800))

# Inicializa pygame
pygame.init()

# Tela 1200x800
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Rain")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Fonte
font = pygame.font.SysFont("Arial", 22, bold=True)

# Configurações do jogador
player_size = 100
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 275
player_speed = 7
player_direction = "right"

# Carrega TODAS as imagens do sapo
sapo_direita = pygame.image.load("sapo_direita.png").convert_alpha()
sapo_direita = pygame.transform.scale(sapo_direita, (player_size, player_size))

sapo_esquerda = pygame.image.load("sapo_esquerda.png").convert_alpha()
sapo_esquerda = pygame.transform.scale(sapo_esquerda, (player_size, player_size))

sapo_pulando_direita = pygame.image.load("sapo_pulando_direita.png").convert_alpha()
sapo_pulando_direita = pygame.transform.scale(sapo_pulando_direita, (player_size, player_size))

sapo_pulando_esquerda = pygame.image.load("sapo_pulando_esquerda.png").convert_alpha()
sapo_pulando_esquerda = pygame.transform.scale(sapo_pulando_esquerda, (player_size, player_size))

sapo_meio_direita = pygame.image.load("sapo_meio_parado_direita.png").convert_alpha()
sapo_meio_direita = pygame.transform.scale(sapo_meio_direita, (player_size, player_size))

sapo_meio_esquerda = pygame.image.load("sapo_meio_parado_esquerda.png").convert_alpha()
sapo_meio_esquerda = pygame.transform.scale(sapo_meio_esquerda, (player_size, player_size))

# Variável pra controlar qual imagem mostrar
imagem_atual = sapo_direita
contador = 0

# Corações (vidas)
heart_img = pygame.image.load("coracao.png").convert_alpha()
heart_size = 30
heart_img = pygame.transform.scale(heart_img, (heart_size, heart_size))

# Configurações do jogo
lives = 3
score = 0
fall_speed = 3
spawn_rate = 20
red_probability = 0.4

# Carrega imagens das frutas e bomba
banana_img = pygame.image.load("banana.png").convert_alpha()
uva_img = pygame.image.load("uva.png").convert_alpha()
melancia_img = pygame.image.load("melancia.png").convert_alpha()
bomba_img = pygame.image.load("bomba.png").convert_alpha()

fruit_size = 40
banana_img = pygame.transform.scale(banana_img, (fruit_size, fruit_size))
uva_img = pygame.transform.scale(uva_img, (fruit_size, fruit_size))
melancia_img = pygame.transform.scale(melancia_img, (fruit_size, fruit_size))
bomba_img = pygame.transform.scale(bomba_img, (fruit_size, fruit_size))

# Lista de objetos (frutas e bombas)
objects = []

# Relógio
clock = pygame.time.Clock()
frame_count = 0

# Loop principal
running = True
while running:
    clock.tick(60)
    frame_count += 1

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento do jogador
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        player_direction = "left"
        
        # Animação: troca a imagem a cada 10 frames
        contador += 1
        if contador < 10:
            imagem_atual = sapo_esquerda
        elif contador < 20:
            imagem_atual = sapo_meio_esquerda
        elif contador < 30:
            imagem_atual = sapo_pulando_esquerda
        else:
            contador = 0
            
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
        player_direction = "right"
        
        # Animação: troca a imagem a cada 10 frames
        contador += 1
        if contador < 10:
            imagem_atual = sapo_direita
        elif contador < 20:
            imagem_atual = sapo_meio_direita
        elif contador < 30:
            imagem_atual = sapo_pulando_direita
        else:
            contador = 0

    # Impede sair da tela
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_size:
        player_x = WIDTH - player_size

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    # Spawn de frutas ou bombas
    if frame_count % spawn_rate == 0:
        x_pos = random.randint(0, WIDTH - fruit_size)
        if random.random() > red_probability:
            fruta_img = random.choice([banana_img, uva_img, melancia_img])
            color = GREEN
        else:
            fruta_img = bomba_img
            color = RED
        objects.append({"rect": pygame.Rect(x_pos, 0, fruit_size, fruit_size), "color": color, "img": fruta_img})

    # Atualiza posição dos objetos
    for obj in objects[:]:
        obj["rect"].y += fall_speed

        # Colisão
        if obj["rect"].colliderect(player_rect):
            if obj["color"] == GREEN:
                score += 1
            else:
                lives -= 1
            objects.remove(obj)
        elif obj["rect"].y > HEIGHT - 200:
            objects.remove(obj)

    # Dificuldade progressiva
    if frame_count % 300 == 0:
        if spawn_rate > 6:
            spawn_rate -= 2
        fall_speed += 1
        if red_probability <= 0.7:
            red_probability += 0.1

    # Desenha fundo
    screen.blit(imagem_fundo, (0, 0))

    # Desenha o sapo (com a imagem atual)
    screen.blit(imagem_atual, (player_x, player_y))

    # Desenha frutas e bombas
    for obj in objects:
        screen.blit(obj["img"], obj["rect"])

    # HUD - Pontos e Recorde
    score_text = font.render(f"Pontos: {score}", True, BLACK)
    recorde_text = font.render(f"Recorde: {recorde()}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(recorde_text, (WIDTH // 2 - 60, 10))

    # Desenha corações (vidas restantes)
    for i in range(lives):
        screen.blit(heart_img, (WIDTH - (i + 1) * (heart_size + 5) - 10, 10))

    # Game Over
    if lives <= 0:
        game_over_text = font.render("GAME OVER", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(2500)
        with open("score.txt", "a") as arquivo:
            arquivo.write(f"{score}\n")
        recorde()
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
