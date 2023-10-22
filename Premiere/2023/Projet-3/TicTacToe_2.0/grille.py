import pyxel

def dessiner_grille():  
    pyxel.line(66, 0, 66, 200, 8)
    pyxel.line(133, 0, 133, 200, 8)
    
    pyxel.line(0, 66, 200, 66, 8)
    pyxel.line(0, 133, 200, 133, 8)

    pyxel.flip()