import pyxel

pyxel.init(256, 256, title="Cookie Clicker") #fenetre du jeu + nom
pyxel.load("teste.pyxres") #charge le fichier des images et des musiques
#pyxel.playm(0, loop=True) #musique + répéter(loop),
#on a choisi pas la mettre car elle n'est pas tres bonne, pas pour la mettre il faut seulement retirer le #

#variables de nb de chaque objet
nbmouse = 0
nbgm = 0
nbjardin = 0
nbmine = 0
nbupggm = 0
nbupgclick = 0
nbupgbonus = 0
nbupgsoldes = 0

#variables de prix
prxmouse = 150
prxgm = 1000
prxjardin = 12000
prxmine = 120000
prixupggm = 50_000
prixupgclick = 100_000
prixupgbonus = 150_000
prixupgsoldes = 100_000

#variables de production de cookies par sec
ckmouse = 1
ckgm = 10
ckjardin = 80
ckmine = 470
ckclick = 10

prod = 0
totalck = 0 #def total de cookies

pyxel.mouse(True) #montrer la souris

upgclick = False #je mets les upgrades = false car sinon ils s activent avant meme de les acheter
upggm = False
upgbonus = False
upgsoldes = False
    
def update():
    
    #global = apporter les variables de dehors de la fonction pour dedans de la fonction 
    global nbmouse
    global nbgm
    global nbjardin
    global nbmine
    global prod
    
    global ckgm
    global ckjardin
    global ckmouse
    global ckmine
    global ckclick
    
    global prxmouse
    global prxgm
    global prxjardin
    global prxmine
    
    global prixupgclick
    global prixupggm
    global prixupgbonus
    global prixupgsoldes
    
    global upgclick
    global upgbonus
    global upggm
    global upgsoldes
    
    global nbupggm
    global nbupgclick
    global nbupgbonus
    global nbupgsoldes
    global totalck
    
    if upgsoldes == True:#je verifie si on a deja achter les upgrades, car si on les a pas acheter ils sont "False"
                         #upgrade des soldes, avec ca chaque prix deviens moins chere
        prxmouse = int(prxmouse * 0.75) #le int est utilise pour ne pas avoir de nombres flotants
        prxgm = int(prxgm * 0.75)
        prxjardin = int(prxjardin * 0.75)
        prxmine = int(prxmine * 0.75)
        totalck = totalck - prixupgsoldes #actualiser le total de cookie qu on a apres avoir achete l upgrade
        prixupgsoldes = prixupgsoldes * 2 #maintenant le prix d un upgrade est 2x plus chere
        nbupgsoldes = nbupgsoldes + 1 #la quantite qu on a de upg soldes maintenant
        upgsoldes = False #Désactiver la variable upgsolde, sinon chaque frame elle va faire des soldes
        
    if upggm == True: #upgrade grand mere, maintenant la grand mere gere 2x plus qu avant
        ckgm = ckgm * 2
        totalck = totalck - prixupggm
        prixupggm = 2 * prixupggm
        nbupggm = nbupggm + 1
        upggm = False
    
    if upgbonus == True: #upgrade bonus, maintenant chaque truc qu on achete gere 2x de cookie qu avant
        ckgm = ckgm * 2
        ckjardin = ckjardin * 2
        ckmine = ckmine * 2
        ckmouse = ckmouse * 2
        totalck = totalck - prixupgbonus
        prixupgbonus = 2 * prixupgbonus
        nbupgbonus = nbupgbonus + 1
        upgbonus = False
        
    #production totale des elements
    prodmouse = nbmouse * ckmouse
    prodgm = nbgm * ckgm
    prodjardin = nbjardin * ckjardin
    prodmine = nbmine * ckmine  
    
    prod = prodmouse + prodgm + prodjardin + prodmine #on actualize la production 
    
    #Comme il y a 30 images par seconde, frame_count % 30 fait un cycle de 0 à 29 où chaque nombre apparaît une seule fois.
    #Donc je peux vérifier si frame_count % 30 donne un nombre spécifique : il ne se mettra à jour qu’une seule fois par seconde, au lieu de se mettre à jour 30 fois par seconde.
    #On va donc mettre à jour chaque seconde, sinon c’est trop rapide. senao e mt rapido
    if pyxel.frame_count % 30 == 1:
        totalck = totalck + prod #adiciona a prod por sec pro total
        
        
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):# si click gauche, augmenter de la valeur des clicks
        pyxel.play(ch=0, snd=10) # son de quand on click
        totalck = totalck + ckclick
        if upgclick == True: #upgrade des click, maintenant si on fait 1 click, on recoit 2 cookie
            ckclick = ckclick * 2
            totalck = totalck - prixupgclick 
            nbupgclick = nbupgclick + 1
            prixupgclick = prixupgclick * 2
            upgclick = False #ont eteint la variable, sinon a chaque frame le upgrade du click va etre multiplie par 2
    
    #code pour achetter, et actualiser le prix de chaque objet
    #dans le jeu officiel, le calcul a faire est de: prix de l'objet * 1.15 ** nombre d'objet de ce type
    #je reproduis ce calcul ci dessous avec une division euclidienne pour ne pas avoir de nb flottants
    if pyxel.btnp(pyxel.KEY_C): #achetter, et actualiser le prix des curseurs
        if totalck >= prxmouse:#condition pour acheter
            pyxel.play(ch=0, snd=11) #son de quand on achete un upgrade
            nbmouse += 1 #adicionner ce qu on a achete
            totalck -= prxmouse #payement
            prxmouse = 150 * ( 115 ** nbmouse ) // ( 100 ** nbmouse ) #calcul pour augmenter le prix
        
    if pyxel.btnp(pyxel.KEY_G): #achetter, et actualiser le prix des grandes meres
        if totalck >= prxgm:
            pyxel.play(ch=0, snd=11)
            nbgm += 1
            totalck -= prxgm
            prxgm = 1000 * ( 115 ** nbgm ) // ( 100 ** nbgm )
        
    if pyxel.btnp(pyxel.KEY_J): #achetter, et actualiser le prix des jardins
        if totalck >= prxjardin:
            pyxel.play(ch=0, snd=12)
            nbjardin += 1
            totalck -= prxjardin
            prxjardin = 12000 * ( 115 ** nbjardin ) // ( 100 ** nbjardin )
        
    if pyxel.btnp(pyxel.KEY_M): #achetter, et actualiser le prix des mines
        if totalck >= prxmine:
            pyxel.play(ch=0, snd=12)
            nbmine+= 1
            totalck -= prxmine
            prxmine = 120000 * ( 115 ** nbmine ) // ( 100 ** nbmine )
            
    if pyxel.btnp(pyxel.KEY_U): #achetter, et actualiser le prix des
        if totalck >= prixupggm:
            pyxel.play(ch=0, snd=14)
            upggm = True
    
    if pyxel.btnp(pyxel.KEY_K):
        if totalck >= prixupgclick:
            pyxel.play(ch=0, snd=14)
            upgclick = True
        
    if pyxel.btnp(pyxel.KEY_B):
        if totalck >= prixupgbonus:
            pyxel.play(ch=0, snd=13)
            upgbonus = True
            
    if pyxel.btnp(pyxel.KEY_S):
        if totalck >= prixupgsoldes:
            pyxel.play(ch=0, snd=14)
            upgsoldes = True
        
