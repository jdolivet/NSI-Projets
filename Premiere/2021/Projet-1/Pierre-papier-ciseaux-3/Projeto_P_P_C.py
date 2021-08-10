from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

def M_P_C ():
    print("regarder l'image explicatif et ensuite fermer-la")
    time.sleep(7)   #avec time.sleep, on peut donner un temp pour que l'utilisateur regarde la phrase
    M_P_P = mpimg.imread("jankenpon.jpg")
    plt.imshow(M_P_P)
    plt.show()
    
    système = randint(1,3)
    print("1 = pierre")
    print("2 = ciseaux")
    print("3 = Papier")

    joueur = int(input("choisie un numero: "))
    print(joueur)     
    if système == 1:
        if joueur == 1:
            print("Le système a choisi la pierre.  LE MATCH TERMINE TOUT ÉGAL")
        elif joueur == 2:
            print("Le système a choisi la pierre.  LE MATCH TERMINE AVEC LA VICTOIRE DU SYSTÈME")
        elif joueur == 3:
            print("Le système a choisi la pierre.  LE MATCH TERMINE AVEC LA VICTOIRE DU JOUEUR")

    elif système == 2:
        if joueur == 1:
            print("Le système a choisi la ciseaux.  LE MATCH TERMINE AVEC LA VICTOIRE DU JOUEUR")
        elif joueur == 2:
            print("Le système a choisi la ciseaux.  LE MATCH TERMINE TOUT ÉGAL")
        elif joueur == 3:
            print("Le système a choisi la ciseaux.  LE MATCH TERMINE AVEC LA VICTOIRE DU SYSTÈME")

    elif système == 3:
        if joueur == 1:
            print("Le système a choisi la Papier.  LE MATCH TERMINE AVEC LA VICTOIRE DU SYSTÈME")
        elif joueur == 2:
            print("Le système a choisi la Papier.  LE MATCH TERMINE AVEC LA VICTOIRE DU JOUEUR")
        elif joueur == 3:
            print("Le système a choisi la Papier.  LE MATCH TERMINE TOUT ÉGAL")

#--------------------------------------------------------------------------------------------------------------

def M_P_C_testes():
#    print("regarder l'image explicatif et ensuite fermer-la")
#    time.sleep(7)
#    M_P_P = mpimg.imread("jankenpon.jpg")
#    plt.imshow(M_P_P)
#    plt.show()
#l'image ne permétait pas la boucle de se dérouler plusieur fois toute seule, donc on dut la metre comme commentaire pour les testes
    système = randint(1,3)
    print("1 = pierre")
    print("2 = ciseaux")
    print("3 = Papier")

    joueur = randint(1, 3)#pour que la boucle se déroule toute seule, on mets "randint(1, 3)" au lieu de "int(input("choisie un numero: "))"
    print(joueur)
    if système == 1:
        if joueur == 1:
            print("Le système a choisi la pierre.  LE MATCH TERMINE TOUT ÉGAL")
        elif joueur == 2:
            print("Le système a choisi la pierre.  LE MATCH TERMINE AVEC LA VICTOIRE DU SYSTÈME")
        elif joueur == 3:
            print("Le système a choisi la pierre.  LE MATCH TERMINE AVEC LA VICTOIRE DU JOUEUR")

    elif système == 2:
        if joueur == 1:
            print("Le système a choisi la ciseaux.  LE MATCH TERMINE AVEC LA VICTOIRE DU JOUEUR")
        elif joueur == 2:
            print("Le système a choisi la ciseaux.  LE MATCH TERMINE TOUT ÉGAL")
        elif joueur == 3:
            print("Le système a choisi la ciseaux.  LE MATCH TERMINE AVEC LA VICTOIRE DU SYSTÈME")

    elif système == 3:
        if joueur == 1:
            print("Le système a choisi la Papier.  LE MATCH TERMINE AVEC LA VICTOIRE DU SYSTÈME")
        elif joueur == 2:
            print("Le système a choisi la Papier.  LE MATCH TERMINE AVEC LA VICTOIRE DU JOUEUR")
        elif joueur == 3:
            print("Le système a choisi la Papier.  LE MATCH TERMINE TOUT ÉGAL")

#pour faire le teste il faut seulement enlever les # de la boucle
for _ in range (10):
    M_P_C_ANDRE()