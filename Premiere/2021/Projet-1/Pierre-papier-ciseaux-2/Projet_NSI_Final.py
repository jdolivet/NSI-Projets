from random import randint

#on utilise global pour chercher des variables qui ne sont pas dans la fonction
def p1(): #fonction qui calcule le nombre de fois que chaque action à été choisis pour l'ordi 1
    global nb_pierre1
    global nb_feuille1  #prend les variables qui sont dehors de la fonction
    global nb_ciseaux1
    global joueur_1 
    if joueur_1 == 0:
        nb_pierre1 += 1#calcul du nombre de fois que le joueur a choisi chaque option
        return nb_pierre1#retourne le nombre de fois que le joueur a choisi chaque option
    if joueur_1 == 1:
        nb_feuille1 += 1
        return nb_feuille1
    if joueur_1 == 2:
        nb_ciseaux1 += 1
        return nb_ciseaux1
    
def p2(): #fonction qui calcule le nombre de fois que chaque action à été choisis pour l'ordi 2
    global nb_pierre2
    global nb_feuille2  #prend les variables qui sont dehors de la fonction
    global nb_ciseaux2
    global joueur_2
    if joueur_2 == 0:
        nb_pierre2 += 1#calcul du nombre de fois que le joueur a choisi chaque option
        return nb_pierre2#retourne le nombre de fois que le joueur a choisi chaque option
    if joueur_2 == 1:
        nb_feuille2 += 1
        return nb_feuille2
    if joueur_2 == 2:
        nb_ciseaux2 += 1
        return nb_ciseaux2
    
def pourcentage1(): #fonction qui affiche les calculs fait dans la fonction p1
    print()
    print("L'ordinateur 1:"
          "\n\tNombres de feuilles =",nb_feuille1,
          "\n\tNombre de ciseaux =",nb_ciseaux1,
          "\n\tNombre de pierres =",nb_pierre1)
    print() #fait le calcul des pourcentages, arrondi à 2 chiffres après la virgules
    print("\tPourcentage de feuilles =", round((nb_feuille1 / rounds) * 100,2), "%"
    "\n\tPourcentage de ciseaux =", round((nb_ciseaux1 / rounds) * 100,2), "%"
    "\n\tPourcentage de pierres =", round((nb_pierre1 / rounds) * 100,2), "%")

def pourcentage2(): #fonction qui affiche les calculs fait dans la fonction p2
    print()
    print("L'ordinateur 2:"
          "\n\tNombres de feuilles =",nb_feuille2,
          "\n\tNombre de ciseaux =",nb_ciseaux2,
          "\n\tNombre de pierres =",nb_pierre2)
    print() #fait le calcul des pourcentages, arrondi à 2 chiffres après la virgules
    print("\tPourcentage de feuilles =", round((nb_feuille2 / rounds) * 100,2), "%"
    "\n\tPourcentage de ciseaux =", round((nb_ciseaux2 / rounds) * 100,2), "%"
    "\n\tPourcentage de pierres =", round((nb_pierre2 / rounds) * 100,2), "%")

def pourcentage3(): #fonction qui affiche l'addition des calculs de p1 et p2
    print()
    print("Au total:"
          "\n\tNombres de feuilles =", nb_feuille1 + nb_feuille2,
          "\n\tNombre de ciseaux  =", nb_ciseaux1 + nb_ciseaux2,
          "\n\tNombre de pierres =", nb_pierre1 + nb_pierre2)
    print() # calcul de pourcentages de p1 et p2, comme ce sont les 2, on doit doubler le nombre de tours quand on divise
    print("\tPourcentage de feuilles =", round(((nb_feuille1 + nb_feuille2) / (rounds * 2)) * 100,2), "%"
    "\n\tPourcentage de ciseaux =", round(((nb_ciseaux1 + nb_ciseaux2) / (rounds * 2)) * 100,2), "%"
    "\n\tPourcentage de pierres =", round(((nb_pierre1 + nb_pierre2) / (rounds * 2)) * 100,2), "%")
    


def stat(): #fonction qui demande à voir les statistiques on quitte la partie quand on fait 4
    st = int(input("Voulez vous des statistiques?"
"\nPour voir des statistiques de l'ordi 1: tappez 1"
"\nPour voir des statistiques de l'ordi 2: tappez 2"
"\nPour voir des statistiques des deux ordis: tappez 3"
"\nPour quittez la partie: tappez 4"
"\n\tChoix: "))
    if st == 1: 
        pourcentage1() #on affiche les statistiques de l'ordi 1 calculer grâce à la fonction p1
        print()
        stat() #l'utilisateur peut revoir autant de fois les statistiques
    if st == 2:
        pourcentage2() #on affiche les statistiques de l'ordi 2 calculer grâce à la fonction p2
        print()
        stat()
    if st == 3:
        pourcentage3() #on affiche les statistiques des ordis calculer grâce aux fonction p1 et p2
        print()
        stat()
    if st == 4: #quitter la partie 
        print()
        print("Merci beacoup, à la prochaine!") 

#rappel pour se rappeler du fonctionnement du jeu
rappel = """rappel: 
pierre = 0
papier = 1    
ciseaux = 2"""

score_joueur_1 = 0
score_joueur_2 = 0

tab_test_gagnant = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]] #tableau qui va tester qui a gagné
# définition des variables

# Menu du jeu où l'utilisateur choisis le mode de jeu
n = int(input("""        Choisissez le mode de jeu: 
Pour joueur contre l'ordinateur: tappez 1
Pour joueur contre un autre joueur: tappez 2     
Pour ordinateur contre ordinateur: tappez 3
                                          
              Choix : """))
print("")


