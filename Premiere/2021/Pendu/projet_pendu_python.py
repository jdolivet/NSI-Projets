from random import choice
from turtle import *
from time import sleep
mots = ["casserole", "cuillere", "patate", "voiture", "maman","zebre","portable","marchandise","stylo","tortue","ours","trousse", "chaussure", "telephone" ,"maison" ,"jour" ,"ordinateur" ,"bouteille" ,"camion" ,"jardin" ,"football" ,"chien" ,"planete"]
# Une liste de mot 
solution = choice(mots)#la variable solution va être égale à un mot choisit au hazard du tableau "mots"
#print(solution): on a mis cette fonctionnalité pour voir le mot choisi, pour faciliter les tests
tentatives = 7 # le nombre de tentatives avec lesquelles on commance
affichage = "" # il va afficher un tiret pour chaque lettre de la solution et si on a trouvé cette lettre,
               # il va afficher la lettre
k='' # liste de lettres proposés 
lettres_trouvees = "" #liste des lettres proposées qui se trouvent dans la solution

for l in solution:
    affichage = affichage + "_ "
    up()
    goto(-130,200)#La position du pinceau
    down()
    write(" Bienvenu dans le pendu ", font=("Arial", 16, "normal"))# les fonctionnalités de la phrases
                                                                   # (taille des lettres, type de lettre)
    # On commence le programme par ici, par cette phrase

