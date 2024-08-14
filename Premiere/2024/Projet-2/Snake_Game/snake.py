import pyxel as PX
import tkinter as tk
from tkinter import ttk

def nova_tela():

 global score, max_score, passoX, passoY, root, reiniciar
 
 if reiniciar=="n" : return
 
 # enregistre le score plus élevé
 if score>max_score : max_score=score
    
 # ajuste la vitesse et le message en fonction du score
 if score <= 10:
          txt1= "Imbecille!"
          passoX= [ 1,  -1,   0,   0 ]
          passoY= [ 0,   0,   1,  -1 ]
 elif score <= 20:
          txt1="Bien"
          passoX= [ 1.5,  -1.5,   0,    0 ]
          passoY= [  0,    0,     1.,  -1.5 ]
 else:
          txt1="Tres bien!"
          passoX= [ 2,  -2,   0,   0 ]
          passoY= [ 0,   0,   2,  -2 ]

 root = tk.Tk()
 root.title("SNAKE")
 root.geometry('600x400+50+50')
 
 # couleur du texte et du arrière plan du texte
 style = ttk.Style()
 style.configure("TLabel", foreground="blue", background="lightblue")

 # couleur de l'arrière plan de la fenêtre principale
 root.configure(bg='lightblue')

 txt1= "\n\n\n\n\n" + txt1 + " Votre score est " + f"{score:04}" + "\n\n"
 msg1 = ttk.Label(root, text=txt1, style="TLabel")
 msg1.pack()

 # crée et affiche le bouton de redémarrage
 button1= ttk.Button(root, text='cliquez ici pour recommencer.',command=click3)
 button1.pack()

 # crée et affiche le bouton pour terminer
 button2= ttk.Button(root, text='cliquez ici pour terminer.',command=click4)
 button2.pack()

 root.mainloop()

 print(" vous avez quitté le nouvel écran ")


def carrega_bd():

 global jogadores
 
 # ouvre le fichier de joueurs
 with open("Snake.txt", 'r') as arquivo:

    for linha in arquivo:
          
          # supprimer les contrôles et les espaces inutiles de la ligne
          linha = linha.strip()
          
          # si il y a une ligne vide, ignore
          if len(linha)==0:
              continue
            
          separados = linha.split(",") 
          nome = separados[0]
          score = int( separados[1] )
         
          # garde dans le dictionnaire
          jogadores[nome]= score

 arquivo.close()    

def click1():
    
 global jogadores, button1, entry1, quem_joga, ordenados
 
 # obtient le nom des joeurs
 quem_joga = entry1.get()
 #message = ttk.Label(root, text=nome)
 #message.pack()

 # crée un dictionnaire vide {jogador:score}
 jogadores={}

 # lit le fichier des joeurs et charge le dictionnaire
 carrega_bd()
 alterou="0"
 
 # trier par score (en ordre décroissant)
 ordenados = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True) )
 
 # affiche les 10 plus grands joeurs de la galaxie
 msg4 = ttk.Label(root, text="\n\n\nLes Plus Grands Joueurs de la Galaxie:\n", style="TLabel" )
 msg4.pack()
 i=0
 for nome, score in ordenados.items():
         
         # crée une ligne avec le nom du joeur , score, et new line
         i=i+1
         if i>10 : break
         linha= nome + ", " + str(score)
         msg5 = ttk.Label(root, text=linha,  style="TLabel")
         msg5.pack()
         
 button1.destroy()
 entry1.destroy()
 msg1.destroy()
 msg2.destroy()
 
 msg5 = ttk.Label(root, text="\n",  style="TLabel")
 msg5.pack()

 # crée et affiche le bouton pour démarrer le jeu
 txt2= "cliquez ici pour démarrer le jeu."
 if len(quem_joga)>0 : txt2= quem_joga + ", " + txt2
 button2= ttk.Button(root, text=txt2,command=click2)
 button2.pack()

def click2():   # le jeu commence
    
 global root, reiniciar
 
 root.destroy() # ferme le tkinter

 
