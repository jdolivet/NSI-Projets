import pyxel
from random import randint, choice
import math
import numpy as np
import cmath
import time
from numba import njit, prange

pyxel.init(160, 120, "Exposition Papillon")


#==============CLASS==================
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


#===========VARIABLES=================
    N_COR = 9
PALETAS = [
    # Butterfly 3000: roxo profundo, magenta, laranja, dourado, turquesa
    [0x1B0B3A, 0x4B1D8F, 0xB5179E, 0xF72585, 0xFF6B35, 0xFFB627, 0x2EC4B6, 0x0E7C86, 0x2A1458],
    # Sgt. Pepper: vermelho, ouro, verde-musgo, azul-royal, rosa
    [0x7A0C1E, 0xD62828, 0xF77F00, 0xFCBF49, 0x6A994E, 0x1D4E89, 0x2B2D9E, 0xE85D9E, 0x3A0F2B],
    # turquesa lisérgico
    [0x03203C, 0x045D6E, 0x00B4A6, 0x7DFFB3, 0xE2F34B, 0xFF8552, 0xE0457B, 0x6B2D8F, 0x22134D],
    # brasa
    [0x2B0A16, 0x6E0F2B, 0xC21E3A, 0xFF4D2E, 0xFF9E1F, 0xFFD23F, 0xFF5CA8, 0x8E2C9E, 0x4A1259],
    # néon noturno
    [0x0A0F3D, 0x1F3FBF, 0x14A3F2, 0x1DE9D6, 0x9DFF3D, 0xFFE53D, 0xFF3DA5, 0x9B2FE0, 0x2A0F6B],
    # fúcsia e ouro
    [0x240046, 0x5A189A, 0x9D4EDD, 0xFF2E93, 0xFF7B54, 0xFFC857, 0xA7E22E, 0x1B998B, 0x12355B],
    # Pepper marinho
    [0x0B132B, 0x1C2E6B, 0x3A6EA5, 0xE63946, 0xFFB703, 0xF4A6C0, 0x5FAD56, 0x7B2CBF, 0x3B0A45],
    # ametista e fogo
    [0x15012D, 0x3C096C, 0x7B2CBF, 0xC77DFF, 0xFF4D6D, 0xFF8C42, 0xFFD60A, 0x00C2A8, 0x07575B],
]
 
# Os 16 primeiros slots ficam para o resto (0 = preto, 7 = linhas, 13 = círculos);
# as paletas ficam logo depois.
BASE = 16
cores_base = pyxel.colors.to_list()[:16]
cores_base[7] = 0xEDE7FF     # linhas da grade
cores_base[13] = 0xFFD166    # contorno dos círculos
SIZE = 128              # tela e grade (Pyxel aceita até 256x256)
DU, DV = 0.16, 0.08
F, K = 0.025, 0.055
DT = 1.0
STEPS_PER_FRAME = 20
VMAX = 0.4
HOLE_RADIUS = 12        # raio do espaço vazio, em células
 
PALETTES = {
    "psicodelica": [0x05010F, 0x2A0B63, 0x7B1FA2, 0xE91E8C, 0xFF7A18, 0xFFE259],
    "pepper":      [0x0D1B2A, 0x1B4965, 0x62B6CB, 0xF4D35E, 0xEE6C4D, 0xB5179E],
    "rosa":        [0xFF007F, 0x39FF14, 0x00E5FF, 0x7A00FF, 0xFFFEE0],
}
palito_normal = [
    0x000000,  # 0  noir
    0x2B2B2B,  # 1  gris très foncé
    0x7E2553,  # 2  violet foncé
    0x008751,  # 3  vert
    0xAB5236,  # 4  brun
    0x5F574F,  # 5  gris
    0xC2C3C7,  # 6  gris clair
    0xFFF1E8,  # 7  blanc cassé
    0xFF004D,  # 8  rouge
    0xFFA300,  # 9  orange
    0xFFEC27,  # 10 jaune
    0x00E436,  # 11 vert vif
    0x29ADFF,  # 12 bleu clair
    0x83769C,  # 13 violet/gris
    0xFF77A8,  # 14 rose
    0xFFCCAA   # 15 pêche
]
PALETTE_NAMES = list(PALETTES)
LARGURA, ALTURA = 256, 192          # resolução interna (a janela é ampliada pelo Pyxel)
FPS = 60
OITAVAS_POR_SEGUNDO = 0.55          # velocidade do zoom (cada oitava = zoom de 2x)
DURACAO_FADE = 1.2                  # segundos de fade ao reiniciar o ciclo
CICLO_CORES = 6.0                   # entradas de paleta por segundo (tecla C liga/desliga)
FREQ_COR = 6.0                      # entradas de paleta por iteração normalizada
BASE_ITER = 100                     # iterações máximas na visão inicial
BAILOUT2 = 256.0 ** 2               # raio de escape grande => coloração suave sem faixas
N_PALETA = 240 
# ---------------------------------------------------------------- estado global
U = None
V = None
palette_id = 0
steps = STEPS_PER_FRAME
hyp_on = True
hyp_zoom = 1.5          # ampliação do centro (1 = tamanho original)
RIM = 0.985             # onde o disco termina (perto de 1 = mais ladrilhos na borda)
HYP_MAP = None
zorb = 160
plok = 120

mira = 6
vex = 90

qalu = (1 + math.sqrt(5)) / 2
nix = 1 / qalu

blip = 0

LARGEUR = 160
HAUTEUR = 120
paii = 16
PERIODE = 60
CLOK = [1, 2, 5, 6, 9, 13]
frwhb = 0
fruit = []
hello = []

for i in range(PERIODE):
    angle = 2 * math.pi * i / PERIODE
    fruit.append(math.cos(angle))
    hello.append(math.sin(angle))

TAILLE = 16
N = 6

anglus = 0

MAIN=1
ab=0
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
zoom = 0.1
zoom_factor = 0.6
iterations = 100
zoom_max = 35
zoom_step = 0
direction = 1
target_x = -0.74368
target_y = 0.13182590420533
xAxis = 1 / zoom
yAxis = (
    pyxel.height
    / (pyxel.width * zoom)
)
xOffset = (
    target_x
    - xAxis / 2
)
yOffset = (
    target_y
    - yAxis / 2
)
ratio = (
    xAxis
    / pyxel.width
)
pixels = []
W = 160
H = 120
CELL = 20
move_x = 0
move_y = 0
speed = 0.7
dir = 0
distance = 18
tiles = []
size = 9
for row in range(-7, 8):
    for col in range(-9, 10):
        x = col * size * 1.5
        y = row * size * 1.73
        # Décalage une ligne sur deux
        if row % 2:
            x += size * 0.75

        tiles.append((x, y))
PHI = (1 + math.sqrt(5)) / 2
angle = 0.0
a = 0
LARGURA, ALTURA = 160, 120          # resolução interna (a janela é ampliada pelo Pyxel)
FPS = 60
OITAVAS_POR_SEGUNDO = 0.55          # velocidade do zoom (cada oitava = zoom de 2x)
DURACAO_FADE = 1.2                  # segundos de fade ao reiniciar o ciclo
CICLO_CORES = 6.0                   # entradas de paleta por segundo (tecla C liga/desliga)
FREQ_COR = 6.0                      # entradas de paleta por iteração normalizada
BASE_ITER = 100                     # iterações máximas na visão inicial
BAILOUT2 = 256.0 ** 2               # raio de escape grande => coloração suave sem faixas
N_PALETA = 240                      # cores do gradiente (índices 16..255 da paleta do Pyxel)

# --------------------------------------------------------------------------
# Geometria do zoom (constantes obtidas com mpmath, 80 dígitos, método de Newton)
# --------------------------------------------------------------------------
VISAO_CENTRO = complex(-0.75, 0.0)  # visão inicial: o conjunto de Mandelbrot inteiro
VISAO_LARGURA = 3.2                 # largura inicial no plano complexo (altura = 2.4)

PERIODO = 39                        # período do minibrot alvo
NUCLEO = complex(-0.7436423016578859461186, 0.1318265198125947234992)   # c*, vale do cavalo-marinho
KAPPA = complex(392874.2814282083309732, -242552.4388293218942412)      # fator de renormalização

LOG_KAPPA = cmath.log(KAPPA)
OITAVAS_TOTAIS = math.log2(abs(KAPPA))                  # ~18.8 oitavas por ciclo
PONTO_FIXO = NUCLEO * KAPPA / (KAPPA - 1.0)             # ponto fixo da semelhança c -> c* + c/KAPPA


# --------------------------------------------------------------------------
# "Shader": kernel numba (um pixel = um c do plano complexo)
# --------------------------------------------------------------------------

cote = 9
centre_x = pyxel.width / 2
centre_y = pyxel.height / 2
col1=2
col2=9
angl = 0
profondeur = 5
taille = 50
butterflies = [
    [20, 25, 0.0,  0.020, 0.42],
    [50, 25, 1.0, -0.017, 0.42],
    [80, 25, 2.0,  0.022, 0.42],
    [110, 25, 3.0, -0.019, 0.42],
    [140, 25, 4.0,  0.018, 0.42],

    [35, 52, 0.5, -0.021, 0.42],
    [65, 52, 1.5,  0.018, 0.42],
    [95, 52, 2.5, -0.020, 0.42],
    [125, 52, 3.5,  0.021, 0.42],

    [20, 79, 1.0,  0.019, 0.42],
    [50, 79, 2.0, -0.022, 0.42],
    [80, 79, 3.0,  0.020, 0.42],
    [110, 79, 4.0, -0.018, 0.42],
    [140, 79, 5.0,  0.021, 0.42],

    [35, 106, 0.3, -0.019, 0.42],
    [65, 106, 1.3,  0.022, 0.42],
    [95, 106, 2.3, -0.020, 0.42],
    [125, 106, 3.3,  0.018, 0.42]
]
ang = 0
cot = 10
distanc = cot * (1 + math.sqrt(3))
an = 0.0
rayon_x = 18
rayon_y = 10
sped = 0.025
SIDE = 7.0
DX = SIDE * 1.5
RAIO_MAX = 181
DY = SIDE * math.sqrt(3)
DODEC_COLORS = [
    8,   # rouge
    9,   # orange
    10,  # jaune
    11,  # vert
    12,  # cyan
    13,  # bleu
    14   # rose
]
TRI_COLORS = [
    10,
    12,
    14,
    9,
    11,
    13
]
hexagons = []
for row in range(-14, 15):
    for col in range(-15, 16):
        x = col * DX
        y = row * DY
        if row % 2:
            x += DX / 2
        hexagons.append((x, y))
