# 1943 Battle of Midway
import pyxel
WIDTH = 256
HEIGHT = 256

FPS = 60
PLANE = (0,16)
PLANE_RIGHT = (0,96)
PLANE_LEFT = (0,112)
PLANE_ZOOM = 0.5
PLANE_ZOOM_STEP = .1
PLANE_LANDING_LIMIT = 70
#PLANE_LANDING = 70
PLANE_SPEED = 3     
PLANE_WIDTH = 16
PLANE_ROTATION_INDEX = 1  # Red plane
PLANE_FIRE_NORMAL =   10  # Frames
PLANE_FIRE_RAPID = 4      # Frames
PLANE_RAPIDFIRE =  7       # seg.

BONUS_RAPIDFIRE = (10,18)
BONUS_BOMB = (10,20)
BONUS_LIFE = (10,22)
BONUS_GUNS = (16,28)
BONUS_STEP = 1

ALLBONUS = [BONUS_RAPIDFIRE,BONUS_BOMB,BONUS_LIFE,BONUS_GUNS]

TILE_SEA = (0,0)
ENEMY_BLUE = (0,22)
ENEMY_RED = (0,24)
ENEMY_RED_SW = (0,26)
ENEMY_RED_W = (0,28)
ENEMY_RED2 = (0,16)
ENEMY_RED2_SE = (0,18)
ENEMY_RED2_E = (0,20)
ENEMY_BROWN = (0,30)
ENEMY_BIG_BLUE = (4,28)
ENEMY_YELLOW = (6,24)
ENEMY_WHITE = (6,26)
CANNON1 = (8,4)
CANNON2 = (8,6)
CANNON3 = (8,10)
CANNON4 = (8,16)
CANNON5 = (8,24)
CANNON6 = (13,5)
CANNON7 = (13,8)
CANNON8 = (12,12)
CANNON9 = (14,12)
CANNON10 = (13,18)
CANNON_SMALL_HIT = 3
CANNON_BIG_HIT = 5
CANNON_SMALL_SCORE = 50
CANNON_BIG_SCORE = 100

BULLET_WIDTH = 2
BULLET_HEIGHT = 4
BULLET_COLOR = 14
BULLET_COLOR_ENEMY = 10
BULLET_SPEED = 4
BULLET_LOW = 3
BULLET_MEDIUM = 4
BULLET_HIGH = 5
BULLET_MAX_FIRES = 5

ENEMIES = [ENEMY_BLUE,ENEMY_RED,ENEMY_RED_SW,ENEMY_RED_W,ENEMY_RED2,ENEMY_RED2_SE,ENEMY_RED2_E,ENEMY_BROWN,ENEMY_BIG_BLUE,ENEMY_YELLOW,ENEMY_WHITE,CANNON1,CANNON2,CANNON3,CANNON4,CANNON5,CANNON6,CANNON7,CANNON8,CANNON9,CANNON10]
ENEMIES_INFOS = [
    (2,2,2,1,0,4,35,BULLET_LOW),  # ENEMY_BLUE
    (2,2,3,0,1,1,25,BULLET_HIGH),  # ENEMY_RED
    (2,2,3,-1,1,1,25,BULLET_HIGH), # ENEMY_RED_SW
    (2,2,3,-1,0,1,25,BULLET_HIGH), # ENEMY_RED_W
    (2,2,3,0,1,1,25,BULLET_HIGH),  # ENEMY_RED2
    (2,2,3,1,1,1,25,BULLET_HIGH), # ENEMY_RED2_SE
    (2,2,3,1,0,1,25,BULLET_HIGH), # ENEMY_RED2_E
    (2,2,1,0,1,4,35,BULLET_LOW),  # ENEMY_BROWN
    (4,4,1,0,1,8,100,BULLET_MEDIUM), # ENEMY_BIG_BLUE
    (2,2,2,0,1,2,25,BULLET_LOW),  # ENEMY_YELLOW
    (2,2,3,0,1,4,35,BULLET_HIGH),  # ENEMY_WHITE
    # Medium ship
    (2,2,0,0,0,CANNON_SMALL_HIT,CANNON_SMALL_SCORE,BULLET_LOW), # CANNON1
    (2,2,0,0,0,CANNON_SMALL_HIT,CANNON_SMALL_SCORE,BULLET_LOW), # CANNON2
    (2,2,0,0,0,CANNON_SMALL_HIT,CANNON_SMALL_SCORE,BULLET_LOW), # CANNON3
    (2,2,0,0,0,CANNON_SMALL_HIT,CANNON_SMALL_SCORE,BULLET_LOW), # CANNON4
    # Small ship
    (2,2,0,0,0,CANNON_SMALL_HIT,CANNON_SMALL_SCORE,BULLET_LOW), # CANNON5
    # Big ship
    (2,2,0,0,0,CANNON_BIG_HIT,CANNON_BIG_SCORE,BULLET_MEDIUM), # CANNON6
    (2,2,0,0,0,CANNON_BIG_HIT,CANNON_BIG_SCORE,BULLET_MEDIUM), # CANNON7
    (2,2,0,0,0,CANNON_BIG_HIT,CANNON_BIG_SCORE,BULLET_MEDIUM), # CANNON8
    (2,2,0,0,0,CANNON_BIG_HIT,CANNON_BIG_SCORE,BULLET_MEDIUM), # CANNON9
    (2,2,0,0,0,CANNON_BIG_HIT,CANNON_BIG_SCORE,BULLET_MEDIUM)  # CANNON10
    ]
#ENEMIES_INFOS = (size_x,size_y,speed,move_x,move_y,hits,score,bullet_speed)
'''
EAST = (1,0)
NORTHEAST = (1,-1)
NORTH = (0,-1)
NORTHWEST = (-1,-1)
WEST = (-1,0)
SOUTHWEST = (-1,1)
SOUTH = (0,1)
SOUTHEAST = (1,1)
NULL = (0,0)
'''

#ENEMIES_BULLETS = (speed,(position,angle1),[(position2, angle2),(position3,angle3),...])
# positions: s=south, n=north, sw=southwest...


plane = []
enemies = []
bullets = []
explosions = []
allbonus = []