while tentatives > 0:
    up()
    goto(-150,-200)#La position du pinceau
    down()
    write(f"Mot à deviner : {affichage}", font=("Arial", 16, "normal"))
    proposition = textinput( "Pendu","Proposez une lettre")
    undo()
    undo()
    # Dès qu'on commence a donné une lettre, on commence par montrer le mot à deviner,
    # puis un message s'affiche pour que l'utilisateur propose une lettre
    
    if len(proposition) > 1:
        up()
        goto(-300,-250)#La position du pinceau
        down()
        write(" Pourquoi tu mets plusieures lettres? Allez... Je te laisse une autre chance.", font=("Arial", 14, "normal"))
        sleep(3) #Une fonctionnalité concernant le temps qu'apparaît la phrase (dans ce cas, 3 secondes).
        undo()
        # Cette première condition permet de voir si on a mis plusieurs lettres comme option,
        # si on en a mis plusieures il revient au début, sinon il continue
        
    else:
        if proposition in k:
            up()
            goto(-300,-250)#La position du pinceau
            down()
            write("Tu as déjà mis cette lettre... Je te laisse une autre chance",font=("Arial", 14, "normal"))
            sleep(3)
            undo()
            up()
            goto(-300,250)#La position du pinceau
            write(f"Lettres déjà proposés: {k}",font=("Arial", 14, "normal")) # affiche les lettres
                                                                              # déjà proposés précédament
            down()
            # Si on a déjà proposé cette lettre, il va revenir au début 
            
        else:
            k += proposition + ', '
            up()
            goto(-300,250)#La position du pinceau
            write(f"Lettres déjà proposés: {k}",font=("Arial", 14, "normal")) #Ici il nous montre les lettres proposés
                                                                              # précédament.
            down()
            #Si on a pas déjà proposé précédament la lettre qu'on vient de proposer, il va continuer
            if proposition in solution:
                lettres_trouvees += proposition
                up()
                goto(-300,-250)
                down()
                write(f"Oui, la lettre {proposition} se trouve dans ce mot", font=("Arial", 16, "normal"))
                sleep(5)
                undo()
                #Dans cette condition, il affiche cette phrase quand la lettre proposé se trouve dans la solution.
            
            else:
                up()
                goto(-300,-250)#La position du pinceau
                down()
                write(f"Non, la lettre {proposition} ne se trouve pas dans ce mot", font=("Arial", 16, "normal"))
                sleep(3)
                undo()
                tentatives -= 1
                #Si la lettre proposée ne se trouve pas dans la solution, il va enlever a tentatives 1
                #et affichera la partie du dessin correspondant
                if tentatives == 6:
                    up()
                    goto(-150, -100)
                    down()
                    begin_fill()
                    forward(280)
                    right(90)
                    forward(5)
                    right(90)
                    forward(280)
                    end_fill()
                    up()
                    goto(-150, -150)#La position du pinceau
                    #Donc avec la première erreur, on dessine une première barre en bas, horrizontale, qui commence le dessin du pendu.
                   
                    
                elif tentatives == 5:
                    up()
                    goto(-150, -105)#La position du pinceau
                    down()
                    begin_fill()
                    right(90)
                    forward(205)
                    right(90)
                    forward(10)
                    right(90)
                    forward(205)
                    right(90)
                    forward(20)
                    right(120)
                    forward(40)
                    right(60)
                    end_fill()
                    up()
                    goto(-150, -150)#La position du pinceau
                    #Si on rate encore une fois, il dessine une barre verticale
                    # à gauche de la première barre horrizontale
                    
                elif tentatives == 4:
                    up()
                    goto(-150,100)#La position du pinceau
                    down()
                    begin_fill()
                    forward(20)
                    right(120)
                    forward(40)
                    left(60)
                    end_fill()
                    goto(-130,100)#La position du pinceau
                    begin_fill()
                    left(60)
                    forward(180)
                    left(90)
                    forward(10)
                    left(90)
                    forward(200)
                    left(90)
                    forward(10)
                    left(90)
                    forward(180)
                    end_fill()
                    # Si on rate encore une fois,  il dessine encore une barre horrizontale vers
                    # la droite en haut de la barre verticale 
                
                elif tentatives == 3:
                    up()
                    goto(30,100)#La position du pinceau
                    down()
                    begin_fill()
                    right(90)
                    forward(10)
                    right(90)
                    forward(6)
                    right(90)
                    forward(10)
                    end_fill()
                    #Si on rate encore une fois,
                    #il nous fait une petite barre vers le bas pour commencer à dessiner le bonhomme
                elif tentatives == 2:
                    up()
                    goto(27,90)#La position du pinceau
                    down()
                    left(90)
                    begin_fill()
                    circle(20)
                    end_fill()
                    #Si on rate encore une fois, il dessine la tête du bonhomme
                elif tentatives == 1 :
                    up()
                    goto(27,50)#La position du pinceau
                    down()
                    begin_fill()
                    forward(5)
                    left(90)
                    forward(40)
                    left(90)
                    forward(10)
                    left(90)
                    forward(40)
                    left(90)
                    forward(10)
                    left(45)
                    forward(40)
                    left(90)
                    forward(4)
                    left(90)
                    forward(36)
                    end_fill()
                    goto(32,50)#La position du pinceau
                    begin_fill()
                    right(90)
                    forward(40)
                    right(90)
                    forward(4)
                    right(90)
                    forward(36)
                    end_fill()
                    #Si on rate encore une fois, il dessine le tronc et les bras
                elif tentatives == 0:
                    up()
                    goto(22,10)#La position du pinceau
                    down()
                    begin_fill()
                    left(120)
                    forward(40)
                    left(90)
                    forward(7)
                    left(90)
                    forward(35)
                    right(150)
                    forward(35)
                    right(270)
                    forward(7)
                    left(90)
                    forward(40)
                    end_fill()
                    up()
                    goto(500,500)#La position du pinceau
                    clear()
                    goto(-200,0)
                    write(f"Tu as perdu, le mot a deviner était {solution}", font=("Arial", 16, "normal"))
                    break
                #Puis finalement, si on rate une dernière fois il fini le dessin avec
                # les jambes et écris la phrase finale en disant qu'on a perdu et montrant la solution
        
    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "
            # cette partie va voir pour chaque caractère de la solution si elle se trouve dans les lettres_trouvees,
            # si elle se trouve il va ajouter à affichage cette lettre, si non il va mettre un tiret
       
   
    if "_" not in affichage:     
        clear()
        up()
        goto(-170,0)
        write(f"Tu avais raison, le mot a deviner était {solution}", font=("Arial", 16, "normal"))
        break
    # Quand il n'y a plus de tiret dans affichage ça veut dire qu'on à trouvé
    # toutes les lettres et on aura alors gagné puis affichera ce message 