def click3():   # redémarrage du jeu
    
 global root, reiniciar
 reiniciar="s"
 root.destroy() # ferme le tkinter
 
def click4():   # terminer le jeu
    
 global root, reiniciar
 reiniciar="n"
 root.destroy() # ferme le tkinter

def grava_bd():

 global ordenados, pontos

 with open("Snake.txt", "w") as arquivo:
                
      # loop pour enregistrer toutes les joeurs
      for nome, score in ordenados.items():
         
         # créer une ligne avec le nom du joueur , score, e new line
         linha= nome + ", " + str(score) + "\n"
         arquivo.writelines(linha)

      # graver la marque de fin
      # arquivo.writelines("*eof\n")
      arquivo.close()

 print("Base de données enregistrée avec succès")
 return(0)

       
            
def colisao(x1, y1, larg1, alt1, x2, y2, larg2, alt2):

 # si les deux rectangles entrent en collision, renvoie True 
 if (x1<x2+larg2 and x1+larg1>x2 and y1<y2+alt2 and y1+alt1>y2):
    return (True)
 else:
    return(False)

def draw():
    
 global score, larg_fg, alt_fg, appleX, appleY, snakeX, snakeY, direc
 
 # si le jeu se termine, il affiche un écran avec des messages et revient
 if fim_de_jogo == True:
    nova_tela()
    return
  
 # l'écran devient vide
 PX.cls(3) # arrière plan =3 vert
 
 # dessine la barre avec le score     
 draw_score()
 
 # dessine la tête du serpent
 PX.rect(snakeX[0], snakeY[0], larg_fg, alt_fg, 10) #  couleur 10=jaune
 
 # dessine la queue du serpent
 PX.rect(snakeX[-1], snakeY[-1], larg_fg, alt_fg, 0) # couleur 0=nour
 
 # dessine le corps du serpent
 max = len(snakeX)-1
 for i in range( 1, max):
     PX.rect(snakeX[i], snakeY[i], larg_fg, alt_fg, 11) # couleur 11=vert
   

 # dessine la pomme en forme de cercle et ajuste
 PX.circ(appleX+4, appleY+4, 3, 8)   # raio=3 couleur 8=rouge
 PX.pset(appleX+5, appleY, 11)       # feuille: couleur 11=vert dans la pomme
 PX.rect(appleX,  appleY+7, 8, 1, 3) # aplati la pomme 3=couleur de l'arrière plan
 
def draw_msg(): # Menssage de fin du jeu
    
 global score, passoX, passoY

 # vide l'écran
 PX.cls(12)  # couleur 12 = bleu

 # dessine la barre avec le score
 draw_score()
 
 # ajuste la vitesse en fonction du score
 if score <= 10:
          PX.text(5, 10, "Imbecille!", 0)  # 0= noir, couleur 5 lin 10
          passoX= [ 1,  -1,   0,   0 ]
          passoY= [ 0,   0,   1,  -1 ]
 elif score <= 20:
          PX.text(5, 10, "Bien", 0)  # 0=noir, couleur 5 lin 10
          passoX= [ 1.5,  -1.5,   0,    0 ]
          passoY= [  0,    0,     1.,  -1.5 ]
 else:
          PX.text(5, 10, "Tres bien!", 0)  # 0=noir, couleur 5 lin 10
          passoX= [ 2,  -2,   0,   0 ]
          passoY= [ 0,   0,   2,  -2 ]

          
 PX.text(5, 25, '    Tapez "r" ', 0)  # 0=noir couleur 5, lin 25
 PX.text(5, 33, '       pour ', 0)    # 0=noir couleur 5, lin 33
 PX.text(5, 41, '   recommencer', 0)  # 0=noir couleur 5, lin 41

 
def draw_score():

 global score
 
 # dessine la barre du score col 0 lin 0  couleur 5=bleu foncé
 PX.rect(0, 0, larg_tel, alt_bar, 5)
 
 # ecrit le score dans la couleur 1 lin 1 avec 4 chiffres
 PX.text(1, 1, f"{score:04}", 6) # couleur du texte  6= bleu clair