vertices = {}
d = 0
progresso = 0.0          # 0 -> visão inicial, 1 -> cópia do conjunto dentro do minibrot
velocidade = 1.0         # multiplicador do zoom (teclas CIMA/BAIXO)
pausado = False
ciclar_cores = True
mostrar_hud = True
fase = 0.0               # deslocamento da paleta (ciclo de cores)
fade = 1.0               # 0..1 durante o fade; 1 = sem fade
dt = 1.0 / FPS
fps_suave = float(FPS)
ultimo_tempo = time.perf_counter()
ultimo_desenho = None    # (progresso, fase) do último quadro calculado
max_iter_atual = BASE_ITER
zoom_atual = 1.0
N_COR=9
def cor(g, a, b):
    global N_COR
    """Cor da célula (a, b) dentro da região de "geração" g.
    g escolhe a paleta e também desloca o padrão da grade, então ao cruzar
    a borda de um círculo tanto as cores quanto o desenho da grade mudam."""
    return BASE + (g % len(PALETAS)) * N_COR + (a + 2 * b + 4 * g) % N_COR
 
 

points_horizontal = [
        [[pyxel.width // 2, pyxel.width // 2],[pyxel.width, 0]],
        [[(pyxel.width // 2) + 32, (pyxel.width // 2) + 32],[pyxel.width, 0]],
        [[(pyxel.width // 2) + 64, (pyxel.width // 2) + 64],[pyxel.width, 0]],
        [[(pyxel.width // 2) + 96, (pyxel.width // 2) + 96],[pyxel.width, 0]],
        [[(pyxel.width // 2) + 128, (pyxel.width // 2) + 128],[pyxel.width, 0]],
        [[(pyxel.width // 2) - 32, (pyxel.width // 2) - 32],[pyxel.width, 0]],
        [[(pyxel.width // 2) - 64, (pyxel.width // 2) - 64],[pyxel.width, 0]],
        [[(pyxel.width // 2) - 96, (pyxel.width // 2) - 96],[pyxel.width, 0]],
        [[(pyxel.width // 2) - 128, (pyxel.width // 2) - 128],[pyxel.width, 0]],
        ]
points_vertical = [
        [[pyxel.width, 0],[(pyxel.width // 2), (pyxel.width // 2)]],
        [[pyxel.width, 0],[(pyxel.width // 2) + 32, (pyxel.width // 2) + 32]],
        [[pyxel.width, 0],[(pyxel.width // 2) + 64, (pyxel.width // 2) + 64]],
        [[pyxel.width, 0],[(pyxel.width // 2) + 96, (pyxel.width // 2) + 96]],
        [[pyxel.width, 0],[(pyxel.width // 2) + 128, (pyxel.width // 2) + 128]],
        [[pyxel.width, 0],[(pyxel.width // 2) - 32, (pyxel.width // 2) - 32]],
        [[pyxel.width, 0],[(pyxel.width // 2) - 64, (pyxel.width // 2) - 64]],
        [[pyxel.width, 0],[(pyxel.width // 2) - 96, (pyxel.width // 2) - 96]],
        [[pyxel.width, 0],[(pyxel.width // 2) - 128, (pyxel.width // 2) - 128]]]
 
    # --- memória das cores dos círculos ---------------------------------
    # Cada círculo carrega uma "geração" (um número inteiro) que escolhe a
    # paleta da região dentro dele. 'fundo' é a geração da região fora de
    # todos os círculos. 'ultima' é a última geração já distribuída.
geracao=[1, 2, 3, 4, 5]
fundo=0
ultima=5
    

# --------------------------------------------------------------------------
# Inicialização: compila o kernel antes de abrir a janela
# --------------------------------------------------------------------------

rayon_cercle = [0, 32, 64, 96, 124]

#======================================================================================
#==========================================FONCTIONS===================================
#======================================================================================


@njit(parallel=True, fastmath=True, cache=True)
def calcular_quadro(saida, cx, cy, sx, sy, max_iter, eps, norm, fase, freq, bailout2):
    """Preenche `saida` (uint8, altura x largura) com índices de paleta.

    Pixel (i, j) -> c = (cx + i*cy) + (sx + i*sy) * (u + i*v), com (u, v) em
    pixels a partir do centro. O passo complexo (sx, sy) carrega zoom e rotação.
    Índice 0 = interior do conjunto; 16..255 = gradiente suave cíclico.
    """
    altura, largura = saida.shape
    meio_x = (largura - 1) * 0.5
    meio_y = (altura - 1) * 0.5
    n_cores = 240.0
    for j in prange(altura):
        v = meio_y - j                       # y da tela cresce para baixo; o plano, para cima
        for i in range(largura):
            u = i - meio_x
            cr = cx + sx * u - sy * v
            ci = cy + sy * u + sx * v

            zr = 0.0
            zi = 0.0
            zr2 = 0.0
            zi2 = 0.0
            salvo_r = 1.0e30                 # ponto salvo para detectar órbitas periódicas
            salvo_i = 1.0e30
            proximo = 8
            n = 0
            while n < max_iter:
                zi = 2.0 * zr * zi + ci
                zr = zr2 - zi2 + cr
                zr2 = zr * zr
                zi2 = zi * zi
                n += 1
                if zr2 + zi2 > bailout2:
                    break
                if abs(zr - salvo_r) < eps and abs(zi - salvo_i) < eps:
                    break                    # órbita periódica => interior
                if n == proximo:
                    salvo_r = zr
                    salvo_i = zi
                    proximo = proximo * 2

            m2 = zr2 + zi2
            if m2 <= bailout2:
                saida[j, i] = 0              # interior
            else:
                # iteração fracionária (suaviza as faixas de cor)
                nu = n + 1.0 - math.log(0.5 * math.log(m2)) * 1.4426950408889634
                x = nu / norm * freq + fase
                saida[j, i] = 16 + int(x % n_cores)

_teste = np.zeros((8, 8), dtype=np.uint8)
calcular_quadro(_teste, -0.75, 0.0, 0.1, 0.0, 16, 1e-6, 1.0, 0.0, 6.0, BAILOUT2)
# --------------------------------------------------------------------------
# Utilitários
# --------------------------------------------------------------------------
def visao_numpy(imagem):
    """Enxerga a memória de uma pyxel.Image como array numpy (altura, largura)."""
    ptr = imagem.data_ptr()
    try:
        plano = np.frombuffer(ptr, dtype=np.uint8)
    except (TypeError, ValueError):
        plano = np.ctypeslib.as_array(ptr, shape=(imagem.width * imagem.height,))
    return plano.reshape(imagem.height, imagem.width)


def gerar_gradiente(n):
    """Gradiente cíclico (azul -> branco -> laranja -> escuro) como lista de 0xRRGGBB."""
    posicoes = [0.0, 0.16, 0.42, 0.6425, 0.8575, 1.0]
    r = [0, 32, 237, 255, 0, 0]
    g = [7, 107, 255, 170, 2, 7]
    b = [100, 203, 255, 0, 0, 100]
    t = np.arange(n) / n
    rr = np.interp(t, posicoes, r).astype(int)
    gg = np.interp(t, posicoes, g).astype(int)
    bb = np.interp(t, posicoes, b).astype(int)
    return [(int(a) << 16) | (int(c) << 8) | int(d) for a, c, d in zip(rr, gg, bb)]


def instalar_paleta():
    """Mantém as 16 cores originais do Pyxel (texto do HUD) e estende até 256 cores."""
    cores = list(pyxel.colors)[:16] + gerar_gradiente(N_PALETA)
    if hasattr(pyxel.colors, "from_list"):
        pyxel.colors.from_list(cores)
    else:
        for indice, cor in enumerate(cores):
            if indice < len(pyxel.colors):
                pyxel.colors[indice] = cor
            else:
                pyxel.colors.append(cor)


def parametros_da_camera(progresso):
    """Câmera em espiral logarítmica: devolve (centro, passo_por_pixel, zoom).

    sigma(0) = 1 (visão inicial); sigma(1) = 1/KAPPA (cópia do conjunto no minibrot).
    """
    sigma = cmath.exp(-progresso * LOG_KAPPA)
    centro = PONTO_FIXO + (VISAO_CENTRO - PONTO_FIXO) * sigma
    passo = (VISAO_LARGURA / LARGURA) * sigma
    zoom = 1.0 / abs(sigma)
    return centro, passo, zoom


def reiniciar_ciclo(novo_progresso):
    """Guarda o último quadro (para o fade) e restaura a câmera."""
    global progresso, fade, ultimo_desenho
    buf_antigo[:] = buf_atual
    progresso = novo_progresso
    fade = 0.0
    ultimo_desenho = None

img_atual = pyxel.Image(LARGURA, ALTURA)     # quadro calculado agora
img_antigo = pyxel.Image(LARGURA, ALTURA)    # último quadro do ciclo anterior (fade)
buf_atual = visao_numpy(img_atual)
buf_antigo = visao_numpy(img_antigo)

def restaurer_palette_normale():
    pyxel.colors.from_list(palito_normal)

def make_ramp(stops, n=16):
    ramp = []
    for i in range(n):
        t = i / (n - 1) * (len(stops) - 1)
        a = int(t)
        b = min(a + 1, len(stops) - 1)
        w = t - a
        rgb = 0
        for shift in (16, 8, 0):
            ca = (stops[a] >> shift) & 0xFF
            cb = (stops[b] >> shift) & 0xFF
            rgb |= round(ca * (1 - w) + cb * w) << shift
        ramp.append(rgb)
    return ramp
 
 
def apply_palette():
    pyxel.colors.from_list(make_ramp(PALETTES[PALETTE_NAMES[palette_id]], 16))
 
 
def laplacian(X):
    n = np.roll(X, 1, 0)
    s = np.roll(X, -1, 0)
    return (
        -X
        + 0.2 * (n + s + np.roll(X, 1, 1) + np.roll(X, -1, 1))
        + 0.05 * (np.roll(n, 1, 1) + np.roll(n, -1, 1)
                  + np.roll(s, 1, 1) + np.roll(s, -1, 1))
    )
 
 
def step():
    global U, V
    Lu = laplacian(U)
    Lv = laplacian(V)
    reaction = U * V * V
    U += (DU * Lu - reaction + F * (1 - U)) * DT
    V += (DV * Lv + reaction - (F + K) * V) * DT
    np.clip(U, 0, 1, out=U)
    np.clip(V, 0, 1, out=V)
 
 
def circle_mask(cx, cy, r):
    """Matriz booleana: True dentro do círculo de centro (cx, cy) e raio r."""
    yy, xx = np.ogrid[:SIZE, :SIZE]
    return (xx - cx) ** 2 + (yy - cy) ** 2 <= r ** 2
 
 
def butterfly_mask(thickness=1):
    """Curva da borboleta (Temple Fay) rasterizada na grade."""
    t = np.linspace(0, 12 * np.pi, 8000)
    g = np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5
    x = np.sin(t) * g
    y = np.cos(t) * g
 
    # centraliza e escala para ocupar ~85% da tela
    scale = 0.85 * SIZE / max(x.max() - x.min(), y.max() - y.min())
    px = SIZE / 2 + (x - (x.max() + x.min()) / 2) * scale
    py = SIZE / 2 - (y - (y.max() + y.min()) / 2) * scale   # y da tela é invertido
 
    base = np.zeros((SIZE, SIZE), dtype=bool)
    base[np.rint(py).astype(int).clip(0, SIZE - 1),
         np.rint(px).astype(int).clip(0, SIZE - 1)] = True
 
    # engrossa a linha deslocando a cópia em todas as direções (np.roll de novo)
    mask = base.copy()
    for dy in range(-thickness, thickness + 1):
        for dx in range(-thickness, thickness + 1):
            mask |= np.roll(np.roll(base, dy, 0), dx, 1)
    return mask
 
 
def reset_butterfly():
    global U, V
    U = np.ones((SIZE, SIZE))
    V = np.zeros((SIZE, SIZE))
    m = butterfly_mask()
    n = int(m.sum())
    U[m] = 0.50 + 0.02 * np.random.randn(n)
    V[m] = 0.25 + 0.02 * np.random.randn(n)
 
 
def reset_noise():
    global U, V
    U = np.ones((SIZE, SIZE)) + 0.05 * np.random.randn(SIZE, SIZE)
    V = np.zeros((SIZE, SIZE)) + 0.05 * np.random.randn(SIZE, SIZE)
 
 
# ---------------------------------------------------------------- EFEITO CIRCLE LIMIT
# Bloco independente: copie estas duas funções para qualquer projeto Pyxel.
def make_hyperbolic_map(w, h, zoom=1.0, rim=0.985):
    """Para cada pixel de DESTINO, calcula de qual pixel de ORIGEM copiar."""
    y, x = np.mgrid[0:h, 0:w]
    cx, cy = (w - 1) / 2, (h - 1) / 2
    c = min(cx, cy)                            # raio do disco, em pixels
    dx, dy = x - cx, y - cy
    dist = np.hypot(dx, dy)
    r = dist / c                               # 0 no centro, 1 na borda do disco
 
    outside = r >= rim                         # fora do disco: vira preto
    r = np.minimum(r, rim)
 
    # Disco de Poincaré: distância hiperbólica = arctanh(r).
    # Cresce devagar no centro e vai a INFINITO quando r -> 1.
    rho = np.arctanh(r)
    r_src = rho * c / zoom                     # raio (em pixels) na imagem original
 
    s = r_src / np.maximum(dist, 1e-9)
    sx = np.rint(cx + dx * s).astype(int) % w  # "% w": a imagem se repete em ladrilhos
    sy = np.rint(cy + dy * s).astype(int) % h
    return (sy * w + sx).ravel(), outside.ravel()
 
 
# def apply_hyperbolic(hmap):
#     """Distorce o que já foi desenhado na tela. Chame no FIM do draw()."""
#     src_index, outside = hmap
#     buf = np.frombuffer(pyxel.screen.data_ptr(), dtype=np.uint8)
#     if buf.size != src_index.size:
#         raise ValueError("o mapa foi criado para outro tamanho de tela")
#     buf[:] = buf[src_index]
def apply_hyperbolic(hmap):
    """Applique la déformation hyperbolique à l'écran."""

    if hmap is None:
        return

    src_index, outside = hmap

    buf = np.frombuffer(
        pyxel.screen.data_ptr(),
        dtype=np.uint8
    )

    if buf.size != src_index.size:
        raise ValueError(
            f"Carte hyperbolique incompatible : "
            f"écran={buf.size}, carte={src_index.size}"
        )

    # On sauvegarde l'image avant de la transformer.
    original = buf.copy()

    # Application de la transformation.
    buf[:] = original[src_index]

    # Tout ce qui est hors du disque devient noir.
    buf[outside] = 0
def simulation_to_screen():
    """
    Convertit la simulation 128x128 vers l'écran Pyxel 160x120.
    """

    # Valeurs de V -> palette Pyxel 0..15
    idx = np.clip(
        V / VMAX * 15,
        0,
        15
    ).astype(np.uint8)

    # Coordonnées source pour chaque pixel écran.
    xs = np.linspace(
        0,
        SIZE - 1,
        pyxel.width
    ).astype(np.int32)

    ys = np.linspace(
        0,
        SIZE - 1,
        pyxel.height
    ).astype(np.int32)

    # Redimensionnement simple par plus proche voisin.
    image = idx[np.ix_(ys, xs)]

    return image


def jut(x, y, paii, deformation, couleur):

    demi = paii // 2

    haut_x = int(x + demi)
    haut_y = int(y + deformation)

    droite_x = int(x + paii)
    droite_y = int(y + demi)

    bas_x = int(x + demi)
    bas_y = int(y + paii - deformation)

    gauche_x = int(x)
    gauche_y = int(y + demi)

    pyxel.line(
        haut_x, haut_y,
        droite_x, droite_y,
        couleur
    )

    pyxel.line(
        droite_x, droite_y,
        bas_x, bas_y,
        couleur
    )

    pyxel.line(
        bas_x, bas_y,
        gauche_x, gauche_y,
        couleur
    )

    pyxel.line(
        gauche_x, gauche_y,
        haut_x, haut_y,
        couleur
    )

def truc(a, b, p):
    return a + (b - a) * p


def muche(x, y, rayon, angle):
    return (
        x + math.cos(angle) * rayon,
        y + math.sin(angle) * rayon
    )


# -----------------------------------------
# FORMES
# -----------------------------------------

def car(x, y, taille, couleur, rotation):
    # On dessine un carré comme 4 trias.
    demi = taille

    p1 = muche(x, y, demi, rotation + math.pi / 4)
    p2 = muche(x, y, demi, rotation + 3 * math.pi / 4)
    p3 = muche(x, y, demi, rotation + 5 * math.pi / 4)
    p4 = muche(x, y, demi, rotation + 7 * math.pi / 4)

    pyxel.tri(
        int(x), int(y),
        int(p1[0]), int(p1[1]),
        int(p2[0]), int(p2[1]),
        couleur
    )

    pyxel.tri(
        int(x), int(y),
        int(p2[0]), int(p2[1]),
        int(p3[0]), int(p3[1]),
        couleur
    )

    pyxel.tri(
        int(x), int(y),
        int(p3[0]), int(p3[1]),
        int(p4[0]), int(p4[1]),
        couleur
    )

    pyxel.tri(
        int(x), int(y),
        int(p4[0]), int(p4[1]),
        int(p1[0]), int(p1[1]),
        couleur
    )


def tria(x, y, taille, couleur, rotation):
    p1 = muche(x, y, taille, rotation)
    p2 = muche(x, y, taille, rotation + 2 * math.pi / 3)
    p3 = muche(x, y, taille, rotation + 4 * math.pi / 3)

    pyxel.tri(
        int(p1[0]), int(p1[1]),
        int(p2[0]), int(p2[1]),
        int(p3[0]), int(p3[1]),
        couleur
    )

def wumbo(a, b):
    return (
        a[0] - b[0],
        a[1] - b[1]
    )


def flarp(a, b):
    return (
        a[0] + b[0],
        a[1] + b[1]
    )


def glorp(a, n):
    return (
        a[0] * n,
        a[1] * n
    )


def sploink(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]

    return math.sqrt(
        dx * dx +
        dy * dy
    )


def wobble(a, b, t):
    return flarp(
        a,
        glorp(
            wumbo(b, a),
            t
        )
    )


# ============================================================
# ROTATION
# ============================================================

def banana(p, theta):

    c = math.cos(theta)
    s = math.sin(theta)

    return (
        p[0] * c - p[1] * s,
        p[0] * s + p[1] * c
    )


# ============================================================
# SUBDIVISION
# ============================================================

def patate(trucs):

    machin = []

    for sorte, a, b, c in trucs:

        if sorte == 0:

            p = wobble(
                a,
                b,
                nix
            )

            machin.append(
                (
                    1,
                    p,
                    c,
                    a
                )
            )

            machin.append(
                (
                    0,
                    c,
                    p,
                    b
                )
            )

        else:

            q = wobble(
                b,
                a,
                nix
            )

            r = wobble(
                b,
                c,
                nix
            )

            machin.append(
                (
                    1,
                    r,
                    c,
                    a
                )
            )

            machin.append(
                (
                    1,
                    q,
                    r,
                    b
                )
            )

            machin.append(
                (
                    0,
                    r,
                    q,
                    a
                )
            )

    return machin


# ============================================================
# GERME
# ============================================================

def cornichon():

    trucs = []

    rayon = 300.0

    for i in range(10):

        alpha = (
            2 * math.pi * i / 10
            - math.pi / 10
        )

        beta = (
            2 * math.pi * i / 10
            + math.pi / 10
        )

        a = (0.0, 0.0)

        b = (
            rayon * math.cos(alpha),
            rayon * math.sin(alpha)
        )

        c = (
            rayon * math.cos(beta),
            rayon * math.sin(beta)
        )

        if i % 2 == 0:
            b, c = c, b

        trucs.append(
            (
                0,
                a,
                b,
                c
            )
        )

    return trucs


# ============================================================
# IDENTIFICATION DES POINTS
# ============================================================

def bidule(p):

    return (
        round(p[0], 6),
        round(p[1], 6)
    )


def machin_bizarre(a, b):

    a = bidule(a)
    b = bidule(b)

    if a < b:
        return (a, b)

    return (b, a)


# ============================================================
# CONSTRUCTION DES LOSANGES
# ============================================================

def schmilblick(trucs):

    bazar = {}

    for i, (sorte, a, b, c) in enumerate(trucs):

        machin = [a, b, c]

        for j in range(3):

            p = machin[j]
            q = machin[(j + 1) % 3]

            cle = machin_bizarre(
                p,
                q
            )

            if cle not in bazar:
                bazar[cle] = []

            bazar[cle].append(i)

    tuiles = []
    poubelle = set()

    for indices in bazar.values():

        if len(indices) != 2:
            continue

        i1, i2 = indices

        if i1 in poubelle or i2 in poubelle:
            continue

        _, a1, b1, c1 = trucs[i1]
        _, a2, b2, c2 = trucs[i2]

        sac = [a1, b1, c1]
        sac2 = [a2, b2, c2]

        commun = []

        for p in sac:
            for q in sac2:

                if bidule(p) == bidule(q):
                    commun.append(p)

        if len(commun) != 2:
            continue

        reste1 = None
        reste2 = None

        for p in sac:

            if (
                bidule(p) != bidule(commun[0])
                and
                bidule(p) != bidule(commun[1])
            ):
                reste1 = p

        for p in sac2:

            if (
                bidule(p) != bidule(commun[0])
                and
                bidule(p) != bidule(commun[1])
            ):
                reste2 = p

        if reste1 is None or reste2 is None:
            continue

        points = [
            commun[0],
            commun[1],
            reste1,
            reste2
        ]

        centre = (
            sum(p[0] for p in points) / 4,
            sum(p[1] for p in points) / 4
        )

        points.sort(
            key=lambda p:
            math.atan2(
                p[1] - centre[1],
                p[0] - centre[0]
            )
        )

        d1 = sploink(
            points[0],
            points[2]
        )

        d2 = sploink(
            points[1],
            points[3]
        )

        cote = (
            sploink(points[0], points[1])
            +
            sploink(points[1], points[2])
            +
            sploink(points[2], points[3])
            +
            sploink(points[3], points[0])
        ) / 4

        grosse = max(d1, d2)

        if grosse / cote > 1.5:
            sorte = 1
        else:
            sorte = 0

        tuiles.append(
            (
                points,
                sorte,
                centre
            )
        )

        poubelle.add(i1)
        poubelle.add(i2)

    return tuiles


# ============================================================
# CONSTRUCTION
# ============================================================

trucs = cornichon()

for _ in range(mira):
    trucs = patate(trucs)

tuiles = schmilblick(trucs)


# ============================================================
# TRANSFORMATION
# ============================================================

def teleportation(p, theta, zoom):

    p = banana(
        p,
        theta
    )

    return (
        int(zorb / 2 + p[0] * zoom),
        int(plok / 2 + p[1] * zoom)
    )


# ============================================================
# PALETTE
# ============================================================

arc_en_ciel = [
    1,
    5,
    6,
    13,
    9,
    10,
    2
]


# ============================================================
# DÉGRADÉ
# ============================================================

def truc_chose(x, y, phase, sorte):

    rayon = math.sqrt(
        x * x +
        y * y
    )

    angle = math.atan2(
        y,
        x
    )

    vague = (
        rayon * 0.045
        - phase
        + angle * 1.5
    )

    patate_chaude = (
        math.sin(vague)
        + 1
    ) * 0.5

    if sorte == 1:
        patate_chaude += 0.18

    numero = int(
        patate_chaude
        * len(arc_en_ciel)
    )

    numero %= len(arc_en_ciel)

    return arc_en_ciel[numero]

SINAL_A = +1
SINAL_B = -1
 
 
def tabela(familia, sinal):
    """Uma entrada por reta: (x1, y1, dx/dy, delta).
    x do cruzamento com a linha y = x1 + (y - y1) * dx/dy.
    delta = +1 se, andando para a direita, o contador da reta sobe; -1 se desce."""
    linhas = []
    for p in familia:
        x1, y1, x2, y2 = p[0][0], p[1][0], p[0][1], p[1][1]
        dx, dy = x2 - x1, y2 - y1
        if dy == 0:
            dy = 1e-9      # reta exatamente horizontal: cruza "no infinito"
        linhas.append((x1, y1, dx / dy, 1 if -sinal * dy > 0 else -1))
    return linhas
 
 
# --- movimento das pontas pela borda --------------------------------------
# O update() original empurra x e y com if's em sequência; nos cantos a ponta
# "corta caminho" (anda 2 pyxel num frame) e as retas dos extremos (x = -1 e
# x = 255) andam numa borda 1-2 pyxel fora da tela. Esse erro se acumula: depois de
# ~4000 frames retas vizinhas passam a se cruzar dentro da tela. Aqui cada ponta
# guarda só a sua posição s ao longo do perímetro (0 .. 4*largura) e a
# posição (x, y) é calculada a partir dela, sem acumular nada.
P = 4 * pyxel.width
 
 
def para_s(x, y):
    """Posição inicial (x, y) na borda -> distância s ao longo do perímetro,
    contada a partir do canto superior esquerdo, no sentido horário."""
    if y <= 0:
        return x                      # borda de cima
    if x >= pyxel.width:
        return pyxel.width + y           # borda da direita
    if y >= pyxel.width:
        return 3 * pyxel.width - x       # borda de baixo
    return P - y                      # borda da esquerda
 
 
def borda(s):
    """Distância s no perímetro -> ponto (x, y) na borda."""
    s %= P
    if s < pyxel.width:
        return s, 0
    if s < 2 * pyxel.width:
        return pyxel.width, s - pyxel.width
    if s < 3 * pyxel.width:
        return 3 * pyxel.width - s, pyxel.width
    return 0, P - s
 
 
S0_A = [[para_s(p[0][i], p[1][i]) for i in range(2)] for p in points_horizontal]
S0_B = [[para_s(p[0][i], p[1][i]) for i in range(2)] for p in points_vertical]
frame = 0
 
 
def avanca_circulos():
    """Cresce todos os círculos 1 pyxel.
 
    Quando um círculo passa a cobrir a tela inteira, ele volta ao centro, mas a
    sua paleta NÃO some: ela vira a cor do fundo (a região fora de todos os
    círculos). Antes do salto, os pixels de fora estavam "dentro" desse círculo;
    depois, estão no "fundo" com a mesma paleta, então nenhum pixel muda de cor.
    O círculo renasce no centro com uma geração nova (paleta nova)."""
    global rayon_cercle, RAIO_MAX, ultima
    for i in range(5):
        rayon_cercle[i] += 1
        if rayon_cercle[i] >= RAIO_MAX:
            rayon_cercle[i] -= int(RAIO_MAX)
            fundo = geracao[i]
            ultima += 1
            geracao[i] = ultima

def losa(x, y, taille, couleur, rotation):
    p1 = muche(x, y, taille, rotation)
    p2 = muche(x, y, taille, rotation + math.pi / 2)
    p3 = muche(x, y, taille, rotation + math.pi)
    p4 = muche(x, y, taille, rotation + 3 * math.pi / 2)

    # On utilise deux trias pour remplir le losa.
    pyxel.tri(
        int(p1[0]), int(p1[1]),
        int(p2[0]), int(p2[1]),
        int(p3[0]), int(p3[1]),
        couleur
    )

    pyxel.tri(
        int(p1[0]), int(p1[1]),
        int(p3[0]), int(p3[1]),
        int(p4[0]), int(p4[1]),
        couleur
    )


def haxego(x, y, taille, couleur, rotation):
    # Un haxego est construit avec 6 trias.
    for i in range(6):
        a1 = rotation + i * math.pi / 3
        a2 = rotation + (i + 1) * math.pi / 3

        p1 = muche(x, y, taille, a1)
        p2 = muche(x, y, taille, a2)

        pyxel.tri(
            int(x), int(y),
            int(p1[0]), int(p1[1]),
            int(p2[0]), int(p2[1]),
            couleur
        )


def crecle(x, y, taille, couleur):
    pyxel.circ(
        int(x),
        int(y),
        int(taille),
        couleur
    )


# -----------------------------------------
# DESSIN D'UNE FORME
# -----------------------------------------

def dess_for(x, y, taille, forme, couleur, rotation):

    if forme == 0:
        car(x, y, taille, couleur, rotation)

    elif forme == 1:
        tria(x, y, taille, couleur, rotation)

    elif forme == 2:
        losa(x, y, taille, couleur, rotation)

    elif forme == 3:
        haxego(x, y, taille, couleur, rotation)

    elif forme == 4:
        crecle(x, y, taille, couleur)


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

def frac(x, y, rat, xOff, yOff, iter):

    # ---------------------------------------------
    # Conversion pixel -> plan complexe
    # ---------------------------------------------

    a = (
        x * rat
        + xOff
    )

    b = (
        y * rat
        + yOff
    )

    ca = a
    cb = b

    n = 0


    # ---------------------------------------------
    # Mandelbrot
    # ---------------------------------------------

    while (
        a * a + b * b < 4
        and n < iter
    ):

        ai = (
            a * a
            - b * b
        )

        bi = (
            2 * a * b
        )

        a = ai + ca
        b = bi + cb

        n += 1


    # ---------------------------------------------
    # Normalisation
    # ---------------------------------------------

    m = n / iter


    # ---------------------------------------------
    # Couleurs
    # ---------------------------------------------

    lin = int(
        255 * m
    ) % 255

    sin = int(
        255
        * (
            -math.cos(math.pi * m)
            + 1
        )
        / 2
    ) % 255

    sqrt = int(
        255 * math.sqrt(m)
    ) % 255

    sqr = int(
        255 * m * m
    ) % 255


    r = sqr
    g = lin
    b = sin


    # ---------------------------------------------
    # RGB -> palette Pyxel
    # ---------------------------------------------

    luminosite = (
        r + g + b
    ) / 3

    couleur = int(
        luminosite
        / 256
        * 16
    )


    if couleur < 0:
        couleur = 0

    if couleur > 15:
        couleur = 15


    return couleur


# =====================================================
# == CALCUL DE L'IMAGE
# =====================================================

def process():

    global pixels

    pixels = []


    for y in range(pyxel.height):

        ligne = []


        for x in range(pyxel.width):

            couleur = frac(
                x,
                y,
                ratio,
                xOffset,
                yOffset,
                iterations
            )

            ligne.append(couleur)


        pixels.append(ligne)


# =====================================================
# == ZOOM AUTOMATIQUE
# =====================================================

def automatic_zoom():

    global ratio
    global xOffset
    global yOffset
    global zoom_step
    global direction


    # ---------------------------------------------
    # Avancer dans l'animation
    # ---------------------------------------------

    zoom_step += direction


    # ---------------------------------------------
    # Arrivé au zoom maximum
    # ---------------------------------------------

    if zoom_step >= zoom_max:

        zoom_step = zoom_max

        # On commence le dézoom
        direction = -1


    # ---------------------------------------------
    # Retour à l'image initiale
    # ---------------------------------------------
# 
    if zoom_step <= 0:
 
         zoom_step = 0

        # On recommence le zoom
         direction = 1


    # ---------------------------------------------
    # Calcul de la nouvelle échelle
    # ---------------------------------------------

    nouveau_ratio = (
        (1 / zoom)
        / pyxel.width
    )


    # ---------------------------------------------
    # Appliquer le zoom autant de fois que
    # nécessaire selon zoom_step
    # ---------------------------------------------

    nouveau_ratio *= (
        zoom_factor ** zoom_step
    )


    # ---------------------------------------------
    # Sécurité
    # ---------------------------------------------

    if nouveau_ratio < 1e-300:

        nouveau_ratio = 1e-300


    ratio = nouveau_ratio


    # ---------------------------------------------
    # Centre de l'écran
    # ---------------------------------------------

    centre_x = (
        pyxel.width / 2
    )

    centre_y = (
        pyxel.height / 2
    )


    # ---------------------------------------------
    # Garder le point intéressant au centre
    # ---------------------------------------------

    xOffset = (
        target_x
        - centre_x * ratio
    )

    yOffset = (
        target_y
        - centre_y * ratio
    )

def draw_hexagon(x, y, r, color):

    points = []

    for i in range(6):

        angle = math.pi / 3 * i

        px = int(x + math.cos(angle) * r)
        py = int(y + math.sin(angle) * r)

        points.append((px, py))

    # Triangle fan
    for i in range(1, 5):

        pyxel.tri(
            int(x), int(y),
            points[i][0], points[i][1],
            points[i + 1][0], points[i + 1][1],
            color
        )

    # Dernier triangle
    pyxel.tri(
        int(x), int(y),
        points[5][0], points[5][1],
        points[0][0], points[0][1],
        color
    )

    # Contour
    for i in range(6):

        a = points[i]
        b = points[(i + 1) % 6]

        pyxel.line(
            a[0], a[1],
            b[0], b[1],
            7
        )
def lerp(a, b, t):
    return (
        a[0] + (b[0] - a[0]) * t,
        a[1] + (b[1] - a[1]) * t
    )


def rotat(p, a):
    c = math.cos(a)
    s = math.sin(a)

    return (
        p[0] * c - p[1] * s,
        p[0] * s + p[1] * c
    )


def subdivide(triangles):
    result = []

    for typ, A, B, C in triangles:

        if typ == 0:
            P = lerp(A, B, 1 / PHI)

            result.append((0, C, P, B))
            result.append((1, P, C, A))

        else:
            P = lerp(A, B, 1 / PHI)
            Q = lerp(A, C, 1 / PHI)

            result.append((1, Q, P, A))
            result.append((0, Q, C, P))
            result.append((0, P, B, Q))

    return result


def create_penrose():
    triangles = []

    radius = 85

    for i in range(10):

        a1 = i * math.pi / 5
        a2 = (i + 1) * math.pi / 5

        B = (
            math.cos(a1) * radius,
            math.sin(a1) * radius
        )

        C = (
            math.cos(a2) * radius,
            math.sin(a2) * radius
        )

        triangles.append(
            (0, (0, 0), B, C)
        )

    for i in range(6):
        triangles = subdivide(triangles)

    return triangles


triangles = create_penrose()

# def tourner1(x, y):
#     global ab
#     cos_a = math.cos(ab)
#     sin_a = math.sin(ab)
# 
#     x2 = (
#         centre_x
#         + (x - centre_x) * cos_a
#         - (y - centre_y) * sin_a
#     )
# 
#     y2 = (
#         centre_y
#         + (x - centre_x) * sin_a
#         + (y - centre_y) * cos_a
#     )
# 
#     return x2, y2
def tourner1(x, y):
    global ab

    c = math.cos(ab)
    s = math.sin(ab)

    # Rotation autour du centre de l'écran
    dx = x - centre_x
    dy = y - centre_y

    x2 = centre_x + dx * c - dy * s
    y2 = centre_y + dx * s + dy * c

    return x2, y2


# -----------------------------
# POINT DU RESEAU TRIANGULAIRE
# -----------------------------

def point(i, j):
    x = centre_x + cote * (i + j / 2)
    y = centre_y + cote * math.sqrt(3) / 2 * j

    return x, y


# -----------------------------
# POINT SUPPRIME ?
# -----------------------------

def point_supprime(i, j):
    # Le réseau supprimé forme une sous-maille
    # d'indice 7.
    #
    # Les points supprimés sont espacés de sqrt(7)
    # côtés du réseau triangulaire.

    return (
        (3 * i + j) % 7 == 0
        and
        (-i + 2 * j) % 7 == 0
    )


# -----------------------------
# DESSIN D'UN POLYGONE
# -----------------------------

def dessiner_polygone_main5(points, couleur):
    points_rot = []

    for x, y in points:
        points_rot.append(tourner_main5(x, y))

    for i in range(1, len(points_rot) - 1):
        x1, y1 = points_rot[0]
        x2, y2 = points_rot[i]
        x3, y3 = points_rot[i + 1]

        pyxel.tri(
            x1, y1,
            x2, y2,
            x3, y3,
            couleur
        )

    for i in range(len(points_rot)):
        x1, y1 = points_rot[i]
        x2, y2 = points_rot[(i + 1) % len(points_rot)]

        pyxel.line(
            x1, y1,
            x2, y2,
            1
        )


# -----------------------------
# HEXAGONE
# -----------------------------

def dessiner_hexagone1(i, j):
    global col1
    x, y = point(i, j)

    points = []

    # Les six voisins du sommet supprimé
    voisins = [
        (i + 1, j),
        (i + 1, j - 1),
        (i, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1)
    ]

    for a, b in voisins:
        px, py = point(a, b)
        points.append((px, py))
    
    dessiner_polygone_main5(points, col1)

def tourner_main5(x, y):
    global ab

    c = math.cos(ab)
    s = math.sin(ab)

    dx = x - centre_x
    dy = y - centre_y

    return (
        centre_x + dx * c - dy * s,
        centre_y + dx * s + dy * c
    )

# -----------------------------
# TRIa
# -----------------------------

def dessiner_tria(i1, j1, i2, j2, i3, j3):
    global col2
    x1, y1 = point(i1, j1)
    x2, y2 = point(i2, j2)
    x3, y3 = point(i3, j3)

    points = [
        (x1, y1),
        (x2, y2),
        (x3, y3)
    ]

    dessiner_polygone_main5(points, col2)

def change_col():
    global col1, col2
    if pyxel.frame_count%5==0:
        col1=randint(1, 7)
    if pyxel.frame_count%10==0:
        col2=randint(8, 15)

def tourner(x, y):

    c = math.cos(angl)
    s = math.sin(angl)

    x2 = (
        centre_x
        + (x - centre_x) * c
        - (y - centre_y) * s
    )

    y2 = (
        centre_y
        + (x - centre_x) * s
        + (y - centre_y) * c
    )

    return x2, y2


# -----------------------------
# POINT SUR UN SEGMENT
# -----------------------------

def interpolation(a, b, proportion):

    x = a[0] + (b[0] - a[0]) * proportion
    y = a[1] + (b[1] - a[1]) * proportion

    return (x, y)


# -----------------------------
# DESSIN D'UN TRIangl
# -----------------------------

def triangl(a, b, c, couleur):

    p1 = tourner(a[0], a[1])
    p2 = tourner(b[0], b[1])
    p3 = tourner(c[0], c[1])

    pyxel.tri(
        p1[0], p1[1],
        p2[0], p2[1],
        p3[0], p3[1],
        couleur
    )

    pyxel.line(
        p1[0], p1[1],
        p2[0], p2[1],
        1
    )

    pyxel.line(
        p2[0], p2[1],
        p3[0], p3[1],
        1
    )

    pyxel.line(
        p3[0], p3[1],
        p1[0], p1[1],
        1
    )


# -----------------------------
# SUBDIVISION PENROSE
# -----------------------------

def subdiviser(triangls):

    nouveaux = []

    for triangl_data in triangls:

        a = triangl_data[0]
        b = triangl_data[1]
        c = triangl_data[2]
        type_triangl = triangl_data[3]

        if type_triangl == 0:

            # Triangl aigu

            p = interpolation(a, b, 1 / PHI)
            q = interpolation(a, c, 1 / PHI)

            nouveaux.append(
                (c, q, p, 0)
            )

            nouveaux.append(
                (q, b, p, 1)
            )

            nouveaux.append(
                (b, c, q, 0)
            )

        else:

            # Triangl obtus

            p = interpolation(b, a, 1 / PHI)
            q = interpolation(b, c, 1 / PHI)

            nouveaux.append(
                (p, q, b, 1)
            )

            nouveaux.append(
                (a, p, q, 0)
            )

            nouveaux.append(
                (c, q, p, 0)
            )

            nouveaux.append(
                (a, c, q, 0
            ))

    return nouveaux


# -----------------------------
# CREATION DU PAVAGE
# -----------------------------

def creer_penrose():

    triangls = []

    # On commence avec 10 triangls
    # autour du centre.
    #
    # Cela donne la symétrie d'ordre 10
    # caractéristique de Penrose.

    for i in range(10):

        a1 = 2 * math.pi * i / 10
        a2 = 2 * math.pi * (i + 1) / 10

        centre = (
            centre_x,
            centre_y
        )

        p1 = (
            centre_x + math.cos(a1) * taille,
            centre_y + math.sin(a1) * taille
        )

        p2 = (
            centre_x + math.cos(a2) * taille,
            centre_y + math.sin(a2) * taille
        )

        triangls.append(
            (
                centre,
                p1,
                p2,
                0
            )
        )

    # Subdivisions successives
    for i in range(profondeur):

        triangls = subdiviser(triangls)

    return triangls


# -----------------------------
# CREATION INITIALE
# -----------------------------

triangls = creer_penrose()

def rotate(x, y, angle, scale):

    x *= scale
    y *= scale

    c = math.cos(angle)
    s = math.sin(angle)

    return (
        x * c - y * s,
        x * s + y * c
    )


# ------------------------------------------------
# Dessin d'un papillon
# ------------------------------------------------

def draw_butterfly(cx, cy, angle, scale):

    def point(x, y):

        rx, ry = rotate(
            x,
            y,
            angle,
            scale
        )

        return (
            int(cx + rx),
            int(cy + ry)
        )


    # --------------------------------------------
    # Ailes
    # --------------------------------------------

    wing_left = [
        (-3, -2),
        (-18, -18),
        (-38, -27),
        (-45, -15),
        (-40, 2),
        (-25, 10),
        (-8, 7)
    ]

    wing_right = [
        (3, -2),
        (18, -18),
        (38, -27),
        (45, -15),
        (40, 2),
        (25, 10),
        (8, 7)
    ]


    # Aile gauche
    p = [point(x, y) for x, y in wing_left]

    for i in range(1, len(p) - 1):

        pyxel.tri(
            p[0][0], p[0][1],
            p[i][0], p[i][1],
            p[i + 1][0], p[i + 1][1],
            14
        )


    # Aile droite
    p = [point(x, y) for x, y in wing_right]

    for i in range(1, len(p) - 1):

        pyxel.tri(
            p[0][0], p[0][1],
            p[i][0], p[i][1],
            p[i + 1][0], p[i + 1][1],
            10
        )


    # --------------------------------------------
    # Motifs
    # --------------------------------------------

    motifs = [
        (-27, -15, 8),
        (-35, -5, 9),
        (-20, 1, 12),

        (27, -15, 13),
        (35, -5, 11),
        (20, 1, 12)
    ]

    for x, y, color in motifs:

        px, py = point(x, y)

        pyxel.circ(
            px,
            py,
            max(1, int(4 * scale)),
            color
        )


    # --------------------------------------------
    # Corps
    # --------------------------------------------

    body = [
        (0, -15),
        (3, -8),
        (3, 8),
        (0, 16),
        (-3, 8),
        (-3, -8)
    ]

    p = [point(x, y) for x, y in body]

    for i in range(1, len(p) - 1):

        pyxel.tri(
            p[0][0], p[0][1],
            p[i][0], p[i][1],
            p[i + 1][0], p[i + 1][1],
            7
        )


    # --------------------------------------------
    # Tête
    # --------------------------------------------

    hx, hy = point(0, -18)

    pyxel.circ(
        hx,
        hy,
        max(2, int(4 * scale)),
        8
    )


    # --------------------------------------------
    # Antennes
    # --------------------------------------------

    a1 = point(-2, -20)
    a2 = point(-9, -27)

    b1 = point(2, -20)
    b2 = point(9, -27)

    pyxel.line(
        a1[0], a1[1],
        a2[0], a2[1],
        12
    )

    pyxel.line(
        b1[0], b1[1],
        b2[0], b2[1],
        12
    )


# ------------------------------------------------
# Lignes géométriques
# ------------------------------------------------

def draw_geometry():

    # On relie les centres selon la grille.
    #
    # Cela crée des triangles et des losanges
    # très réguliers entre les papillons.

    lines = [
        # horizontales
        (0, 1), (1, 2), (2, 3), (3, 4),
        (5, 6), (6, 7), (7, 8),
        (9, 10), (10, 11), (11, 12), (12, 13),
        (14, 15), (15, 16), (16, 17),

        # diagonales
        (0, 5), (1, 5), (1, 6),
        (2, 6), (2, 7),
        (3, 7), (3, 8),
        (4, 8),

        (5, 9), (5, 10),
        (6, 10), (6, 11),
        (7, 11), (7, 12),
        (8, 12), (8, 13),

        (9, 14), (10, 14),
        (10, 15), (11, 15),
        (11, 16), (12, 16),
        (12, 17), (13, 17)
    ]


    for n, (a, b) in enumerate(lines):

        x1 = int(butterflies[a][0])
        y1 = int(butterflies[a][1])

        x2 = int(butterflies[b][0])
        y2 = int(butterflies[b][1])

        # Plusieurs couleurs géométriques
        colors = [1, 5, 6, 12]

        color = colors[n % len(colors)]

        pyxel.line(
            x1, y1,
            x2, y2,
            color
        )
def tourner_point(x, y):
    centre_x = pyxel.width / 2
    centre_y = pyxel.height / 2

    cos_a = math.cos(ang)
    sin_a = math.sin(ang)

    nouveau_x = (
        centre_x
        + (x - centre_x) * cos_a
        - (y - centre_y) * sin_a
    )

    nouveau_y = (
        centre_y
        + (x - centre_x) * sin_a
        + (y - centre_y) * cos_a
    )

    return nouveau_x, nouveau_y


# -----------------------------
# DESSIN D'UN POLYGONE
# -----------------------------

def dessiner_polygone(points, couleur):
    points_rot = []

    for x, y in points:
        points_rot.append(tourner_point(x, y))

    # On remplit le polygone avec des triangs
    # depuis le premier sommet
    for i in range(1, len(points_rot) - 1):

        x1, y1 = points_rot[0]
        x2, y2 = points_rot[i]
        x3, y3 = points_rot[i + 1]

        pyxel.tri(
            x1, y1,
            x2, y2,
            x3, y3,
            couleur
        )

    # Contour du polygone
    for i in range(len(points_rot)):

        x1, y1 = points_rot[i]
        x2, y2 = points_rot[(i + 1) % len(points_rot)]

        pyxel.line(
            x1, y1,
            x2, y2,
            1
        )


# -----------------------------
# HEXAGONE
# -----------------------------

def dessiner_hexagone2(x, y):

    points = []

    # Hexagone régulier
    for i in range(6):

        a = math.radians(30 + i * 60)

        px = x + math.cos(a) * cot
        py = y + math.sin(a) * cot

        points.append((px, py))

    dessiner_polygone(points, 8)


# -----------------------------
# CARRE
# -----------------------------

def dessiner_carre(x1, y1, x2, y2):

    # Vecteur du côté entre les deux centres
    dx = x2 - x1
    dy = y2 - y1

    longueur = math.sqrt(dx * dx + dy * dy)

    ux = dx / longueur
    uy = dy / longueur

    # Vecteur perpendiculaire
    px = -uy
    py = ux

    # Centre du carré
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    # Demi-côté
    demi = cot / 2

    # Les quatre coins
    points = [
        (
            cx - ux * demi - px * demi,
            cy - uy * demi - py * demi
        ),

        (
            cx + ux * demi - px * demi,
            cy + uy * demi - py * demi
        ),

        (
            cx + ux * demi + px * demi,
            cy + uy * demi + py * demi
        ),

        (
            cx - ux * demi + px * demi,
            cy - uy * demi + py * demi
        )
    ]

    dessiner_polygone(points, 12)


# -----------------------------
# TRIang
# -----------------------------

def dessiner_triang(x, y, vers_le_haut):

    hauteur = cot * math.sqrt(3) / 2

    if vers_le_haut:

        points = [
            (x - cot / 2, y - hauteur / 3),
            (x + cot / 2, y - hauteur / 3),
            (x, y + 2 * hauteur / 3)
        ]

    else:

        points = [
            (x - cot / 2, y + hauteur / 3),
            (x + cot / 2, y + hauteur / 3),
            (x, y - 2 * hauteur / 3)
        ]

    dessiner_polygone(points, 11)


# -----------------------------
# CENTRE D'UN HEXAGONE
# -----------------------------

def centre_hexagone(colonne, ligne):

    x = (
        pyxel.width / 2
        + colonne * distanc
        + ligne * distanc / 2
    )

    y = (
        pyxel.height / 2
        + ligne * distanc * math.sqrt(3) / 2
    )

    return x, y
def hex_vertices(cx, cy):

    result = []

    for i in range(6):

        a = i * math.pi / 3

        result.append((
            cx + math.cos(a) * SIDE,
            cy + math.sin(a) * SIDE
        ))

    return result


for hx, hy in hexagons:

    points = hex_vertices(hx, hy)

    for p in points:

        key = (
            round(p[0], 5),
            round(p[1], 5)
        )

        vertices[key] = p


# =========================================================
# DODÉCAGONES
#
# Chaque hexagone est tronqué à 1/3 de ses arêtes.
#
# Les 6 coins deviennent donc 12 sommets.
# =========================================================

dodecagons = []

for hx, hy in hexagons:

    v = hex_vertices(hx, hy)

    polygon = []

    for i in range(6):

        a = v[i]
        b = v[(i + 1) % 6]

        # 1/3 depuis A
        p1 = (
            a[0] * 2 / 3 + b[0] / 3,
            a[1] * 2 / 3 + b[1] / 3
        )

        # 1/3 depuis B
        p2 = (
            a[0] / 3 + b[0] * 2 / 3,
            a[1] / 3 + b[1] * 2 / 3
        )

        polygon.append(p1)
        polygon.append(p2)

    dodecagons.append(polygon)


# =========================================================
# TRIanS
#
# Autour de chaque ancien sommet hexagonal, les trois
# points de coupe forment exactement un trian.
# =========================================================

trians = []

for key, vertex in vertices.items():

    vx, vy = vertex

    points = []

    # Recherche des trois points situés à 1/3 de distance
    # du sommet vers les centres des hexagones voisins.
    #
    # Les six directions possibles sont examinées.

    for hx, hy in hexagons:

        dx = hx - vx
        dy = hy - vy

        dist = math.sqrt(dx * dx + dy * dy)

        if dist > 0 and dist < SIDE * 1.01:

            px = vx + dx * (1 / 3)
            py = vy + dy * (1 / 3)

            points.append((px, py))


    # Dans certains cas les coordonnées sont légèrement
    # différentes à cause des flottants.
    #
    # On garde uniquement les trois points du trian.

    if len(points) >= 3:

        # Tri des points autour du sommet

        points.sort(
            key=lambda p: math.atan2(
                p[1] - vy,
                p[0] - vx
            )
        )

        # Les trois premiers correspondent aux trois
        # hexagones qui se rencontrent au sommet.

        trian = [
            points[0],
            points[1],
            points[2]
        ]

        trians.append(trian)


# =========================================================
# DESSIN POLYGONE
# =========================================================

def draw_polygon(points, color):

    if len(points) < 3:
        return

    # Centre du polygone

    cx = 0
    cy = 0

    for x, y in points:

        cx += x
        cy += y

    cx /= len(points)
    cy /= len(points)

    # Trian fan

    for i in range(len(points)):

        a = points[i]
        b = points[(i + 1) % len(points)]

        pyxel.tri(
            int(cx),
            int(cy),
            int(a[0]),
            int(a[1]),
            int(b[0]),
            int(b[1]),
            color
        )


# =========================================================
# AUTO-RÉFÉRENCE
#
# On ajoute de petits motifs à l'intérieur des grands
# dodécagones.
#
# Ils suivent exactement le même mouvement.
# =========================================================

def draw_inner_pattern(points, color1, color2):

    if len(points) != 12:
        return

    cx = 0
    cy = 0

    for x, y in points:

        cx += x
        cy += y

    cx /= 12
    cy /= 12

    # Petit hexagone intérieur

    r = 2.1

    inner = []

    for i in range(6):

        a = i * math.pi / 3

        inner.append((
            cx + math.cos(a) * r,
            cy + math.sin(a) * r
        ))

    draw_polygon(
        inner,
        color1
    )

    # Petit trian intérieur

    r2 = 0.9

    trian = []

    for i in range(3):

        a = -math.pi / 2 + i * math.pi * 2 / 3

        trian.append((
            cx + math.cos(a) * r2,
            cy + math.sin(a) * r2
        ))

    draw_polygon(
        trian,
        color2
    )

#===============================================================================
#========================UPDATE================================================
#==============================================================================
def update():
    global MAIN
    if pyxel.frame_count%900==0:
        if MAIN>=15:
            MAIN=1
        else:
            MAIN+=1
    if pyxel.btnp(pyxel.KEY_RIGHT):
        if MAIN>=15:
            MAIN=1
        else:
            MAIN+=1
        restaurer_palette_normale()
    if pyxel.btnp(pyxel.KEY_LEFT):
        if MAIN<=1:
            MAIN=15
        else:
            MAIN-=1
        restaurer_palette_normale()
    if MAIN==1:
        deplacementMeteores()
        gestionExplosions()
    if MAIN==2:
        global progresso, velocidade, pausado, ciclar_cores, mostrar_hud, hyp_on
        global fase, fade, dt, ultimo_tempo, fps_suave
        instalar_paleta()
        agora = time.perf_counter()
        dt = min(agora - ultimo_tempo, 0.1)      # limita saltos (janela arrastada, etc.)
        ultimo_tempo = agora
        if dt > 0.0:
            fps_suave += (1.0 / dt - fps_suave) * 0.1

        if pyxel.btnp(pyxel.KEY_SPACE):
            pausado = not pausado
        if pyxel.btnp(pyxel.KEY_R):
            reiniciar_ciclo(0.0)

        if not pausado:
            progresso += dt * velocidade * OITAVAS_POR_SEGUNDO / OITAVAS_TOTAIS
            if ciclar_cores:
                fase = (fase + CICLO_CORES * dt) % N_PALETA
            if progresso >= 1.0:
                reiniciar_ciclo(progresso - 1.0)  # imagem do Mandelbrot reencontrada: restaura

        if fade < 2.0:
            fade = min(2.0, fade + dt / DURACAO_FADE)
    if MAIN==3:
        global move_x
        global move_y
        global dir

        if dir == 0:
        # Vers la gauche
            move_x -= speed

            if move_x <= -distance:
                move_x = -distance
                dir = 1

        elif dir == 1:
        # Vers le haut
            move_y -= speed

            if move_y <= -distance:
                move_y = -distance
                dir = 2

        elif dir == 2:
        # Vers la droite
            move_x += speed

            if move_x >= distance:
                move_x = distance
                dir = 3

        elif dir == 3:
        # Vers le bas
            move_y += speed

            if move_y >= distance:
                move_y = distance
                dir = 0

    if MAIN==4:
        global angle

        angle += 0.015

        if angle >= math.pi * 2:
            angle -= math.pi * 2
            
    if MAIN==5:
        global ab
    # Rotation du pavage
        ab += 0.025
        if ab >= 2 * math.pi:
            ab -= 2 * math.pi
            
    if MAIN==6:
        global angl
        angl += 0.015
        if angl >= 2 * math.pi:
            angl -= 2 * math.pi

    if MAIN==7:
        for butterfly in butterflies:
            butterfly[2] += butterfly[3]
            if butterfly[2] > math.pi * 2:
                butterfly[2] -= math.pi * 2
            if butterfly[2] < -math.pi * 2:
                butterfly[2] += math.pi * 2
            
    if MAIN==8:
        global ang
        ang += 0.025
        if ang >= 2 * math.pi:
            ang -= 2 * math.pi

    if MAIN==9:
        global an
        an += sped
        if an >= math.pi * 2:
            an -= math.pi * 2

    if MAIN==10:
        global anglus
        anglus += 1.5

        if anglus >= 360:
            anglus -= 360
    if MAIN==11:
        global d
        d += 1
        
    if MAIN==12:
        global frwhb
        frwhb = (frwhb + 1) % PERIODE
    if MAIN==13:
        global blip

        blip = (
            blip + 1
        ) % vex
        
    if MAIN==14:

        global palette_id, steps, hyp_on, hyp_zoom, HYP_MAP

        # -----------------------------------------
        # Initialisation de sécurité
        # -----------------------------------------

        if U is None or V is None:
            reset_butterfly()

        if HYP_MAP is None:
            HYP_MAP = make_hyperbolic_map(
                pyxel.width,
                pyxel.height,
                hyp_zoom,
                RIM
            )

        # -----------------------------------------
        # Réinitialisations automatiques
        # -----------------------------------------

        if pyxel.frame_count % 150 == 0:
            reset_butterfly()

        if pyxel.frame_count % 450 == 0:
            reset_noise()

        if pyxel.frame_count % 350 == 0:
            palette_id = (
                palette_id + 1
            ) % len(PALETTE_NAMES)

            apply_palette()

        # -----------------------------------------
        # Activation / désactivation hyperbolique
        # -----------------------------------------

        if pyxel.btnp(pyxel.KEY_F):
            hyp_on = not hyp_on

        # -----------------------------------------
        # Zoom hyperbolique
        # -----------------------------------------

        if pyxel.btnp(pyxel.KEY_RIGHT):
            hyp_zoom = min(
                4.0,
                hyp_zoom + 0.25
            )

            HYP_MAP = make_hyperbolic_map(
                pyxel.width,
                pyxel.height,
                hyp_zoom,
                RIM
            )

        if pyxel.btnp(pyxel.KEY_LEFT):
            hyp_zoom = max(
                0.5,
                hyp_zoom - 0.25
            )

            HYP_MAP = make_hyperbolic_map(
                pyxel.width,
                pyxel.height,
                hyp_zoom,
                RIM
            )

        # -----------------------------------------
        # Création du trou
        # -----------------------------------------

        hole = None

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):

            mx = min(
                max(pyxel.mouse_x, 0),
                SIZE - 1
            )

            my = min(
                max(pyxel.mouse_y, 0),
                SIZE - 1
            )

            if hyp_on and HYP_MAP is not None:

                origin = HYP_MAP[0][
                    my * pyxel.width + mx
                ]

                mx = origin % pyxel.width
                my = origin // pyxel.width

                # Conversion écran -> simulation
                mx = int(
                    mx * SIZE / pyxel.width
                )

                my = int(
                    my * SIZE / pyxel.height
                )

                mx = min(
                    max(mx, 0),
                    SIZE - 1
                )

                my = min(
                    max(my, 0),
                    SIZE - 1
                )

            hole = circle_mask(
                mx,
                my,
                HOLE_RADIUS
            )

        elif pyxel.btn(pyxel.KEY_SPACE):

            hole = circle_mask(
                SIZE // 2,
                SIZE // 2,
                HOLE_RADIUS
            )

        # -----------------------------------------
        # Simulation Gray-Scott
        # -----------------------------------------

        for _ in range(steps):

            step()

            if hole is not None:
                U[hole] = 1.0
                V[hole] = 0.0

    
    if MAIN==15:
        pyxel.colors.from_list(cores_base + [c for p in PALETAS for c in p])
        global frame
        frame += 1
        for familia, s0 in ((points_horizontal, S0_A), (points_vertical, S0_B)):
            for point, s in zip(familia, s0):
                for i in range(2):
                    point[0][i], point[1][i] = borda(s[i] + frame)
     
    avanca_circulos()

process()
    
    
    
def pinta_celulas():
    ta = tabela(points_horizontal, SINAL_A)
    tb = tabela(points_vertical, SINAL_B)
    # contadores em x = -infinito: retas cujo contador desce ao andar p/ direita
    # já começam "ligadas"
    a0 = sum(1 for t in ta if t[3] < 0)
    b0 = sum(1 for t in tb if t[3] < 0)
 
    # círculos visíveis, do maior para o menor
    circulos = sorted(((r, g) for r, g in zip(rayon_cercle, geracao) if r >= 1),
                      reverse=True)
    raios = [r for r, _ in circulos]
    # regiao[k] = geração da região que está dentro de exatamente k círculos
    regiao = [fundo] + [g for _, g in circulos]
 
    cx = cy = pyxel.width // 2
    W = pyxel.width
 
    for y in range(pyxel.height):
        ev = []                                    # (x, qual contador, variação)
        for x1, y1, inv, d in ta:
            ev.append((x1 + (y - y1) * inv, 0, d))
        for x1, y1, inv, d in tb:
            ev.append((x1 + (y - y1) * inv, 1, d))
        dy2 = (y - cy) ** 2
        for r in raios:
            if dy2 < r * r:
                h = math.sqrt(r * r - dy2)
                ev.append((cx - h, 2, +1))         # entra no círculo
                ev.append((cx + h, 2, -1))         # sai do círculo
        ev.sort()
 
        c = [a0, b0, 0]
        x0 = 0                                     # 1º pixel do trecho atual
        for x, qual, d in ev:
            xi = math.ceil(x)                      # 1º pixel já depois do evento
            if xi > x0:
                if xi >= W:
                    break
                pyxel.rect(x0, y, xi - x0, 1, cor(regiao[c[2]], c[0], c[1]))
                x0 = xi
            c[qual] += d
        pyxel.rect(x0, y, W - x0, 1, cor(regiao[c[2]], c[0], c[1]))
 
#==============================================================================
#======================================DRAW====================================
#==============================================================================

def draw():
    global MAIN, d, hyp_on
    if MAIN==1:
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
            
    if MAIN==2:
        global ultimo_desenho, max_iter_atual, zoom_atual, hyp_on, buf_atual

        # 1) "shader": só recalcula se a câmera ou a paleta mudaram
        if ultimo_desenho != (progresso, fase):
            centro, passo, zoom = parametros_da_camera(progresso)
            fator = PERIODO ** progresso         # escala de iterações: 1 -> PERIODO ao longo do ciclo
            max_iter_atual = int(BASE_ITER * fator)
            eps = abs(passo) * 1.0e-3            # tolerância da detecção de periodicidade
            calcular_quadro(buf_atual, centro.real, centro.imag, passo.real, passo.imag,
                            max_iter_atual, eps, fator, fase, FREQ_COR, BAILOUT2)
            zoom_atual = zoom
            ultimo_desenho = (progresso, fase)

        # 2) Pyxel: apenas projeção na tela
        pyxel.cls(0)
        if fade < 1.0:
            pyxel.blt(0, 0, img_antigo, 0, 0, LARGURA, ALTURA)
            pyxel.dither(fade)                   # o quadro novo entra gradualmente por cima
            pyxel.blt(0, 0, img_atual, 0, 0, LARGURA, ALTURA)
            pyxel.dither(1.0)
        else:
            pyxel.blt(0, 0, img_atual, 0, 0, LARGURA, ALTURA)
        
    if MAIN==3:
        pyxel.cls(0)

        center_x = W // 2
        center_y = H // 2

        for i, (x, y) in enumerate(tiles):

        # Position du pavage
            px = center_x + x + move_x
            py = center_y + y + move_y

        # Couleurs vives
            colors = [
                8,   # rouge
                9,   # orange
                10,  # jaune
                11,  # vert
                12,  # cyan
                13,  # bleu
                14   # rose
            ]

            color = colors[i % len(colors)]

            draw_hexagon(
                px,
                py,
                size,
                color
            )

    if MAIN==4:
        global angle
        pyxel.cls(0)

        centre_x = W // 2
        centre_y = H // 2

        for typ, A, B, C in triangles:

            A = rotat(A, angle)
            B = rotat(B, angle)
            C = rotat(C, angle)

            ax = int(centre_x + A[0])
            ay = int(centre_y + A[1])

            bx = int(centre_x + B[0])
            by = int(centre_y + B[1])

            cx = int(centre_x + C[0])
            cy = int(centre_y + C[1])

        # Couleurs très vives
            if typ == 0:
                color = 10      # jaune vif
            else:
                color = 14      # rose vif

            pyxel.tri(
                ax, ay,
                bx, by,
                cx, cy,
                color
            )

        # Contours cyan
            pyxel.line(ax, ay, bx, by, 12)
            pyxel.line(bx, by, cx, cy, 12)
            pyxel.line(cx, cy, ax, ay, 12)

    if MAIN==5:
        global aba
        pyxel.cls(0)
        change_col()
        for j in range(-12, 13):

            for i in range(-14, 15):

                if point_supprime(i, j):

                    dessiner_hexagone1(i, j)
        for j in range(-13, 13):

            for i in range(-15, 15):
                aba = (i, j)
                bb = (i + 1, j)
                cb = (i, j + 1)

                if (
                    not point_supprime(aba[0], aba[1])
                    and not point_supprime(bb[0], bb[1])
                    and not point_supprime(cb[0], cb[1])
                ):

                    dessiner_tria(
                        aba[0], aba[1],
                        bb[0], bb[1],
                        cb[0], cb[1]
                    )
                aba = (i + 1, j + 1)
                bb = (i + 1, j)
                cb = (i, j + 1)

                if (
                    not point_supprime(aba[0], aba[1])
                    and not point_supprime(bb[0], bb[1])
                    and not point_supprime(cb[0], cb[1])
                ):

                    dessiner_tria(
                        aba[0], aba[1],
                        bb[0], bb[1],
                        cb[0], cb[1]
                    )

    if MAIN==6:
        pyxel.cls(0)

        for t in triangls:

            ac = t[0]
            bc = t[1]
            cc = t[2]
            type_triangl = t[3]

            if type_triangl == 0:

                triangl(
                    ac,
                    bc,
                    cc,
                    9
                )

            else:

                triangl(
                    ac,
                    bc,
                    cc,
                    12
                )

    if MAIN==7:
        pyxel.cls(0)

    # Géométrie en arrière-plan
        draw_geometry()

    # Papillons par-dessus
        for butterfly in butterflies:

            x = butterfly[0]
            y = butterfly[1]
            angle = butterfly[2]
            scale = butterfly[4]

            draw_butterfly(
                x,
                y,
                angle,
                scale
            )

    if MAIN==8:
        pyxel.cls(0)
        for ligne in range(-5, 6):

            for colonne in range(-6, 7):

                x, y = centre_hexagone(colonne, ligne)

                dessiner_hexagone2(x, y)

        for ligne in range(-5, 6):

            for colonne in range(-6, 7):

                x, y = centre_hexagone(colonne, ligne)

            # Voisin à droite
                x2, y2 = centre_hexagone(
                    colonne + 1,
                    ligne
                )

                dessiner_carre(x, y, x2, y2)

            # Voisin en haut à droite
                x2, y2 = centre_hexagone(
                    colonne,
                    ligne + 1
                )

                dessiner_carre(x, y, x2, y2)

            # Voisin en haut à gauche
                x2, y2 = centre_hexagone(
                    colonne - 1,
                    ligne + 1
                )

                dessiner_carre(x, y, x2, y2)
        for ligne in range(-5, 5):

            for colonne in range(-6, 6):

                x1, y1 = centre_hexagone(
                    colonne,
                    ligne
                )

                x2, y2 = centre_hexagone(
                    colonne + 1,
                    ligne
                )

                x3, y3 = centre_hexagone(
                    colonne,
                    ligne + 1
                )

            # Centre du triang
                cx = (x1 + x2 + x3) / 3
                cy = (y1 + y2 + y3) / 3

                dessiner_triang(
                    cx,
                    cy,
                    True
                )


    # Triangs orientés vers le bas

        for ligne in range(-5, 5):

            for colonne in range(-6, 6):

                x1, y1 = centre_hexagone(
                    colonne + 1,
                    ligne + 1
                )

                x2, y2 = centre_hexagone(
                    colonne,
                    ligne + 1
                )

                x3, y3 = centre_hexagone(
                    colonne + 1,
                    ligne
                )

            # Centre du triang
                cx = (x1 + x2 + x3) / 3
                cy = (y1 + y2 + y3) / 3

                dessiner_triang(
                    cx,
                    cy,
                    False
                )

    if MAIN==9:
        pyxel.cls(0)
        offset_x = math.cos(an) * rayon_x
        offset_y = math.sin(an) * rayon_y
        center_x = W / 2
        center_y = H / 2
        for i, polygon in enumerate(dodecagons):

            moved = []

            for x, y in polygon:

                moved.append((
                    center_x + x + offset_x,
                    center_y + y + offset_y
                ))

            color = DODEC_COLORS[
                i % len(DODEC_COLORS)
            ]

            draw_polygon(
                moved,
                color
            )
            inner1 = DODEC_COLORS[
                (i + 3) % len(DODEC_COLORS)
            ]

            inner2 = DODEC_COLORS[
                (i + 5) % len(DODEC_COLORS)
            ]

            draw_inner_pattern(
                moved,
                inner1,
                inner2
            )
        for i, trian in enumerate(trians):

            moved = []

            for x, y in trian:

                moved.append((
                    center_x + x + offset_x,
                    center_y + y + offset_y
                ))

            color = TRI_COLORS[
                i % len(TRI_COLORS)
            ]

            draw_polygon(
                moved,
                color
            )

    if MAIN==10:
        global N, TAILLE, LARGEUR, HAUTEUR
        pyxel.cls(0)

    # Centre de la fenêtre
        cx = 80
        cy = 60

        a = math.radians(anglus)

        for y in range(-N, N + 1):
            for x in range(-N, N + 1):

            # Position par rapport au centre
                px = x * TAILLE
                py = y * TAILLE

            # Rotation
                rx = px * math.cos(a) - py * math.sin(a)
                ry = px * math.sin(a) + py * math.cos(a)

            # Alternance des couleurs
                if (x + y) % 2 == 0:
                    couleur = 7
                else:
                    couleur = 13

            # Dessin de la case
                pyxel.rect(
                    cx + rx - TAILLE / 2,
                    cy + ry - TAILLE / 2,
                    TAILLE - 1,
                    TAILLE - 1,
                    couleur
                )
    if MAIN==11:
        pyxel.cls(0)
        periode = 240
        phase = (d % periode) / periode
        if phase < 0.25:
            progression = phase / 0.25
            forme_a = 0
            forme_b = 1
        elif phase < 0.5:
            progression = (phase - 0.25) / 0.25
            forme_a = 1
            forme_b = 2
        elif phase < 0.75:
            progression = (phase - 0.5) / 0.25
            forme_a = 2
            forme_b = 3
        else:
            progression = (phase - 0.75) / 0.25
            forme_a = 3
            forme_b = 0
        p = (1 - math.cos(progression * math.pi)) / 2
        for ligne, y in enumerate(range(-10, H + 20, CELL)):
            for colonne, x in enumerate(range(-10, W + 20, CELL)):
                decalage = 0
                if ligne % 2 == 1:
                    decalage = CELL / 2
                cx = x + decalage
                cy = y
                dx = cx - W / 2
                dy = cy - H / 2
                distance = math.sqrt(dx * dx + dy * dy)
                mouvement_x = math.sin(
                    distance * 0.08 - d * 0.04
                ) * 3
                mouvement_y = math.cos(
                    distance * 0.06 + d * 0.03
                ) * 3
                cx += mouvement_x
                cy += mouvement_y
                oscillation = math.sin(
                    d * 0.05 + distance * 0.08
                )
                taille_a = 7 + oscillation * 2
                taille_b = 7 - oscillation * 2
                taille = truc(
                    taille_a,
                    taille_b,
                    p
                )
                effet_transition = math.sin(
                    progression * math.pi
                )
                taille += effet_transition * 3
                rotation = (
                    d * 0.015
                    + colonne * 0.2
                    + ligne * 0.15
                )
                if (colonne + ligne) % 2 == 0:
                    couleur = 9
                else:
                    couleur = 12
                if int(distance / 20) % 2 == 0:
                    couleur = 10
                valeur = (
                    colonne
                    + ligne
                    + int(progression * 4)
                ) % 4
                if progression < 0.5:
                    forme = forme_a
                    if valeur == 0:
                        forme = forme_b
                else:
                    forme = forme_b
                    if valeur == 0:
                        forme = forme_a
                dess_for(
                    cx,
                    cy,
                    taille,
                    forme,
                    couleur,
                    rotation
                )
                rayon = 1.5 + abs(
                    math.sin(
                        d * 0.08
                        + distance * 0.05
                    )
                ) * 1.5
                pyxel.circ(
                    int(cx),
                    int(cy),
                    int(rayon),
                    7
                )
                
    if MAIN==12:
        pyxel.cls(0)

    # Valeurs EXACTES de cette image
        s = fruit[frwhb]
        c = hello[frwhb]

        for ligne, y in enumerate(
            range(-paii, H + paii, paii)
        ):

            for colonne, x in enumerate(
                range(-paii, W + paii, paii)
            ):

            # Phase spatiale
                phase = (
                    colonne * 0.55
                    + ligne * 0.75
                )

            # On crée plusieurs composantes du mouvement.
            # Elles sont toutes basées sur le même cycle.

                s1 = math.cos(
                    phase
                    + 2 * math.pi * frwhb / PERIODE
                )

                c1 = math.sin(
                    phase
                    + 2 * math.pi * frwhb / PERIODE
                )

            # Déformation du jut
                deformation = s1 * 5

            # Déplacement horizontal
                decalage_x = c1 * 4

            # Déplacement vertical
                decalage_y = s1 * 3

                xx = x + decalage_x
                yy = y + decalage_y

                couleur = CLOK[
                    (colonne + ligne) % len(CLOK)
                ]

                jut(
                    xx,
                    yy,
                    paii,
                    deformation,
                    couleur
                )
    if MAIN==13:
        pyxel.cls(0)

        phase = (
        2 * math.pi
        * blip
        / vex
    )

        theta = (
        math.sin(phase)
        * 0.035
    )

        zoom = (
        0.48
        + math.sin(phase)
        * 0.012
    )

        for points, sorte, centre in tuiles:

            couleur = truc_chose(
            centre[0],
            centre[1],
            phase,
            sorte
        )

            p = []

            for point in points:

                p.append(
                teleportation(
                    point,
                    theta,
                    zoom
                )
            )

            pyxel.tri(
            p[0][0], p[0][1],
            p[1][0], p[1][1],
            p[2][0], p[2][1],
            couleur
        )

            pyxel.tri(
            p[0][0], p[0][1],
            p[2][0], p[2][1],
            p[3][0], p[3][1],
            couleur
        )

            for i in range(4):

                a = p[i]
                b = p[(i + 1) % 4]

                pyxel.line(
                a[0],
                a[1],
                b[0],
                b[1],
                0
            )

    if MAIN == 14:
        apply_palette()
        # Sécurité
        if V is None:
            return

        # Conversion 128x128 -> 160x120
        image = simulation_to_screen()

        # Accès au framebuffer Pyxel
        buf = np.frombuffer(
            pyxel.screen.data_ptr(),
            dtype=np.uint8
        )

        # Copie de l'image dans l'écran
        buf[:] = image.ravel()
    if MAIN==15:
        global hyp_on
        pyxel.cls(0)
        CENTRE = pyxel.width // 2
     
        pinta_celulas()
     
        for r in rayon_cercle:
            pyxel.circb(CENTRE, CENTRE, r, 13)
        for familia in (points_horizontal, points_vertical):
            for p in familia:
                pyxel.line(p[0][0], p[1][0], p[0][1], p[1][1], 7)

        # Déformation hyperbolique
    if hyp_on and HYP_MAP is not None:
        apply_hyperbolic(HYP_MAP)
    if pyxel.frame_count%730==0:
        hyp_on = not hyp_on
            
    

# =====================================================
# INITIALISATION FINALE
# =====================================================

# Simulation Gray-Scott
reset_butterfly()

# Palette


# Carte hyperbolique
HYP_MAP = make_hyperbolic_map(
    pyxel.width,
    pyxel.height,
    hyp_zoom,
    RIM
)

# Calcul initial du fractal pour MAIN==2
process()

# =====================================================
# LANCEMENT
# =====================================================

pyxel.run(update, draw)