rounds = int(input("Nombre de tours que vous souhaitez jouez superieur a 0 : ")) #Définition du nombre de tours
print("")
while rounds <= 0:
    rounds = int(input("Nombre de tours invalide, ressayez : "))

#Testage pour lancer le code pour le mode de jeu choisi, joueur x ordi
if n == 1:
    print("Mode chosi: joueur contre ordinateur avec", rounds, "tours")
    print("")
    for i in range(rounds): #lance le code le nombre de fois que le joueur choisi de tours
        print(rappel)
        print("")
        joueur_1 = int(input("Choix entre les 3: "))#annonce du choix du joueur
        if joueur_1 == 0:
            print("Vous avez choisi pierre")
        elif joueur_1 == 1:
            print("Vous avez choisi papier")
        elif joueur_1 == 2:
            print("Vous avez choisi ciseaux")
        joueur_2 = randint(0,2)
        if joueur_2 == 0:
            print("L'adversaire a choisi pierre")  #annonce du choix du joueur
        elif joueur_2 == 1:
            print("L'adversaire a choisi papier")
        else:
            print("L'adversaire a choisi ciseaux")
        gagnant = tab_test_gagnant[joueur_1][joueur_2] #Teste qui est le gagnant
        if gagnant == joueur_1:
            score_joueur_1 += 1#calcul du score de chaque joueur et actualise le score a chaque round
            print("")
            print ("Vous avez gagné")#Affiche le gagnant
        elif gagnant == joueur_2:
            score_joueur_2 += 1#calcul du score de chaque joueur et actualise le score a chaque round
            print("")
            print ("L’ordinateur à gagné")#Affiche le gagnant
        else:
            print("")
            print("Égalité!")#Affiche égalité en cas d'égalité
        print("")
        print("Joueur: ",score_joueur_1,"points","\nOrdinateur:", score_joueur_2,"points")#Affiche le score actuel après chaque round
        print("")
    if score_joueur_1 > score_joueur_2:  #Teste qui est le gagnant a la fin de tous les rounds
        print("\tJoueur est le gagnant!") #Affiche le gagnant a la fin de tous les rounds
    elif score_joueur_2 > score_joueur_1:
        print("\tL'ordinateur est le gagnant!")#Affiche le gagnant a la fin de tous les rounds
    else:
        print("\tÉgalité!")#Affiche égalité a la fin de tous les rounds si il a eu égalité
    print("\tBon match!")

  
#Testage pour lancer le code pour le mode de jeu choisi, joueur x joueur
if n == 2:
    print("Mode chosi: joueur contre joueur avec", rounds, "tours")
    print("")
    for i in range(rounds):
        print(rappel)
        print("")
        joueur_1 = int(input("Joueur 1: Choix entre les 3: ")) #affichage du choix du joueur caché
        print("Joueur 1 a choisi ********")
        joueur_2 = int(input("Joueur 2: Choix entre les 3: "))
        print("Joueur 2 a choisi ********")
        gagnant = tab_test_gagnant[joueur_1][joueur_2]
        print("")
        if joueur_1 == 0:
            print("Joueur 1 avait choisi pierre") #Affichage du choix des joueurs simultannées
        elif joueur_1 == 1:
            print("Joueur 1 avait choisi papier")
        elif joueur_1 == 2:
            print("Joueur 1 avait choisi ciseaux")
        if joueur_2 == 0:
            print("Joueur 2 avait choisi pierre")
        elif joueur_2 == 1:
            print("Joueur 2 avait choisi papier")
        elif joueur_2 == 2:
            print("Joueur 2 avait choisi ciseaux")
        gagnant = tab_test_gagnant[joueur_1][joueur_2] #Teste qui est le gagnant 
        if gagnant == joueur_1:
            score_joueur_1 += 1#calcul du score de chaque joueur et actualise le score a chaque round
            print("")
            print ("Joueur 1 a gagné") #Affiche le gagnant
        elif gagnant == joueur_2:
            score_joueur_2 += 1 #calcul du score de chaque joueur et actualise le score a chaque round
            print("")
            print ("Joueur 2 a gagné") #Affiche le gagnant
        else:
            print("")
            print("Égalité!")#Affiche égalité en cas d'égalité
        print("")
        print("Joueur 1: ",score_joueur_1,"points","\nJoueur 2:", score_joueur_2,"points") #Affiche le score actuel après chaque round
        print("")
        
        if score_joueur_1 > score_joueur_2:
            print("\tJoueur 1 est le gagnant!")
        elif score_joueur_2 > score_joueur_1:
            print("\tJoueur 2 est le gagnant!")
        else:
            print("\tÉgalité!")
        print("\tBon match!")

  
#Testage pour lancer le code pour le mode de jeu choisi, ordi x ordi (statistiques)
if n == 3:
    nb_pierre1 = 0
    nb_feuille1 = 0
    nb_ciseaux1 = 0              #compteurs des deux ordis  pour chaque option
    nb_pierre2 = 0
    nb_feuille2 = 0
    nb_ciseaux2 = 0
    print("Mode chosi: ordinateur contre ordinateur avec", rounds, "tours")
    print()
    for i in range(rounds): #lance le code le nombre de fois que le joueur choisi de tours
        joueur_1 = randint(0,2)
        p1()
        joueur_2 = randint(0,2)
        p2()
        gagnant = tab_test_gagnant[joueur_1][joueur_2] #chercher le gagnant
        if gagnant == joueur_1:
            score_joueur_1 += 1         #addition au compteur
        elif gagnant == joueur_2:
            score_joueur_2 += 1
    print(" Joueur 1: ",score_joueur_1,"points","\n","Joueur 2:", score_joueur_2,"points", "\n", "Égalités:", rounds - (score_joueur_1 + score_joueur_2), "fois")
    print()
    stat()       #affichage du menu du choix des stats  