def generate_apple(): # Fait apparaître une pomme à un endroit aléatoire sur l'écran
    
 global appleX, appleY, snakeX, snakeY, larg_fg, alt_fg

 # génère un point aléatoire sous la barre de score
 appleX = PX.rndi(0, larg_tel - larg_fg - 1)
 appleY = PX.rndi(alt_bar + 1, alt_tel - alt_fg - 1)
 
 # si la pomme tombe sur le serpent cela génère un autre point
 max=len(snakeX)
 for i in range (0, max ):
   while colisao(appleX, appleY, larg_fg, alt_fg,
                 snakeX[i],snakeY[i],larg_fg,alt_fg):
      appleX = PX.rndi(     0,      larg_tel-larg_fg-1)
      appleY = PX.rndi( alt_bar+1,  alt_tel-alt_fg-1)
      

def reset(): # démarre les variables du jeu
    
 global direc, snakeX, snakeY, fim_de_jogo, score
 global appleX, appleY, reiniciar
   
 fim_de_jogo = False
 reiniciar=""
 score = 0
 
 # crée une serpent dans la lin 10, aller à droite
 # tête dans la couleur 11 corps couleur 6 a 10 e queue dans la couleur 5
 #         tête  corps   corps  corps   corps   corps   queue
 snakeX = [  11,   10,     9,      8,      7,      6,     5   ]
 snakeY = [  10,  10,     10,     10,     10,      10,    10  ]
 direc = 0  # 0= indo para a direita

 # crée une pomme dans la couleur 30 lin 20
 appleX, appleY = 30, 20


def update():
    
 global snakeX, snakeY, appleX, appleY, passoX, passoY
 global direc, score, fim_de_jogo, larg_fg, alt_fg
 global reiniciar
 
 # si vous avez cliqué sur redémarrer
 if reiniciar=="s" :  reset()
      
 # si la fin du jeu est signalée
 if fim_de_jogo == True:
     
     # mettre à jour la base de données
     update_bd()
     
     # termine le programme
     PX.quit()
     return
    
# si une touche a été enfoncée, ajuste la direction du serpent
 # direction=0 à droite
 # =1 à gauche
 # =2 vers le bas
 # =3 vers le haut

 if PX.btn(PX.KEY_UP):
     # (si tu descends, n'accepte pas de monter)
     if direc != 2:
         direc = 3 # en haut

 elif PX.btn(PX.KEY_DOWN):
     # (si tu monte, n'accepte pas de descendre)
     if direc != 3:
         direc = 2 # en bas

 elif PX.btn(PX.KEY_LEFT):
     # (si tu vas à droite, n'accepte pas la gauche)
     if direc != 0:
         direc = 1 # vers la gauche

 elif PX.btn(PX.KEY_RIGHT):
     # (si tu vas à gauche, n'accepte pas la droite)
     if direc != 1:
         direc = 0 # vers la droite

 # copiez le serpent avant de franchir le pas
 oldX, oldY = snakeX, snakeY
 
 # enregistrer la position où se trouvait la queue
 old_tailX, old_tailY = snakeX[-1], snakeY[-1]

 # calculer le pas du serpent
 new_headX = snakeX[0] + passoX[direc]
 new_headY = snakeY[0] + passoY[direc]

 # vide la snake
 snakeX, snakeY = [], []
 
 # ajouter une nouvelle position de tête
 snakeX.append(new_headX) 
 snakeY.append(new_headY)

 # ajouter des positions du corps et de la queue
 max=len(oldX)-1
 for i in range(0, max):
    snakeX.append(oldX[i])
    snakeY.append(oldY[i])
 
 # Si la tête du serpent quitte l'écran, cela signale la fin de la partie
 hX, hY= snakeX[0], snakeY[0]
 if hX<0 or hY<alt_bar or hX>=larg_tel-larg_fg or hY>=alt_tel-alt_fg:
      fim_de_jogo = True
      
 # si le serpent se chevauche, cela signale la fin de la partie
 else:
      max=len(snakeX)-1
      for i in range(1, max):
          if snakeX[0]==snakeX[i] and snakeY[0]==snakeY[i]:
              fim_de_jogo = True
  
 # si c'est la fin du jeu
 if fim_de_jogo == True:
      PX.play(0, 1)    # commence le sound[1]
      return           # et retourne

 # si le serpent prends la pomme
 if colisao(snakeX[0], snakeY[0], larg_fg, alt_fg,
            appleX, appleY, larg_fg, alt_fg):
  
     PX.play(0, 0)     # commence le sound[0]
     
     score = score + 1
     
     # augmente la taille du serpent
     snakeX.append(old_tailX)
     snakeY.append(old_tailY)

     # crée une nouvelle pomme
     generate_apple()
     

