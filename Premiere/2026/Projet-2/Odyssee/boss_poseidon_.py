import pyxel as px
from random import randint
import math
import sys
import subprocess



px.init(256,256,"Ile du boss")
px.load("musica_game_ulysse.pyxres")
px.playm(2, loop=True)
px.load('teste.pyxres')
v={
       "vitesse_x" : 0,
       "vitesse_y" : 0,
       "x_perso" : 112,
       "y_perso" : 112,
       "vie" : 5,
       "a" : 4,
       "projectiles_joueur" : [],
       "acce_joueur" : 0,
       "orientation" : 0,
       "timer_joueur" : 0,
       "coord_projectiles_alterne": [],
       "marque_temps_alterne" : 0,
       "alterne_cycle" : 15,
       "acce_alterne" : 0,
       "fase1_alterne": False,
       "gigue" : 1,
       "coord_projectiles_sin": [],
       "acce_sin" : 0,
       "coord_projectiles_cos": [],
       "acce_cos" : 0,
       "rotation" : 0,
       "depla_boss" : [194, 0, 1],
       "vie_boss" : 500,
       "bateau_ennemi" : [],
       "ballon_bateau" : [],
       "commence_cycle" : False,
       "death" : False,
       "v" : False,
       "frame_buffer" : 0,
}


def deplacement_perso():
    if (v['vitesse_x'] < 0):
        v['vitesse_x'] += 20
    if (v['vitesse_x'] > 0):
        v['vitesse_x'] -= 20
        
    if (v['vitesse_y'] < 0):
        v['vitesse_y'] += 20
    if (v['vitesse_y'] > 0):
        v['vitesse_y'] -= 20
    
    
    if px.btn(px.KEY_UP):
        v['orientation'] = 0
        if v['vitesse_y'] > -220:
            v['vitesse_y'] -= 40
    if px.btn(px.KEY_DOWN):
        v['orientation'] = 0
        if v['vitesse_y'] < 220:
            v['vitesse_y'] += 40
    if px.btn(px.KEY_RIGHT):
        v['orientation'] = 1
        if v['vitesse_x'] < 220:
            v['vitesse_x'] += 40
    if px.btn(px.KEY_LEFT):
        v['orientation'] = 1
        if v['vitesse_x'] > -220:
            v['vitesse_x'] -= 40
            


def coord_perso():
    v['x_perso'] += v['vitesse_x'] / 100
    v['y_perso'] += v['vitesse_y'] / 100
    
    if v['x_perso'] < 0:
        v['x_perso'] = 0
    elif v['x_perso'] > 246:
        v['x_perso'] = 246
        
    if v['y_perso'] < 0:
        v['y_perso'] = 0
    elif v['y_perso'] > 246: 
        v['y_perso'] = 246
    
def commencer():
    if px.frame_count < (15 * 30):
        v['commence_cycle'] = True
        v['x_perso'] = 112
        v['y_perso'] = 112
        v['projectiles_joueur'] = []
    elif px.frame_count == 15 * 30:
        v['commence_cycle'] = False     
        
def depl_boss():
    if px.frame_count < (15 * 30):
        v['depla_boss'][1] += 0.2
    if px.frame_count == 0:
        v['vie_boss'] = 200
    if v['vie_boss'] < 100:
        v['depla_boss'][2] += 0.02
        v['depla_boss'][1] =112 + 100*(math.sin(v['depla_boss'][2]))
    if v['vie_boss'] < 0:
        v['v'] = True
        
def projectiles_alterne():      
    endroits1 = [[230, 21 + i * 42] for i in range(6)]
    endroits2 = [[230, 0 + i * 42] for i in range(7)]
    
    if v["fase1_alterne"]:
        v['coord_projectiles_alterne'] = endroits1
        if (px.frame_count - v['marque_temps_alterne']) > v['alterne_cycle']:
            v['acce_alterne'] += 0.5
            v['coord_projectiles_alterne'] = endroits1
            for i in range(len(v['coord_projectiles_alterne'])):
                v['coord_projectiles_alterne'][i][0] = 250 - (v['acce_alterne'] - 5)**2
            for trident in v['coord_projectiles_alterne'][:]:
                if trident[0] < -25:
                    v['coord_projectiles_alterne'].remove(trident)
        else:
            v['gigue'] *= -1
            for trident in v['coord_projectiles_alterne']:
                trident[1] += v['gigue']
        
        if v['coord_projectiles_alterne'] == []:
            v["fase1_alterne"] = False
            v['acce_alterne'] = 0
            v['marque_temps_alterne'] = px.frame_count
            v['coord_projectiles_alterne'] = endroits2
            
    elif (px.frame_count - v['marque_temps_alterne']) > v['alterne_cycle']:
        v['acce_alterne'] += 0.5
        for i in range(len(v['coord_projectiles_alterne'])):
            v['coord_projectiles_alterne'][i][0] = 250 - (v['acce_alterne'] - 5)**2
        for trident in v['coord_projectiles_alterne'][:]:
                if trident[0] < -25:
                    v['coord_projectiles_alterne'].remove(trident)
                
        if v['coord_projectiles_alterne'] == []:
            v['acce_alterne'] = 0
            v['marque_temps_alterne'] = px.frame_count
            v['alterne_cycle'] -= 5
            if v['alterne_cycle'] > 0:
                v["fase1_alterne"] = True
            else:
                v['commence_cycle'] = False


