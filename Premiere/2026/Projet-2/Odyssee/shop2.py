import pyxel as px
import sys

px.init(200, 200, "Boutique")
px.load("musica_game_ulysse.pyxres")
px.playm(1, loop=True)



#====================VARIABLES=======================
with open("donnees.txt", 'r') as file:
    argent = int(file.readline())
    vie = int(file.readline())
    deplacement = int(file.readline())
    localisation = list(map(int, file.readline().split()))
    case1 = int(file.readline())
    case2 = int(file.readline())
    case3 = int(file.readline())
    case4 = int(file.readline())
    case5 = int(file.readline())
    case6 = int(file.readline())
    case7 = int(file.readline())
    case8 = int(file.readline())
    case9 = int(file.readline())
    bateau_x = int(file.readline())
    bateau_y = int(file.readline())
    en_mer = file.readline()=="True\n"
    end_of_turn = file.readline()=="True\n"
    map1 = [[int(file.readline()) for _ in range(30)] for _ in range(30)]
    nb_destination = int(file.readline())
    liste_destin = [list(map(int, file.readline().split())) for _ in range(3)]
option = 0
message = "Bonjour, etranger."




#===========================FONCTIONS================================

def retour_map():
    global argent, vie, deplacement, localisation, case1, case2, case3, case4, case5, case6, case7, case8, case9, bateau_x, bateau_y, en_mer, end_of_turn, map1
    if px.btnp(px.KEY_Q):
        with open("donnees.txt", 'w') as file:
            file.write(str(argent))
            file.write("\n")
            file.write(str(vie))
            file.write("\n")
            file.write(str(deplacement))
            file.write("\n")
            file.write(str(localisation[0])+" "+str(localisation[1]))
            file.write("\n")
            file.write(str(case1))
            file.write("\n")
            file.write(str(case2))
            file.write("\n")
            file.write(str(case3))
            file.write("\n")
            file.write(str(case4))
            file.write("\n")
            file.write(str(case5))
            file.write("\n")
            file.write(str(case6))
            file.write("\n")
            file.write(str(case7))
            file.write("\n")
            file.write(str(case8))
            file.write("\n")
            file.write(str(case9))
            file.write("\n")
            file.write(str(bateau_x))
            file.write("\n")
            file.write(str(bateau_y))
            file.write("\n")
            file.write(str(en_mer))
            file.write("\n")
            file.write(str(end_of_turn))
            file.write("\n")
            for ligne in map1:
                for elt in ligne:
                    file.write(str(elt))
                    file.write("\n")
            file.write(str(nb_destination))
            file.write("\n")
            for i in range(len(liste_destin)):
                file.write(str(liste_destin[i][0])+" "+str(liste_destin[i][1]))
                file.write("\n")
        sys.exit(7)


def draw_marchand():
    px.rect(65, 18, 70, 70, 1)
    px.tri(70, 25, 130, 25, 100, 80, 2)
    px.circ(100, 42, 16, 5)
    px.circ(94, 42, 2, 7)
    px.circ(106, 42, 2, 7)
    px.line(95, 53, 105, 53, 8)
    px.rect(84, 58, 32, 18, 2)
    px.line(84, 76, 75, 88, 2)
    px.line(116, 76, 125, 88, 2)
    px.line(92, 76, 92, 92, 2)
    px.line(108, 76, 108, 92, 2)

#================UPDATE======================
def update():
    global argent, deplacement, vie, option, message

    if px.btnp(px.KEY_DOWN):
        option += 1
        if option > 1:
            option = 0

    if px.btnp(px.KEY_UP):
        option -= 1
        if option < 0:
            option = 1

    if px.btnp(px.KEY_RETURN):
        if option == 0:
            if argent >= 50:
                argent -= 50
                deplacement += 1
                message = "Tu as achete du deplacement."
            else:
                message = "Pas assez d'argent."

        elif option == 1:
            if argent >= 100:
                argent -= 100
                vie += 1
                message = "Tu as achete de la vie."
            else:
                message = "Pas assez d'argent."
    retour_map()




#=====================DRAW==========================
def draw():
    px.cls(0)

    px.text(72, 8, "BOUTIQUE", 7)

    draw_marchand()

    px.rectb(10, 100, 180, 25, 7)
    px.text(18, 108, message, 7)

    px.rectb(10, 130, 180, 55, 7)

    if option == 0:
        px.text(18, 142, ">", 8)
    px.text(30, 142, "DEPLACEMENT", 7)
    px.text(145, 142, "50 G", 6)

    if option == 1:
        px.text(18, 158, ">", 8)
    px.text(30, 158, "VIE", 7)
    px.text(145, 158, "100 G", 6)

    px.text(10, 190, "ARGENT : " + str(argent), 10)
    px.text(110, 190, "DEP : " + str(deplacement), 11)
    px.text(155, 190, "VIE : " + str(vie), 8)



px.run(update, draw)