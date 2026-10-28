import pyxel as px

px.init(255, 255, 'grille')

v = {
    'points_horizontal' : [
        [[px.width // 2, px.width // 2],[px.width, 0]],
        [[(px.width // 2) + 32, (px.width // 2) + 32],[px.width, 0]],
        [[(px.width // 2) + 64, (px.width // 2) + 64],[px.width, 0]],
        [[(px.width // 2) + 96, (px.width // 2) + 96],[px.width, 0]],
        [[(px.width // 2) + 128, (px.width // 2) + 128],[px.width, 0]],
        [[(px.width // 2) - 32, (px.width // 2) - 32],[px.width, 0]],
        [[(px.width // 2) - 64, (px.width // 2) - 64],[px.width, 0]],
        [[(px.width // 2) - 96, (px.width // 2) - 96],[px.width, 0]],
        [[(px.width // 2) - 128, (px.width // 2) - 128],[px.width, 0]],
        ],
    "points_vertical" : [
        [[px.width, 0],[(px.width // 2), (px.width // 2)]],
        [[px.width, 0],[(px.width // 2) + 32, (px.width // 2) + 32]],
        [[px.width, 0],[(px.width // 2) + 64, (px.width // 2) + 64]],
        [[px.width, 0],[(px.width // 2) + 96, (px.width // 2) + 96]],
        [[px.width, 0],[(px.width // 2) + 128, (px.width // 2) + 128]],
        [[px.width, 0],[(px.width // 2) - 32, (px.width // 2) - 32]],
        [[px.width, 0],[(px.width // 2) - 64, (px.width // 2) - 64]],
        [[px.width, 0],[(px.width // 2) - 96, (px.width // 2) - 96]],
        [[px.width, 0],[(px.width // 2) - 128, (px.width // 2) - 128]]],
    "rayon" : [0, 32, 64, 96, 124],
    "cores" : [[8, 11, 12, 10, 9, 14, 2, 3, 6],
            [11, 2, 9, 10, 14, 12, 6, 8, 3],
            [12, 10, 9, 3, 2, 14, 6, 8, 11],
            [10, 9, 3, 2, 14, 6, 8, 11, 12],
            [9, 3, 2, 14, 6, 8, 11, 12, 10],
            [14, 2, 3, 6, 8, 11, 12, 10, 9],
            [2, 14, 6, 8, 11, 12, 10, 9, 3],
            [14, 6, 8, 11, 12, 10, 9, 3, 2],
            [6, 8, 11, 12, 10, 9, 3, 2, 14]],

    }

def update():
    for point in v['points_horizontal']:
        for i in range(2):
            if point[1][i] <= 0:
                point[0][i] += 1
            if point[0][i] >= px.width:
                point[1][i] += 1
            if point[1][i] >= px.width:
                point[0][i] -= 1
            if point[0][i] <= 0:
                point[1][i] -= 1
    for point in v['points_vertical']:
        for i in range(2):
            if point[1][i] <= 0:
                point[0][i] += 1
            if point[0][i] >= px.width:
                point[1][i] += 1
            if point[1][i] >= px.width:
                point[0][i] -= 1
            if point[0][i] <= 0:
                point[1][i] -= 1
                
    for i in range(len(v['rayon'])):
        v['rayon'][i] = (v['rayon'][i] + 1) % (px.width / 2**0.5)
    
def draw():
    px.cls(0)
    CENTRE = px.width // 2
    for i in range(len(v['rayon'])):
        px.circb(CENTRE, CENTRE, v['rayon'][i], 13)
    
    for point in v['points_horizontal']:
        for i in range(2):
            px.line(point[0][0], point[1][0], point[0][1], point[1][1], 7)
    for point in v['points_vertical']:
        for i in range(2):
            px.line(point[0][0], point[1][0], point[0][1], point[1][1], 7)
    acc_i = 0
    acc_j = 0
    for i in range(px.width):
        acc_j = 0
        if px.pget(i, 0) == 7:
            px.pset(i, 0, 7)
            acc_i += 1
        for j in range(1, px.width):
            if (px.pget(i, j) == 7):
                px.pset(i, j, 7)
            elif (px.pget(i, j) == 13):
                px.pset(i, j, 13)
                acc_j += 1
            else:
                px.pset(i, j, v['cores'][acc_i % 9][acc_j % 9])
            if (px.pget(i, j) == 7) and (px.pget(i, j - 1) != 7):
                acc_j += 1
    
px.run(update, draw)