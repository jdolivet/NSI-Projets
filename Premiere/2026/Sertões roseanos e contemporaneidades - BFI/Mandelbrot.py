"""
Zoom infinito no Vale do Cavalo-Marinho do conjunto de Mandelbrot, com Pyxel.

Instalação:
    pip install pyxel numpy numba
Execução:
    python mandelbrot_cavalo_marinho.py

Como o programa está organizado (mesma separação do repositório de referência,
oprogramadorreal/Mandelbrot: a CPU guarda o estado da câmera e a "placa gráfica"
calcula cada pixel):

  * atualizar()        -> "CPU": avança a câmera (centro, escala, rotação) e lê o teclado.
  * calcular_quadro()  -> "shader": kernel numba paralelo, uma execução por pixel.
                          Escreve índices de paleta direto na memória de uma pyxel.Image.
  * desenhar()         -> Pyxel só projeta: blt() da imagem para a tela (e dither()
                          para o fade entre ciclos).

Por que o zoom é "infinito":
  Em c* = NUCLEO existe um minibrot (cópia do conjunto inteiro) de período 39.
  A renormalização c' = KAPPA * (c - c*) mapeia a vizinhança de c* de volta no
  conjunto de Mandelbrot original. A câmera faz uma espiral logarítmica (zoom +
  rotação) em torno do ponto fixo dessa semelhança, de modo que, ao fim do ciclo,
  o quadro é (quase) idêntico ao quadro inicial. Aí os valores são restaurados e
  o zoom recomeça, com um fade curto para disfarçar as pequenas diferenças da
  vizinhança. Tudo cabe em float64 (o menor campo de visão é ~7e-6).

Controles:
    ESPAÇO  pausa / continua        CIMA / BAIXO  acelera / desacelera o zoom
    R       reinicia o ciclo        C  liga/desliga ciclo de cores
    H       mostra/oculta o HUD     ESC  sai
"""

import cmath
import math
import time

import numpy as np
import pyxel
from numba import njit, prange

# --------------------------------------------------------------------------
# Parâmetros ajustáveis
# --------------------------------------------------------------------------
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


# --------------------------------------------------------------------------
# Estado global (programação procedural: nada de classes)
# --------------------------------------------------------------------------
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

hyp_on = True
hyp_zoom = 1.5          # ampliação do centro (1 = tamanho original)
RIM = 0.985             # onde o disco termina (perto de 1 = mais ladrilhos na borda)
HYP_MAP = None

# --------------------------------------------------------------------------
# Inicialização: compila o kernel antes de abrir a janela
# --------------------------------------------------------------------------
print("Compilando o kernel numba (só demora na primeira execução)...")
_teste = np.zeros((8, 8), dtype=np.uint8)
calcular_quadro(_teste, -0.75, 0.0, 0.1, 0.0, 16, 1e-6, 1.0, 0.0, 6.0, BAILOUT2)

pyxel.init(LARGURA, ALTURA, title="Mandelbrot - Vale do Cavalo-Marinho", fps=FPS)
instalar_paleta()

img_atual = pyxel.Image(LARGURA, ALTURA)     # quadro calculado agora
img_antigo = pyxel.Image(LARGURA, ALTURA)    # último quadro do ciclo anterior (fade)
buf_atual = visao_numpy(img_atual)
buf_antigo = visao_numpy(img_antigo)

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


# --------------------------------------------------------------------------
# Laço do Pyxel
# --------------------------------------------------------------------------
def atualizar():
    global progresso, velocidade, pausado, ciclar_cores, mostrar_hud, hyp_on
    global fase, fade, dt, ultimo_tempo, fps_suave

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
    if pyxel.btnp(pyxel.KEY_F):
        hyp_on = not hyp_on


def desenhar():
    global ultimo_desenho, max_iter_atual, zoom_atual, hyp_on

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
    if hyp_on:
        apply_hyperbolic(HYP_MAP)

HYP_MAP = make_hyperbolic_map(pyxel.width, pyxel.height, hyp_zoom, RIM)
pyxel.run(atualizar, desenhar)