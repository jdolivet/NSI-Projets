import pyxel

WIDTH = 256
HEIGHT = 256
FPS = 30
MAN_CENTER = 0
MAN_LEFT = -1
MAN_RIGHT = 1
SCORE_HEIGHT = 22
BACKGROUND_COLOR = 3
GROUND_COLOR = 11
SKY_COLOR = 6
INFOS_BACKGROUND = 2
SCORE_COLOR = 12
SCORE_COLOR_BORDER = 5
LINE_COLOR = 7
FIRE_NONE = 1
FIRE_LEFT = 8
FIRE_RIGHT = 14
TARGET_X1 = 10
TARGET_X2 = WIDTH - 30
TARGET_Y = int(2.5*HEIGHT/4) - 30
TARGET_DELAY = FPS * 2
TARGET_DELAY2 = FPS
gravity1 = 0.2
gravity2 = 0.2
GRAVITY = -5
EXPLOSION_SIZE = 0.007
EXPLOSION_MAX_CYCLE = 10
EXPLOSION_SPEED = 200
dots = []
MAX_TARGETS = 16
FIRE_LIMIT = HEIGHT//2

class Explosion:
    
    def __init__(self,x,y):
        for _ in range(40):
            angle = pyxel.rndi(0, 360)
            radius = pyxel.rndf(0, 1) 
            vx = EXPLOSION_SPEED * radius * pyxel.sin(angle)
            vy = EXPLOSION_SPEED * radius * pyxel.cos(angle)
            dots.append((x, y, vx, vy, 0))
            
    def update(self):
        dots_new = []
        for (x, y, vx, vy, dots_cycle) in dots:
            if dots_cycle <= EXPLOSION_MAX_CYCLE:
                x += vx * EXPLOSION_SIZE
                y += vy * EXPLOSION_SIZE
                dots_cycle += 1
                dots_new.append((x, y, vx, vy, dots_cycle))
        dots[:] = dots_new
        
    def draw(self):
        for x, y, *_ in dots:
            pyxel.pset(int(x), int(y), (pyxel.frame_count % 7) + 6)
    
    def explode(self,x, y, speed=100):
        dots_cycle = 0     
        for _ in range(40):
            angle = pyxel.rndi(0, 360)
            radius = pyxel.rndf(0, 1) ** 0.5
            vx = speed * radius * pyxel.sin(angle)
            vy = speed * radius * pyxel.cos(angle)
            dots.append((x, y, vx, vy, dots_cycle))
            
