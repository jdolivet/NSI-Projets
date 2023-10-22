import pyxel

def dessiner_o(x, y):
    pyxel.circb(x, y, 20, 10)  
    pyxel.flip()

def dessiner_x(x, y):
    pyxel.line(x - 20, y - 20, x + 20, y + 20, 6)  
    pyxel.line(x + 20, y - 20, x - 20, y + 20, 6)
    pyxel.flip()



