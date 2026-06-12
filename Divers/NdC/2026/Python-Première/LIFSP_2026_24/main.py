"""
Ce jeux est de minimalisme extreme, fait especialment pour des profs.
Il suit exactement le KISS (Keep It Simple, Stupid).

Prenez les diamands, bouger avec les arrow keys, faites en moins de 15 secondes et voila.
"""

import pyxel


class App:
    def __init__(self):

        pyxel.init(128, 128, title="nuit du code")
        pyxel.load("U3.pyxres")

        self.jump = 1
        self.n_diamond = 0
        self.xplayer = 50
        self.yplayer = 100
        self.regard = 16
        self.yfloor = 112
        self.maxregard = 0
        self.xback03 = 0
        self.yback03 = 64

        self.diamond = [
            [40, 20, True],
            [87, 22, True],
            [60, 20, True],
            [22, 67, True],
            [100, 60, True],
        ]

        self.tempo = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.movimentation_player()
        self.verifiercol()
        self.diamondtouche()
        if pyxel.frame_count % 10 == 0:
            self.tempo += 1

    def draw(self):
        if self.n_diamond != 5 and self.tempo < 15:
            pyxel.bltm(0, 0, 0, 0, 0, 128, 128)

            pyxel.blt(
                self.xplayer, self.yplayer, 0, 48, self.yfloor, self.regard, 16, 1
            )

            pyxel.text(0, 20, f"{self.n_diamond}", 10)
            pyxel.text(0, 25, f"{self.tempo}", 10)

            for d in self.diamond:
                if d[2] == True:
                    pyxel.blt(d[0], d[1], 0, 96, 32, 16, 16, 1)
        elif self.tempo >= 15:
            pyxel.cls(1)
            pyxel.text(50, 50, "Perdu", 20)
        elif self.n_diamond == 5:
            pyxel.cls(1)
            pyxel.text(50, 50, "Gagnez", 20)

    def movimentation_player(self):
        if self.xplayer >= 0 and self.xplayer <= 128:
            if pyxel.btn(pyxel.KEY_LEFT):
                self.xplayer += -1
                self.regard = -16
                if pyxel.frame_count % 4 == 0:
                    self.yfloor = 128
                else:
                    self.yfloor = 112
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.xplayer += 1
                self.regard = 16
                if pyxel.frame_count % 4 == 0:
                    self.yfloor = 128
                else:
                    self.yfloor = 112
            if pyxel.btn(pyxel.KEY_UP) and self.yplayer >= 0:
                for i in range(10):
                    self.yplayer -= 1
            else:
                if not self.verifiercol():
                    self.yplayer += 2
        if self.xplayer == 128:
            self.xplayer -= 5
        if self.xplayer == 0:
            self.xplayer += 5

    def verifiercol(self):
        if self.yplayer <= 105:
            return False
        return True

    def diamondtouche(self):
        for d in self.diamond:
            if abs(self.xplayer - d[0]) <= 5 and abs(d[1] - self.yplayer) <= 5:
                if d[2]:
                    d[2] = False
                    self.n_diamond += 1


App()
