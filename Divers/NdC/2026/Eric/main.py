import pyxel
import random

GRID_SIZE = 14
BLOCK_SIZE = 28
HEIGHT_STEP = 3
CAM_X = 128
CAM_Y = 60
START_X = -1
START_Y = GRID_SIZE - 1
TILE_BORDER_COLOR = 0
TOWER_COST = 10
TOWER_FIX_COST = 8
GUARDIAN_FIX_COST = 30
BOSS_BASE_LIFE = 175
WAVE_LEVEL = ["","L'INVASION","ON ACCELERE","CHEMIN DES KAMIKAZES","METEORS","TONNERRE DE ZEUS", "TREMBLEMENT DE TERRE", "- TSUNAMI -"]

class ExplosionPixel:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.vx = random.uniform(-0.1, 0.1)
        self.vy = random.uniform(-0.1, 0.1)
        self.vz = random.uniform(0.05, 0.2)
        self.life = 20  
        self.color = random.choice([7, 10, 8]) 

    def update(self):
        self.x += self.vx; self.y += self.vy; self.z += self.vz
        self.vz -= 0.02; self.life -= 1

class Meteor:
    def __init__(self, target_tile):
        self.target = target_tile
        self.offset = 15 
        self.x = target_tile.x - self.offset
        self.y = target_tile.y - self.offset
        self.z = 60 # Altitude de départ
        self.speed = 1.2
        self.dead = False

    def update(self, app):
        # On réduit l'altitude
        self.z -= self.speed
        progression_step = self.speed * (self.offset / 60)
        self.x += progression_step
        self.y += progression_step
        # Collision
        if self.z <= self.target.h:
            self.dead = True
            self.x, self.y = self.target.x, self.target.y 
            self.target.h = -3 
            self.target.kind = "hole"
            app.towers = [t for t in app.towers if t.tile != self.target]
            pyxel.play(3, 3)
            # Tremblement
            app.shake_amount = 8
            for _ in range(20):
                app.particles.append(ExplosionPixel(self.x, self.y, self.target.h + 1))

class Tile:
    def __init__(self, x, y, h, kind):
        self.x = x; self.y = y; self.h = h; self.kind = kind
        self.original_kind = kind

class Bullet:
    def __init__(self, x, y, z, target, damage):
        self.x, self.y, self.z = x, y, z
        self.target = target
        self.damage = damage
        self.speed = 0.15
        self.dead = False
        pyxel.play(0, 0)

    def update(self, app):
        tx, ty = self.target.pos()
        tz = 1
        dx, dy, dz = tx - self.x, ty - self.y, tz - self.z
        dist = (dx**2 + dy**2 + dz**2)**0.5
        if dist < 0.3:
            self.target.hp -= self.damage
            app.floating_texts.append(FloatingText(self.target.pos()[0], self.target.pos()[1], 1.5, f"-{self.damage}", 7))
            self.dead = True
        else:
            self.x += (dx/dist) * self.speed
            self.y += (dy/dist) * self.speed
            self.z += (dz/dist) * self.speed + 0.02

class FloatingText:
    def __init__(self, x, y, z, text, color):
        self.x, self.y, self.z = x, y, z
        self.text = text
        self.color = color
        self.life = 40  
        self.vz = 0.1 

    def update(self):
        self.z += self.vz
        self.life -= 1

    def draw(self, app):
        sx, sy = app.iso(self.x, self.y, self.z)
        pyxel.text(sx + CAM_X + app.cam_x, sy + CAM_Y + app.cam_y, self.text, self.color)
    
class Enemy:
    def __init__(self, path, kind="normal"):
        self.path = path
        self.kind = kind
        self.i = 0
        self.t = 0
        if kind == "tank":
            self.max_hp = 16
            self.speed = 0.03
            self.reward = 5
        elif kind == "fast":
            self.max_hp = 5
            self.speed = 0.09
            self.reward = 5
        elif kind == "kamikaze":
            self.max_hp = 6       
            self.speed = 0.060     
            self.reward = 8       
        elif kind == "boss":
            self.max_hp = 150
            self.speed = 0.050
            self.reward = 50
        else: # normal
            self.max_hp = 10
            self.speed = 0.05
            self.reward = 5
        self.hp = self.max_hp
        self.dead = False
        self.cooldown = 0

    def update(self, towers, enemy_bullets, app=None):
        if self.i < len(self.path) - 1:
            self.t += self.speed
            if self.t >= 1:
                self.t = 0
                self.i += 1
        if self.kind == "kamikaze":
            ex, ey = self.pos()
            for t in towers:
                # Proche d'un tour
                if abs(t.tile.x - ex) <= 1.2 and abs(t.tile.y - ey) <= 1.2:
                    self.explode(app)
                    break
        else:
            if self.cooldown > 0:
                self.cooldown -= 1
            else:
                for t in towers:
                    ex, ey = self.pos()
                    if ((t.tile.x - ex)**2 + (t.tile.y - ey)**2) < 3**2:
                        enemy_bullets.append(EnemyBullet(ex, ey, 1, t))
                        self.cooldown = 60
                        break

    def explode(self, app):
        if self.dead:
            return
        self.dead = True
        ex, ey = self.pos()
        pyxel.play(3, 3) # Explosion
        for _ in range(25): 
            p = ExplosionPixel(ex + random.uniform(-0.2, 0.2), ey + random.uniform(-0.2, 0.2), 1)
            p.vx *= 2.5
            p.vy *= 2.5
            p.color = random.choice([8, 9, 10]) # Rouge, Orange, Jaune
            app.particles.append(p)
        # Explosion sur 9 cases    
        center_x = round(ex)
        center_y = round(ey)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                target_x = center_x + dx
                target_y = center_y + dy
                for _ in range(10): # particules de l'explosion des 9 cases
                    p = ExplosionPixel(
                        target_x + random.uniform(-0.3, 0.3), 
                        target_y + random.uniform(-0.3, 0.3), 
                        1
                    )
                    # Effet leger 
                    p.vx = random.uniform(-0.15, 0.15)
                    p.vy = random.uniform(-0.15, 0.15)
                    p.color = random.choice([9, 10, 7])
                    app.particles.append(p)
        for t in app.towers:
            if abs(t.tile.x - ex) <= 1.5 and abs(t.tile.y - ey) <= 1.5:
                t.hp -= 6 # Gros dégâts aux tours aux alentours
                app.floating_texts.append(FloatingText(t.tile.x, t.tile.y, t.tile.h + 2, "-6", 8))
                if t.hp <= 0:
                    t.dead = True
                    for _ in range(15):
                        app.particles.append(ExplosionPixel(t.tile.x, t.tile.y, t.tile.h + 1))
                    t.tile.kind = "hole"
                    t.tile.h = -3
                    pyxel.play(2, 3)

    def pos(self):
        if self.i >= len(self.path) - 1:
            return self.path[-1]
        x1, y1 = self.path[self.i]
        x2, y2 = self.path[self.i + 1]
        return x1 + (x2 - x1) * self.t, y1 + (y2 - y1) * self.t

