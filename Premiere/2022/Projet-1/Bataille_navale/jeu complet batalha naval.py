#jeu
def jeu1(a):
    from random import randint    
    t1 = [[0] * 5 for loop in range (5)]# grille Player 1
    t2 = [[0] * 5 for loop in range (5)]# grlle Player 2(pc)
    ac1 = 0 # score player 1
    ac2 = 0 # score player 2
    print()
    print()
    print("Étape 1 sélection : ")
    print()
    for i in range(5):
        print()
        cord_y = int(input(f"Entrez la coordonnées de l'ordonné de votre bateau.{i + 1} entre 0 et 4: ")) # coordonée grille colone Player 1
        cord_x = int(input(f"Entrez la coordonnées de l'abcisse de votre bateau.{i + 1} entre 0 et 4: "))# coordonée grille ligne P1
        t1[cord_y][cord_x] = "x"         
        cord_y_pc = randint(0,4) # coordonée grille colone pc
        cord_x_pc = randint(0,4) # coordonée grille ligne pc
        while t2[cord_y_pc][cord_x_pc] != 0: # éviter répetition de même cordonnée
            cord_y_pc = randint(0,4)
            cord_x_pc = randint(0,4)
        t2[cord_y_pc][cord_x_pc] = "x"
        
    



    
    print()
        
    print("Voici votre grille : ")
    print()
    for i in range(len(t1)):
        print(t1[i])
    print()    
    print("Étape 2 ")
    
    
    print()
    
    while ac1 != 5 or ac2 != 5:
        print()
        print("Tour Player 1 : ")
        attack_y = int(input(" Player 1: Entrez la coordonnée de l'ordonnée où vous allez attaquer votre adversaire : "))
        attack_x = int(input(" Player 1: Entrez la coordonnée de l'abcisse où vous allez attaquer votre adversaire : "))
        if t2[attack_y][attack_x] != 0:
            ac1 += 1
            print()
            print("Score Player 1 : ", ac1)
        elif t2[attack_y][attack_x] == 0:
            print()
            print("Ooh, aucun bateau rencontré")        
        while t2[attack_y][attack_x] != 0 and ac1 < 5:                       
            t2[attack_y][attack_x] = 0
            print()
            print("Boom!! Bateau ennemi détruit !!!")
            print("vous avez le droit de jouer à nouveau : ")
            print()
            attack_y = int(input(" Player 1: Entrez la coordonnée de l'ordonnée où vous allez attaquer votre adversaire : "))
            attack_x = int(input(" Player 1: Entrez la coordonnée de l'abcisse où vous allez attaquer votre adversaire : "))
            print()
            if t2[attack_y][attack_x] != 0:
                ac1 += 1
                print("Score Player 1 : ", ac1)
            if t2[attack_y][attack_x] == 0:
                print()
                print("Ohh, aucun bateau rencontré")
            print()            
        if ac1 == 5:
            print()
            print("uhuull Vous avez ganhé !!!!!")
            break
            
                




        if t2[attack_y][attack_x] == 0:
            print()
            print("Tour Player 2 : ")
            attack_y_pc = randint(0,4)
            attack_x_pc = randint(0,4)
            if t1[attack_y_pc][attack_x_pc] != 0:
                    ac2 += 1
            elif t1[attack_y_pc][attack_x_pc] == 0:                
                print("Player 2 n'a pas rencontré de bateau sur votre grille")                
            while t1[attack_y_pc][attack_x_pc] != 0 and ac2 < 5:                               
                t1[attack_y_pc][attack_x_pc] = 0                
                print("Oops!! Votre bateau a été détruit !!!")
                print()
                print("Player 2 a le droit de jouer à nouveau : ")
                attack_y_pc = randint(0,4)
                attack_x_pc = randint(0,4)
                if t1[attack_y_pc][attack_x_pc] != 0:
                    ac2 += 1
                if t1[attack_y_pc][attack_x_pc] == 0:                    
                    print("Player 2 n'a pas rencontré de bateau sur votre plan")
                print()    
                print("Voici votre plan actualisé : ")
                print()
                for j in range(len(t1)):
                     print(t1[j])
            if ac2 == 5:
                print()
                print("Oops!! Votre bateau a été détruit !!!") 
                print("Dommage, vous avez perdu !")
                break
            