def projectiles_sin():
    endroits1 = [[230, i * 42] for i in range(7)]
    
    if v['coord_projectiles_sin'] == []:
        v['coord_projectiles_sin'] = [p for p in endroits1]
        
    if v['commence_cycle']:
        v['acce_sin'] += 0.01
        for i in range(len(v['coord_projectiles_sin'])):
            v['coord_projectiles_sin'][i][1] = 50*(math.sin(5 * v['acce_sin'])) + i * 42
            v['coord_projectiles_sin'][i][0] = 230 - v['acce_sin'] * 300
            
        for trident in v['coord_projectiles_sin'][:]:
            if trident[0] < -25:
                v['coord_projectiles_sin'].remove(trident)
        
        if v['coord_projectiles_sin'] == []:
            v['commence_cycle'] = False
            v['acce_sin'] = 0

def projectiles_cos():
    endroits1 = [[230, 64] for i in range(2)]
    
    if v['coord_projectiles_cos'] == []:
        v['coord_projectiles_cos'] = [p for p in endroits1]
        
    if v['commence_cycle']:
        v['acce_cos'] += 0.01
        for i in range(len(v['coord_projectiles_cos'])):
            if i == 0:
                v['coord_projectiles_cos'][i][1] = 100*(math.sin(4 * v['acce_cos'] - math.pi)) + 112
            elif i == 1:
                v['coord_projectiles_cos'][i][1] = 100*(math.sin(4 * v['acce_cos'])) + 112
            v['coord_projectiles_cos'][i][0] = 230 - v['acce_cos'] * 220
        for trident in v['coord_projectiles_cos'][:]:
            if trident[0] < -25:
                v['coord_projectiles_cos'].remove(trident)
        
        if v['coord_projectiles_cos'] == []:
            v['commence_cycle'] = False
            v['acce_cos'] = 0
def projectiles_alterne_haut_bas():      
    endroits1 = [[21 + i * 42, 230] for i in range(6)]
    endroits2 = [[0 + i * 42, 230] for i in range(7)]
    
    if v["fase1_alterne"]:
        v['coord_projectiles_alterne'] = endroits1
        if (px.frame_count - v['marque_temps_alterne']) > v['alterne_cycle']:
            v['acce_alterne'] += 0.5
            v['coord_projectiles_alterne'] = endroits1
            for i in range(len(v['coord_projectiles_alterne'])):
                v['coord_projectiles_alterne'][i][1] = 250 - (v['acce_alterne'] - 5)**2 
            for trident in v['coord_projectiles_alterne'][:]:
                if trident[1] < -25:
                    v['coord_projectiles_alterne'].remove(trident)
        
        if v['coord_projectiles_alterne'] == []:
            v["fase1_alterne"] = False
            v['acce_alterne'] = 0
            v['marque_temps_alterne'] = px.frame_count
            v['coord_projectiles_alterne'] = endroits2
            
    elif (px.frame_count - v['marque_temps_alterne']) > v['alterne_cycle']:
        v['acce_alterne'] += 0.5
        for i in range(len(v['coord_projectiles_alterne'])):
            v['coord_projectiles_alterne'][i][1] = 250 - (v['acce_alterne'] - 5)**2
        for trident in v['coord_projectiles_alterne'][:]:
                if trident[1] < -25:
                    v['coord_projectiles_alterne'].remove(trident)
                
        if v['coord_projectiles_alterne'] == []:
            v['acce_alterne'] = 0
            v['marque_temps_alterne'] = px.frame_count
            v['alterne_cycle'] -= 8
            if v['alterne_cycle'] > 0:
                v["fase1_alterne"] = True
            else:
                v['commence_cycle'] = False

        