class Tower:
    def __init__(self, tile, kind="basic", is_guardian=False):
        self.tile = tile
        self.kind = kind
        self.cooldown = 0
        self.is_guardian = is_guardian
        if is_guardian:
            self.range = 2.5
            self.cooldown_max = 20
            self.damage = 2
            self.max_hp = 20
        elif kind == "sniper":
            self.range = 3.5
            self.cooldown_max = 40
            self.damage = 3
            self.max_hp = 8
        elif kind == "rapid":
            self.range = 1.5
            self.cooldown_max = 8
            self.damage = 1
            self.max_hp = 8
        else:  # basic
            self.range = 2
            self.cooldown_max = 15
            self.damage = 1
            self.max_hp = 10
        self.hp = self.max_hp
        self.dead = False

    def update(self, enemies, bullets):
        if self.cooldown > 0:
            self.cooldown -= 1
            return
        # Bonus hauteur
        bonus_altura = max(0, (self.tile.h - 1) * 0.5)
        alcance_total = self.range + bonus_altura
        for e in enemies:
            ex, ey = e.pos()
            if ((self.tile.x - ex)**2 + (self.tile.y - ey)**2) < alcance_total**2:
                bullets.append(Bullet(self.tile.x, self.tile.y, self.tile.h + 2, e, self.damage))
                self.cooldown = self.cooldown_max
                break

class EnemyBullet:
    def __init__(self, x, y, z, target):
        self.x, self.y, self.z = x, y, z
        self.target = target; self.speed = 0.1; self.dead = False
        pyxel.play(1, 1)

    def update(self, app): 
        tx, ty = self.target.tile.x, self.target.tile.y
        tz = self.target.tile.h + 2
        dx, dy, dz = tx - self.x, ty - self.y, tz - self.z
        dist = (dx**2 + dy**2 + dz**2)**0.5
        if dist < 0.2:
            self.target.hp -= 1
            app.floating_texts.append(FloatingText(self.target.tile.x, self.target.tile.y, self.target.tile.h + 2, "-1", 10))
            if self.target.hp <= 0:
                self.target.dead = True
                for _ in range(15):
                    app.particles.append(ExplosionPixel(tx, ty, self.target.tile.h + 1))
                # Explosion tour + trou
                self.target.tile.kind = "hole"
                self.target.tile.h = -3
                pyxel.play(2, 3)
            self.dead = True
        else:
            self.x += (dx/dist) * self.speed
            self.y += (dy/dist) * self.speed
            self.z += (dz/dist) * self.speed

