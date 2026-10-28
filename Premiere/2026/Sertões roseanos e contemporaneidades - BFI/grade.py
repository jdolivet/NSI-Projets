import math
import numpy as np
 
import pyxel
 
pyxel.init(255, 255, 'grille')
 
# ----------------------------------------------------------------------
# PALETAS
# ----------------------------------------------------------------------
# Cada paleta tem 9 cores (uma por "posição" na grade 9x9).
# Escuras e saturadas, na linha de Butterfly 3000 (KGLW) e Sgt. Pepper's.
# Precisa de um Pyxel que aceite mais de 16 cores na paleta (versões recentes).
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
pyxel.colors.from_list(cores_base + [c for p in PALETAS for c in p])
 
 
def cor(g, a, b):
    """Cor da célula (a, b) dentro da região de "geração" g.
    g escolhe a paleta e também desloca o padrão da grade, então ao cruzar
    a borda de um círculo tanto as cores quanto o desenho da grade mudam."""
    return BASE + (g % len(PALETAS)) * N_COR + (a + 2 * b + 4 * g) % N_COR
 
 
v = {
    'points_horizontal' : [
        [[pyxel.width // 2, pyxel.width // 2],[pyxel.width, 0]],
        [[(pyxel.width // 2) + 32, (pyxel.width // 2) + 32],[pyxel.width, 0]],
        [[(pyxel.width // 2) + 64, (pyxel.width // 2) + 64],[pyxel.width, 0]],
        [[(pyxel.width // 2) + 96, (pyxel.width // 2) + 96],[pyxel.width, 0]],
        [[(pyxel.width // 2) + 128, (pyxel.width // 2) + 128],[pyxel.width, 0]],
        [[(pyxel.width // 2) - 32, (pyxel.width // 2) - 32],[pyxel.width, 0]],
        [[(pyxel.width // 2) - 64, (pyxel.width // 2) - 64],[pyxel.width, 0]],
        [[(pyxel.width // 2) - 96, (pyxel.width // 2) - 96],[pyxel.width, 0]],
        [[(pyxel.width // 2) - 128, (pyxel.width // 2) - 128],[pyxel.width, 0]],
        ],
    "points_vertical" : [
        [[pyxel.width, 0],[(pyxel.width // 2), (pyxel.width // 2)]],
        [[pyxel.width, 0],[(pyxel.width // 2) + 32, (pyxel.width // 2) + 32]],
        [[pyxel.width, 0],[(pyxel.width // 2) + 64, (pyxel.width // 2) + 64]],
        [[pyxel.width, 0],[(pyxel.width // 2) + 96, (pyxel.width // 2) + 96]],
        [[pyxel.width, 0],[(pyxel.width // 2) + 128, (pyxel.width // 2) + 128]],
        [[pyxel.width, 0],[(pyxel.width // 2) - 32, (pyxel.width // 2) - 32]],
        [[pyxel.width, 0],[(pyxel.width // 2) - 64, (pyxel.width // 2) - 64]],
        [[pyxel.width, 0],[(pyxel.width // 2) - 96, (pyxel.width // 2) - 96]],
        [[pyxel.width, 0],[(pyxel.width // 2) - 128, (pyxel.width // 2) - 128]]],
    "rayon" : [0, 32, 64, 96, 124],
 
    # --- memória das cores dos círculos ---------------------------------
    # Cada círculo carrega uma "geração" (um número inteiro) que escolhe a
    # paleta da região dentro dele. 'fundo' é a geração da região fora de
    # todos os círculos. 'ultima' é a última geração já distribuída.
    "geracao" : [1, 2, 3, 4, 5],
    "fundo" : 0,
    "ultima" : 5,
    }
 
# Raio a partir do qual o círculo cobre a tela inteira (canto: 127 * raiz(2) ≈ 179,6).
RAIO_MAX = 181
hyp_on = True
hyp_zoom = 1.5          # ampliação do centro (1 = tamanho original)
RIM = 0.985             # onde o disco termina (perto de 1 = mais ladrilhos na borda)
HYP_MAP = None
 
# ----------------------------------------------------------------------
# GEOMETRIA (varredura de linha)
# ----------------------------------------------------------------------
# Em vez de montar polígonos, percorremos a tela linha por linha (y fixo).
# Em cada linha, só alguns pontos x mudam a cor:
#   - onde a linha y cruza cada uma das 18 retas  (interseção reta x linha)
#   - onde a linha y entra/sai de cada círculo     (corda do círculo)
# Ordenamos esses pontos e pintamos cada trecho entre dois deles com UMA cor.
# Três contadores dizem em que "célula" estamos:
#   a = quantas retas da 1ª família ficaram à esquerda
#   b = quantas retas da 2ª família ficaram acima
#   k = em quantos círculos o ponto está DENTRO
# Como os círculos são concêntricos, os k círculos que contêm o ponto são
# sempre os k MAIORES; o menor deles dá a "região" (e portanto a paleta).
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
 
 
S0_A = [[para_s(p[0][i], p[1][i]) for i in range(2)] for p in v['points_horizontal']]
S0_B = [[para_s(p[0][i], p[1][i]) for i in range(2)] for p in v['points_vertical']]
frame = 0
 
 
def avanca_circulos():
    """Cresce todos os círculos 1 pyxel.
 
    Quando um círculo passa a cobrir a tela inteira, ele volta ao centro, mas a
    sua paleta NÃO some: ela vira a cor do fundo (a região fora de todos os
    círculos). Antes do salto, os pixels de fora estavam "dentro" desse círculo;
    depois, estão no "fundo" com a mesma paleta, então nenhum pixel muda de cor.
    O círculo renasce no centro com uma geração nova (paleta nova)."""
    for i in range(len(v['rayon'])):
        v['rayon'][i] += 1
        if v['rayon'][i] >= RAIO_MAX:
            v['rayon'][i] -= RAIO_MAX
            v['fundo'] = v['geracao'][i]
            v['ultima'] += 1
            v['geracao'][i] = v['ultima']
            
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
 
 
def apply_hyperbolic(hmap):
    """Distorce o que já foi desenhado na tela. Chame no FIM do draw()."""
    src_index, outside = hmap
    buf = np.frombuffer(pyxel.screen.data_ptr(), dtype=np.uint8)
    if buf.size != src_index.size:
        raise ValueError("o mapa foi criado para outro tamanho de tela")
    buf[:] = buf[src_index]
    #buf[outside] = 0
 
 
 
 
def update():
    global frame, hyp_on
    frame += 1
    for familia, s0 in ((v['points_horizontal'], S0_A), (v['points_vertical'], S0_B)):
        for point, s in zip(familia, s0):
            for i in range(2):
                point[0][i], point[1][i] = borda(s[i] + frame)
 
    avanca_circulos()
    if pyxel.frame_count%300==0:
        hyp_on = not hyp_on
 
 
def pinta_celulas():
    ta = tabela(v['points_horizontal'], SINAL_A)
    tb = tabela(v['points_vertical'], SINAL_B)
    # contadores em x = -infinito: retas cujo contador desce ao andar p/ direita
    # já começam "ligadas"
    a0 = sum(1 for t in ta if t[3] < 0)
    b0 = sum(1 for t in tb if t[3] < 0)
 
    # círculos visíveis, do maior para o menor
    circulos = sorted(((r, g) for r, g in zip(v['rayon'], v['geracao']) if r >= 1),
                      reverse=True)
    raios = [r for r, _ in circulos]
    # regiao[k] = geração da região que está dentro de exatamente k círculos
    regiao = [v['fundo']] + [g for _, g in circulos]
 
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
 
 
def draw():
    global hyp_on
    pyxel.cls(0)
    CENTRE = pyxel.width // 2
 
    pinta_celulas()
 
    for r in v['rayon']:
        pyxel.circb(CENTRE, CENTRE, r, 13)
    for familia in (v['points_horizontal'], v['points_vertical']):
        for p in familia:
            pyxel.line(p[0][0], p[1][0], p[0][1], p[1][1], 7)
            
    if hyp_on:
        apply_hyperbolic(HYP_MAP) 
 
HYP_MAP = make_hyperbolic_map(pyxel.width, pyxel.height, hyp_zoom, RIM)
pyxel.run(update, draw)
 