def creation_cycle_projectiles():
    if not v['commence_cycle']:
        v['a'] = randint(0, 3)
        v['rotation'] = 0
    
        if v['a'] == 0:
            v['commence_cycle'] = True
            v["fase1_alterne"] = True
            v['marque_temps_alterne'] = px.frame_count
            v['acce_alterne'] = 0
            v['alterne_cycle'] = 11

        if v['a'] == 1:
            v['commence_cycle'] = True
            v['acce_sin'] = 0

        if v['a'] == 2:
            v['commence_cycle'] = True
            v['acce_cos'] = 0
            
        if v['a'] == 3:
            v['commence_cycle'] = True
            v["fase1_alterne"] = True
            v['marque_temps_alterne'] = px.frame_count
            v['acce_alterne'] = 0
            v['alterne_cycle'] = 9
    
    if v['commence_cycle']:
        if v['a'] == 0:
            projectiles_alterne()
        if v['a'] == 1:
            projectiles_sin()
            v['rotation'] -= 1
        if v['a'] == 2:
            projectiles_cos()
            v['rotation'] -= 1
        if v['a'] == 3:
            projectiles_alterne_haut_bas()
            
def projectiles_joueur():
    if px.btn(px.KEY_SPACE) and ((px.frame_count - v['timer_joueur']) > 30):
        for i in range(2):
            v['projectiles_joueur'].append([v['x_perso'], v['y_perso'], v['orientation'], i])
        v['timer_joueur'] = px.frame_count
    for ballon in v['projectiles_joueur']:
        if ballon[3] == 0:
            orient = ballon[2]
            ballon[orient] += 4
        if ballon[3] != 0:
            orient = ballon[2]
            ballon[orient] -= 4
    for ballon in v['projectiles_joueur'][:]:
        if (ballon[0] < -25) or (ballon[0] > 300):
            v['projectiles_joueur'].remove(ballon)
        if (ballon[1] < -25) or (ballon[1] > 300):
            v['projectiles_joueur'].remove(ballon)
            
def colision():
    for i in range(2):
        for j in range(int(v['x_perso']), int(v['x_perso']) + 10):
            if (px.pget(j, v['y_perso'] + (i*11)) == 10) and ((px.frame_count - v['frame_buffer']) > 60):
                v["vie"]-=1
                v['frame_buffer'] = px.frame_count
                
        for j in range(int(v['y_perso']), int(v['y_perso']) + 10):
            if (px.pget(v['x_perso'] + (i*11), j) == 10) and ((px.frame_count - v['frame_buffer']) > 60):
                v["vie"]-=1
                v['frame_buffer'] = px.frame_count
                
def collision_projectile():
    for ballon in v['projectiles_joueur'][:]:
        if (ballon[0] > v['depla_boss'][0]) and (ballon[0] < v['depla_boss'][0] * 64) and (ballon[1] > v['depla_boss'][1]) and (ballon[1] < v['depla_boss'][1] * 64):
            v['vie_boss'] -= 4
            v['projectiles_joueur'].remove(ballon)
            
def spawn_bateau_ennemi():
    positions = [[112, 0, 1], [0, 112, 1], [112, 200, 1]]
    if v['vie_boss'] < 100:
        if px.frame_count % 120 == 119:
            v['bateau_ennemi'].append(positions[randint(0, 2)])
        
    for bateau in v['bateau_ennemi']:
        if bateau[1] == 0:
            if (bateau[0] == 10) or (bateau[0] == 230):
                bateau[2] *= -1
            bateau[0] += 1 * bateau[2]
            if (px.frame_count % 60) == 59:
                v['ballon_bateau'].append([bateau[0], bateau[1], 1, 1])
        if bateau[0] == 0:
            if (bateau[1] == 10) or (bateau[1] == 190):
                bateau[2] *= -1
            bateau[1] -= 1 * bateau[2]
            if (px.frame_count % 60) == 59:
                v['ballon_bateau'].append([bateau[0], bateau[1], 0, 1])
        if bateau[1] == 200:
            if (bateau[0] == 10) or (bateau[0] == 230):
                bateau[2] *= -1
            bateau[0] += 1 * bateau[2]
            if (px.frame_count % 60) == 59:
                v['ballon_bateau'].append([bateau[0], bateau[1], 1, -1])
        
    for ballon in v['projectiles_joueur'][:]:
        for bateau in v['bateau_ennemi'][:]:
            if (ballon[0] > bateau[0]) and (ballon[0] < bateau[0] + 12) and (ballon[1] > bateau[1]) and (ballon[1] < bateau[1] + 12):
                try:
                    v['bateau_ennemi'].remove(bateau)
                    v['projectiles_joueur'].remove(ballon)
                except ValueError:
                    pass
                