def draw():
    pyxel.cls(1)  # écran avec un fond noir
    

    pyxel.text(2, 1,   f"{nbmouse} curseurs", 15)
    pyxel.text(2, 12,  f"{nbgm} grandes meres", 15)
    pyxel.text(2, 24,  f"{nbjardin} jardins de cookies", 15)
    pyxel.text(2, 36,  f"{nbmine} mines de cookies", 15)
    
    pyxel.text(100, 12,  f"S--{nbupgsoldes} upgrades des soldes : {prixupgsoldes}$", 13)
    pyxel.text(100, 1, f"U--{nbupggm} upgrades de grandes meres : {prixupggm}$", 13)
    pyxel.text(100, 24, f"K--{nbupgclick} upgrades de click : {prixupgclick}$", 13)
    pyxel.text(100, 36, f"B--{nbupgbonus} upgrades de bonus : {prixupgbonus}$", 13)

    pyxel.text(2, 52,  f"prix curseur : {prxmouse}$", 14)
    pyxel.text(2, 64,  f"prix grande mere : {prxgm}$", 14)
    pyxel.text(2, 76,  f"prix jardin de cookies: {prxjardin}$", 14)
    pyxel.text(2, 88,  f"prix mine de cookies: {prxmine}$", 14)

    ckcount = totalck

    pyxel.text(2, 232, f"{totalck} cookies ", 9)
    pyxel.text(2, 244, f"{prod} cookies par seconde", 9)

    pyxel.text(2, 208, f"pro tip: laisse le jeu de cote", 4)
    pyxel.text(2, 220, f"et reviens plus tard!!!", 4)
 
 
    #dessin du cookie au milieu
    #pyxel.blt(x, y, img, u, v, w, h, colkey) x et y = coords, img = numero de l'image, u, v = choisir l'image que tu veux,
    #w et h = choisir la quantite de pixel de l'image, colkey = rendre invisible une couleur au fond de l'image(ex:0, je rend invisible la couleur noir)
    pyxel.blt(100, 112, 1, 0, 0, 128, 128, 0)
    
   
    x = 0
    y = 136
    for i in range(nbmouse): #pour les souries
        pyxel.blt(x, y, 2, 0, 0, 8, 8, 0)
        x = 10 + x
        if x >= 100:
            x = 0
            y -= 10            
    x = 0
    y = 150
    for i in range(nbgm): #pour les grandes meres
        pyxel.blt(x, y, 2, 8, 0, 8, 8, 0)
        x = 10 + x
        if x >= 100:
            x = 0
            y += 10
    x = 0
    y = 182
    for i in range(nbjardin): #pour les jardins
        pyxel.blt(x, y, 2, 0, 8, 8, 8, 0)
        x = 10 + x
        if x >= 100:
            x = 0
            y += 10
        
    for i in range(nbmine): #pour les mines
        pyxel.blt(0 + 10 * i, 200, 2, 8, 8, 8, 8, 0)
        
    x = 140
    y = 180
    for i in range(nbupggm): #pour les upgrades
        pyxel.blt(x, y, 0, 21, 2, 19, 21, 0)
        x = 25 + x
    
    x = 140
    y = 204
    for i in range(nbupgclick):
        pyxel.blt(x, y, 0, 0, 0, 16, 17, 0)
        x = 25 + x
    
    x = 140
    y = 221
    for i in range(nbupgsoldes):
        pyxel.blt(x, y, 0, 20, 30, 26, 20, 0)
        x = 25 + x
    
    x = 145
    y = 242
    for i in range(nbupgbonus):
        pyxel.blt(x, y, 0, 0, 49, 16, 16, 0)
        x = 25 + x
        
#fonction de pyxel qui commence le jeu avec les fonctions update et draw effectuees 30 fois par seconde
pyxel.run(update, draw)