SCROLL_Y = 2048 - HEIGHT
SCROLL_X = 0
SCORE= 0
LEVEL = 1 # NOT USED
DIFICULTY = 1
TAKEOFF = True
LANDING = False
FLYING = False
# Hit by bullet or plane
HIT = False
#How many hits to die (1 for player)
HITS = 1
GAMEOVER = False
PAUSE = False
LANDED = False
LIVES = 3
TRYAGAIN = False
START = False
STOP = False
COUNTDOWN = 3
HIGHSCORE = 0
EXPLOSION_DURATION = 3 # frames
CONTINUE_GAME = 5      # 5 seg to continue
CONTINUE_OK = False
RESTART = True
BACK = 100
TRACK_SIZE = 0
FLIP = False
FLIP_COUNT = 5
FLIP_STEP = 1          # x seg. to flip
FLIP_TIMER = 0
high_score = HIGHSCORE
level = LEVEL
MEGABONUS250 = False
MEGABONUS500 = False
MEGABONUS_TIMEUP = 3   # seg.
IMORTAL = False
IMORTAL_DELAY = 10
IMORTAL_ON_START = True

def update_entities(entities):
    for entity in entities:
        entity.update()

def draw_entities(entities):
    for entity in entities:
        entity.draw()


def cleanup_entities(entities, clear = False):
    for i in range(len(entities) - 1, -1, -1):
        if clear:
            del entities[i]
        else:
            if not entities[i].is_alive:
                del entities[i]
            
def get_tile(tile_x, tile_y):
    return pyxel.tilemaps[0].pget(tile_x, tile_y)

def set_tile(tile_x, tile_y,tile):
    return pyxel.tilemaps[0].pset(tile_x, tile_y,tile)

def read_map():
    for y in range(0,HEIGHT):
        for x in range(0, 2*WIDTH):
            tile = get_tile(x,y)
            if tile in ALLBONUS:
                index = ALLBONUS.index(tile)
                Bonus(x*8,y*8,index)
                set_tile(x,y,TILE_SEA)
                set_tile(x+1,y,TILE_SEA)
                set_tile(x+1,y+1,TILE_SEA)
                set_tile(x,y+1,TILE_SEA)
            if tile in ENEMIES:
                index = ENEMIES.index(tile)
                Enemy(x*8,y*8,index)
                for j in range(0,ENEMIES_INFOS[index][1] ):
                    for i in range(0,ENEMIES_INFOS[index][0]):
                        # Planes
                        if tile[0]<8: 
                            set_tile(x+i,y+j,TILE_SEA)
                        

