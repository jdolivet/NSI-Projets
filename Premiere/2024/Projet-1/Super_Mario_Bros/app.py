# Pyxel Studio

# Pyxel Studio

import pyxel
import random

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16

    def update(self):
        self.x -= 2
        if self.x < 0:
            self.x = random.randint(240, 250)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class App:
    def __init__(self):
        pyxel.init(150, 120)
        self.player_image = pyxel.image(0)
        self.obstacle_image = pyxel.image(1)
        pyxel.load("res.pyxres")  # Carrega o arquivo de recurso
        self.reset_game()
        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.player = Player(10, 104)
        self.obstacles = [Obstacle(150, 104), Obstacle(230, 104), Obstacle(310, 104)]
        self.jump = False
        self.game_over = False
        self.jump_height = 3

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R):
                self.reset_game()
            return

        if pyxel.btnp(pyxel.KEY_SPACE) and not self.jump:
            self.jump = True

        if self.jump:
            self.player.y -= self.jump_height
            if self.player.y < 75:
                self.jump = False
        else:
            if self.player.y < 104:
                self.player.y += self.jump_height

        for obstacle in self.obstacles:
            obstacle.update()
            if abs(self.player.x - obstacle.x) < 6 and abs(self.player.y - obstacle.y) < 6:
                self.game_over = True

    def draw(self):
        pyxel.cls(0)
        if self.game_over:
            pyxel.text(2, 50, "Game Over! Appuyer 'R' pour réessayer", pyxel.frame_count % 16)
        else:
            pyxel.blt(self.player.x, self.player.y, 0, 0, 0, 20, 16, 0) 
            for obstacle in self.obstacles:
                pyxel.blt(obstacle.x, obstacle.y, 1, 0, 0, 16, 16, 0) 
         

App()