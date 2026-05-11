import pyxel, json

pyxel.init(264, 264, title="Pyano")
pyxel.mouse(True)

#=======================VARIABLES(globales)===========================
v = {
    'grille' : [],
    'notes' : [],
    'ynotes' : [],
    'selection' : [],
    'hard_selection' : [],
    'descend' : 0,
    'bpm' : 120,
    'scroll' : 0,
    'texte' : pyxel.user_data_dir("NSI_1", "Pyano_roll") + "sauvegarde.txt",
    'music' : 0,
    'y' : 240,
    'l' : 12,
    'a' : 12
    
    
}
color = [7,0,7,7,0,7,0,7,7,0,7,0,7,0,7,7,0,7,0,7,7,0]
button_pressed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
button_pressed2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#coordonnées de la grille du piano (22 notes + sans son)
for i in range(1, 23):
    for j in range(30):
        v['grille'].append([(i * 12) - 10, (j * 16)])
    

EXTENDED_CHANNELS = []

for _ in range(22):
    EXTENDED_CHANNELS.append((1 / 10, 0))
    
    
channels = []
for gain, detune in EXTENDED_CHANNELS:
    channel = pyxel.Channel()
    channel.gain = gain
    channel.detune = detune
    channels.append(channel)
pyxel.channels.from_list(channels)
    
nom_des_notes = ['a1', 'a#1', 'b1', 'c2', 'c#2', 'd2', 'd#2', 'e2', 'f2', 'f#2', 'g2', 'g#2', 'a2', 'a#2', 'b2', 'c3', 'c#3', 'd3', 'd#3', 'e3', 'f3', 'f#3']

for i in range(22):
    nom_des_notes[i] = nom_des_notes[i] * 1 # à changer si on veut des notes plus longues

for i in range(22):
    pyxel.sounds[i].set_notes(nom_des_notes[i])
    pyxel.sounds[i].set_volumes("7")
    
    
pyxel.musics[0].set(
    [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15],[16, 16], [17, 17], [18, 18], [19, 19], [20, 20], [21, 21], [22, 22]
    )
    
#=====================FONCTIONS=====================
def proche(t1, t2):
    
    compar = [10000000000000000000000000]
    for item in t1:
        if [abs(item[0] - t2[0]), abs(item[1] - t2[1])] < compar:
            compar = [abs(item[0] - t2[0]), abs(item[1] - t2[1])]
            res = item
    return res

#^^^Fonction pour trouver les coordonnées de la grille les plus proches de la souris

def bool_occurences(t1, t2):
    
    for item in t1:
        if item == t2:
            return True
    return False



def creation_note(t):
    
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT, 5) and (v['descend'] == 0):
        if not bool_occurences(t, proche(v['grille'], [pyxel.mouse_x, pyxel.mouse_y])):
            v['selection'] = []
            v['hard_selection'] = []
            
            grille_copie = proche(v['grille'], [pyxel.mouse_x, pyxel.mouse_y])
            t.append(grille_copie[:])
            
            v['ynotes'] = (v['ynotes'] + [((t[len(t) - 1])[1]) - v['scroll']])
            
            
#^^^Création de la note lorsqu'on appui avec la souris, on crée qu'une note même si on touche plusieurs fois
# Aussi on note toutes les positions y des notes
            
        elif bool_occurences(t, proche(v['grille'], [pyxel.mouse_x, pyxel.mouse_y])):
            if not pyxel.btn(pyxel.KEY_CTRL):
                v['selection'] = []
                v['hard_selection'] = []
            
            if not bool_occurences(v['selection'], proche(v['grille'], [pyxel.mouse_x, pyxel.mouse_y])):
                    grille_copie_selection = proche(v['grille'], [pyxel.mouse_x, pyxel.mouse_y])
                    v['selection'].append(grille_copie_selection[:])
                    
                    v['hard_selection'] = (v['hard_selection'] + [((v['selection'][len(v['selection']) - 1])[1]) - v['scroll']])

#Coordonnées de la selection de la note, on peut selectionner plusieurs notes avec ctrl         
        
def note_activation():
    if pyxel.btnp(pyxel.KEY_SPACE) and (v['descend'] != 1):
        v['selection'] = []
        v['hard_selection'] = []
        if v['descend'] != 2:
            for i in range(len(v['notes'])):
                (v['notes'][i])[1] = (v['ynotes'])[i]
                
        if v['notes'] != []: 
            v['descend'] = 1
            v['scroll'] = 0
            v['music'] = 1
            
    if v['descend'] == 1:
        for note in v['notes']:
            if note[1] < pyxel.width + 100:
                note[1] = note[1] + (v['bpm']/120)
            
                
#^^^État où les notes tombent pour créer la musique, les notes s'arretent 100 pixels après depasser la fenêtre
#Actif par la touche space            

def note_deactivation():
    if pyxel.btnp(pyxel.KEY_D) and (v['descend'] > 0):
        for i in range(len(v['notes'])):
            (v['notes'][i])[1] = (v['ynotes'])[i]
        v['descend'] = 0
        v['music'] = 0
        
#^^^ revient les sprites à leurs états originaux avec la touce d

def note_stop():
    if pyxel.btnp(pyxel.KEY_S) and (v['descend'] > 0):
        v['descend'] = 2
        v['music'] = 0
        
#^^^ arrete les notes avec "s"
        
def delete_selection():
    if pyxel.btnp(pyxel.KEY_BACKSPACE) and (v['descend'] == 0):
        if v['selection'] != []:
            for select in v['selection'][:]:
                v['notes'].remove(select)
            v['ynotes'] = []
            for note in v['notes'][:]:
                v['ynotes'].append(note[1] - v['scroll'])
            v['selection']  = []
            v['hard_selection'] = []
        