def collision(self):
    global score, tryagain, hit, lives, scroll_x, scroll_y, flip, flip_count, flip_step, flip_timer, imortal, imortal_counter
    global megabonus500, megabonus500_counter, megabonus500_timer, megabonus500_x, megabonus500_y 
    global megabonus250, megabonus250_counter, megabonus250_timer, megabonus250_x, megabonus250_y
    # Check bonus
    for bonus in allbonus:
        if bonus.is_alive and ((bonus.x - scroll_x <= plane[0].x  and bonus.x + 16 - scroll_x >= plane[0].x) or (bonus.x - scroll_x <= plane[0].x + PLANE_WIDTH and bonus.x + 16 - scroll_x >= plane[0].x + PLANE_WIDTH)) and ((bonus.y - scroll_y <= plane[0].y and bonus.y - scroll_y + 16 >= plane[0].y) or (bonus.y - scroll_y  <= plane[0].y + PLANE_WIDTH  and bonus.y - scroll_y + 16  >= plane[0].y + PLANE_WIDTH)):
            if ALLBONUS[bonus.idx] == BONUS_BOMB:
                flip = True
                bonus.is_alive = False
                pyxel.play(0, 6)
            if ALLBONUS[bonus.idx] == BONUS_LIFE:
                lives += 1
                bonus.is_alive = False
                pyxel.play(0, 6)
            if ALLBONUS[bonus.idx] == BONUS_GUNS:
                plane[0].guns += 1
                if plane[0].guns > 3:
                    plane[0].guns == 3
                bonus.is_alive = False
                pyxel.play(0, 6)
            if ALLBONUS[bonus.idx] == BONUS_RAPIDFIRE:
                plane[0].rapidfire = True
                plane[0].rapidfire_counter = PLANE_RAPIDFIRE
                plane[0].rapidfire_timer = PLANE_RAPIDFIRE * FPS
                bonus.is_alive = False
                pyxel.play(0, 6)
    for bullet in bullets:
        # Enemy hit (type = true => player's bullet)   
        if bullet.type == True:
            if self.x <= bullet.x and self.x + ENEMIES_INFOS[self.index][0]*8 >= bullet.x + 1 and self.y - scroll_y <= bullet.y and self.y -scroll_y + ENEMIES_INFOS[self.index][1]*8 >= bullet.y:
                self.hits -= 1
                bullet.is_alive = False
                pyxel.play(3, 1)
                if self.hits == 0:
                    self.is_alive = False
                    score = score + self.score
                    # Bonus 6 red planes 250pts
                    if ((ENEMIES[self.index] == ENEMY_RED or ENEMIES[self.index] == ENEMY_RED2) and not megabonus250):
                        megabonus250_counter += 1
                        if megabonus250_counter >= 6:
                            pyxel.play(0, 6)
                            megabonus250_counter = 0
                            megabonus250_timer = pyxel.frame_count + FPS * MEGABONUS_TIMEUP
                            megabonus250 = True
                            megabonus250_x = self.x
                            megabonus250_y = self.y
                    # Bonus 3 Big plane 500pts
                    if (ENEMIES_INFOS[self.index][0] == 4 and not megabonus500):
                        megabonus500_counter += 1
                        if megabonus500_counter >= 3:
                            pyxel.play(0, 6)
                            megabonus500_counter = 0
                            megabonus500_timer = pyxel.frame_count + FPS * MEGABONUS_TIMEUP
                            megabonus500 = True
                            megabonus500_x = self.x
                            megabonus500_y = self.y
                    # Explode
                    if self.tile_x >= 12:
                        set_tile(self.x//8,self.y//8,(self.tile_x+4,self.tile_y))
                        set_tile(self.x//8+1,self.y//8,(self.tile_x+5,self.tile_y))
                        set_tile(self.x//8,self.y//8+1,(self.tile_x+4,self.tile_y+1))
                        set_tile(self.x//8+1,self.y//8+1,(self.tile_x+5,self.tile_y+1))
                    if self.tile_x >= 8 and self.tile_x < 12:
                        set_tile(self.x//8,self.y//8,(self.tile_x+2,self.tile_y))
                        set_tile(self.x//8+1,self.y//8,(self.tile_x+3,self.tile_y))
                        set_tile(self.x//8,self.y//8+1,(self.tile_x+2,self.tile_y+1))
                        set_tile(self.x//8+1,self.y//8+1,(self.tile_x+3,self.tile_y+1))
                    Explosion(self.x,self.y,ENEMIES_INFOS[self.index][0]//2,True)
                else:
                    # Hit only
                    Explosion(self.x,self.y,ENEMIES_INFOS[self.index][0]//2,False)
        # Player hit (type = false => enemy's bullet))
        else:
            if not imortal and not hit and not plane[0].flip and plane[0].x <= bullet.x and plane[0].x + PLANE_WIDTH >= bullet.x + 1 and plane[0].y <= bullet.y and plane[0].y + PLANE_WIDTH >= bullet.y:
                self.is_alive = False
                bullet.is_alive = False
                pyxel.play(3, 1)
                hit = True
                imortal = True
                imortal_counter = pyxel.frame_count + FPS * IMORTAL_DELAY
    # Check collision with plane (not with ship)
    if not imortal and not tryagain and not plane[0].flip and ENEMIES[self.index][0]<8:
        if ((self.x - scroll_x <= plane[0].x and self.x - scroll_x + ENEMIES_INFOS[self.index][0]*8 >= plane[0].x) or (self.x - scroll_x <= plane[0].x + PLANE_WIDTH and self.x - scroll_x + ENEMIES_INFOS[self.index][0]*8 >= plane[0].x + PLANE_WIDTH)) and ((self.y - scroll_y <= plane[0].y and self.y - scroll_y + ENEMIES_INFOS[self.index][1]*8 >= plane[0].y) or (self.y - scroll_y  <= plane[0].y + PLANE_WIDTH  and self.y - scroll_y + ENEMIES_INFOS[self.index][1]*8  >= plane[0].y + PLANE_WIDTH)):
            pyxel.play(3, 1)
            Explosion(self.x,self.y,2,True)
            self.is_alive = False
            hit = True
            imortal = True
            imortal_counter = pyxel.frame_count + FPS * IMORTAL_DELAY
            
class Explosion:
    def __init__(self,x,y,size,full):
        self.size = size
        # full = False : 1 coup
        # full = True  : Explosion totale
        self.full = full
        if self.full:
            self.x = x + self.size*8 - 8
            self.y = y + self.size*8//2 -8
        else:
            self.x = x + self.size*8 - 4
            self.y = y + self.size*8//2 - 4
        self.is_alive = True
        self.sprite = 0
        if self.full:
            self.sprite = 2
        self.counter = pyxel.frame_count
        self.counter_limit = self.counter +  EXPLOSION_DURATION
        explosions.append(self)
     
    def update(self):
        if self.counter < self.counter_limit:
            self.counter += 1
        else:
            self.counter = pyxel.frame_count
            self.counter_limit = self.counter +  EXPLOSION_DURATION
            self.sprite -= 1
            if self.sprite < 0:
                self.is_alive = False

    def draw(self):
        global scroll_x, scroll_y
        if self.full:
            # 3 explosions
            pyxel.blt(self.x ,self.y ,0,144,176+self.sprite*16,16,16,0,0,1*self.size)
        else:
            # 1 explosion
            pyxel.blt(self.x ,self.y ,0,128,160,8,16,0,0,1*self.size)
 
class Bonus:
    def __init__(self,x,y,index):
        self.x = x
        self.y = y
        self.index = index
        self.idx = index
        self.is_alive = True
        allbonus.append(self)      
    
    def update(self):
        #if pyxel.frame_count % 30 < 5:
        limit = 100
        dir_x = pyxel.rndi(0,limit)
        if dir_x == 0:
            dir_x = -1
        else:
            if dir_x == limit:
                dir_x = 1
            else:
                dir_x = 0
        self.x += BONUS_STEP * dir_x
        dir_y = pyxel.rndi(0,limit)
        if dir_y == 0:
            dir_y = -1
        else:
            if dir_y == limit:
                dir_y = 1
            else:
                dir_y = 0
        self.y += BONUS_STEP * dir_y
        
    def draw(self):
        global scroll_x, scroll_y
        if pyxel.frame_count % 16 < 12:
            if plane[0].guns >= 2 and ALLBONUS[self.index] == BONUS_GUNS:
                pyxel.blt(self.x - scroll_x,self.y,0, ALLBONUS[self.index][0]*8+16,ALLBONUS[self.index][1]*8,16,16,1,0,1)
            else:
                pyxel.blt(self.x - scroll_x,self.y,0, ALLBONUS[self.index][0]*8,ALLBONUS[self.index][1]*8,16,16,1,0,1)
            
class Enemy:
    def __init__(self,x,y,index):
        self.x = x
        self.y = y
        self.index = index
        self.is_alive = True
        self.waiting = True
        self.tile_x = ENEMIES[self.index][0]
        self.tile_y = ENEMIES[self.index][1]
        self.tile = (self.tile_x,self.tile_y)
        self.size_x  = ENEMIES_INFOS[self.index][0]
        self.size_y = ENEMIES_INFOS[self.index][1]
        self.speed  = ENEMIES_INFOS[self.index][2]
        self.move_x = ENEMIES_INFOS[self.index][3]
        self.move_y = ENEMIES_INFOS[self.index][4]
        self.hits   = ENEMIES_INFOS[self.index][5] 
        self.score  = ENEMIES_INFOS[self.index][6]
        self.bullet_speed = ENEMIES_INFOS[self.index][7]
        self.plane_rotation_index = index
        self.rotation = False
        if self.tile == ENEMY_RED or self.tile == ENEMY_RED2:
            # Steps before rotation
            self.count = 50
            self.rotation = True
        else:
            #  No rotation
            self.count = 0
        enemies.append(self)
          
    def update(self):
        global scroll_x,scroll_y,lives, hit, score
        # Out of screen
        if self.is_alive and (self.y  > HEIGHT + scroll_y or self.x  < 0 or self.x  > WIDTH):
            self.is_alive = False
        else:
            # Activate enemy
            if self.y + self.size_y*8 + 1 >= scroll_y and self.waiting:
                self.waiting = False
            # Enemy allready activated
            if not self.waiting:
                # Firing?
                if pyxel.rndi(1,100) == 1:
                    if self.tile == ENEMY_BLUE or self.tile == ENEMY_RED2_E or (self.index == (self.plane_rotation_index + 2) and self.move_x == 1 and self.move_y == 0):
                        # EAST
                        Bullet(self.x + (self.size_x*8) //2 , self.y + (self.size_y*8) // 2 - scroll_y , False, 1, 0 , self.bullet_speed)
                    if self.tile == ENEMY_RED or self.tile == ENEMY_RED2 or self.tile == ENEMY_YELLOW or self.tile == CANNON10:
                        # SOUTH
                        Bullet(self.x  + (self.size_x*8) //2 , self.y + (self.size_y*8) // 2 - scroll_y , False, 0, 1 , self.bullet_speed)
                    if self.tile == ENEMY_BROWN or self.tile == CANNON4 or self.tile == CANNON5:
                        # 2x SOUTH
                        Bullet(self.x + (self.size_x*8) //3 , self.y + (self.size_y*8) // 2 - scroll_y , False,0, 1 , self.bullet_speed)
                        Bullet(self.x + 2* (self.size_x*8) //3 , self.y + (self.size_y*8) // 2 - scroll_y , False,0, 1 , self.bullet_speed)
                    if self.tile == ENEMY_RED_W or (self.index == (self.plane_rotation_index + 2) and self.move_x == -1 and self.move_y == 0):
                        # WEST
                        Bullet(self.x + (self.size_x*8) //2 , self.y + (self.size_y*8) // 2 - scroll_y , False, -1, 0 , self.bullet_speed)
                    if self.tile == CANNON6 or self.tile == CANNON7:
                        # NORTH
                        Bullet(self.x + (self.size_x*8) //2 , self.y + (self.size_y*8) // 2 - scroll_y , False, 0, -1 , self.bullet_speed)
                    if self.tile == CANNON1:
                        # 2x NORTH
                        Bullet(self.x + (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, 0, -1 , self.bullet_speed)
                        Bullet(self.x + 3* (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False,0, -1 , self.bullet_speed)
                    if self.tile == ENEMY_RED_SW or self.tile == CANNON8 or (self.index == (self.plane_rotation_index + 1) and self.move_x == -1 and self.move_y == 1):
                        # SOUTHWEST
                        Bullet(self.x + (self.size_x*8) //2 - 4, self.y + (self.size_y*8) // 2 - scroll_y, False, -1, 1 , self.bullet_speed)
                    if self.tile == ENEMY_RED2_SE or (self.index == (self.plane_rotation_index + 1) and self.move_x == 1 and self.move_y == 1):
                        # SOUTHEAST
                        Bullet(self.x + (self.size_x*8) //2 - 4, self.y + (self.size_y*8) // 2 - scroll_y,  False, 1, 1 , self.bullet_speed)  
                    if self.tile == CANNON9:
                        # NORTHEAST
                        Bullet(self.x + (self.size_x*8) //2 , self.y + (self.size_y*8) // 2 - scroll_y , False, 1, -1 , self.bullet_speed)
                    if self.tile == CANNON2:
                        # 2x SOUTHEAST
                        Bullet(self.x + (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y - 4, False, 1, 1 , self.bullet_speed)
                        Bullet(self.x + 3* (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y - 4, False, 1, 1 , self.bullet_speed)
                    if self.tile == CANNON3:
                        # 2x NORTHWEST
                        Bullet(self.x + (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, -1, -1 , self.bullet_speed)
                        Bullet(self.x + 3* (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, -1, -1 , self.bullet_speed)
                    if self.tile == ENEMY_WHITE:
                        # 3x SOUTHWEST,SOUTH,SOUTHEAST
                        Bullet(self.x + (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, -1, 1 , self.bullet_speed)
                        Bullet(self.x + (self.size_x*8) //2 , self.y + (self.size_y*8) // 2 - scroll_y , False, 0, 1 , self.bullet_speed)
                        Bullet(self.x + 3* (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, 1, 1 , self.bullet_speed)
                    if self.tile == ENEMY_BIG_BLUE:
                        # 5x SOUTHWEST,SOUTH,,SOUTHEAST,NORTHWEST,NORTHEAST
                        Bullet(self.x + (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, -1, 1 , self.bullet_speed)
                        Bullet(self.x + (self.size_x*8) //2 , self.y + (self.size_y*8) // 2 - scroll_y , False, 0, 1 , self.bullet_speed)
                        Bullet(self.x + 3* (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, 1, 1 , self.bullet_speed)
                        Bullet(self.x + (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, -1, -1 , self.bullet_speed)
                        Bullet(self.x + 3* (self.size_x*8) //4 , self.y + (self.size_y*8) // 2 - scroll_y , False, 1, -1 , self.bullet_speed)
                # Rotation ?
                if self.rotation:
                    if (self.index == self.plane_rotation_index or self.index == (self.plane_rotation_index + 1) or self.index == (self.plane_rotation_index + 2)) :
                        self.count -= 1
                        if (self.count == 0 and self.index > self.plane_rotation_index) or (self.y - scroll_y > HEIGHT // 3 and self.index == self.plane_rotation_index):
                            self.index += 1
                            self.count = 20
                        self.move_x = ENEMIES_INFOS[self.index][3] 
                        self.move_y = ENEMIES_INFOS[self.index][4]
                        if self.index == (self.plane_rotation_index + 2):
                            self.rotation = False
                # Move enemy
                if pyxel.frame_count % PLANE_SPEED == 0:
                    self.x += self.speed * self.move_x
                    self.y += self.speed * self.move_y
                
            # Check collision bullets / player         
            collision(self)
            
    def draw(self):
        global scroll_x, scroll_y
        # plane
        if ENEMIES[self.index][0] < 8:
            pyxel.blt(self.x ,self.y,0, ENEMIES[self.index][0]*8,ENEMIES[self.index][1]*8,8*ENEMIES_INFOS[self.index][1],8*ENEMIES_INFOS[self.index][1],1,0,1)
            
class Bullet:
    def __init__(self, x, y, bullet_type, dir_x = 0, dir_y = -1, speed = BULLET_SPEED):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        # 0: Player
        # 1: Enemies
        self.type = bullet_type
        self.is_alive = True
        self.speed = speed
        bullets.append(self)

    def update(self):
        self.x += self.speed * self.dir_x
        self.y += self.speed * self.dir_y
        if self.y + self.h - 1 < 0:
            self.is_alive = False

    def draw(self):
        global scroll_x, scroll_y
        pyxel.rect(self.x , self.y + scroll_y, self.w, self.h, (BULLET_COLOR if self.type == True else BULLET_COLOR_ENEMY))

class Plane:
    def __init__(self,x = WIDTH//2, y = HEIGHT - 32):
        self.x = x
        self.y = y
        self.dir = 0
        self.is_alive = True
        self.size = PLANE_ZOOM
        self.shoot = 1
        self.counter = pyxel.frame_count
        self.counter_limit = self.counter +  PLANE_FIRE_NORMAL
        self.rapidfire = False
        self.rapidfire_timer = 0
        self.rapidfire_counter = 0
        self.guns = 1
        self.flip = False
        plane.append(self)
        
        
    def update(self):
        global scroll_y, landing, flying, takeoff, track_size, flip, flip_count, flip_step, flip_timer, stop
        # Take off
        if ((pyxel.frame_count ) % 40 == 0) and takeoff and self.size <= 1:
                self.size += PLANE_ZOOM_STEP
                if self.size >= 1:
                    self.size = 1
                    flying = True
                    takeoff = False
                    track_size = scroll_y
        # Landing
        if scroll_y <= PLANE_LANDING_LIMIT:
            if pyxel.frame_count % PLANE_SPEED == 0:
                if self.y < PLANE_LANDING_LIMIT:
                    self.y += 8
                if self.y > PLANE_LANDING_LIMIT:
                    self.y -= 8
                if self.x < WIDTH // 2:
                    self.x += 8
                if self.x > WIDTH // 2:
                    self.x -= 8
                if self.x == WIDTH // 2 and self.y <= PLANE_LANDING_LIMIT:
                    flying = False
                    self.y -= 8
                    if self.y <= PLANE_LANDING_LIMIT:
                        if not landing:
                            pyxel.play(0, 3)
                        landing = True                 
        if ((pyxel.frame_count ) % 60 == 0) and landing and not flying and self.size >= PLANE_ZOOM:
            self.size -= PLANE_ZOOM_STEP
            if self.size <= PLANE_ZOOM:
                self.size = PLANE_ZOOM
                landing = False
                stop = True
        # Controls
        if flying:
            # Firing
            if self.counter > self.counter_limit  and pyxel.btn(pyxel.KEY_SPACE):
                if self.guns == 1 or self.guns == 3:
                    Bullet(self.x + (PLANE_WIDTH - BULLET_WIDTH) / 2, self.y - BULLET_HEIGHT / 2, True)
                if self.guns == 2:
                    Bullet(self.x + PLANE_WIDTH // 4, self.y - BULLET_HEIGHT / 2, True)
                    Bullet(self.x + 2 * PLANE_WIDTH // 4 + BULLET_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True)
                if self.guns == 3:
                    Bullet(self.x + PLANE_WIDTH // 4, self.y - BULLET_HEIGHT / 2, True, -1, -2)
                    Bullet(self.x + 2 * PLANE_WIDTH // 4 + BULLET_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 1, -2)
                pyxel.play(0, 0)
                self.counter = pyxel.frame_count
                if self.rapidfire:
                   self.counter_limit = self.counter +  PLANE_FIRE_RAPID 
                else:
                    self.counter_limit = self.counter +  PLANE_FIRE_NORMAL
            self.counter += 1
            if pyxel.frame_count % PLANE_SPEED == 0: 
                # Super fire
                if pyxel.btn(pyxel.KEY_ALT) or pyxel.btn(pyxel.KEY_RETURN):
                    if flip and not self.flip:
                        pyxel.play(0, 5)
                        for i in range(1,9):
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, -1, -1) # TOP LEFT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, -1, -2) # TOP LEFT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, -2, -1) # TOP LEFT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 0, -1)  # TOP CENTER
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 1, -1)  # TOP RIGHT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 1, -2)  # TOP RIGHT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, -2, -1)  # TOP RIGHT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, -1, 0)  # LEFT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 1, 0)  # RIGHT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, -1, 1) # DOWN LEFT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, -1, 2) # DOWN LEFT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, -2, 1) # DOWN LEFT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 0, 1)  # DOWN CENTER
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 1, 1)  # DOWN RIGHT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 1, 2)  # DOWN RIGHT
                            Bullet(self.x + PLANE_WIDTH // 2, self.y - BULLET_HEIGHT / 2, True, 2, 1)  # DOWN RIGHT
                                                
                        self.flip = True
                        flip_count = FLIP_COUNT
                        flip_step= int(FLIP_STEP* FPS / 5)
                        flip_timer = pyxel.frame_count + flip_step
                    return
                if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_X):
                    self.x += 8
                    if self.x > WIDTH - 16:
                        self.x = WIDTH - 16
                if pyxel.btn(pyxel.KEY_LEFT)  or pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_W):
                    self.x -= 8
                    if self.x < 0:
                        self.x = 0
                if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_L) or pyxel.btn(pyxel.KEY_K):
                    self.y -= 8
                    if self.y < 0:
                        self.y = 0
                if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_COMMA):
                    self.y += 8
                    if self.y >  HEIGHT - 16:
                        self.y = HEIGHT - 16
                
    def draw(self):
        global flip,flip_count, flip_timer, imortal, imortal_counter
        if flip and flip_count > 0 and plane[0].flip:
            if pyxel.frame_count == flip_timer:
                flip_timer = pyxel.frame_count + flip_step
                flip_count -= 1
        if flip_count <= 0:
            flip = False
            plane[0].flip = False
        if imortal:
            if pyxel.frame_count % 20 < 10:
                pyxel.blt(self.x ,self.y + scroll_y,0,0,16 + 16*flip_count ,16,16,1,0,self.size)
            if pyxel.frame_count > imortal_counter:
                imortal_counter = 0
                imortal = False
        else:
            pyxel.blt(self.x ,self.y + scroll_y,0,0,16 + 16*flip_count ,16,16,1,0,self.size)
               
def init(clear = False):
    global start, stop, pause, scroll_x, scroll_y, takeoff, landing, flying, hit, gameover, landed, lives, countdown
    global tryagain, score, continue_game, continue_ok, restart, track_size, flip, flip_count, flip_step, flip_timer
    global megabonus500, megabonus500_counter, megabonus500_timer, megabonus500_x, megabonus500_y , imortal_counter
    global megabonus250, megabonus250_counter, megabonus250_timer, megabonus250_x, megabonus250_y , imortal
    pyxel.load("1943.pyxres")
    if clear:
        cleanup_entities(allbonus,True)
        cleanup_entities(enemies,True)
        cleanup_entities(bullets,True)
        cleanup_entities(explosions,True)
        cleanup_entities(plane,True)
    dificulty = DIFICULTY
    start = START
    stop = STOP
    pause = PAUSE
    scroll_x = SCROLL_X
    scroll_y = SCROLL_Y
    takeoff = TAKEOFF
    landing = LANDING
    flying = FLYING
    hit = HIT
    hits = HITS
    gameover = GAMEOVER
    landed = LANDED
    lives = LIVES
    tryagain = TRYAGAIN
    continue_game = CONTINUE_GAME
    continue_ok = CONTINUE_OK
    countdown = COUNTDOWN
    restart = RESTART
    score = SCORE
    track_size = TRACK_SIZE
    flip = FLIP
    flip_count = FLIP_COUNT
    flip_step = FLIP_STEP
    flip_timer = FLIP_TIMER
    megabonus250_counter = 0
    megabonus500_counter = 0
    megabonus250_timer = 0
    megabonus500_timer = 0
    megabonus250 = MEGABONUS250
    megabonus500 = MEGABONUS500
    megabonus500_x = 0
    megabonus500_y = 0
    megabonus250_x = 0
    megabonus250_y = 0
    imortal = IMORTAL
    imortal_counter = 0 
    read_map()
    Plane()

class App:
    def __init__(self):
        pyxel.init(WIDTH , HEIGHT, title="1943 Battle of Middway",fps=FPS,quit_key=pyxel.KEY_Q,display_scale=3)
        #pyxel .sounds[0].set("a3a2c1a1", "p", "7", "s", 7)
        pyxel.colors[8] = 0xE71818 # Red
        init(False)
        pyxel.run(self.update, self.draw)

    def update(self):
        global scroll_x, scroll_y, lives, gameover, flying, landing, landed, hit
        global imortal, imortal_counter, pause, start, continue_ok, restart, tryagain
        # PLAY
        if not start and (pyxel.btnp(pyxel.KEY_J) or pyxel.btnp(pyxel.KEY_S) or pyxel.btnp(pyxel.KEY_C) or pyxel.btnp(pyxel.KEY_RETURN)):
            start = True
            # Take off sound
            if IMORTAL_ON_START:
                imortal = True
                imortal_counter = pyxel.frame_count + FPS * IMORTAL_DELAY
            pyxel.play(0, 2)
        # You WIN
        if stop and (pyxel.btnp(pyxel.KEY_J) or pyxel.btnp(pyxel.KEY_S) or pyxel.btnp(pyxel.KEY_C) or pyxel.btnp(pyxel.KEY_RETURN)):
            init(True)
        # Exit game
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        # PAUSE
        if pyxel.btnp(pyxel.KEY_P) and start and not gameover:
            pause = not pause
        # RESTART
        if gameover and (pyxel.btn(pyxel.KEY_R) or pyxel.btn(pyxel.KEY_C) or pyxel.btn(pyxel.KEY_RETURN)):
            if not continue_ok and not restart:
                continue_game = 0
            else:
                continue_ok = True
                restart = False
                gameover = False
        if not pause and start  and not hit:
            update_entities(allbonus)
            update_entities(enemies)
            update_entities(explosions)
            if not gameover and not landed and not hit and not tryagain:
                update_entities(plane)
                update_entities(bullets)
                cleanup_entities(bullets,False)
            else:
                cleanup_entities(bullets,True)
            cleanup_entities(allbonus,False)
            cleanup_entities(enemies,False)
            cleanup_entities(explosions,False)
            cleanup_entities(plane,False)
            # Scrolling
            if pyxel.frame_count % 4 == 0 and not gameover and not hit and not tryagain:
                if scroll_y > 0:
                    scroll_y -= 1
                else:
                    if not landing and not flying and not takeoff:
                        landed = True
            
    def draw(self):
        global gameover, lives, score, high_score, pause, countdown, tryagain, hit, takeoff
        global continue_game, score, continue_ok, restart, track_size, flip, stop, scroll_y
        global megabonus500, megabonus500_timer, megabonus500_x, megabonus500_y
        global megabonus250, megabonus250_timer, megabonus250_x, megabonus250_y
        pyxel.cls(1)
        # Draw background
        pyxel.camera()
        pyxel.bltm(0, 0, 0, scroll_x, scroll_y, WIDTH, HEIGHT, 1)
        pyxel.camera(0,scroll_y)
        draw_entities(allbonus)    
        draw_entities(bullets)
        draw_entities(enemies)
        draw_entities(explosions)
        # Lives
        pyxel.blt(10 , 1 + scroll_y,0,80+8*lives,240,8,16,1,0,.8)
        pyxel.blt(19 , 1 + scroll_y,0,80,208,16,16,1)
       
        # SCORE
        number = score
        n_len = len(str(score))
        position = (n_len*8) + n_len - 1
        for i in range(n_len,0,-1):
            digit = number % 10
            number = number // 10
            pyxel.blt(2 + position , 17 + scroll_y,0,80+8*digit,240,8,16,1,0,1)
            position -= 9
        if high_score < score:
            high_score = score
        # HIGH SCORE
        pyxel.blt(WIDTH//2 - 32 , 1 + scroll_y,0,64,224,64,16,1)
        number = high_score
        n_len = len(str(high_score))
        position = ((n_len*8) + n_len - 1)//2
        for i in range(0,n_len):
            digit = number % 10
            number = number // 10
            position -= 9
            pyxel.blt(WIDTH//2 + position , 17 + scroll_y,0,80+8*digit,240,8,16,1,0,1)
        # Track progess
        if track_size >0 and (track_size - scroll_y) > 0:
            track_lenght = 60
            track_step = track_lenght // 5
            track_x = 65  #Distance from right border
            track_y = 6
            track_height = 6
            progress = pyxel.ceil((track_size - scroll_y) / track_size * track_lenght)
            if progress < track_step:
                pyxel.rect(WIDTH - track_x , track_y + scroll_y, progress ,track_height ,8)
            if progress >= track_step and progress < track_step*2:
                pyxel.rect(WIDTH - track_x , track_y + scroll_y, track_step ,track_height ,8)
                pyxel.rect(WIDTH - track_x + track_step , track_y + scroll_y, progress - track_step ,track_height , 9)
            if progress >= track_step*2 and progress < track_step*3:
                pyxel.rect(WIDTH - track_x , track_y + scroll_y, track_step ,track_height ,8)
                pyxel.rect(WIDTH - track_x + track_step , track_y + scroll_y, track_step ,track_height ,9)
                pyxel.rect(WIDTH - track_x + track_step*2 , track_y + scroll_y, progress - track_step*2 ,track_height , 10)
            if progress >= track_step*3 and progress < track_step*4:
                pyxel.rect(WIDTH - track_x , track_y + scroll_y, track_step ,track_height ,8)
                pyxel.rect(WIDTH - track_x + track_step , track_y + scroll_y, track_step ,track_height ,9)
                pyxel.rect(WIDTH - track_x + track_step*2 , track_y + scroll_y, track_step ,track_height , 10)
                pyxel.rect(WIDTH - track_x + track_step*3 , track_y + scroll_y, progress - track_step*3 ,track_height , 6)
            if progress >= track_step*4 and progress <= track_lenght:
                pyxel.rect(WIDTH - track_x , track_y + scroll_y, track_step ,track_height ,8)
                pyxel.rect(WIDTH - track_x + track_step , track_y + scroll_y, track_step ,track_height ,9)
                pyxel.rect(WIDTH - track_x + track_step*2 , track_y + scroll_y, track_step ,track_height , 10)
                pyxel.rect(WIDTH - track_x + track_step*3 , track_y + scroll_y, track_step ,track_height , 6)
                pyxel.rect(WIDTH - track_x + track_step*4 , track_y + scroll_y, progress - track_step*4 ,track_height , 11)

        # BONUS
        if flip:
            pyxel.blt(WIDTH - 60 , 17 + scroll_y,0,80,160,16,16,1)
        if plane[0].guns == 2:
            pyxel.blt(WIDTH - 40 , 17 + scroll_y,0,128,224,16,16,1)
        if plane[0].guns >2:
            pyxel.blt(WIDTH - 40 , 17 + scroll_y,0,144,224,16,16,1)
        if not pause and plane[0].rapidfire_timer > 0:
            plane[0].rapidfire_timer -= 1
            if plane[0].rapidfire_timer % FPS == 0:
                plane[0].rapidfire_counter -= 1
            if plane[0].rapidfire_timer == 0:
                plane[0].rapidfire = False
                plane[0].rapidfire_timer = 0
                plane[0].rapidfire_counter = 0
        if plane[0].rapidfire:
            pyxel.blt(WIDTH - 20 , 17 + scroll_y,0,80,144,16,16,1)
            pyxel.rect(WIDTH - 21 , 29 + scroll_y,5,7,5)
            pyxel.text(WIDTH - 20 , 30 + scroll_y,str(plane[0].rapidfire_counter),7)
        # Megabonus 250
        if megabonus250:
            if pyxel.frame_count == megabonus250_timer:
                megabonus250 = False
            else:
                limit = 50
                dir_x = pyxel.rndi(0,limit)
                if dir_x == 0:
                    dir_x = -1
                else:
                    if dir_x == limit:
                        dir_x = 1
                    else:
                        dir_x = 0
                megabonus250_x += BONUS_STEP * dir_x
                dir_y = pyxel.rndi(0,limit)
                if dir_y == 0:
                    dir_y = -1
                else:
                    if dir_y == limit:
                        dir_y = 1
                    else:
                        dir_y = 0
                megabonus250_y += BONUS_STEP * dir_y
                pyxel.blt(megabonus250_x -7 , megabonus250_y -9,0,48,176,16,8,1)
                pyxel.blt(megabonus250_x + 9, megabonus250_y -9,0,48,184,9,8,1)
                pyxel.blt(megabonus250_x -4, megabonus250_y ,0,60,184,4,8,1)
                pyxel.blt(megabonus250_x , megabonus250_y ,0,64,248,16,8,1)
        # Megabonus 500
        if megabonus500:
            if pyxel.frame_count == megabonus500_timer:
                megabonus500 = False
            else:
                limit = 50
                dir_x = pyxel.rndi(0,limit)
                if dir_x == 0:
                    dir_x = -1
                else:
                    if dir_x == limit:
                        dir_x = 1
                    else:
                        dir_x = 0
                megabonus500_x += BONUS_STEP * dir_x
                dir_y = pyxel.rndi(0,limit)
                if dir_y == 0:
                    dir_y = -1
                else:
                    if dir_y == limit:
                        dir_y = 1
                    else:
                        dir_y = 0
                megabonus500_y += BONUS_STEP * dir_y
                pyxel.blt(megabonus500_x -7 , megabonus500_y -9,0,48,176,16,8,1)
                pyxel.blt(megabonus500_x + 9, megabonus500_y -9,0,48,184,9,8,1)
                pyxel.blt(megabonus500_x -4, megabonus500_y ,0,60,184,4,8,1)
                pyxel.blt(megabonus500_x , megabonus500_y ,0,64,240,16,8,1)
        # Died
        if continue_ok:
            lives = LIVES
            score = 0
        if (hit or continue_ok) and lives > 0:
            if hit:
                lives -= 1
            # Reset bonus
            plane[0].guns = 1
            plane[0].rapidfire = False
            plane[0].rapidfire_timer = 0
            plane[0].rapidfire_counter = 0
            plane[0].flip = False 
            flip = False
            tryagain = True
            countdown = COUNTDOWN
            hit = False
            cleanup_entities(bullets,True)
            continue_ok = False
            gameover = False
            
        if lives == 0 and not gameover:
            tryagain = False
            gameover = True
            continue_game = CONTINUE_GAME
        if not gameover and not tryagain:
            draw_entities(plane)
        if stop:
            # END OF GAME : You WIN !!!
            pyxel.rect(WIDTH//2 - 80 , HEIGHT//2 - 60 + scroll_y, 160, 120, 0)
            pyxel.rectb(WIDTH//2 - 80 , HEIGHT//2 - 60 + scroll_y, 160, 120, 9)
            # 1943
            pyxel.blt(WIDTH//2 - 16 , HEIGHT//2 - 50 + scroll_y,0,128,112,32,16,0)
            # BATTLE OF MIDWAY
            pyxel.blt(WIDTH//2 - 24 , HEIGHT//2 - 30 + scroll_y,0,96,208,48,16,0)
            pyxel.text(WIDTH//2 - 40 , HEIGHT//2 - 12 + scroll_y,"by Eric TABBONE 2025",12)
            # SCORE or HIGH SCORE
            if score == high_score:
                pyxel.blt(WIDTH//2 - 44 , HEIGHT//2 + scroll_y,0,136,160,20,16,1)
                pyxel.blt(WIDTH//2 - 20 , HEIGHT//2 + scroll_y,0,64,224,64,16,1)
            else:
                pyxel.blt(WIDTH//2 - 16 , HEIGHT//2 + scroll_y,0,96,224,32,16,1)
            # SCORE
            number = score
            n_len = len(str(score)) 
            position = (n_len - 1)*8 
            for i in range(n_len,0,-1):
                digit = number % 10
                number = number // 10
                pyxel.blt(WIDTH//2 - (n_len*8)//2 + position + scroll_x, HEIGHT//2 + 16 + scroll_y, 0, 80+8*digit, 240, 8, 16, 1)
                position -= 9
            # Press space
            pyxel.blt(WIDTH//2 - 64 , HEIGHT//2 + 42 + scroll_y,0,128,0,32,8,0,0,1)
            pyxel.blt(WIDTH//2 - 32 , HEIGHT//2 + 42 + scroll_y,0,128,8,32,8,0,0,1)
            pyxel.blt(WIDTH//2  , HEIGHT//2 + 42 + scroll_y,0,128,16,32,8,0,0,1)
            pyxel.blt(WIDTH//2 + 32 , HEIGHT//2 + 42 + scroll_y,0,128,24,32,8,0,0,1) 
        if gameover:
            # GAME OVER
            pyxel.rect(WIDTH//2 - 80 , HEIGHT//2 - 50 + scroll_y, 160, 100, 0)
            pyxel.rectb(WIDTH//2 - 80 , HEIGHT//2 - 50 + scroll_y, 160, 100, 9)
            pyxel.blt(WIDTH//2 - 16 , HEIGHT//2 - 30 + scroll_y,0,128,128,32,16,0,0,2)
            # Press enter to continue
            # Continue
            if restart:
                pyxel.blt(WIDTH//2 - 64 , HEIGHT//2 + 10 + scroll_y,0,128,0,32,8,0,0,1)
                pyxel.blt(WIDTH//2 - 32 , HEIGHT//2 + 10 + scroll_y,0,128,8,32,8,0,0,1)
                pyxel.blt(WIDTH//2  , HEIGHT//2 + 10 + scroll_y,0,128,16,32,8,0,0,1)
                pyxel.blt(WIDTH//2 + 32 , HEIGHT//2 + 10 + scroll_y,0,128,24,32,8,0,0,1)   
            else:
                # Game OVER
                pyxel.blt(WIDTH//2 - 27 , HEIGHT//2 + 10 + scroll_y,0,128,80,32,8,0,0,1)
                pyxel.blt(WIDTH//2 + 5 , HEIGHT//2 + 10 + scroll_y,0,128,88,23,8,0,0,1)
            pyxel.blt(WIDTH//2 - 4 , HEIGHT//2 + 23 + scroll_y,0,80+8*continue_game,240,8,16,1,0,1)
            if pyxel.frame_count % FPS == 0:
                continue_game -= 1
            if continue_game <= 0:
                init(True)
        if tryagain or (takeoff and start) and not gameover:
            # Ready
            if countdown == 2:
                pyxel.blt(WIDTH//2 - 18 , HEIGHT//2 - 4 + scroll_y,0,96,192,38,8,1,0,2)
            # Steady 
            if countdown == 1:
                pyxel.blt(WIDTH//2 - 22 , HEIGHT//2 - 4 + scroll_y,0,96,200,43,8,1,0,2)
            # Go!
            if countdown == 0:
                pyxel.blt(WIDTH//2 - 11 , HEIGHT//2 - 4 + scroll_y,0,128,176,16,8,1,0,2)
                pyxel.blt(WIDTH//2 + 21 , HEIGHT//2 - 4 + scroll_y,0,128,184,6,8,1,0,2)
            if pyxel.frame_count % FPS*2 == 0:
                countdown -=1
                if countdown == -1:
                    tryagain = False
        if pause:
            pyxel.rect(WIDTH//2 - 30 , HEIGHT//2 - 8 + scroll_y, 60, 13, 0)
            pyxel.rectb(WIDTH//2 - 30 , HEIGHT//2 - 8 + scroll_y, 60, 13, 9)
            pyxel.text(WIDTH//2 - 17 ,HEIGHT//2 - 4 + scroll_y,"P A U S E",10)
        if not start :
            pyxel.rect(30 , 20 + scroll_y, WIDTH - 60, HEIGHT - 60, 0)
            # 1943
            pyxel.blt(WIDTH//2 - 16 , HEIGHT//2 - 80 + scroll_y,0,128,112,32,16,0,0,2)
            # BATTLE OF MIDWAY
            pyxel.blt(WIDTH//2 - 24 , HEIGHT//2 - 35 + scroll_y,0,96,208,48,16,0,0,2)
            # INFOS KEYS
            pyxel.text(WIDTH//2 - 60 , HEIGHT//2 + 5 + scroll_y,"APPUYER SUR ENTRER POUR JOUER",15)
            pyxel.text(WIDTH//2 - 55 , HEIGHT//2 + 24 + scroll_y,"APPUYER SUR P POUR LA PAUSE",7)
            pyxel.text(WIDTH//2 - 52 , HEIGHT//2 + 30 + scroll_y,"APPUYER SUR Q POUR QUITTER",7)
            pyxel.text(WIDTH//2 - 45 , HEIGHT//2 + 46 + scroll_y,"FLECHES : SE DEPLACER",12)
            pyxel.text(WIDTH//2 - 45 , HEIGHT//2 + 54 + scroll_y,"ESPACE  : TIRER",12)
            pyxel.text(WIDTH//2 - 45 , HEIGHT//2 + 62 + scroll_y,"ALT     : SUPER ARME",11)
            
App()
# Eric TABBONE eaodobrasil@gmail.com
# Nuit du Code 2025
# 05/06/2025 v1.1