class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, fps=FPS, title="TIR AUX PIGEONS - BALL TRAP")
        self.highscore = 0
        # Sky
        pyxel.colors[6] = 0x9BFFFF
        # Red
        pyxel.colors[8] = 0xFF0000
        self.initVars()
        pyxel.run(self.update, self.draw)
        
    def initVars(self):
        self.dir = MAN_CENTER
        self.visor_width = self.visor_height = 20
        self.visor_circle = 14
        self.visor_color_normal = 0
        self.visor_color_fire = 8
        self.fire = FIRE_NONE
        self.score = 0
        self.targets = MAX_TARGETS
        self.speed = 1
        self.target = []
        self.target_next1 = pyxel.frame_count + TARGET_DELAY
        self.target_next2 = self.target_next1 + TARGET_DELAY2
        pyxel.mouse(False)
        self.target_x1 = TARGET_X1
        self.target_y1 = self.target_y2 = TARGET_Y
        self.target_x2 = TARGET_X2
        self.gravity1 = GRAVITY
        self.gravity2 = GRAVITY
        self.degrees1 = int(pyxel.rndi(30,50))
        self.degrees2 = int(pyxel.rndi(30,50))
        self.speed1 = int(pyxel.rndf(1.5,2))
        self.speed2 = int(pyxel.rndf(1.5,2))
        self.count = 0
        self.max_count = MAX_TARGETS
        self.game_over = False
        self.bullet_left = True
        self.bullet_right = True
        self.reload_left = False
        self.reload_right = False
        self.bullets = MAX_TARGETS
        self.bullets_empty = False
        self.fire_limit_alert = False
        self.success = []
        self.wheel_last = pyxel.mouse_wheel
        
    def update(self):
        if self.count >= MAX_TARGETS:
            self.game_over = True
        else:
            self.dir = MAN_CENTER
            if pyxel.frame_count > self.target_next1 and self.count <= MAX_TARGETS - 2:
                self.target_update(1)
                if self.target_x1 > pyxel.width:
                    self.count += 1
                    self.success.append(False)
                    self.target_x1 = TARGET_X1
                    self.target_y1 = TARGET_Y
                    self.gravity1 = GRAVITY
                    self.target_next1 = pyxel.frame_count + TARGET_DELAY
            if pyxel.frame_count > self.target_next2 and self.count <= MAX_TARGETS - 1:
                self.target_update(2)
                if self.target_x2 < 0:
                    self.count += 1
                    self.success.append(False)
                    self.target_x2 = TARGET_X2
                    self.target_y2 = TARGET_Y 
                    self.gravity2 = GRAVITY
                    self.target_next2 = pyxel.frame_count + TARGET_DELAY
            if pyxel.mouse_x < pyxel.width/3:
                self.dir = MAN_LEFT
            if pyxel.mouse_x > 2*pyxel.width/3:
                self.dir = MAN_RIGHT
            self.fire = FIRE_NONE
            self.reloading = False
            if (pyxel.mouse_wheel != self.wheel_last):
                self.reloading = True
            if self.reloading or pyxel.btnp(pyxel.KEY_SPACE) and self.bullets > 0:
                if self.reload_right:
                    self.bullet_right = True
                    self.reload_right = False
                if  self.reload_left:
                    self.bullet_left = True
                    self.reload_left = False
            if self.bullets <= 0:
                self.bullets_empty = True
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.bullet_left:
                if pyxel.mouse_y > FIRE_LIMIT:
                    self.fire_limit_alert = True
                    self.game_over = True
                self.fire = FIRE_LEFT
                self.bullet_left = False
                self.reload_left = True
                self.collision()
                self.bullets -= 1
            if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT) and self.bullet_right:
                if pyxel.mouse_y > FIRE_LIMIT:
                    self.fire_limit_alert = True
                    self.game_over = True
                self.fire = FIRE_RIGHT
                self.bullet_right = False
                self.reload_right = True
                self.collision()
                self.bullets -= 1
            Explosion.update(self)
            self.wheel_last = pyxel.mouse_wheel
            
    def draw(self):
        if self.game_over:
            self.end_width = 200
            self.end_height = 50
            # Game over message
            pyxel.rect(pyxel.width//2 - self.end_width//2,pyxel.height//2 - self.end_height//2,self.end_width,self.end_height,0)
            pyxel.text(pyxel.width//2 - self.end_width//2 + 10,pyxel.height//2 - self.end_height//2 + 10, "FIN DE LA COMPETITION", 7)
            pyxel.text(pyxel.width//2 - self.end_width//2 + 10,pyxel.height//2 - self.end_height//2 + 20, "RESULTAT:   SUR " + str(MAX_TARGETS) + " CIBLES POSSIBLES", 6)
            pyxel.text(pyxel.width//2 - self.end_width//2 + 50,pyxel.height//2 - self.end_height//2 + 20, str(self.score), 8)
            if self.score == self.highscore and self.score > 0:
                pyxel.text(pyxel.width//2 - self.end_width//2 + 10,pyxel.height//2 - self.end_height//2 + 30, "VOUS AVEZ EGALE LE MEILLEUR RESULTAT. BRAVO", 9)
            if self.score > self.highscore and self.score > 0:
                pyxel.text(pyxel.width//2 - self.end_width//2 + 10,pyxel.height//2 - self.end_height//2 + 30, "VOUS AVEZ LE MEILLEUR RESULTAT. EXCELLENT !", 10)
            if self.score > self.highscore:
                self.highscore = self.score
            pyxel.text(pyxel.width//2 - self.end_width//2 + 100,pyxel.height//2 - self.end_height//2 + 40, "TOUCHE R POUR PARTICIPER",7)
            if pyxel.btnp(pyxel.KEY_R):
                self.initVars()
        else:
            pyxel.cls(BACKGROUND_COLOR)
            self.background()
            self.infos()
            self.reload()
            self.target_draw()
            self.visor(self.fire)
            self.man(self.dir)
            self.triangles()
            self.showScore()
            Explosion.draw(self)
            
    def collision(self):
        self.target_square = 10
        if pyxel.mouse_x >= self.target_x1 - self.target_square and pyxel.mouse_x <= self.target_x1 + self.target_square:
            if pyxel.mouse_y >= self.target_y1 - self.target_square and pyxel.mouse_y <= self.target_y1 + self.target_square:
                Explosion(pyxel.mouse_x,pyxel.mouse_y)
                self.target_x1 = pyxel.width + 10
                self.score += 1
                self.success.append(True)
                self.degrees1 = int(pyxel.rndi(30,50))
                self.speed1 = int(pyxel.rndf(1.5,2.5))
        if pyxel.mouse_x >= self.target_x2 - self.target_square and pyxel.mouse_x <= self.target_x2 + self.target_square:
            if pyxel.mouse_y >= self.target_y2 - self.target_square and pyxel.mouse_y <= self.target_y2 + self.target_square:
                Explosion(pyxel.mouse_x,pyxel.mouse_y)
                self.target_x2 = 0
                self.score += 1
                self.success.append(True)
                self.degrees2 = int(pyxel.rndi(30,50))
                self.speed2 = int(pyxel.rndf(1.5,2.5))
       
     
    def target_update(self,target):
        # 1st left or right ? 0: left / 1: right
        if target == 1:
            self.gravity1 = self.gravity1 + gravity1
            self.target_x1 = self.target_x1 + pyxel.cos(self.degrees1) * self.speed1*5
            self.target_y1 = self.target_y1 - pyxel.sin(self.degrees1) * self.speed1 + self.gravity1
        else:
            self.gravity2 = self.gravity2 + gravity2
            self.target_x2 = self.target_x2 - pyxel.cos(self.degrees2) * self.speed2*5
            self.target_y2 = self.target_y2 - pyxel.sin(self.degrees2) * self.speed2 + self.gravity2
            
    def target_draw(self):
        self.target_width = 20
        self.target_height = 10
        self.target_color = 13
        pyxel.elli(self.target_x1-1,self.target_y1+1,self.target_width , self.target_height,0)
        pyxel.elli(self.target_x1,self.target_y1,self.target_width , self.target_height,self.target_color)
        pyxel.elli(self.target_x2-1,self.target_y2+1,self.target_width , self.target_height,0)
        pyxel.elli(self.target_x2,self.target_y2,self.target_width , self.target_height,self.target_color)
        
        
    def visor(self,fire):
        self.visor_color = fire
        if pyxel.mouse_y > FIRE_LIMIT:
            self.visor_color = 8
        pyxel.line(pyxel.mouse_x - self.visor_width//2, pyxel.mouse_y, pyxel.mouse_x + self.visor_width//2, pyxel.mouse_y, self.visor_color)
        pyxel.line(pyxel.mouse_x, pyxel.mouse_y - self.visor_height//2, pyxel.mouse_x, pyxel.mouse_y + self.visor_height//2, self.visor_color)
        if fire == FIRE_NONE:
            pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, self.visor_circle//2, self.visor_color)
        else:
            pyxel.circ(pyxel.mouse_x, pyxel.mouse_y, self.visor_circle//2, self.visor_color)
        pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, 2, self.visor_color)
        
            
    def man(self,dir):
        self.man_width = 20
        self.man_height = 40
        self.man_head = 24
        self.man_body_color = 8
        self.man_strip_color = 7
        self.headphone_color = 5
        self.headphone_offset = 2
        self.headphone_puff_width = 8
        self.headphone_puff_height = 12
        self.man_head_color = 4
        self.man_head_offset = 2
        self.man_arm_offset = 6
        self.gun_width = 4
        self.gun_height = 40
        self.bottom = pyxel.height - 30
        if dir == MAN_CENTER:
            # Gun
            pyxel.rect(pyxel.width //2 + self.man_width//2,self.bottom - self.man_height - self.gun_height, self.gun_width , self.gun_height , 0)
            # Arms
            pyxel.tri(pyxel.width //2 - self.man_width//2, self.bottom - self.man_height, pyxel.width //2 - self.man_width//2, self.bottom - self.man_height//3, pyxel.width//2 - self.man_width, self.bottom - self.man_height, self.man_body_color)
            pyxel.tri(pyxel.width //2 + self.man_width//2, self.bottom - self.man_height, pyxel.width //2 + self.man_width//2, self.bottom - self.man_height//3, pyxel.width//2 + self.man_width, self.bottom - self.man_height, self.man_body_color)
        if dir == MAN_RIGHT:
            # Gun
            for i in range (1,5):
                pyxel.line(pyxel.width //2 + self.man_width//2,self.bottom - self.man_height - i, pyxel.width //2 + self.man_width//2 + 40,self.bottom - self.man_height - self.gun_height - i, 0)
            # Arms
            pyxel.tri(pyxel.width //2 - self.man_width//2, self.bottom - self.man_height, pyxel.width //2 - self.man_width//2, self.bottom - self.man_height//3, pyxel.width//2 - self.man_width, self.bottom - self.man_height, self.man_body_color)
            pyxel.tri(pyxel.width //2 + self.man_width//2, self.bottom - self.man_height, pyxel.width //2 + self.man_width//2, self.bottom - self.man_height//2, pyxel.width//2 + int(1.5*self.man_width), self.bottom - self.man_height - 20, self.man_body_color)
            pyxel.tri(pyxel.width //2 + self.man_width//2, self.bottom - self.man_height + self.man_arm_offset, pyxel.width //2 + self.man_width//2, self.bottom - self.man_height//2 - self.man_arm_offset, pyxel.width//2 + int(1.5*self.man_width) - self.man_arm_offset *1.5, self.bottom - self.man_height + int(0.5*self.man_arm_offset) - 10, BACKGROUND_COLOR)
        if dir == MAN_LEFT:
            # Gun
            for i in range (1,5):
                pyxel.line(pyxel.width //2 + self.man_width//2,self.bottom - self.man_height - i, pyxel.width //2 + self.man_width//2 - 40,self.bottom - self.man_height - self.gun_height - i, 0)
            # Arms
            pyxel.tri(pyxel.width //2 - self.man_width//2, self.bottom - self.man_height, pyxel.width //2 - self.man_width//2, self.bottom - int(0.5*self.man_height//3), pyxel.width//2 - self.man_width + self.man_width//4, self.bottom - self.man_height, self.man_body_color)
            pyxel.tri(pyxel.width //2 + self.man_width//2, self.bottom - self.man_height, pyxel.width //2 + self.man_width//2, self.bottom - self.man_height//2, pyxel.width//2 - int(1*self.man_width), self.bottom - self.man_height - 30, self.man_body_color)
            
        # Body
        pyxel.rect(pyxel.width //2 - self.man_width//2, self.bottom - self.man_height , self.man_width,self.man_height , self.man_body_color)
        # Strip
        for i in range (1, 8):
            pyxel.rect(pyxel.width //2 - self.man_width//2, self.bottom - self.man_height + i*4 , self.man_width, 2, self.man_strip_color)
        # Headphone
        pyxel.circ(pyxel.width //2 , self.bottom - self.man_height - self.man_head//2 - self.headphone_offset, self.man_head//2, self.headphone_color)
        pyxel.circ(pyxel.width //2 , self.bottom - self.man_height - self.man_head//2 + self.man_head_offset, self.man_head//2, self.man_head_color)
        pyxel.elli(pyxel.width //2 - self.man_head//2 - self.headphone_puff_width//2, self.bottom - self.man_height - self.man_head//2 - self.headphone_puff_height//2, self.headphone_puff_width, self.headphone_puff_height, self.headphone_color)
        pyxel.elli(pyxel.width //2 + self.man_head//2 - self.headphone_puff_width//2, self.bottom - self.man_height - self.man_head//2 - self.headphone_puff_height//2, self.headphone_puff_width, self.headphone_puff_height, self.headphone_color)
        
    
    def infos(self):
        self.infos_color_title = 6
        self.infos_color_infos =7
        self.infos_color = 10
        self.infos_offset = 6
        self.infos_pos_y = pyxel.height - 27
        pyxel.text(5, self.infos_pos_y, "BIENVENUE AUX JO 2024 DE PARIS" , self.infos_color_title)
        pyxel.text(143, self.infos_pos_y, "TIR AUX PIGEONS - BALL TRAP", self.infos_color_title)
        self.infos_pos_y += self.infos_offset
        pyxel.text(5, self.infos_pos_y, "VOUS AVEZ " + str(MAX_TARGETS) + " CIBLES A ATTEINDRE, SOYEZ RAPIDE." , self.infos_color_infos)
        self.infos_pos_y += self.infos_offset + 2
        pyxel.text(5, self.infos_pos_y, "TIRER: BOUTONS SOURIS GAUCHE/DROITE" , self.infos_color)
        self.infos_pos_y += self.infos_offset
        pyxel.text(5, self.infos_pos_y, "RECHARGER: MOLETTE SOURIS/ESPACE" , self.infos_color)
        pyxel.text(168, self.infos_pos_y, "QUE LE MEILLEUR GAGNE" , self.infos_color_infos)
        
    def showScore(self):
        self.bullets_pos_x = 5
        self.score_pos_y = 3
        self.bullets_offset = 55
        self.score_space_x = 10
        self.score_color_yes = 7
        self.score_color_no = 8
        self.highscore_pos_x = 165
        self.score_circle = 4
        self.score_spaces = 16
        self.score_circle_offset = 4
        pyxel.text(self.bullets_pos_x, self.score_pos_y,"CIBLES : ",6)
        if MAX_TARGETS - self.count >= 0:
            self.result = MAX_TARGETS - self.count
        else :
            self.result = 0
        pyxel.text(self.bullets_pos_x + 34,self.score_pos_y,str(self.result),self.score_color_yes)
        pyxel.text(self.bullets_pos_x + self.bullets_offset,self.score_pos_y ,"CARTOUCHES : ",6)
        if self.bullets> 4:
            self.score_color = self.score_color_yes
        else:
            self.score_color = self.score_color_no
        pyxel.text(self.bullets_pos_x + self.bullets_offset + 50,self.score_pos_y,str(self.bullets ),self.score_color)
        pyxel.text(self.highscore_pos_x, self.score_pos_y,"MEILLEUR RESULTAT : ",10)
        pyxel.text(self.highscore_pos_x + 80, self.score_pos_y,str(self.highscore),10)
        self.score_pos_y += 12
        for i in range(0,MAX_TARGETS):
            if i < len(self.success):
                if self.success[i] == True:
                    pyxel.circ(i*self.score_spaces+self.score_circle + self.score_circle_offset,self.score_pos_y,self.score_circle,11)
                else:
                    pyxel.circ(i*self.score_spaces+self.score_circle + self.score_circle_offset,self.score_pos_y,self.score_circle,8)
            else:
                pyxel.circb(i*self.score_spaces+self.score_circle + self.score_circle_offset,self.score_pos_y,self.score_circle,0)
        
    def background(self):
        self.infos_height = 30
        self.score_border = 15
        self.line_offset = 10
        # Ground
        pyxel.rect(0, 0, pyxel.width, pyxel.height//2 - self.line_offset,GROUND_COLOR)
        # Sky
        pyxel.rect(0,0,pyxel.width,pyxel.height//3,SKY_COLOR)
        #pyxel.rect(0, pyxel.height//3, pyxel.width, pyxel.height//3 - pyxel.height//2,GROUND_COLOR)
        # Score
        pyxel.rect(0,0,pyxel.width,SCORE_HEIGHT,SCORE_COLOR)
        pyxel.rectb(0,0,pyxel.width,SCORE_HEIGHT,SCORE_COLOR_BORDER)
        pyxel.rect(0,pyxel.height- self.infos_height,pyxel.width,pyxel.height,INFOS_BACKGROUND)
        #pyxel.rect(0,pyxel.height- SCORE_HEIGHT,pyxel.width,pyxel.height,self.infos_background)
        pyxel.rectb(0,pyxel.height - self.infos_height,pyxel.width,pyxel.height,SCORE_COLOR_BORDER)
        pyxel.line(0,pyxel.height//2 - self.line_offset,pyxel.width,pyxel.height//2  - self.line_offset,LINE_COLOR)
        
    def reload(self):
        self.gun_width = 18
        self.gun_height = 16
        self.gun_top = SCORE_HEIGHT + 4
        self.gun_left = 5
        self.gun_color = 4
        self.gun_full = 11
        self.relaod_top = self.empty_top = self.gun_top + 27
        self.relaod_left = 7
        self.gun_empty_left = 5
        self.relaod_color = 8
        self.bullet_color = 12
        self.bullet_left_empty = self.gun_left + 5
        self.bullet_right_empty = self.gun_left + self.gun_width + self.gun_height- 2
        self.gun_color_left  = self.gun_color_right = 0
        pyxel.text(self.gun_left,self.gun_top,"CARTOUCHES",self.bullet_color)
        self.gun_top += 8
        self.gun_left += 10
        pyxel.circ(self.gun_left, self.gun_top + self.gun_height // 2 -1, self.gun_height//2 -1, self.gun_color)
        pyxel.circ(self.gun_left + self.gun_width ,self.gun_top + self.gun_height // 2 -1, self.gun_height//2 -1, self.gun_color)
        pyxel.rect(self.gun_left,self.gun_top,self.gun_width ,self.gun_height, self.gun_color)
        if self.bullet_left:
            self.gun_color_left = self.gun_full
        if self.bullet_right:
            self.gun_color_right = self.gun_full
        pyxel.circ(self.gun_left + 2 , self.gun_top + self.gun_height // 2 -1, self.gun_height//3, self.gun_color_left)
        pyxel.circ(self.gun_left + self.gun_width - 2 , self.gun_top + self.gun_height // 2 -1, self.gun_height//3, self.gun_color_right)
        if self.bullets_empty:
            if pyxel.frame_count % (FPS/2) > 0:
                pyxel.text(self.gun_empty_left,self.empty_top, " PLUS DE", 8)
                self.empty_top += 8
                pyxel.text(self.gun_empty_left,self.empty_top, "CARTOUCHES", 8)
        else:
            if self.reload_left and self.reload_right:
                if pyxel.frame_count % (FPS/2) > 0:
                    pyxel.text(self.relaod_left,self.relaod_top, "RECHARGER", 8)
            else:
                if self.reload_left:
                    if pyxel.frame_count % (FPS/2) > 0:
                        pyxel.text(self.bullet_left_empty,self.relaod_top, "R", 8)
                if self.reload_right:
                    if pyxel.frame_count % (FPS/2) > 0:
                        pyxel.text(self.bullet_right_empty,self.relaod_top, "R", 8)
            
        
    def triangles(self):
        self.stand_color = 9
        self.stand_margin = 40
        self.stand_width = 20
        self.stand_height = 40
        self.stand_y = int(2.5*pyxel.height/4)
        pyxel.tri(-self.stand_margin, self.stand_y, self.stand_width, self.stand_y, self.stand_width, self.stand_y - self.stand_height, self.stand_color)
        pyxel.tri(pyxel.width + self.stand_margin, self.stand_y, pyxel.width - self.stand_width, self.stand_y, pyxel.width - self.stand_width, self.stand_y - self.stand_height, self.stand_color)
        
App()