def projectiles_bateau():
    for ballon in v['ballon_bateau']:
        ballon[ballon[2]] += ballon[3]
    
    for ballon in v['ballon_bateau'][:]:
        if (ballon[0] < -25) or (ballon[0] > 300):
            v['ballon_bateau'].remove(ballon)
        if (ballon[1] < -25) or (ballon[1] > 300):
            v['ballon_bateau'].remove(ballon)
                
def death():
    if v["vie"]<=0:
        v["death"]=True
        
    if v['death']:
        if px.btn(px.KEY_R):
            v['vie'] = 5
            v['commence_cycle'] = False
            v['death'] = False
            v['vie_boss'] = 200
            v["depla_boss"] = [194, 80, 1]
            v['frame_buffer'] = px.frame_count
            v['bateau_ennemi'] = []
            v['ballon_bateau'] = []
            v['coord_projectiles_alterne'] = []
            v['coord_projectiles_sin'] = []
            v['coord_projectiles_cos'] = []

def update():
    
    commencer()
    
    deplacement_perso()
    
    coord_perso()
    
    creation_cycle_projectiles()
    
    colision()
    
    death()
    
    projectiles_joueur()
    
    collision_projectile()
    
    depl_boss()
    
    spawn_bateau_ennemi()
    
    projectiles_bateau()

def draw():
    px.cls(1)
#Joueur
    #px.rect(v['x_perso'], v['y_perso'], 10, 10, 7)
    px.blt(v['x_perso'], v['y_perso'], 0, 16, 0, 16, 16, 0, rotate=v['orientation'] * 90)
#Boss -> Poséidon
    #px.rect(v['depla_boss'][0], v['depla_boss'][1], 64, 64, 2)
    px.blt(v['depla_boss'][0], v['depla_boss'][1], 0, 0, 16, 64, 64, 0)
    
    px.text(10, 210, "POSEIDON", 7)
    px.rect(10, 220, v['vie_boss'], 10, 8)
    px.blt(10, 10, 0, 0, 80, v["vie"] * 16, 16, colkey=0)
    
    if px.frame_count < (7 * 30):
        px.text(64, 64, "Appuyez sur space pour tirer", 7)
    elif px.frame_count < (14 * 30):
        px.text(64, 64, "etes vous prets?", 7)
    elif px.frame_count < (15 * 30):
        px.text(64, 64, "Partez!", 7)
    
    for trident in v["coord_projectiles_alterne"]:
        if v['a'] == 3:
            px.blt(trident[0], trident[1], 0, 0, 0, 16, 16, colkey=0, scale=1.5)
        if v['a'] == 0:
            px.blt(trident[0], trident[1], 0, 0, 0, 16, 16, colkey=0, rotate=-90, scale=1.5)
    for trident in v["coord_projectiles_sin"]:
         px.blt(trident[0], trident[1], 0, 0, 0, 16, 16, colkey=0, rotate=v['rotation'], scale=1)
    for trident in v["coord_projectiles_cos"]:
        px.blt(trident[0], trident[1], 0, 0, 0, 16, 16, colkey=0, rotate=v['rotation'], scale=3)
        px.blt(230 - v['acce_cos'] * 220, 112, 0, 0, 0, 16, 16, colkey=0, rotate=-90, scale=3)
    for balle in v['projectiles_joueur']:
        px.rect(balle[0], balle[1], 5, 5, 11)
    for bateau in v['bateau_ennemi']:
        #px.rect(bateau[0], bateau[1], 10, 10, 2)
        px.blt(bateau[0], bateau[1], 0, 32, 0, 16, 16, 0)
    for ballon in v['ballon_bateau']: 
        px.rect(ballon[0], ballon[1], 2, 2, 10)
        
    px.rect(10, 220, v['vie_boss'], 20, 8)
    
    #   Pour montrer la vie faire dans pyxel editor une barre de vie et faire quelque chose similaire avec la vie du boss
    
    if v["death"]:
        px.cls(0)
        px.text(0, 124, "Ulysse, ulysse, je n'ai pas perturbe le temps pour rien", 7)
        px.text(0, 134, "tu DOIS vaincre Poseidon. appuie sur 'r' pour reessayer -Cronos", 7)
    if v["v"]:
        px.cls(7)
        px.text(124, 124, "Vous avez gagne", 0)
        if px.frame_count % 200 == 0:
            sys.exit(0)
            
        
    

px.run(update, draw)

