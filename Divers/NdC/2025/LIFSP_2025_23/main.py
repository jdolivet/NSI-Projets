# regles du jeu
# appuyez sur, 1, 2, et/ou 3 pour faire apparaitres les personages respectives
#un ninja, un skeleton, ou un mage
#utilisez les touches wasd, ijkl, ou les fleches du clavier pour bouger
#explorez la map et profitez!






import pyxel
import random
import time
def init():
    pyxel.init(128, 128, "Nuit du Code", fps = 60)
    pyxel.load("2.pyxres")

def cpt_frame():
    global cpt
    if pyxel.frame_count % 1 == 0:
        cpt += 1
    if cpt > 30:
        cpt = 0
    
cpt = 0

x_ninja = 70
y_ninja = -70000

x_skel = -90000
y_skel = -700000

imgx_skel = 64
imgy_skel = 16
imgX_skel = 15
imgY_skel = 16

imgx_ninja = 0
imgy_ninja = 16
imgX_ninja = 15
imgY_ninja = 16

x_mage = -50000
y_mage = -70000
imgx_mage = 128 
imgy_mage = 16
imgX_mage = 15
imgY_mage = 16

col1 = 0
col2 = 0
col3 = 0

mage_vies = 3
ninja_vies = 3
skel_vies = 3


def colision_epee():
    global x_épée
    global y_épée
    if x_épée == x_mage:
        mage_vies = -1
    if x_épée == x_skel:
        skel_vies = -1
    print(mage_vies, skel_vies)
        


def interface_début():
    pyxel.text(23, 3, "Select 2 players", col1)
    pyxel.text(23, 10, "Click on 1 for skeleton", col1)
    pyxel.text(23, 17, "Click on 2 for ninja", col2)
    pyxel.text(23, 24, "Click on 3 for wizard", col3)
    
def choisir_persos():
    global x_skel
    global y_skel
    global x_ninja
    global y_ninja
    global x_mage
    global y_mage
    global col1
    global col2
    global col3
    
    if pyxel.btn(pyxel.KEY_1):
        x_skel = 90
        y_skel = 90
        col1 = 7
    if pyxel.btn(pyxel.KEY_2):
        x_ninja = 30
        y_ninja = 90
        col2 = 7
    if pyxel.btn(pyxel.KEY_3):
        x_mage = 50
        y_mage = 90
        col3 = 7
        
        

def quitter():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
        
       
def colisions_bord():
    global x_skel
    global y_skel
    global x_ninja
    global y_ninja
    global x_mage
    global y_mage
    
    
    if x_mage + 14 > 128:
        x_mage -= 1
    if x_skel + 14 > 128:
        x_skel -= 1
    if x_ninja + 14 > 128:
        x_ninja -= 1
    if x_mage < 0:
        x_mage += 1
    if x_ninja < 0:
        x_ninja += 1
    if x_skel < 0:
        x_skel += 1
        
    
def colisions_caisse1():
    global x_skel
    global y_skel
    global x_ninja
    global y_ninja
    global x_mage
    global y_mage
    
    if 31 < x_skel < 38:
        x_skel -= 1
    
    if 31 < x_mage < 38:
        x_mage -= 1
    
    if 30 < x_ninja < 38:
        x_ninja -= 1    
        
def colisions_caisse2():
    global x_skel
    global y_skel
    global x_ninja
    global y_ninja
    global x_mage
    global y_mage
    
    if 84 < x_skel < 90: 
        x_skel += 1
    
    if 84 < x_mage < 90: 
        x_mage += 1
    
    if 84 < x_ninja < 90: 
        x_ninja += 1    
    
def bouger_ninja():
    global y_ninja
    global x_ninja
    global imgx_ninja
    global imgy_ninja
    global imgX_ninja
    global imgY_ninja
    global cpt
    if pyxel.btn(pyxel.KEY_A):
         x_ninja -= 1
         if cpt == 0:
             imgx_ninja = 0
             imgy_ninja = 16
             imgX_ninja = -15
             imgY_ninja = 16
         if cpt == 7:
             imgx_ninja = 16
             imgy_ninja = 16
             imgX_ninja = -15
             imgY_ninja = 16
         if cpt == 14:    
             imgx_ninja = 32
             imgy_ninja = 16
             imgX_ninja = -15
             imgY_ninja = 16
         if cpt == 22:  
             imgx_ninja = 48
             imgy_ninja = 16
             imgX_ninja = -15
             imgY_ninja = 16
        
    if pyxel.btn(pyxel.KEY_D):
         x_ninja += 1
         if cpt == 0:
             imgx_ninja = 0
             imgy_ninja = 16
             imgX_ninja = 15
             imgY_ninja = 16
         if cpt == 7:
             imgx_ninja = 16
             imgy_ninja = 16
             imgX_ninja = 15
             imgY_ninja = 16
         if cpt == 14:    
             imgx_ninja = 32
             imgy_ninja = 16
             imgX_ninja = 15
             imgY_ninja = 16
         if cpt == 22:  
             imgx_ninja = 48
             imgy_ninja = 16
             imgX_ninja = 15
             imgY_ninja = 16
         if pyxel.btn(pyxel.KEY_W):
            y_ninja -= 1
         if pyxel.btn(pyxel.KEY_S):
            y_ninja += 1

            
        

        
        


        
