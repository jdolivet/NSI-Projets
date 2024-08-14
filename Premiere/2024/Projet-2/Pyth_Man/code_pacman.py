import pyxel
import random



Taille = 8
labirynthe = [
    "####################",
    "#........#.........#",
    "#.##.###.#.###.##..#",
    "#.................##",
    "#.##.#.#####.#.##..#",
    "#....#...#...#.....#",
    "####.###.#.###.#####",
    "####.#.......#.#####",
    "####.#.## ##.#.#####",
    "####.#.#   #.#.#####",
    "####.#.#   #.#.#####",
    "#........#.........#",
    "#.##.###.#.###.##..#",
    "#..#.............#.#",
    "##.#.#.#####.#.#.#.#",
    "#....#...#...#.....#",
    "#.######.#.######..#",
    "#..................#",
    "####################",]

pacman = {'x': 1, 'y': 1, 'dir': (1, 0)}
fantômes = [
    {'x': 10, 'y': 10, 'dir': (1, 0), 'color': pyxel.COLOR_RED},
    {'x': 13, 'y': 10, 'dir': (-1, 0), 'color': pyxel.COLOR_RED},
    {'x': 10, 'y': 13, 'dir': (0, 1), 'color': pyxel.COLOR_RED},
    {'x': 13, 'y': 13, 'dir': (0, -1), 'color': pyxel.COLOR_RED}]
points = []
fruits = []
score = 0
vies = 3

conteur_mouv_pacman = 0
conteur_mouv_fant = 0
interval_mouv_pacman = 6  
interval_mouv_fant = 6   



def debut():
    global points, fruits
    points = [(x, y) for y, a in enumerate(labirynthe) for x, cellule in enumerate(a) if cellule == '.']
    fruits = []


def update():
    global pacman, score, vies, conteur_mouv_pacman, conteur_mouv_fant

    def detection_mur(x, y):
        return labirynthe[y][x] != '#'

    def mouv_pacman(dx, dy):
        if detection_mur(pacman['x'] + dx, pacman['y'] + dy):
            pacman['x'] += dx
            pacman['y'] += dy

    conteur_mouv_pacman += 1
    if conteur_mouv_pacman >= interval_mouv_pacman:
        conteur_mouv_pacman = 0
        if pyxel.btn(pyxel.KEY_RIGHT):
            mouv_pacman(1, 0)
        elif pyxel.btn(pyxel.KEY_LEFT):
            mouv_pacman(-1, 0)
        elif pyxel.btn(pyxel.KEY_UP):
            mouv_pacman(0, -1)
        elif pyxel.btn(pyxel.KEY_DOWN):
            mouv_pacman(0, 1)

    if (pacman['x'], pacman['y']) in points:
        points.remove((pacman['x'], pacman['y']))
        score += 10

    if (pacman['x'], pacman['y']) in fruits:
        fruits.remove((pacman['x'], pacman['y']))
        score += 100

    conteur_mouv_fant += 1
    if conteur_mouv_fant >= interval_mouv_fant:
        conteur_mouv_fant = 0
        for fantôme in fantômes:
            dx, dy = fantôme['dir']
            if detection_mur(fantôme['x'] + dx, fantôme['y'] + dy):
                fantôme['x'] += dx
                fantôme['y'] += dy
            else:
                fantôme['dir'] = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    for fantôme in fantômes:
        if (pacman['x'], pacman['y']) == (fantôme['x'], fantôme['y']):
            vies -= 1
            pacman = {'x': 1, 'y': 1, 'dir': (1, 0)}
            if vies == 0:
                pyxel.quit()

    if random.random() < 0.01:
        x, y = random.choice([(x, y) for y, a in enumerate(labirynthe) for x, cellule in enumerate(a) if cellule == '.'])
        fruits.append((x, y))

def draw():
    pyxel.cls(0)

    for y, a in enumerate(labirynthe):
        for x, cellule in enumerate(a):
            if cellule == "#":
                pyxel.rect(x * Taille, y * Taille, Taille, Taille, pyxel.COLOR_GREEN)
            else:
                pyxel.rect(x * Taille, y * Taille, Taille, Taille, pyxel.COLOR_BLACK)

    for (x, y) in points:
        pyxel.circ(x * Taille + Taille // 2, y * Taille + Taille // 2, 1, pyxel.COLOR_WHITE)
    for (x, y) in fruits:
        pyxel.circ(x * Taille + Taille // 2, y * Taille + Taille // 2, 2, pyxel.COLOR_RED)
    pyxel.rect(pacman['x'] * Taille, pacman['y'] * Taille, Taille, Taille, pyxel.COLOR_YELLOW)
    for fantôme in fantômes:
        pyxel.rect(fantôme['x'] * Taille, fantôme['y'] * Taille, Taille, Taille, fantôme['color'])

    pyxel.text(5, 5, f"Score: {score}", pyxel.COLOR_WHITE)
    pyxel.text(5, 15, f"Vies: {vies}", pyxel.COLOR_WHITE)



pyxel.init(160, 160, title="Pac-Man")
debut()
pyxel.run(update, draw)
