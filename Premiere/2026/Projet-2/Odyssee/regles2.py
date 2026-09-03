import pyxel as px
import sys
import os


px.init(160, 120, title="Regles du jeu")
px.load("musica_game_ulysse.pyxres")
px.playm(0, loop=True)

pages = [
    [
        "HISTOIRE",
        "",
        "Bienvenue dans l'Odyssee!",
        "Dans ce jeu, vous incarnez",
        "Ulysse, celebre heros grec",
        "de la guerre de Troie,",
        "durant son voyage de retour a",
        "Ithaque, son ile natale."
    ],
    [
        "",
        "",
        "Malheureusement, plusieurs dieux",
        "tentent de l'empecher de revenir",
        "chez vous, entre autres, Poseidon",
        "et Chronos, qui vont utiliser",
        "leurs pouvoirs pour vous empecher de",
        "gagner. Vous pouvez appuyer sur 'R'",
        "pour voir les regles a tout moment."
    ],
    [
        "AFFICHAGE",
        "",
        "Le numero en haut a gauche de",
        "l'ecran indique le nombre de",
        "deplacements qu'il vous reste",
        "avant que Chronos remonte le",
        "temps. Lorsqu'il le fera, vous",
        "reprendrez votre place de depart",
        "sur la carte avec tout votre argent."
        
    ],
    [
        "ILES DU JEU :",
        "",
        "Il existe six iles differentes :",
        "l'ile du donjon, l'ile du manoir,",
        "l'ile au tresor, l'ile puzzle, l'ile",
        "magasin et l'ile drapeau. Chacune (a",
        "part la derniere) permet de gagner ou",
        "de depenser votre argent. Pour en",
        "sortir, appuyer sur 'q'."
    ],
    [
        "ILE MAGASIN",
        "",
        "Cette ile vous permettra de depenser",
        "votre argent pour acheter des",
        "deplacements ou des points de vie.",
        "C'est le seul endroit ou vous verrez",
        "l'etat de vos finances. Utilisez les",
        "fleches haut et bas pour choisir",
        "et appuyez sur 'entree' pour acheter."
    ],
    [
        "ILE DONJON",
        "",
        "Sur cette ile, vous devez trouver le",
        "tresor tout en evitant les fantomes.",
        "Pour bouger, utilisez les fleches",
        "directionnelles. Apres avoir",
        "trouve un tresor, un autre apparait",
        "aleatoirement sur le terrain. Mais",
        "si vous vous faites capturer"
    ],
    [
        "",
        "",
        "par un fantome, non seulement vous",
        "perdrez 1 point de vie mais",
        "aussi tout l'argent que vous",
        "aviez gagne sur cette ile."
        ""
    ],
    [
        "ILE DU MANOIR",
        "",
        "Une fois arrive sur cette ile,",
        "vous tombez dans un profond",
        "sommeil et vous revez que vous",
        "etes dans un labyrinthe et que",
        "les objets inertes vous attaquent.",
        "Sur cette ile, vous devez trouver",
        "le tresor dans le dedale de votre"
    ],
    [
        "",
        "esprit, heureusement, vous pouvez",
        "traverser les murs meme si cela",
        "vous fait perdre des points de vie.",
        "Selon la rumeur, il existerait une",
        "salle remplie de pieces quelque",
        "part dans ce monde / reve. Pour vous",
        "deplacer, utilisez les fleches",
        "multidirectionnelles."
    ],
    [
        "ILE AU TRESOR",
        "",
        "Sur cette ile, il pleut de l'or",
        "et vous pouvez en recuperer",
        "autant que vous voulez. Chacun",
        "rapporte 2 argents. Mais prenez",
        "garde aux bombes car si vous",
        "en touchez une, vous perdez 1",
        "point de vie et toutes les pieces"
    ],
    [
        "",
        "",
        "recuperees sur cette ile. Pour",
        "vous deplacer, appuyez sur",
        "les fleches de droite et de",
        "gauche."
    ],
    [
        "ILE DRAPEAU",
        "",
        "Votre objectif. En effet, pour",
        "gagner il vous faut atteindre 6",
        "de ces iles drapeau, l'inconvenient",
        "est qu'elles apparaissent une",
        "apres l'autre et qu'il vous faut",
        "toutes les decouvrir avant que",
        "Chronos remonte le temps, sinon"
    ],
    [
        "",
        "",
        "il faudra redecouvrir les 6 iles",
        "de nouveau. Une fois que vous",
        "en atteignez une, celle-ci",
        "disparait et la suivante apparait sur",
        "la carte, a vous de la decouvrir."
    ],
    [
        "ILE PUZZLE",
        "",
        "Sur cette ile, trois personnages sont",
        "presents, un dit la verite et un",
        "ment. Le troisieme peut soit",
        "mentir soit dire la verite. Un seul",
        "d'entre eux sait ou se trouve l'ile",
        "drapeau, a vous de trouver lequel",
        "a partir de ce qu'ils disent."
    ],
    [
        "CHRONOS REMONTE LE TEMPS ET DEFAITE",
        "",
        "Si a un moment, vos points de vie",
        "atteignent 0, vous aurez perdu et il",
        "vous faudra retenter votre chance.",
        "Si vos deplacements atteignent 0,",
        "Chronos fera remonter le temps et",
        "Poseidon fera bouger les iles. Mais",
        "les iles drapeau resteront aux"
    ],
    [
        "",
        "",
        "memes endroits et votre argent et",
        "vos points de vie seront les memes.",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "PRET A JOUER ?",
        "",
        "Vous connaissez maintenant les",
        "regles. Felicitation pour avoir",
        "lu jusqu'ici. Pour la peine, voici",
        "un indice : la premiere ile",
        "drapeau se trouve a l'est.",
        "Pour commencer a jouer, appuyer",
        "sur 'espace'. Bon jeu."
    ]
]

page = 0

#==================UPDATE=======================

def update():
    global page
    
    if px.btnp(px.KEY_SPACE):
        sys.exit(7)


    if px.btnp(px.KEY_RIGHT):
        if page < len(pages) - 1:
            page += 1

    if px.btnp(px.KEY_LEFT):
        if page > 0:
            page -= 1

#===================DRAW======================

def draw():
    px.cls(0)

    for i in range(len(pages[page])):
        px.text(10, 10 + i * 10, pages[page][i], 7)
        
    px.text(10, 110, f"Page {page+1} sur {len(pages)}  ", 11)
    px.text(10, 100, "Fleche droite pour tourner la page", 11) 
    

px.run(update, draw)