def bouger_skel():
    global x_skel
    global y_skel
    global imgx_skel
    global imgy_skel
    global imgX_skel
    global imgY_skel
    global cpt
    if pyxel.btn(pyxel.KEY_LEFT):
         x_skel -= 1
         if cpt == 0:
             imgx_skel = 64
             imgy_skel = 16
             imgX_skel = 15
             imgY_skel = 16
         if cpt == 7:
             imgx_skel = 80
             imgy_skel = 16
             imgX_skel = 15
             imgY_skel = 16
         if cpt == 14:    
             imgx_skel = 96
             imgy_skel = 16
             imgX_skel = 15
             imgY_skel = 16
         if cpt == 22:  
             imgx_skel = 112
             imgy_skel = 16
             imgX_skel = 15
             imgY_skel = 16
        
    if pyxel.btn(pyxel.KEY_RIGHT):
         x_skel += 1
         if cpt == 0:
             imgx_skel = 64
             imgy_skel = 16
             imgX_skel = -15
             imgY_skel = 16
         if cpt == 7:
             imgx_skel = 80
             imgy_skel = 16
             imgX_skel = -15
             imgY_skel = 16
         if cpt == 14:    
             imgx_skel = 96
             imgy_skel = 16
             imgX_skel = -15
             imgY_skel = 16
         if cpt == 22:  
             imgx_skel= 112
             imgy_skel = 16
             imgX_skel = -15
             imgY_skel = 16
         if pyxel.btn(pyxel.KEY_UP):
                y_skel -= 1
         if pyxel.btn(pyxel.KEY_DOWN):
                y_skel += 1
                    
         

def bouger_mage():
    global y_mage
    global x_mage
    global imgx_mage
    global imgy_mage
    global imgX_mage
    global imgY_mage
    if pyxel.btn(pyxel.KEY_L):
        x_mage += 1
        imgX_mage = -15
        
    if pyxel.btn(pyxel.KEY_J):
        x_mage -= 1
        imgX_mage = 15
    if pyxel.btn(pyxel.KEY_I):
        y_mage -= 1
    if pyxel.btn(pyxel.KEY_K):
        y_mage += 1
        

def epée():
    pass



def update():
    bouger_ninja()
    bouger_skel()
    bouger_mage()
    cpt_frame()
    quitter()
    choisir_persos()
    #colisions_bord()
    #colisions_caisse1()
    #colisions_caisse2()
    
def draw():
    pyxel.cls(7)
    global x_ninja
    global y_ninja
    global imgx_ninja
    global imgy_ninja
    global imgX_ninja
    global imgY_ninja
    global x_épée
    global y_épée
    interface_début()
    pyxel.blt(x_ninja, y_ninja, 0, imgx_ninja, imgy_ninja, imgX_ninja, imgY_ninja, 2, 0, 1)
    pyxel.blt(x_skel, y_skel, 0, imgx_skel, imgy_skel, -imgX_skel, imgY_skel, 2, 0, 1)
    pyxel.blt(x_mage, y_mage, 0, imgx_mage, imgy_mage, imgX_mage, imgY_mage, 2, 0, 1)
    pyxel.blt(58, 90, 0, 16, 32, 15, 16, 2, 0, 1)
    pyxel.blt(44, 90, 0, 0, 96, 16, 16, 2, 0, 1)
    pyxel.blt(16, 50, 0, 16, 96, 16, 16, 2, 0, 1)
    pyxel.blt(0, 50, 0, 0, 96, 16, 16, 2, 0, 1)
    pyxel.blt(76, 90, 0, 0, 96, 16, 16, 2, 0, 1)
    pyxel.blt(76, 74, 0, 16, 96, 16, 16, 2, 0, 1)
    pyxel.blt(44, 30, 0, 0, 96, 16, 16, 2, 0, 1)
    pyxel.blt(60, 30, 0, 32, 96, 16, 16, 2, 0, 1) 
    pyxel.blt(76, 61, 0, 0, 48, 16, 16, 2, 0, 1)
    pyxel.blt(58, 80, 0, 16, 48, 16, 16, 2, 0, 1)
    pyxel.blt(44, 76, 0, 32, 48, 16, 16, 2, 0, 1)
    pyxel.blt(0, 38, 0, 64, 64, 16, 16, 2, 0, 1)
    pyxel.blt(0, 96, 0, 80, 64, 16, 16, 2, 0, 1)
    pyxel.blt(30, 70, 0, 96, 64, 16, 16, 2, 0, 1)
    pyxel.blt(46, 106, 0, 112, 16, 16, 2, 0, 1)
    pyxel.blt(44, 14, 0, 16, 80, 16, 16, 2, 0, 1)
    pyxel.blt(60, 14, 0, 32, 80, 16, 16, 2, 0, 1)
    pyxel.blt(62, 40, 0, 48, 80, 16, 16, 2, 0, 1)
    pyxel.blt(78, 55, 0, 64, 80, 16, 16, 2, 0, 1)
    pyxel.blt(94, 15, 0, 80, 80, 16, 16, 2, 0, 1)
    pyxel.blt(16, 36, 0, 32, 64, 16, 16, 2, 0, 1)
    pyxel.blt(120, 45, 0, 128, 32, 16, 16, 2, 0, 1)
    
init()
pyxel.run(update, draw)