#jeu a 2 
def jeu2(b):        
    t1 = [[0] * 5 for loop in range (5)]# grille Player 1
    t2 = [[0] * 5 for loop in range (5)]# grlle Player 2
    ac1 = 0 # score player 1
    ac2 = 0 # score player 2
    print()
    print()
    print("Étape 1 sélection : ")
    print()
    for i in range(5):
        print()
        cord_y = int(input(f"Player 1 : Entrez la coordonnées de l'ordonné de votre bateau.{i + 1} entre 0 et 4: ")) # coordonée grille colone Player 1
        cord_x = int(input(f"Player 1 : Entrez la coordonnées de l'abcisse de votre bateau.{i + 1} entre 0 et 4: "))# coordonée grille ligne Player 1
        t1[cord_y][cord_x] = "x"
    print()
    print("Player 2 : ")
    for j in range(5):
        cord_y_p2 = int(input(f"Player 2 : Entrez la coordonnées de l'ordonné de votre bateau.{i + 1} entre 0 et 4: ")) # coordonée grille colone Player 1
        cord_x_p2 = int(input(f"Player 2 : Entrez la coordonnées de l'abcisse de votre bateau.{i + 1} entre 0 et 4: ")) # coordonée grille ligne Player 1
        t2[cord_y_p2][cord_x_p2] = "x"    
    print()
    print("Étape 2 ")
    
    
    print()
    
    while ac1 != 5 or ac2 != 5:
        print()
        print("Tour Player 1 : ")
        attack_y = int(input(" Player 1: Entrez la coordonnée de l'ordonnée où vous allez attaquer votre adversaire : "))
        attack_x = int(input(" Player 1: Entrez la coordonnée de l'abcisse où vous allez attaquer votre adversaire : "))
        if t2[attack_y][attack_x] != 0:
            ac1 += 1
            print()
            print("Score Player 1 : ", ac1)
        elif t2[attack_y][attack_x] == 0:
            print()
            print("Ooh, aucun bateau rencontré")        
        while t2[attack_y][attack_x] != 0 and ac1 < 5:                       
            t2[attack_y][attack_x] = 0
            print()
            print("Boom!! Bateau ennemi détruit !!!")
            print("vous avez le droit de jouer à nouveau : ")
            print()
            attack_y = int(input(" Player 1: Entrez la coordonnée de l'ordonnée où vous allez attaquer votre adversaire : "))
            attack_x = int(input(" Player 1: Entrez la coordonnée de l'abcisse où vous allez attaquer votre adversaire : "))
            print()
            if t2[attack_y][attack_x] != 0:
                ac1 += 1
                print("Score Player 1 : ", ac1)
            if t2[attack_y][attack_x] == 0:
                print()
                print("Ohh, aucun bateau rencontré")
            print()            
        if ac1 == 5:
            print()
            print("uhuull Player 1 a ganhé !!!!!")
            break
            
                




        if t2[attack_y][attack_x] == 0:
            print()
             
            print("Tour Player 2 : ")
            attack_y_p2 = int(input(" Player 2: Entrez la coordonnée de l'ordonnée où vous allez attaquer votre adversaire : "))
            attack_x_p2 = int(input(" Player 2: Entrez la coordonnée de l'abcisse où vous allez attaquer votre adversaire : "))
            if t1[attack_y_p2][attack_x_p2] != 0:
                ac2 += 1
                print()
                print("Score Player 2 : ", ac2)
            elif t1[attack_y_p2][attack_x_p2] == 0:
                print()
                print("Ooh, aucun bateau rencontré")        
            while t1[attack_y_p2][attack_x_p2] != 0 and ac2 < 5:                       
                t1[attack_y_p2][attack_x_p2] = 0
                print()
                print("Boom!! Bateau ennemi détruit !!!")
                print("vous avez le droit de jouer à nouveau : ")
                print()
                attack_y_p2 = int(input(" Player 1: Entrez la coordonnée de l'ordonnée où vous allez attaquer votre adversaire : "))
                attack_x_p2 = int(input(" Player 1: Entrez la coordonnée de l'abcisse où vous allez attaquer votre adversaire : "))
                print()
                if t1[attack_y_p2][attack_x_p2] != 0:
                    ac1 += 1
                    print("Score Player 1 : ", ac1)
                if t2[attack_y_p2][attack_x_p2] == 0:
                    print()
                    print("Ohh, aucun bateau rencontré")
                print()            
            if ac2 == 5:
                print()
                print("uhuull Player 2 a ganhé !!!!!")
                break
