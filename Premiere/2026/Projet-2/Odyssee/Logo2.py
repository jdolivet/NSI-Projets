import pyxel as px
import sys
import os

px.init(150, 120, "L'Odyssée")
px.load("logo.pyxres")


def update():
    if px.btnp(px.KEY_SPACE):
        os.execv(sys.executable, [sys.executable, "MAIN3.py"])
        


def draw():
    px.cls(0)
    px.blt(45, 34, 0, 0, 0, 56, 16)
    px.text(5, 65, "appuyer sur 'espace' pour continuer", 7)

px.run(update, draw)