#On a besoin de créer une copie de la liste selection pour eviter que les deux listes soient "enmelées"
# + réorganisation des coordonées des notes


        
def delete_all():
    if pyxel.btnp(pyxel.KEY_A, 5) and (v['descend'] == 0):
        v['descend'] = 0
        v['notes'] = []
        v['ynotes'] = []
        v['selection'] = []
        v['hard_selection'] = []
"""
La grille est connectée avec les notes de mode qu'on ne peut pas placer des notes dans un même endroit
après le supprimer si on les supprime pendant l'état de stopper(??? - A ameliorer) - résolu
     """   
        
def scroll_effet():
    if v['descend'] == 0:
        if pyxel.btn(pyxel.KEY_UP):
            v['scroll'] += 16
            v['music']=0
        
        if pyxel.btn(pyxel.KEY_DOWN):
            if v['scroll'] >= 16:
                v['scroll'] -= 16
                v['music']=0
            
        for i in range(len(v['notes'])):
            (v['notes'][i])[1] = ((v['ynotes'])[i]) + v['scroll']
            
        for i in range(len(v['selection'])):
            (v['selection'][i])[1] = (v['hard_selection'][i]) + v['scroll']
            
            
#monte la variable scroll de manière que les notes soient alignées avec la grille, responsable pour stocker
#les coordonnées des notes plus hautes
            
            
def bpm_set():
    if pyxel.btnp(pyxel.KEY_0):
        v['bpm'] = 120
    if pyxel.btnp(pyxel.KEY_1):
        v['bpm'] = 140
    if pyxel.btnp(pyxel.KEY_2):
        v['bpm'] = 180
    if pyxel.btnp(pyxel.KEY_3):
        v['bpm'] = 220
    if pyxel.btnp(pyxel.KEY_4):
        v['bpm'] = 240
    if pyxel.btnp(pyxel.KEY_5):
        v['bpm'] = 280
    if pyxel.btnp(pyxel.KEY_6):
        v['bpm'] = 320
    if pyxel.btnp(pyxel.KEY_7):
        v['bpm'] = 360
    if pyxel.btnp(pyxel.KEY_8):
        v['bpm'] = 400
    if pyxel.btnp(pyxel.KEY_9):
        v['bpm'] = 420
            
        
def detect_piano():
    for note in v['notes']:
        if note[1]>=240 and note[1]<=250 and v['music']==1:
            for i  in range(0, 21, 2):
                if note[0] == i * 12 + 2:
                    button_pressed[i] = 1
                    button_pressed[i] = 1
                    pyxel.play(i, i)
            for i  in range(1, 22, 2):
                if note[0] == i * 12 + 2:
                    button_pressed[i] = 1
                    button_pressed[i] = 1
                    pyxel.play(i, i)

#Les notes de musiques sont joués une fois qu'elles arrivent à un certain point y et produisent des sons différents
#en fonction de leurs position x.

def sauvegarde():
    if pyxel.btnp(pyxel.KEY_SPACE) and (v['descend'] != 1):    
        with open(v["texte"],'w') as fichier:
            fichier.write(str(v['notes']))
            fichier.write('_')
            fichier.write(str(v['ynotes']))
        
#Ouvre un fichier txt dans le directoire de l'utilisateur créé par pyxel et sauvegarde les notes lorsque tape sur space
            
            
def lire_fichier():
    if pyxel.btnp(pyxel.KEY_L):
        with open(v['texte'], 'r') as fichier:
            contenu = fichier.read()
            if (contenu != ""):
                separ = contenu.split('_')
                v['ynotes'] = json.loads(separ[1])
                v['notes'] = json.loads(separ[0])

#si on appuis sur la touche "L" et le fichier n'est pas vide, assigne les valeurs sauvegardées des notes
            
            
def draw_piano():
    for i in range(22):
        pyxel.rect(0+i*12,240,12,24,7)
            
#=====================UPDATE========================
def update():
    creation_note(v['notes'])
    
    sauvegarde()
    
    lire_fichier()
    
    note_activation()
    
    note_deactivation()
    
    note_stop()
    
    delete_selection()
    
    delete_all()
    
    scroll_effet()
    
    bpm_set()
    
    detect_piano()
    
#=====================DRAW==========================    
def draw():
    pyxel.cls(1)
    
    # modelisation de la grille
    for i in range(22):
        pyxel.line(0 + i * 12, 0, 0 + i * 12, pyxel.width, 13)
        
    # notes du piano
    for note in v['notes']:
        pyxel.rect(note[0], note[1], 8, 12, 11)
        
    for select in v['selection']:
        pyxel.rectb(select[0], select[1], 8, 12, 0)
    
    #piano
        
    draw_piano()
    
    for i in range(22):
        cor = color[i]
        
        if button_pressed[i]==1:
            cor = 13
            button_pressed[i]=0

        pyxel.rect(i * v['l'], v['y'], v['l'], v['a'], cor)
    
    for i in range(22):
        cor=7
        if button_pressed2[i]==1:
            cor = 13
            button_pressed2[i]=0
        pyxel.rect(i*v['l'],v['y']+12,v['l'],v['a'],cor)
        
    #UI
    pyxel.text(10, 10, f"scroll : {v['scroll']}", 7)
    pyxel.text(10, 20, f"bpm : {v['bpm']}", 7)
    
    #debug - effacer cela lors de rendre
#     pyxel.text(10, 30, str(v['music']), 0)
#     pyxel.text(10, 40, str(v['notes']), 0)
#     pyxel.text(10, 50, str(v['selection']), 0)
#     pyxel.text(10, 60, str(v['hard_selection']), 0)
        
        
pyxel.run(update, draw)