def update_bd():

 global quem_joga, max_score, ordenados

 primeira_chave = next(iter(ordenados))
 primeiro_score = ordenados[primeira_chave]
 print ("Le premier du classement est ", primeira_chave, primeiro_score)
 ultima_chave = list(ordenados.keys())[-1]
 ultimo_score = ordenados[ultima_chave]
 print("Le dernier du classement est ", ultima_chave, ultimo_score)
 alterou="0"

 # si le joueur est déjà classé
 meu_ranking = ordenados.get(quem_joga)
 if meu_ranking is not None:
    print(f"Vous êtes un joueur classé ", meu_ranking)
    
    # si vous dépassez le classement, mettez à jour la base de données
    if max_score > meu_ranking:
        ordenados[quem_joga] = max_score
        alterou="1"

 # le joueur n'est pas classé    
 else:
    print("Vous n'êtes pas un joueur classé.")
    
    # s'il égale ou dépasse le dernier du classement, il est inclus dans la base de données
    if max_score >= ultimo_score:
        print("Vous venez d'entrer dans le classement")
        ordenados[quem_joga] = max_score
        alterou="1"

 # écrit la base de données mise à jour et ordonnée
 if alterou=="1": grava_bd()
 
    
 print(ordenados)

              
#########################################################################

#     programme principal

quem_joga=""
reiniciar=""
max_score=0

root = tk.Tk()
root.title("Le jeu de la SNAKE")
root.geometry('600x400+50+50')

# Couleur du texte et de l’arrière-plan du texte
style = ttk.Style()
style.configure("TLabel", foreground="blue", background="lightblue")

# Couleur d’arrière-plan de la fenêtre principale
root.configure(bg='lightblue')

msg1 = ttk.Label(root, text="\n\n\nVoulez-vous jouer snake?", style="TLabel")
msg1.pack()

msg2 = ttk.Label(root, text="Entrez votre nom.", style="TLabel")
msg2.pack()

# Crée une boîte pour l'entrer du nom
entry1 = tk.Entry(root, width=40)
entry1.pack(pady=10)

# crée et affiche le bouton
button1= ttk.Button(root, text='Cliquez ici.',command=click1)
button1.pack()

# loop du tkinter
root.mainloop()


#            pas du serpent
#        droi  gau   bas      haut
passoX= [ 1,  -1,     0,        0 ]
passoY= [ 0,   0,     1,       -1 ]

# définit la hauteur de la barre de score
alt_bar = PX.FONT_HEIGHT + 1

# définit la taille des figures (carré 8x8)
larg_fg, alt_fg = 8, 8

# commence pyxel
larg_tel, alt_tel = 220, 160
PX.init(larg_tel, alt_tel, title="Snake, par Manuela et Claire")

# définit le son [0] à utiliser lorsque le serpent attrape la pomme
PX.sounds[0].set( speed=7, tones="s",
    notes="c3e3g3c4 c4", volumes="44444", effects=("nnnnn"))
    
# définit le son [1] à utiliser à la fin du jeu
PX.sounds[1].set( speed=15, tones="p",
    notes="f3b2f2b1f1f1", volumes=("444477"), effects=("nnnnnnn") )

# démarre les variables du jeu
reset()

# boucle pour toujours du pyxel exécutant les fonctions de update e draw
PX.run(update, draw)


##############################################################################