def jeu3(c):
    from random import randint    
    t1 = [[0] * 5 for loop in range (5)]# grille Player 1
    t2 = [[0] * 5 for loop in range (5)]# grlle Player 2(pc)
    ac1 = 0 # score player 1
    ac2 = 0 # score player 2
    print()
    print()
    print("Étape 1 sélection : ")
    print()
    for i in range(5):
        print()
        cord_y = int(input(f"Entrez la coordonnées de l'ordonné de votre bateau.{i + 1} entre 0 et 4: ")) # coordonée grille colone Player 1
        cord_x = int(input(f"Entrez la coordonnées de l'abcisse de votre bateau.{i + 1} entre 0 et 4: ")) # coordonée grille ligne Player 1
        t1[cord_y][cord_x] = "x"         
        cord_y_pc = randint(0,4) # coordonée grille colone pc
        cord_x_pc = randint(0,4) # coordonée grille ligne pc
        while t2[cord_y_pc][cord_x_pc] != 0: # éviter répetition de même cordonnée
            cord_y_pc = randint(0,4)
            cord_x_pc = randint(0,4)
        t2[cord_y_pc][cord_x_pc] = "x"
        
    



    
    print()
        
    print("Voici votre grille : ")
    print()
    for i in range(len(t1)):
        print(t1[i])
    print()    
    print("Étape 2 ")
    
    
    print()
    
    while ac1 != 5 or ac2 != 5:
        print()
        print("Tour Player 1 : ")
        attack_y = int(input(" Player 1: Entrez la coordonnée de l'ordonnée où vous allez attaquer votre adversaire : "))
        attack_x = int(input(" Player 1: Entrez la coordonnée de l'abcisse où vous allez attaquer votre adversaire : "))
        if t2[attack_y][attack_x] != 0:
            ac1 += 1
            print()
            print("Score Player 1 : ", ac1)
        elif t2[attack_y][attack_x] == 0:
            print()
            print("Ooh, aucun bateau rencontré")        
        while t2[attack_y][attack_x] != 0  and ac1 < 5:                       
            t2[attack_y][attack_x] = 0
            print()
            print("Boom!! Bateau ennemi détruit !!!")
            print("vous avez le droit de jouer à nouveau : ")
            print()
            attack_y = int(input(" Player 1: Entrez la coordonnée de l'ordonnée où vous allez attaquer votre adversaire : "))
            attack_x = int(input(" Player 1: Entrez la coordonnée de l'abcisse où vous allez attaquer votre adversaire : "))
            print()
            if t2[attack_y][attack_x] != 0:
                ac1 += 1               
                print("Score Player 1 : ", ac1)
            if t2[attack_y][attack_x] == 0:
                print()
                print("Ohh, aucun bateau rencontré")
            print()            
        if ac1 == 5:
            print()
            print("uhuull Vous avez ganhé !!!!!")
            break
            
                




        if t2[attack_y][attack_x] == 0:
            print()
            print("Tour Player 2 : ")
            attack_y_pc = randint(0,4)
            attack_x_pc = randint(0,4)
            while t1[attack_y_pc][attack_x_pc] == 1:
                attack_y_pc = randint(0,4)
                attack_x_pc = randint(0,4)
            if t1[attack_y_pc][attack_x_pc] == "x":
                    ac2 += 1
            elif t1[attack_y_pc][attack_x_pc] == 0:
                t1[attack_y_pc][attack_x_pc] = 1                
                print("Player 2 n'a pas rencontré de bateau sur votre grille")               
            while t1[attack_y_pc][attack_x_pc] == "x" and ac2 < 5:                               
                t1[attack_y_pc][attack_x_pc] = 1                
                print("Oops!! Votre bateau a été détruit !!!")
                print()
                print("Player 2 a le droit de jouer à nouveau : ")
                attack_y_pc = randint(0,4)
                attack_x_pc = randint(0,4)
                if t1[attack_y_pc][attack_x_pc] =="x":
                    ac2 += 1
                if t1[attack_y_pc][attack_x_pc] == 0:                    
                    print("Player 2 n'a pas rencontré de bateau sur votre plan")              
                print()    
                print("Voici votre plan actualisé : ")
                print("les 1 correspondent aux ataques du Player 2 et les  x  correspondent à vos bateau")
                print()
                for j in range(len(t1)):
                     print(t1[j])
            if ac2 == 5:
                print()
                print("Oops!! Votre bateau a été détruit !!!") 
                print("Dommage, vous avez perdu !")
                break
            

        
        
        
print("Bienvenus à la bataille navale")
print()
print("Voici les règles du jeu :")
print("  -Le jeu commence quand chaque joueur place 5 bateaux sur sa grille.")
print("  -Ensuite, un à un, les joueurs se tirent dessus pour détruire les navires ennemis")
print("  -pour cela vous devez citer les coordonnées d’un emplacement.")
print("  -La bataille finit lorsqu' un des joueurs fait couler tous les bateaux adversaires.")
cm = int(input("Pour jouer seul contre l'ordi entrez 1, pour jouer à deux rentrez 2 : "))
if cm == 1:
    dif = int(input("Pour jouer le mode facile entrez 1, pour le dificile 2 : "))
    if dif == 1:
        print(jeu1(1))
    elif dif == 2:
        print(jeu3(1))
elif cm == 2:
    print(jeu2(1))