class App:
    def __init__(self):
        pyxel.init(256, 256, title="NdC Tower Defense")
        pyxel.fullscreen(True)
        pyxel.colors[8] = 0xE71818 # Rouge
        self.game_started = False
        self.setup_sounds()
        self.sound_enabled = True
        self.high_scores = [0, 0, 0]
        self.game_over = False
        self.two_path = False
        self.wave_two_ways = 3 
        self.wave_meteors = 4 
        self.wave_rain = 5
        self.wave_fog = 3
        self.wave_kamikaze = 3
        self.wave_boss = 9
        self.reset_game()
        self.game_frame_count = 0
        self.first_rain_delay = 30 * 30  # 30s em frames
        self.tower_types = ["basic", "rapid", "sniper"]
        self.next_tower_kind = random.choice(self.tower_types)
        self.wave_timer = 0
        self.wave_interval = 15 * 30 # Une nouvelle vague d'ennemis toutes les 30s
        self.tsunami_alert_timer = 0
        self.tsunami_receding = False
        self.tsunami_water_line = 0
        self.tsunami_speed_counter = 0
        self.next_tsunami_wave = 7
        self.tsunami_active = False
        # Brume - Bruit de Perlin
        self.fog_time = 0.0
        self.fog_opacity = 0.0          # Opacité
        self.fog_target_opacity = 0.0   # Opacité 0.0 = soleil / 1.0 = brouillard)
        self.fog_cooldown = 400         # Temps entre les brumes
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.cam_x = 0; self.cam_y = 0
        self.money = 20; self.score = 0
        self.grid = []; self.enemies = []; self.enemy_bullets = []
        self.towers = []; self.bullets = []; self.particles = []; self.meteors = []
        self.hover_tile = None
        self.wave = 1; self.wave_size = 4; self.spawned = 0; self.spawn_timer = 0
        self.wave_started = False
        self.wave_timer = 0
        self.tsunami_active = False
        self.tsunami_receding = False
        self.tsunami_water_line = 0
        self.tsunami_speed_counter = 0
        self.next_tsunami_wave = 7
        self.game_over = False
        self.is_raining = False
        self.rain_timer = 0
        self.flash_timer = 0
        self.strike_target = None
        self.shake_amount = 0
        self.floating_texts = []
        self.two_path = False
        self.tsunami_active = False
        self.tsunami_receding = False
        self.tsunami_alert_timer = 0
        self.apply_rain_palette(False)
        
        # Init brume
        self.fog_opacity = 0.0
        self.fog_target_opacity = 0.0
        self.fog_cooldown = 400
        self.generate()

    def setup_sounds(self):
        # Son de canon
        pyxel.sounds[0].set("c1c0", "p", "7", "f", 10)      
        pyxel.sounds[1].set("c2c1", "n", "5", "f", 7)      
        pyxel.sounds[2].set("g2g1g0", "n", "764", "f", 10) 
        pyxel.sounds[3].set("c1c0c0g0", "n", "77654", "f", 25)
        # éclair
        pyxel.sounds[4].set("f0f0f1f0", "n", "7765", "f", 30)
        pyxel.sounds[5].set("c0", "n", "2", "f", 60)
    
    def draw_hud_tower(self, px, py, tile, kind, is_guardian):
        screen_x = px + self.cam_x
        screen_y = py 
        self.draw_tower_direct(screen_x, screen_y, kind, is_guardian)

    def draw_tower_direct(self, sx, sy, kind, is_guardian):
        if is_guardian:
            colors, steps = [13, 13, 6, 7], 8
        elif kind == "sniper":
            colors, steps = [2, 8, 14, 7], 7
        elif kind == "rapid":
            colors, steps = [1, 5, 6, 12], 3
        else: # basic
            colors, steps = [4, 9, 10, 7], 5
        for i in range(steps):
            h_offset = i * 2
            curr_y = sy - h_offset - 4
            c = colors[i % len(colors)]
            w = BLOCK_SIZE // 6 if kind == "sniper" else BLOCK_SIZE // 4
            pyxel.tri(sx, curr_y, sx + w, curr_y + w//2, sx, curr_y + w, c)
            pyxel.tri(sx, curr_y, sx, curr_y + w, sx - w, curr_y + w//2, c)

    def draw_hud_enemy(self, sx, sy, kind):
        sx += self.cam_x 
        if kind == "tank":
            body_c, dark_c, size = 13, 5, 5
        elif kind == "fast":
            body_c, dark_c, size = 11, 3, 3
        elif kind == "kamikaze":
            body_c, dark_c, size = 5, 0, 4
        elif kind == "boss":
            body_c, dark_c, size = 11, 1, 9   # Violet et Bleu nuit, taille PRESQUE DOUBLE !
        else:
            body_c, dark_c, size = 8, 2, 4
        top = [(sx, sy), (sx + size, sy + size//2), (sx, sy + size), (sx - size, sy + size//2)]
        pyxel.tri(*top[0], *top[1], *top[2], body_c)
        pyxel.tri(*top[0], *top[2], *top[3], body_c)
        pyxel.tri(top[3][0], top[3][1], top[2][0], top[2][1], top[2][0], top[2][1] + size, dark_c)
        pyxel.tri(top[3][0], top[3][1], top[2][0], top[2][1] + size, top[3][0], top[3][1] + size, dark_c)
        pyxel.tri(top[1][0], top[1][1], top[2][0], top[2][1], top[2][0], top[2][1] + size, 1)
        pyxel.tri(top[1][0], top[1][1], top[2][0], top[2][1] + size, top[1][0], top[1][1] + size, 1)
        
    def draw_minimap(self):
        map_size = GRID_SIZE
        scale = 3  
        off_x = 208 
        off_y = 14  
        pyxel.rect(off_x - 1, off_y - 1, map_size * scale + 2, map_size * scale + 2, 0)
        pyxel.rectb(off_x - 1, off_y - 1, map_size * scale + 2, map_size * scale + 2, 7)
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                tile = self.grid[y][x]
                # Coordonnées = 90° à droite
                rot_x = (map_size - 1) - y
                rot_y = x
                color = 3 
                if tile.kind == "path" or tile.kind == "bridge": color = 10
                elif tile.kind == "water": color = 6
                elif tile.kind == "wall" or tile.kind == "exit": color = 8
                elif tile.kind == "hole": color = 0
                pyxel.rect(off_x + rot_x * scale, off_y + rot_y * scale, scale, scale, color)
        # Tours
        for t in self.towers:
            rot_tx = (map_size - 1) - t.tile.y
            rot_ty = t.tile.x
            pyxel.pset(off_x + rot_tx * scale + 1, off_y + rot_ty * scale + 1, 7)
        # Ennemis
        for e in self.enemies:
            ex, ey = e.pos()
            rot_ex = (map_size - 1) - ey
            rot_ey = ex
            pyxel.pset(off_x + int(rot_ex * scale), off_y + int(rot_ey * scale), 8)	
    
    def next_wave(self):
        if self.wave == self.next_tsunami_wave and self.tsunami_active:
            self.end_tsunami_flood()
        self.wave += 1
        self.wave_size += 1
        self.spawned = 0
        self.wave_timer = 0
        # Bonus argent pour fin de vague = +10
        #self.money += 10
        # Init vague 6 et 7 (pré et tsunami)
        if self.wave == (self.next_tsunami_wave - 1):
            self.tsunami_alert_timer = 0
        elif self.wave == self.next_tsunami_wave:
            self.start_tsunami_flood()
        if self.wave == self.wave_two_ways:
            self.generate()
            
    def start_tsunami_flood(self):
        self.tsunami_active = True
        self.tsunami_water_line = 0 
        self.tsunami_speed_counter = 0
     
    def end_tsunami_flood(self):
        self.tsunami_active = False
        self.tsunami_receding = True 
        self.tsunami_water_line = 0 
        self.tsunami_speed_counter = 0
        # Prochain Tsunami dans 4 ou plus tours
        self.next_tsunami_wave = self.wave + 4 + random.randint(0, 2)
        
    def apply_rain_palette(self, active):
        if active:
            # Vert clair
            pyxel.colors[11] = 0x8EAB9C
            # Verde Fonncé
            pyxel.colors[3]  = 0x56837E
            # Jaune
            pyxel.colors[10] = 0xBEA88E
            # Orange
            pyxel.colors[9]  = 0xA07A6D
            # ROse
            pyxel.colors[8]  = 0x8B4B71
            # Bleu clair
            pyxel.colors[6]  = 0xB2BFCF
            # Marron
            pyxel.colors[4]  = 0x725B62
        else:
            # Retour normal
            pyxel.colors[11] = 0x70C6A9
            pyxel.colors[3]  = 0x19959C
            pyxel.colors[10] = 0xE9C35B
            pyxel.colors[9]  = 0xD38441
            pyxel.colors[8]  = 0xE71818
            pyxel.colors[6]  = 0xA9C1FF
            pyxel.colors[4]  = 0x8B4852
        
    def update_high_scores(self):
        if self.score not in self.high_scores:
            self.high_scores.append(self.score)
            self.high_scores.sort(reverse=True)
            self.high_scores = self.high_scores[:3]

    def generate(self):
        if self.two_path:
            return
        # Chemin 1
        def create_path(sx, sy, avoid_towers=False):
            p = [(sx, sy)]
            curr_x, curr_y = sx, sy
            tower_coords = {(t.tile.x, t.tile.y) for t in self.towers} if avoid_towers else set()
            # anti freeze
            fail_safe = 0 
            while not (curr_x >= GRID_SIZE - 2 and curr_y <= 1) and fail_safe < 200:
                fail_safe += 1
                direction = random.choice(["right", "up"])
                next_x, next_y = curr_x, curr_y
                length = random.randint(2, 4)
                valid_stretch = True
                temp_coords = []
                # Evite les tours / trous
                for _ in range(length):
                    if direction == "right" and next_x < GRID_SIZE - 2: 
                        next_x += 1
                    elif direction == "up" and next_y > 1: 
                        next_y -= 1
                    if (next_x, next_y) in tower_coords:
                        valid_stretch = False
                        break
                    # 1er chemin, pas de trou,
                    # deuxieme cheminm trou = pont
                    #if self.grid and self.grid[next_y][next_x] and self.grid[next_y][next_x].kind == "hole":
                    #    valid_stretch = False
                    #    break
                    if (next_x, next_y) not in p:
                        temp_coords.append((next_x, next_y))
                # Tout ok, on valide
                if valid_stretch and temp_coords:
                    p.extend(temp_coords)
                    curr_x, curr_y = next_x, next_y
            return p
        
        # Création du terrain avec la 1ère route
        if self.wave < self.wave_two_ways:
            self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
            # Rivière
            river_x = GRID_SIZE // 2; self.river_path = []
            for y in range(GRID_SIZE):
                self.river_path.append((river_x, y))
                if random.random() < 0.4:
                    river_x += random.choice([-1, 1])
                    river_x = max(2, min(GRID_SIZE - 3, river_x))
            # Chemin Principal
            start_x1 = pyxel.rndi(5, GRID_SIZE // 3)
            self.path1 = create_path(start_x1, GRID_SIZE - 1, avoid_towers=False)
            self.all_paths = [self.path1]
            # Construction de la carte
            for gy in range(GRID_SIZE):
                for gx in range(GRID_SIZE):
                    dist = min(abs(gx - rx) for rx, ry in self.river_path if ry == gy)
                    if (gx, gy) in self.river_path: 
                        h, kind = 0, "water"
                    else:
                        h = 1 if dist == 1 else random.choice([1, 2])
                        kind = "grass"
                    if (gx, gy) in set(self.path1): 
                        h, kind = 2, "path"
                    self.grid[gy][gx] = Tile(gx, gy, h, kind)
            # Ponts
            for (px, py) in set(self.path1):
                for (rx, ry) in self.river_path:
                    if px == rx and py == ry:
                        t = self.grid[py][px]
                        t.bridge, t.kind, t.h = True, "bridge", 2
            # Sortie
            end_x, end_y = self.path1[-1] 
            self.grid[end_y - 1][end_x].kind = "exit"
            self.grid[end_y - 1][end_x].h = 4
            # Gardiens
            guardian_positions = [(end_x - 1, end_y - 1), (end_x + 1, end_y - 1)]
            for gx, gy in guardian_positions:
                if 0 <= gx < GRID_SIZE and 0 <= gy < GRID_SIZE:
                    tile = self.grid[gy][gx]; tile.kind = "wall"; tile.h = 4
                    if not any(t.is_guardian and t.tile.x == gx and t.tile.y == gy for t in self.towers):
                        self.towers.append(Tower(tile, is_guardian=True))

        # idem chemiin 2
        else:
            self.two_path = True
            start_y2 = pyxel.rndi(GRID_SIZE // 2, GRID_SIZE - 3)
            path2 = create_path(0, start_y2, avoid_towers=False)
            self.all_paths = [self.path1, path2] 
            for (gx, gy) in set(path2):
                tile = self.grid[gy][gx]
                tile.h = 2
                if (gx, gy) in self.river_path:
                    tile.bridge = True
                    tile.kind = "bridge"
                elif tile.kind == "hole":
                    tile.kind = "bridge"
                else:
                    tile.kind = "path"
                
    def update(self):
        if not self.game_started:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.game_started = True
            return
            
        if self.game_started:
        # Caméra
            if pyxel.btn(pyxel.KEY_LEFT): self.cam_x += 4
            if pyxel.btn(pyxel.KEY_RIGHT): self.cam_x -= 4
            edge_margin = 10
            scroll_speed = 4
            if pyxel.mouse_x < edge_margin:
                self.cam_x += scroll_speed
            elif pyxel.mouse_x > pyxel.width - edge_margin:
                self.cam_x -= scroll_speed
                
                
        self.game_frame_count += 1 
        # Brume - Bruit de perlin (Merci internet!)
        if self.wave >= self.wave_fog:
            self.fog_time += 0.002  
            # Transition suave vers l'opacité cible (Fade in / Fade out)
            if self.fog_opacity < self.fog_target_opacity:
                self.fog_opacity = min(self.fog_opacity + 0.003, self.fog_target_opacity)
            elif self.fog_opacity > self.fog_target_opacity:
                self.fog_opacity = max(self.fog_opacity - 0.003, self.fog_target_opacity)
            # Changement d'état
            self.fog_cooldown -= 1
            if self.fog_cooldown <= 0:
                self.fog_cooldown = random.randint(200, 450)
                if self.fog_target_opacity == 0.0:
                    if random.random() < 0.4:
                        self.fog_target_opacity = random.choice([0.7, 0.9])
                else:
                    if random.random() < 0.7:
                        self.fog_target_opacity = 0.0
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R) or pyxel.btnp(pyxel.KEY_SPACE):
                self.reset_game()
                return
            return

        guardians_alive = any(t.is_guardian for t in self.towers)
        if not guardians_alive:
            self.game_over = True
            self.update_high_scores()
            pyxel.play(3, 3)
            return
        
        
        # Réparation   
        if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT) and self.hover_tile:
            for t in self.towers:
                if t.tile == self.hover_tile:
                    if self.money >= TOWER_FIX_COST and not t.is_guardian:
                        t.max_hp += 5
                        t.hp = t.max_hp
                        t.range += 0.5
                        self.money -= TOWER_FIX_COST
                    if self.money >= GUARDIAN_FIX_COST and t.is_guardian:
                        t.max_hp += 5
                        t.hp = t.max_hp
                        t.range += 0.5
                        self.money -= GUARDIAN_FIX_COST
                        
        # Limites da Câmera (Opcional, para não fugir do mapa)
        self.cam_x = max(-70, min(70, self.cam_x))
        
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        best, best_d = None, 50
        for row in self.grid:
            for tile in row:
                sx, sy = self.iso_center(tile)
                d = (sx - mx)**2 + (sy - my)**2
                if d < best_d: best_d, best = d, tile
        self.hover_tile = best

        if self.shake_amount > 0:
            self.shake_amount -= 1
        # Alerte Tsunami
        if self.wave == (self.next_tsunami_wave - 1):
            if getattr(self, 'tsunami_alert_timer', 0) == 0 and self.wave_timer == 1:
                self.tsunami_alert_timer = 180  
                pyxel.play(3, 4)
        # Tremblement de terre
        if getattr(self, 'tsunami_alert_timer', 0) > 0:
            self.tsunami_alert_timer -= 1
            t = 180 - self.tsunami_alert_timer
            if 1 <= t <= 60:
                self.shake_amount = max(self.shake_amount, 5)
            # Pause 2seg
            elif 121 <= t <= 180:
                self.shake_amount = max(self.shake_amount, 6)
        # Init tsunami
        if self.wave == self.next_tsunami_wave and not self.tsunami_active and not getattr(self, 'tsunami_receding', False) and self.tsunami_water_line == 0:
            self.start_tsunami_flood()

        if self.wave % self.wave_boss == 0:
            self.wave_size = 1  # Un seul Boss !
        elif self.wave == 1:
            self.wave_size = 6
        else:
            self.wave_size = 6 + (self.wave - 1)

        # BOSS
        is_wave_boss = (self.wave % self.wave_boss == 0)
        # Boss uniquement quand tous les ennemis sont mort
        autorisation_spawn_boss = not is_wave_boss or (is_wave_boss and len(self.enemies) == 0)
        self.spawn_timer += 1
        if self.spawned < self.wave_size and self.spawn_timer > 60 and autorisation_spawn_boss:
            self.spawn_timer = 0
            if is_wave_boss:
                kind = "boss"
            elif self.wave >= self.wave_kamikaze:
                kind = random.choices(
                    ["normal", "fast", "tank", "kamikaze"], 
                    weights=[30, 30, 25, 15], 
                    k=1
                )[0]
            else:
                kind = random.choice(["normal", "fast", "tank"])
            
            chosen_path = random.choice(self.all_paths)
            enemy = Enemy(chosen_path, kind)
            if kind == "boss":
                enemy.max_hp = BOSS_BASE_LIFE + (self.wave // self.wave_boss) * 100
                enemy.hp = enemy.max_hp
                enemy.speed = 0.02
                enemy.reward = 50
            else:
                enemy.max_hp += self.wave // 2
                enemy.hp = enemy.max_hp
                enemy.speed += self.wave * 0.001
            self.enemies.append(enemy)
            self.spawned += 1

        # transition des vagues
        self.wave_timer += 1
        boss_alive = any(e.kind == "boss" for e in self.enemies)
        if self.wave == 1:
            # Vague 1 change seulement quand tout le monde meurt
            condition_suivante = (self.spawned >= self.wave_size and len(self.enemies) == 0)
        elif is_wave_boss:
            # Vague du Boss change seulement quand il meurt 
            condition_suivante = (self.spawned >= self.wave_size and not boss_alive)
        else:
            # Vagues normales changent au bout du temps imparti (15 secondes)
            condition_suivante = (self.wave_timer >= self.wave_interval)
        if condition_suivante:
            self.next_wave()

        # Météores
        if self.wave >= self.wave_meteors:
            if pyxel.frame_count % 300 == 0:
                valid = [t for row in self.grid for t in row if t.kind not in ["path", "water", "bridge", "exit", "wall", "hole"]]
                if valid: 
                    self.meteors.append(Meteor(random.choice(valid)))
        # Pluie
        if self.wave >= self.wave_rain:
            if not self.is_raining:
                if random.random() < 0.002: 
                    self.is_raining = True
                    self.rain_timer = random.randint(400, 800)
            
        for m in self.meteors: m.update(self)
        self.meteors = [m for m in self.meteors if not m.dead]

        # Tsunami
        if self.tsunami_active and self.tsunami_water_line < GRID_SIZE:
            self.tsunami_speed_counter += 1
            if self.tsunami_speed_counter >= 5:
                self.tsunami_speed_counter = 0
                y = self.tsunami_water_line
                for x in range(GRID_SIZE):
                    tile = self.grid[y][x]
                    if tile.original_kind == "grass" and tile.h == 1:
                        for t in self.towers:
                            if t.tile == tile and not t.is_guardian:
                                t.dead = True
                                for _ in range(15):
                                    self.particles.append(ExplosionPixel(tile.x, tile.y, tile.h + 1))
                                pyxel.play(2, 3)
                        if tile.kind != "hole":
                            tile.kind = "water"
                self.tsunami_water_line += 1
        # Fin du Tsunami
        if getattr(self, 'tsunami_receding', False) and self.tsunami_water_line < GRID_SIZE:
            self.tsunami_speed_counter += 1
            if self.tsunami_speed_counter >= 5:
                self.tsunami_speed_counter = 0
                y = (GRID_SIZE - 1) - self.tsunami_water_line
                for x in range(GRID_SIZE):
                    tile = self.grid[y][x]
                    if tile.original_kind == "grass" and tile.h == 1 and tile.kind == "water":
                        tile.kind = "grass"
                self.tsunami_water_line += 1
                if self.tsunami_water_line >= GRID_SIZE:
                    self.tsunami_receding = False
        
        for e in self.enemies:
            e.update(self.towers, self.enemy_bullets, self)
            if e.hp <= 0:
                if e.kind == "kamikaze":
                    # Si tué par une tour, il explose
                    e.explode(self)
                    self.money += e.reward
                    self.score += 150 # Bonus Kamikaze
                else:
                    e.dead = True
                    self.money += e.reward
                    self.score += 100
                    pyxel.play(2, 2)
                    ex, ey = e.pos()
                    for _ in range(12): 
                        self.particles.append(ExplosionPixel(ex, ey, 1))
        self.enemies = [e for e in self.enemies if not e.dead]
        
        for t in self.towers:
            if t.tile.kind == "path":
                t.dead = True
                tx, ty = t.tile.x, t.tile.y
                pyxel.play(2, 3)
                for _ in range(15):
                    self.particles.append(ExplosionPixel(tx, ty, t.tile.h + 1))
            t.update(self.enemies, self.bullets)
        self.towers = [t for t in self.towers if not t.dead]
        
        for b in self.bullets:
            b.update(self)
        self.bullets = [b for b in self.bullets if not b.dead]
        
        for eb in self.enemy_bullets:
            eb.update(self)
        self.enemy_bullets = [eb for eb in self.enemy_bullets if not eb.dead]
        
        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.life > 0]
        
        for ft in self.floating_texts:
            ft.update()
        self.floating_texts = [ft for ft in self.floating_texts if ft.life > 0]
        
        if self.is_raining:
            self.rain_timer -= 1
            self.apply_rain_palette(True) # Change les couleurs
            # Déclenchement aléatoire d'un éclair pendant la pluie
            if random.random() < 0.009: 
                # On liste toutes les cibles possibles (tours et ennemis)
                potential_targets = self.towers + self.enemies
                if potential_targets:
                    self.flash_timer = 4
                    self.strike_target = random.choice(potential_targets)
                    pyxel.play(3, 2)
                    # Tours
                    if isinstance(self.strike_target, Tower):
                        self.strike_target.hp -= 2
                        if self.strike_target.hp <= 0:
                            self.strike_target.dead = True
                            tx, ty = self.strike_target.tile.x, self.strike_target.tile.y
                            for _ in range(15):
                                self.particles.append(ExplosionPixel(tx, ty, self.strike_target.tile.h + 1))
                    # Ennemi
                    elif isinstance(self.strike_target, Enemy):
                        self.strike_target.hp -= 4
                        if self.strike_target.hp <= 0:
                            self.strike_target.dead = True
                            self.money += self.strike_target.reward
                            self.score += 100
                            ex, ey = self.strike_target.pos()
                            for _ in range(15):
                                self.particles.append(ExplosionPixel(ex, ey, 1))
            if self.rain_timer <= 0:
                self.is_raining = False
                self.apply_rain_palette(False)
                
        # Place une tour
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.hover_tile:
            t = self.hover_tile
            if t.kind not in ["path", "water", "bridge", "wall", "exit", "hole"]:
                if self.money >= TOWER_COST and not any(tw.tile == t for tw in self.towers):
                    self.towers.append(Tower(t, kind=self.next_tower_kind))
                    self.money -= TOWER_COST
                    self.next_tower_kind = random.choice(self.tower_types)
                        
    def iso(self, x, y, h):
        sx = (x - y) * (BLOCK_SIZE // 2)
        sy = (x + y) * (BLOCK_SIZE // 4) - h * HEIGHT_STEP
        return sx, sy

    def iso_center(self, tile):
        sx, sy = self.iso(tile.x, tile.y, tile.h)
        return sx + CAM_X + self.cam_x, sy + CAM_Y + self.cam_y + BLOCK_SIZE // 4

    def draw_block(self, tile):
        sx, sy = self.iso(tile.x, tile.y, tile.h)
        sx += CAM_X + self.cam_x; sy += CAM_Y + self.cam_y
        top = [(sx, sy), (sx + BLOCK_SIZE//2, sy + BLOCK_SIZE//4), (sx, sy + BLOCK_SIZE//2), (sx - BLOCK_SIZE//2, sy + BLOCK_SIZE//4)]
        
        if tile.kind == "grass": top_c, left_c, right_c = (11, 3, 1) if tile.h < 2 else (3, 3, 1)
        elif tile.kind == "path": top_c, left_c, right_c = 10, 9, 4
        elif tile.kind == "water": top_c, left_c, right_c = 6, 5, 1
        elif tile.kind == "bridge": top_c, left_c, right_c = 4, 9, 2
        elif tile.kind == "wall": top_c, left_c, right_c = 13, 5, 1
        elif tile.kind == "exit": top_c, left_c, right_c = 8, 2, 2
        elif tile.kind == "hole": top_c, left_c, right_c = 0, 0, 0
        
        pyxel.tri(*top[0], *top[1], *top[2], top_c)
        pyxel.tri(*top[0], *top[2], *top[3], top_c)
        h_val = max(tile.h, 1) * HEIGHT_STEP
        if tile.kind == "hole": h_val = 1 
        pyxel.tri(top[3][0], top[3][1], top[2][0], top[2][1], top[2][0], top[2][1]+h_val, left_c)
        pyxel.tri(top[3][0], top[3][1], top[2][0], top[2][1]+h_val, top[3][0], top[3][1]+h_val, left_c)
        pyxel.tri(top[1][0], top[1][1], top[2][0], top[2][1], top[2][0], top[2][1]+h_val, right_c)
        pyxel.tri(top[1][0], top[1][1], top[2][0], top[2][1]+h_val, top[1][0], top[1][1]+h_val, right_c)
        for i in range(4): pyxel.line(*top[i], *top[(i+1)%4], TILE_BORDER_COLOR)
    
    def text_pos(self, t):
        char_s = 4
        txt_p = pyxel.width // 2 - (len(t) * char_s) // 2
        return txt_p
    
    def draw(self):
        if self.shake_amount > 0:
            shake_x = random.randint(-self.shake_amount, self.shake_amount)
            shake_y = random.randint(-self.shake_amount, self.shake_amount)
            pyxel.camera(shake_x, shake_y)
        else:
            pyxel.camera(0, 0)

        pyxel.cls(0)
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if self.grid and y < len(self.grid) and x < len(self.grid[y]) and self.grid[y][x] is not None:
                    self.draw_block(self.grid[y][x])
        
        # Présentation
        if not self.game_started:
            msg1 = "TOWER DEFENSE"
            msg2 = "PROTEGEZ VOS GARDIENS DE L'ATTAQUE ENNEMIE"
            msg3 = "FAITES ATTENTION A VOTRE ARGENT"
            msg4 = "ET NE FAITES PAS CONFIANCE A LA NATURE"
            msg5 = "SURVIVRE N'EST PAS UNE OPTION"
            msg6 = "BOUTON GAUCHE DE LA SOURIS POUR PLACER VOS TOURS ($10)"
            msg7 = "BOUTON DROIT DE LA SOURIS POUR REPARER VOS TOURS ($10)"
            msg8 = "DEPLACAMENT DE LA CARTE AVES LA SOURIS"
            msg9 = "OU LES FLECHES GAUCHE/DROITE"
            msg10 = "PRESSEZ [ESPACE] POUR COMMENCER"
            msg_max_size = self.text_pos(msg7)
            margin = 26
            msg_x = pyxel.width // 2 - (msg_max_size * 9)// 2 -  margin
            msg_w = msg_max_size * 9 + 2 * margin
            msg_y = pyxel.height // 3  - 1.5 * margin
            msg_h = 146
            pyxel.line(msg_x + 1 , msg_y + msg_h, msg_x + msg_w, msg_y + msg_h, 1)
            pyxel.line(msg_x + msg_w , msg_y + 1, msg_x + msg_w, msg_y + msg_h , 1)
            pyxel.rect(msg_x, msg_y, msg_w, msg_h, 0)
            pyxel.rectb(msg_x, msg_y, msg_w, msg_h, 9)
            pyxel.text(self.text_pos(msg1) +1 , msg_y + 12, msg1, 1)
            pyxel.text(self.text_pos(msg1),msg_y + 11, msg1, 8)
            pyxel.text(self.text_pos(msg2) + 1 , msg_y + 30, msg2, 7)
            pyxel.text(self.text_pos(msg3), msg_y + 38, msg3, 10)
            pyxel.text(self.text_pos(msg4), msg_y + 46, msg4, 11)
            pyxel.text(self.text_pos(msg5), msg_y + 58, msg5, 8)
            pyxel.text(self.text_pos(msg6), msg_y + 80, msg6, 5)
            pyxel.text(self.text_pos(msg7), msg_y + 88, msg7, 5)
            pyxel.text(self.text_pos(msg8), msg_y + 100, msg8, 5)
            pyxel.text(self.text_pos(msg9), msg_y + 108, msg9, 5)
            if pyxel.frame_count % 30 < 15:
                pyxel.text(self.text_pos(msg10), msg_y + 130, msg10, 7)
            return
        
        if not self.game_over:
            if self.hover_tile:
                pyxel.mouse(False)
                tx, ty = self.iso_center(self.hover_tile)
                is_occ = any(tw.tile == self.hover_tile for tw in self.towers)
                is_inv = self.hover_tile.kind in ["path", "water", "bridge", "wall", "exit", "hole"]
                hover_color = 7 if (self.money >= TOWER_COST and not is_occ and not is_inv) else 8
                pyxel.line(tx-7, ty, tx, ty-3, hover_color)
                pyxel.line(tx, ty-3, tx+7, ty, hover_color)
                pyxel.line(tx+7, ty, tx, ty+3, hover_color)
                pyxel.line(tx, ty+3, tx-7, ty, hover_color)
            else:
                pyxel.mouse(True)
            
        # Ellipse 
        if self.hover_tile and not self.game_over:
            current_tower = next((tw for tw in self.towers if tw in self.towers if tw.tile == self.hover_tile), None)
            if current_tower:
                # Tour existe déjà
                bonus_altura = max(0, (current_tower.tile.h - 1) * 0.5)
                alcance_total = current_tower.range + bonus_altura
                ellipse_color = 7 
                show_ellipse = True
            elif self.hover_tile.kind not in ["path", "water", "bridge", "wall", "exit", "hole"] and self.money >= TOWER_COST:
                # On peut mettre une tour donc on montre aussi l'ellipse 
                temp_tower = Tower(self.hover_tile, kind=self.next_tower_kind)
                bonus_altura = max(0, (self.hover_tile.h - 1) * 0.5)
                alcance_total = temp_tower.range + bonus_altura
                ellipse_color = 13
                show_ellipse = True
            else:
                show_ellipse = False

            if show_ellipse:
                tx, ty = self.iso_center(self.hover_tile)
                rx = alcance_total * (BLOCK_SIZE // 2)
                ry = rx / 2
                steps = 32
                for i in range(steps):
                    angle1 = i * 360 / steps
                    angle2 = (i + 1) * 360 / steps
                    x1 = tx + pyxel.cos(angle1) * rx
                    y1 = ty + pyxel.sin(angle1) * ry
                    x2 = tx + pyxel.cos(angle2) * rx
                    y2 = ty + pyxel.sin(angle2) * ry
                    pyxel.line(x1, y1, x2, y2, ellipse_color)
                
        # icone réparation souris
        if self.hover_tile:
            for t in self.towers:
                if t.tile == self.hover_tile and t.hp < t.max_hp and ((self.money >= TOWER_FIX_COST and not t.is_guardian) or (self.money >= GUARDIAN_FIX_COST and t.is_guardian)):
                    mx, my = pyxel.mouse_x, pyxel.mouse_y
                    ix, iy = mx + 12, my - 14
                    pyxel.circ(ix + 4, iy + 8, 4, 7)
                    pyxel.circb(ix + 4, iy + 8, 4, 0)
                    pyxel.rect(ix, iy, 9, 9, 7)
                    pyxel.line(ix, iy, ix + 8, iy, 0)
                    pyxel.line(ix, iy, ix, iy + 8, 0)
                    pyxel.line(ix + 8, iy, ix + 8, iy + 8, 0)
                    pyxel.line(ix + 4, iy, ix + 4, iy + 5, 0)
                    pyxel.line(ix, iy + 5, ix + 8, iy + 5, 0)
                    pyxel.rect(ix + 5, iy + 1, 3, 4, 14)
                    pyxel.text(ix, iy + 15, "FIX", 7)
                    break
                
        for t in self.towers:
            self.draw_tower_sprite(t.tile, t.kind, t.is_guardian)
            # barre de vie
            tx, ty = self.iso_center(t.tile)
            bx, by = tx - 5, ty - (22 if t.is_guardian else 16)
            pyxel.rect(bx, by, 10, 2, 8);
            pyxel.rect(bx, by, int(10 * (t.hp / t.max_hp)), 2, 9 if not t.is_guardian else 6)
            pyxel.rectb(bx - 1, by - 1, 12, 4, (5 if t.is_guardian else 0));

        for b in self.bullets:
            sx, sy = self.iso(b.x, b.y, b.z)
            pyxel.circ(sx + CAM_X + self.cam_x, sy + CAM_Y + self.cam_y, 1, 10)

        for e in self.enemies:
            x, y = e.pos()
            sx, sy = self.iso(x, y, 1)
            sy -= 3
            sx, sy = sx + CAM_X + self.cam_x, sy + CAM_Y + self.cam_y
            if e.kind == "tank":
                body_c, dark_c, size = 13, 5, 5
            elif e.kind == "fast":
                body_c, dark_c, size = 11, 3, 3
            elif e.kind == "kamikaze":
                body_c, dark_c, size = 5, 0, 4
            elif e.kind == "boss":
                sy -= 5
                body_c, dark_c, size = 13, 1, 9
            else:
                body_c, dark_c, size = 8, 2, 4
            top = [(sx, sy), (sx + size, sy + size//2), (sx, sy + size), (sx - size, sy + size//2)]
            pyxel.tri(*top[0], *top[1], *top[2], body_c)
            pyxel.tri(*top[0], *top[2], *top[3], body_c)
            pyxel.tri(top[3][0], top[3][1], top[2][0], top[2][1], top[2][0], top[2][1] + size, dark_c)
            pyxel.tri(top[3][0], top[3][1], top[2][0], top[2][1] + size, top[3][0], top[3][1] + size, dark_c)
            pyxel.tri(top[1][0], top[1][1], top[2][0], top[2][1], top[2][0], top[2][1] + size, 1)
            pyxel.tri(top[1][0], top[1][1], top[2][0], top[2][1] + size, top[1][0], top[1][1] + size, 1)
            # Barre de vie
            bx, by = sx - 5, sy - 6
            pyxel.rect(bx, by, 10, 2, 8)
            pyxel.rect(bx, by, int(10 * (e.hp / e.max_hp)), 2, 11)
            pyxel.rectb(bx-1, by-1, 12, 4, 0)
            
        for m in self.meteors:
            msx, msy = self.iso(m.x, m.y, m.z)
            msx += CAM_X + self.cam_x
            msy += CAM_Y + self.cam_y
            pyxel.circ(msx, msy, 4, 10)
            pyxel.circ(msx, msy, 2, 7)
            # Traînée de feu
            for i in range(3):
                trail_offset = (i + 1) * 2
                tsx, tsy = self.iso(m.x - (trail_offset * 0.2), m.y - (trail_offset * 0.2), m.z + trail_offset)
                pyxel.pset(tsx + CAM_X + self.cam_x, tsy + CAM_Y + self.cam_y, random.choice([8, 14, 10]))

        for eb in self.enemy_bullets:
            sx, sy = self.iso(eb.x, eb.y, eb.z); pyxel.circ(sx + CAM_X + self.cam_x, sy + CAM_Y + self.cam_y, 1, 2)
            
        for p in self.particles:
            px, py = self.iso(p.x, p.y, p.z); pyxel.pset(px + CAM_X + self.cam_x, py + CAM_Y + self.cam_y, p.color)
        
        if self.is_raining:
            for _ in range(15): 
                rx = random.randint(0, 255)
                ry = random.randint(0, 255)
                pyxel.line(rx, ry, rx - 1, ry + 2, 6) 
        
        for ft in self.floating_texts:
            ft.draw(self)
        
        # Brume de Perlin
        if self.fog_opacity > 0.005 and not self.game_over:
            pyxel.dither(self.fog_opacity * 0.45)
            fog_block = 2
            for fy in range(14, pyxel.height, fog_block):
                for fx in range(0, pyxel.width, fog_block):
                    screen_x_virtual = fx - CAM_X - self.cam_x
                    screen_y_virtual = fy - CAM_Y - self.cam_y
                    world_x = (screen_x_virtual / (BLOCK_SIZE // 2) + screen_y_virtual / (BLOCK_SIZE // 4)) * 10
                    world_y = (screen_y_virtual / (BLOCK_SIZE // 4) - screen_x_virtual / (BLOCK_SIZE // 2)) * 10
                    n_val = pyxel.noise(world_x / 40.0, world_y / 40.0, self.fog_time)
                    seuil_apparition = 0.4 - (self.fog_opacity * 0.3)
                    if n_val > seuil_apparition:
                        c_fog = 7 if n_val > (seuil_apparition + 0.25) else 13
                        pyxel.rect(fx, fy, fog_block, fog_block, c_fog)
            pyxel.dither(1.0)
            
        # HUD
        pyxel.camera(0, 0)
        pyxel.rect(0, 0, 256, 14, 0)
        pyxel.text(5, 4, f"ARGENT: ${self.money}", 10 if self.money >= TOWER_COST else 8)
        pyxel.text(70, 4, f"SCORE: {self.score:05}", 15)
        
        from_border = pyxel.width - 80
        base_hud_y = 10
        # Chrono
        is_wave_boss = (self.wave % self.wave_boss == 0)
        boss_alive = any(e.kind == "boss" for e in self.enemies)
    
        if is_wave_boss :
            if not (not boss_alive and self.spawned == 0):
                pyxel.text(from_border + 28, 4 , "TUER LE BOSS", 8) # Couleur rouge
        elif self.wave == 1:
            pyxel.text(from_border + 10, 4 , f"RESTE: {len(self.enemies)} ENNEMIS", 7)
        else:
            # Évite affichage négatif
            frames_restantes = max(0, self.wave_interval - self.wave_timer)
            secondes_restantes = frames_restantes // 30
            pyxel.text(from_border , 4 , f"EVENEMENT DANS {secondes_restantes}s", 7)
            
        base_hud_y = pyxel.height - 55
        fake_tile = Tile(0, 0, 0, "grass")
        
        # Prochaine tour
        center_x = pyxel.width // 2
        pyxel.text(70, 14, "Prochaine tour:", 7)
        self.draw_tower_direct(140, 18, self.next_tower_kind, False)
        
        # Tour en bas
        x_base_world = -50 
        pyxel.text( self.cam_x + x_base_world + 22, base_hud_y, "TOURS", 12)
        
        self.draw_hud_tower(x_base_world, base_hud_y + 16, fake_tile, "sniper", False)
        pyxel.text(x_base_world + 22 + self.cam_x, base_hud_y + 10, "Sniper", 7)
        
        self.draw_hud_tower(x_base_world, base_hud_y + 32, fake_tile, "basic", False)
        pyxel.text(x_base_world + 22 + self.cam_x, base_hud_y + 24, "Basic", 7)
    
        self.draw_hud_tower(x_base_world, base_hud_y + 46, fake_tile, "rapid", False)
        pyxel.text(x_base_world + 22 + self.cam_x, base_hud_y + 38, "Rapid", 7)
    
        
        # Ennemis
        from_border = pyxel.width + 20
        x_inimigos = from_border + self.cam_x
        pyxel.text( x_inimigos + 15, base_hud_y, "ENNEMIS", 8)
        self.draw_hud_enemy(from_border + 6, base_hud_y + 10, "normal")
        pyxel.text(x_inimigos + 15, base_hud_y + 10, "Normal", 7)
        self.draw_hud_enemy(from_border + 6, base_hud_y + 22, "fast")
        pyxel.text(x_inimigos + 15, base_hud_y + 22, "Fast", 7)
        self.draw_hud_enemy(from_border + 6, base_hud_y + 32, "tank")
        pyxel.text(x_inimigos + 15, base_hud_y + 34, "Tank", 7)
        self.draw_hud_enemy(from_border + 6, base_hud_y + 44, "kamikaze")
        pyxel.text(x_inimigos + 15, base_hud_y + 47, "Kamikaze", 7)
        
        base_wave_name = 30
        if self.wave == (self.next_tsunami_wave - 1) and getattr(self, 'tsunami_alert_timer', 0) > 0:
            if pyxel.frame_count % 20 < 10:
                wave_n = "TREMBLEMENT DE TERRE"
                pyxel.text(self.text_pos(wave_n) +1, base_wave_name + 1, wave_n, 1)
                pyxel.text(self.text_pos(wave_n), base_wave_name, wave_n, 8)
        
        is_boss_wave = (self.wave == len(WAVE_LEVEL) - 1)
        if self.wave == self.next_tsunami_wave:
            wave_n = "- TSUNAMI -"
            pyxel.text(self.text_pos(wave_n) + 1, base_wave_name + 1 , wave_n, 1)
            pyxel.text(self.text_pos(wave_n), base_wave_name, wave_n, 12)
        elif is_boss_wave:
            # Texte clignotant rouge et blanc pour le côté dramatique
            wave_n = "- The BOSS -"
            boss_color = 8 if (pyxel.frame_count // 10) % 2 == 0 else 7
            pyxel.text(self.text_pos(wave_n), base_wave_name + 10, "- The BOSS -", boss_color)
            level_name = WAVE_LEVEL[self.wave] if self.wave < len(WAVE_LEVEL) else ""
            if level_name:
                wave_n = level_name
                pyxel.text(self.text_pos(wave_n), base_wave_name, f"{level_name}", 10) 
        elif self.wave < len(WAVE_LEVEL):
            if WAVE_LEVEL[self.wave] != "":
                #wave_n = WAVE_LEVEL[self.wave]
                wave_n = WAVE_LEVEL[min(len(WAVE_LEVEL)-1, self.wave)]
                pyxel.text(self.text_pos(wave_n) + 1, base_wave_name + 1 , f"{WAVE_LEVEL[self.wave]}", 1)
                pyxel.text(self.text_pos(wave_n), base_wave_name, f"{WAVE_LEVEL[self.wave]}", 9)
        else:
            wave_n = "SURVIVRE"
            pyxel.text(self.text_pos(wave_n) + 1, base_wave_name + 1 , wave_n, 1)
            pyxel.text(self.text_pos(wave_n), base_wave_name, wave_n, 7)
            
        pyxel.text(5, 14, "MEILLEURS", 7)
        pyxel.text(5, 22, "SCORES", 7)
        for i, s in enumerate(self.high_scores):
            c = 10 if self.score == s and self.score > 0 else 5
            pyxel.text(5, 30 + i * 8, f"{i+1}. {s:05}", c)
 
         
        if self.game_over:
            self.apply_rain_palette(False)
            msg1 = "CHUTE DES GUARDIENS"
            msg2 = "PRESSEZ [R] POUR REJOUER"
            msg3 = "(c) Eric Tabbone 2026"
            msg_max_size = max(self.text_pos(msg1),self.text_pos(msg2))
            margin = 20
            msg_x = pyxel.width // 2 - msg_max_size // 2 - margin
            msg_w = msg_max_size + 2 * margin
            msg_y = pyxel.height // 2 - 1.5 * margin
            pyxel.line(msg_x + 1 , msg_y + 50, msg_x + msg_w, msg_y + 50, 1)
            pyxel.line(msg_x + msg_w , msg_y + 1, msg_x + msg_w, msg_y + 50, 1)
            pyxel.rect(msg_x, msg_y, msg_w, 50, 0)
            pyxel.rectb(msg_x, msg_y, msg_w, 50, 9)
            pyxel.text(self.text_pos(msg1) +1 , msg_y + 12, msg1, 1)
            pyxel.text(self.text_pos(msg1),msg_y + 11, msg1, 8)
            pyxel.text(self.text_pos(msg2) +1 , msg_y + 26, msg2, 1)
            pyxel.text(self.text_pos(msg2),  msg_y + 25, msg2, 7)
            pyxel.text(self.text_pos(msg3),  msg_y + 40, "(c) Eric Tabbone 2026", 10)
        
        # Éclair
        if self.flash_timer > 0 and self.strike_target:
            # Calcul de la position de réception selon le type de cible
            if isinstance(self.strike_target, Tower):
                tx, ty = self.iso_center(self.strike_target.tile)
                target_y = ty - (15 if self.strike_target.is_guardian else 5)
                target_x = tx
            else: # C'est un ennemi
                ex, ey = self.strike_target.pos()
                sx, sy = self.iso(ex, ey, 1)
                target_x = sx + CAM_X + self.cam_x
                target_y = sy + CAM_Y + self.cam_y
            
            # Point de départ céleste
            start_x = target_x + random.randint(-30, 30)
            start_y = 0
            
            # Dessin de l'éclair brisé
            mid_x = (start_x + target_x) // 2 + random.randint(-15, 15)
            mid_y = target_y // 2
            
            # Rendu visuel (Jaune + Blanc)
            pyxel.line(start_x, start_y, mid_x, mid_y, 10)
            pyxel.line(mid_x, mid_y, target_x, target_y, 10)
            pyxel.line(start_x + 1, start_y, mid_x + 1, mid_y, 7)
            pyxel.line(mid_x + 1, mid_y, target_x + 1, target_y, 7)
            
            # Quelques étincelles au point d'impact
            for _ in range(3):
                self.particles.append(ExplosionPixel(
                    self.strike_target.tile.x if isinstance(self.strike_target, Tower) else ex,
                    self.strike_target.tile.y if isinstance(self.strike_target, Tower) else ey,
                    2
                ))
            
        if self.flash_timer > 0:
            if self.flash_timer > 2:
                pyxel.cls(7)
            self.flash_timer -= 1
            if self.flash_timer == 0:
                self.strike_target = None # Reset
        
        self.draw_minimap()
        
    def draw_tower_sprite(self, tile, kind, is_guardian=False):
        base_x, base_y = self.iso_center(tile)
        base_y -= 2
        if is_guardian:
            colors = [13, 13, 6, 7]
            height_steps = 8
        elif kind == "sniper":
            colors = [2, 8, 14, 7]
            height_steps = 7
        elif kind == "rapid":
            colors = [1, 5, 6, 12]
            height_steps = 3
        else: # basic
            colors = [4, 9, 10, 7]
            height_steps = 5
        # Dessin des couches de la tour
        for i in range(height_steps):
            h_offset = i * 2
            sx, sy = base_x, base_y - h_offset
            c = colors[i % len(colors)]
            # Sniper plus fin
            w = BLOCK_SIZE // 6 if kind == "sniper" else BLOCK_SIZE // 4
            pyxel.tri(sx, sy, sx + w, sy + w//2, sx, sy + w, c)
            pyxel.tri(sx, sy, sx, sy + w, sx - w, sy + w//2, c)
            sy -= 1
            pyxel.tri(sx, sy, sx + w, sy + w//2, sx, sy + w, c)
            pyxel.tri(sx, sy, sx, sy + w, sx - w, sy + w//2, c)

App()

