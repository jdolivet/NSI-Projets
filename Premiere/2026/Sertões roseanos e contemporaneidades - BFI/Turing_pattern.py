"""
Turing patterns (Gray-Scott) em Pyxel — semente em forma de borboleta.
 
Controles:
  Botão esquerdo do mouse (segurar) -> abre um "espaço vazio" sob o cursor
  ESPAÇO (segurar)                  -> abre o espaço vazio no centro
  (ao soltar, o resto de U e V invade o vazio)
  R   -> reinicia com a semente em borboleta
  N   -> reinicia com ruído aleatório (como no código original)
  P   -> troca de paleta
  ↑/↓ -> mais/menos passos de simulação por frame
"""
import numpy as np
import pyxel
 
# ---------------------------------------------------------------- parâmetros
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
    "rosa":        [0xAAAAFF, 0xFFAAAA],
}
PALETTE_NAMES = list(PALETTES)
 
# ---------------------------------------------------------------- estado global
U = None
V = None
palette_id = 0
steps = STEPS_PER_FRAME
fast = True
 
 
# ---------------------------------------------------------------- funções auxiliares
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


# ---------------------------------------------------------------- laço do Pyxel
def update():
    global palette_id, steps
 
    if pyxel.btnp(pyxel.KEY_R):
        reset_butterfly()
    if pyxel.btnp(pyxel.KEY_N):
        reset_noise()
    if pyxel.btnp(pyxel.KEY_P):
        palette_id = (palette_id + 1) % len(PALETTE_NAMES)
        apply_palette()
    if pyxel.btnp(pyxel.KEY_UP):
        steps = min(100, steps + 5)
    if pyxel.btnp(pyxel.KEY_DOWN):
        steps = max(1, steps - 5)
 
    # espaço vazio: enquanto o botão estiver apertado, a região é mantida
    # em U=1, V=0 (estado "vazio"); ao soltar, os vizinhos invadem o buraco.
    hole = None
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        hole = circle_mask(pyxel.mouse_x, pyxel.mouse_y, HOLE_RADIUS)
    elif pyxel.btn(pyxel.KEY_SPACE):
        hole = circle_mask(SIZE // 2, SIZE // 2, HOLE_RADIUS)
 
    for _ in range(steps):
        step()
        if hole is not None:
            U[hole] = 1.0
            V[hole] = 0.0
 
 
def draw():
    global fast
    idx = np.clip(V / VMAX * 15, 0, 15).astype(np.uint8)
    if fast:
        try:
            buf = np.frombuffer(pyxel.screen.data_ptr(), dtype=np.uint8)
            buf[:] = idx.ravel()
            return
        except Exception:
            fast = False
 
    for y in range(SIZE):
        row = idx[y]
        for x in range(SIZE):
            pyxel.pset(x, y, int(row[x]))
            
 
 
# ---------------------------------------------------------------- início
pyxel.init(SIZE, SIZE, title="Turing patterns", fps=30)
pyxel.mouse(True)
apply_palette()
reset_butterfly()
pyxel.run(update, draw)