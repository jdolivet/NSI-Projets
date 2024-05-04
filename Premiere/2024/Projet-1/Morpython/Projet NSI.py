from turtle import *
import sys

# Définition des fonctions



def verificationa():
    if a == 1:
        if c1==50 and c2==50 and c3==50:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c1==50 and c4==50 and c7==50:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c1==50 and c5==50 and c9==50:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c2==50 and c5==50 and c8==50:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c3==50 and c5==50 and c7==50:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c3==50 and c6==50 and c9==50:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c4==50 and c5==50 and c6==50:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c7==50 and c8==50 and c9==50:
            print (f"{n1} a gagné!")
            sys.exit()
    if a == 2:
        if c1==100 and c2==100 and c3==100:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c1==100 and c4==100 and c7==100:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c1==100 and c5==100 and c9==100:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c2==100 and c5==100 and c8==100:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c3==100 and c5==100 and c7==100:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c3==100 and c6==100 and c9==100:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c4==100 and c5==100 and c6==100:
            print (f"{n1} a gagné!")
            sys.exit()
        elif c7==100 and c8==100 and c9==100:
            print (f"{n1} a gagné!")
            sys.exit()
            

def croix1():
    color("blue")
    up()
    goto(-150, 150)
    down()
    goto(-50, 50)
    goto(-100,100)
    goto(-150,50)
    goto(-50,150)
def croix2():
    color("blue")
    up()
    goto(-50,150)
    down()
    goto(50, 50)
    goto(0,100)
    goto(-50,50)
    goto(50,150)
def croix3():
    color("blue")
    up()
    goto(150, 150)
    down()
    goto(50, 50)
    goto(100,100)
    goto(150,50)
    goto(50,150)
    
def croix4():
    color("blue")
    up()
    goto(-150,50)
    down()
    goto(-50,-50)
    goto(-100,0)
    goto(-150,-50)
    goto(-50,50)
def croix5():
    color("blue")
    up()
    goto(-50,50)
    down()
    goto(50,-50)
    goto(0,0)
    goto(-50,-50)
    goto(50,50)

def croix6():
    color("blue")
    up()
    goto(150,50)
    down()
    goto(50,-50)
    goto(100,0)
    goto(150,-50)
    goto(50,50)
def croix7():
    color("blue")
    up()
    goto(-150,-50)
    down()
    goto(-50,-150)
    goto(-100,-100)
    goto(-150,-150)
    goto(-50,-50)
def croix8():
    color("blue")
    up()
    goto(-50,-50)
    down()
    goto(50,-150)
    goto(0,-100)
    goto(-50,-150)
    goto(50,-50)
def croix9():
    color("blue")
    up()
    goto(150,-50)
    down()
    goto(50,-150)
    goto(100,-100)
    goto(150,-150)
    goto(50,-50)
    

def cercle1():
    color("red")
    up()
    goto(-100,50)
    down()
    circle(49)

def cercle2():
    color("red")
    up()
    goto(0,50)
    down()
    circle(49)

def cercle3():
    color("red")
    up()
    goto(100,50)
    down()
    circle(49)

def cercle4():
    color("red")
    up()
    goto(-100,-50)
    down()
    circle(49)
    
def cercle5():
    color("red")
    up()
    goto(0,-50)
    down()
    circle(49)

def cercle6():
    color("red")
    up()
    goto(100,-50)
    down()
    circle(49)

def cercle7():
    color("red")
    up()
    goto(-100,-150)
    down()
    circle(49)
    
def cercle8():
    color("red")
    up()
    goto(0, -150)
    down()
    circle(49)

def cercle9():
    color("red")
    up()
    goto(100,-150)
    down()
    circle(49)
    

def tableau():
    up()
    goto (-150,50)
    down()
    goto(150,50)
    goto(50,50)
    goto(50,150)
    goto(150,150)
    goto(-150,150)
    goto(50,150)
    goto(50,-150)
    goto(-150,-150)
    goto(150,-150)
    up()
    goto(-50,50)
    down()
    goto(-50,150)
    goto(-50,-150)
    up()
    goto(-150,50)
    down()
    goto(-150,150)
    goto(-150,-150)
    up()
    goto(150,50)
    down()
    goto(150,150)
    goto(150,-150)
    goto(150,-50)
    goto(-150,-50)
    
#Création Variables des cases   
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0

#Présentation du jeux
print ("Bienvenue dans le Tic, Tac, Toe!")
print ("Fait par: Breno, Alphonse et Louis")
print("")
print("Le but du jeu est de remplir une ligne du quadrillage avec 3 cercle ou bien 3 croix, soit en diagonale, verticale ou horizontale. ")
print(" Pour cela, chacun votre tour, vous devrez indiquer si vous voulez déposer")
print("votre symbole sur la case 1,2,3,4,5,6,7,8 ou 9. ")
print(" Lorsque l'un des joueurs parvient à réaliser une ligne, ")
print("il remporte directement la partie. Si'l y a égalité, aucun vainqueur n'est déclaré.")
print("Atention une autre application va s'ouvrir  pour  déssiner  le  quadrillage  veuillez cliquez pour voir le résultat.")
print("")

#Début du jeux
n1= input("Entrez le prénom du joueur 1: ")
n2= input ("Entrez le prénom du joueur 2: ")
print("")
print (" Voici le cadrillage:")
print("Atention le nombre de la case sera le nombre à entrez pour jouer cette dernière!")
print("")
print("#"*13 )
print("# 1 # 2 # 3 #")
print("#"*13)
print("# 4 # 5 # 6 #")
print("#"*13)
print("# 7 # 8 # 9 #")
print("#"*13)
print("")


a=int(input(f"{n1} entrez le numéro 1 pour choisir la croix ou le numéro 2 pour le cercle: "))
print("")


if a==1:
    b=2
    print(f"{n1} sera la croix")
    print(f"{n2} sera le cercle")
if a==2:
    b=1
    print(f"{n1} sera le cercle")
    print(f"{n2} sera la croix")
ja1= int(input(f"{n1} entrez la case que vous voulez jouer: "))

if a==1:
    if ja1==1:
        width(5)
        tableau()
        croix1()
        c1=50
    if ja1==2:
        width(5)
        tableau()
        croix2()
        c2=50
    if ja1==3:
        width(5)
        tableau()
        croix3()
        c3=50
    if ja1==4:
        width(5)
        tableau()
        croix4()
        c4=50
    if ja1==5:
        width(5)
        tableau()
        croix5()
        c5=50
    if ja1==6:
        width(5)
        tableau()
        croix6()
        c6=50
    if ja1==7:
        width(5)
        tableau()
        croix7()
        c7=50
    if ja1==8:
        width(5)
        tableau()
        croix8()
        c8=50
    if ja1==9:
        width(5)
        tableau()
        croix9()
        c9=50
if a==2:
    if ja1==1:
        width(5)
        tableau()
        cercle1()
        c1=100
    if ja1==2:
        width(5)
        tableau()
        cercle2()
        c2=100
    if ja1==3:
        width(5)
        tableau()
        cercle3()
        c3=100
    if ja1==4:
        width(5)
        tableau()
        cercle4()
        c4=100
    if ja1==5:
        width(5)
        tableau()
        cercle5()
        c5=100
    if ja1==6:
        width(5)
        tableau()
        cercle6()
        c6=100
    if ja1==7:
        width(5)
        tableau()
        cercle7()
        c7=100
    if ja1==8:
        width(5)
        tableau()
        cercle8()
        c8=100
    if ja1==9:
        width(5)
        tableau()
        cercle9()
        c9=100

ja2= int(input(f"{n2} entrez la case que vous voulez jouer: "))

if b==1:
    if ja2==1:
        if c1==0:
            croix1()
            c1=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            
    
    elif ja2==2:
        if c2==0:
            croix2()
            c2=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
        
   
        
    elif ja2==3 :
        if c3==0:
            croix3()
            c3=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
        
   
    elif ja2==4:
        if c4==0:
            croix4()
            c4=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
        
    
    elif ja2==5 :
        if c5==0:
            croix5()
            c5=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            
    elif ja2==6:
        if c6==0:
            croix6()
            c6=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
    
    elif ja2==7 :
        if c7==0:
            croix7()
            c7=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
    
    elif ja2==8 :
        if c8==0:
            croix8()
            c8=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
    
    elif ja2==9 :
        if c9==0:
            croix9()
            c9=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
if b==2:
    if ja2==1:
        if c1==0:
            cercle1()
            c1=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja2==2 :
        if c2==0:
            cercle2()
            c2=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja2==3 :
        if c3==0:
            cercle3()
            c3=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()

    
    elif ja2==4:
        if c4==0:
            cercle4()
            c4=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja2==5:
        if c5==0:
            cercle5()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja2==6 :
        if c6==0:
            cercle6()
            c6=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja2==7:
        if c7==0:
            cercle7()
            c7=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja2==8:
        if c8==0:
            cercle8()
            c8=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja2==9 :
        if c9==0:
            cercle9()
            c9=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()





ja3= int(input(f"{n1} entrez la case que vous voulez jouer: "))



if a==1:
    if ja3==1:
        if c1==0:
            croix1()
            c1=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    
    elif ja3==2:
        if c2==0:
            croix2()
            c2=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
        
    elif ja3==3 :
        if c3==0:
            croix3()
            c3=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
    elif ja3==4:
        if c4==0:
            croix4()
            c4=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja3==5 :
        if c5==0:
            croix5()
            c5=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja3==6:
        if c6==0:
            croix6()
            c6=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja3==7 :
        if c7==0:
            croix7()
            c7=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja3==8 :
        if c8==0:
            croix8()
            c8=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja3==9 :
        if c9==0:
            croix9()
            c9=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
if a==2:
    if ja3==1:
        if c1==0:
            cercle1()
            c1=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja3==2 :
        if c2==0:
            cercle2()
            c2=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja3==3 :
        if c3==0:
            cercle3()
            c3=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()

    
    elif ja3==4:
        if c4==0:
            cercle4()
            c4=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja3==5:
        if c5==0:
            cercle5()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja3==6 :
        if c6==0:
            cercle6()
            c6=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja3==7:
        if c7==0:
            cercle7()
            c7=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja3==8:
        if c8==0:
            cercle8()
            c8=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    elif ja3==9 :
        if c9==0:
            cercle9()
            c9=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
        
ja4= int(input(f"{n2} entrez la case que vous voulez jouer: "))

if b==1:
    if ja4==1:
        if c1==0:
            croix1()
            c1=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja4==2:
        if c2==0:
            croix2()
            c2=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
        
    elif ja4==3 :
        if c3==0:
            croix3()
            c3=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
    elif ja4==4:
        if c4==0:
            croix4()
            c4=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja4==5 :
        if c5==0:
            croix5()
            c5=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja4==6:
        if c6==0:
            croix6()
            c6=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja4==7 :
        if c7==0:
            croix7()
            c7=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja4==8 :
        if c8==0:
            croix8()
            c8=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja4==9 :
        if c9==0:
            croix9()
            c9=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
if b==2:
    if ja4==1:
        if c1==0:
            cercle1()
            c1=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja4==2 :
        if c2==0:
            cercle2()
            c2=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja4==3 :
        if c3==0:
            cercle3()
            c3=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()

    
    elif ja4==4:
        if c4==0:
            cercle4()
            c4=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja4==5:
        if c5==0:
            cercle5()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja4==6 :
        if c6==0:
            cercle6()
            c6=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja4==7:
        if c7==0:
            cercle7()
            c7=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja2==8:
        if c8==0:
            cercle8()
            c8=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja4==9 :
        if c9==0:
            cercle9()
            c9=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
#5eme coup
ja5= int(input(f"{n1} entrez la case que vous voulez jouer: "))

if a==1:
    if ja5==1:
        if c1==0:
            croix1()
            c1=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    
    elif ja5==2:
        if c2==0:
            croix2()
            c2=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
        
    elif ja5==3 :
        if c3==0:
            croix3()
            c3=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
    elif ja5==4:
        if c4==0:
            croix4()
            c4=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja5==5 :
        if c5==0:
            croix5()
            c5=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja5==6:
        if c6==0:
            croix6()
            c6=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja5==7 :
        if c7==0:
            croix7()
            c7=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    elif ja5==8 :
        if c8==0:
            croix8()
            c8=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja5==9 :
        if c9==0:
            croix9()
            c9=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
if a==2:
    if ja5==1:
        if c1==0:
            cercle1()
            c1=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja5==2 :
        if c2==0:
            cercle2()
            c2=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja5==3 :
        if c3==0:
            cercle3()
            c3=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()

    
    elif ja5==4:
        if c4==0:
            cercle4()
            c4=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja5==5:
        if c5==0:
            cercle5()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja5==6 :
        if c6==0:
            cercle6()
            c6=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja5==7:
        if c7==0:
            cercle7()
            c7=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja5==8:
        if c8==0:
            cercle8()
            c8=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja5==9 :
        if c9==0:
            cercle9()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
#vérification
if a == 1:
    if c1==50 and c2==50 and c3==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==50 and c4==50 and c7==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==50 and c5==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c2==50 and c5==50 and c8==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==50 and c5==50 and c7==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==50 and c6==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c4==50 and c5==50 and c6==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c7==50 and c8==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
if a == 2:
    if c1==100 and c2==100 and c3==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==100 and c4==100 and c7==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==100 and c5==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c2==100 and c5==100 and c8==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==100 and c5==100 and c7==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==100 and c6==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c4==100 and c5==100 and c6==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c7==100 and c8==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()

    

#6eme coup
ja6= int(input(f"{n2} entrez la case que vous voulez jouer: "))

if b==1:
    if ja6==1:
        if c1==0:
            croix1()
            c1=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    
    elif ja6==2:
        if c2==0:
            croix2()
            c2=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
        
    elif ja6==3 :
        if c3==0:
            croix3()
            c3=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
    elif ja6==4:
        if c4==0:
            croix4()
            c4=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja6==5 :
        if c5==0:
            croix5()
            c5=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja6==6:
        if c6==0:
            croix6()
            c6=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==7 :
        if c7==0:
            croix7()
            c7=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==8 :
        if c8==0:
            croix8()
            c8=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==9 :
        if c9==0:
            croix9()
            c9=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
if b==2:
    if ja6==1:
        if c1==0:
            cercle1()
            c1=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==2 :
        if c2==0:
            cercle2()
            c2=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==3 :
        if c3==0:
            cercle3()
            c3=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja6==4:
        if c4==0:
            cercle4()
            c4=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==5:
        if c5==0:
            cercle5()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja6==6 :
        if c6==0:
            cercle6()
            c6=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==7:
        if c7==0:
            cercle7()
            c7=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==8:
        if c8==0:
            cercle8()
            c8=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja6==9 :
        if c9==0:
            cercle9()
            c9=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()

#Vérification
if b == 1:
    if c1==50 and c2==50 and c3==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c1==50 and c4==50 and c7==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c1==50 and c5==50 and c9==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c2==50 and c5==50 and c8==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c3==50 and c5==50 and c7==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c3==50 and c6==50 and c9==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c4==50 and c5==50 and c6==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c7==50 and c8==50 and c9==50:
        print (f"{n2} a gagné!")
        sys.exit()
if b == 2:
    if c1==100 and c2==100 and c3==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c1==100 and c4==100 and c7==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c1==100 and c5==100 and c9==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c2==100 and c5==100 and c8==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c3==100 and c5==100 and c7==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c3==100 and c6==100 and c9==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c4==100 and c5==100 and c6==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c7==100 and c8==100 and c9==100:
        print (f"{n2} a gagné!")
        sys.exit()


#7eme coup
ja7= int(input(f"{n1} entrez la case que vous voulez jouer: "))

if a==1:
    if ja7==1:
        if c1==0:
            croix1()
            c1=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja7==2:
        if c2==0:
            croix2()
            c2=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja7==3 :
        if c3==0:
            croix3()
            c3=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
    elif ja7==4:
        if c4==0:
            croix4()
            c4=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja7==5 :
        if c5==0:
            croix5()
            c5=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja7==6:
        if c6==0:
            croix6()
            c6=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja7==7 :
        if c7==0:
            croix7()
            c7=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    elif ja7==8 :
        if c8==0:
            croix8()
            c8=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja7==9 :
        if c9==0:
            croix9()
            c9=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
if a==2:
    if ja7==1:
        if c1==0:
            cercle1()
            c1=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja7==2 :
        if c2==0:
            cercle2()
            c2=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja7==3 :
        if c3==0:
            cercle3()
            c3=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()

    
    elif ja7==4:
        if c4==0:
            cercle4()
            c4=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja7==5:
        if c5==0:
            cercle5()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja7==6 :
        if c6==0:
            cercle6()
            c6=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja7==7:
        if c7==0:
            cercle7()
            c7=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja7==8:
        if c8==0:
            cercle8()
            c8=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja7==9 :
        if c9==0:
            cercle9()
            c9=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
#Verification

if a == 1:
    if c1==50 and c2==50 and c3==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==50 and c4==50 and c7==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==50 and c5==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c2==50 and c5==50 and c8==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==50 and c5==50 and c7==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==50 and c6==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c4==50 and c5==50 and c6==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c7==50 and c8==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
if a == 2:
    if c1==100 and c2==100 and c3==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==100 and c4==100 and c7==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==100 and c5==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c2==100 and c5==100 and c8==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==100 and c5==100 and c7==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==100 and c6==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c4==100 and c5==100 and c6==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c7==100 and c8==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()

#8eme coup
ja8= int(input(f"{n2} entrez la case que vous voulez jouer: "))

if b==1:
    if ja8==1:
        if c1==0:
            croix1()
            c1=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    
    elif ja8==2:
        if c2==0:
            croix2()
            c2=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
        
    elif ja8==3 :
        if c3==0:
            croix3()
            c3=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
    elif ja8==4:
        if c4==0:
            croix4()
            c4=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja2==5 :
        if c5==0:
            croix5()
            c5=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja8==6:
        if c6==0:
            croix6()
            c6=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja8==7 :
        if c7==0:
            croix7()
            c7=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja8==8 :
        if c8==0:
            croix8()
            c8=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja8==9 :
        if c9==0:
            croix9()
            c9=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
if b==2:
    if ja8==1:
        if c1==0:
            cercle1()
            c1=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja8==2 :
        if c2==0:
            cercle2()
            c2=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja8==3 :
        if c3==0:
            cercle3()
            c3=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()

    
    elif ja8==4:
        if c4==0:
            cercle4()
            c4=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja8==5:
        if c5==0:
            cercle5()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja8==6 :
        if c6==0:
            cercle6()
            c6=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja8==7:
        if c7==0:
            cercle7()
            c7=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    elif ja8==8:
        if c8==0:
            cercle8()
            c8=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja8==9 :
        if c9==0:
            cercle9()
            c9=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
#Verification
if b == 1:
    if c1==50 and c2==50 and c3==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c1==50 and c4==50 and c7==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c1==50 and c5==50 and c9==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c2==50 and c5==50 and c8==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c3==50 and c5==50 and c7==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c3==50 and c6==50 and c9==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c4==50 and c5==50 and c6==50:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c7==50 and c8==50 and c9==50:
        print (f"{n2} a gagné!")
        sys.exit()
if b == 2:
    if c1==100 and c2==100 and c3==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c1==100 and c4==100 and c7==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c1==100 and c5==100 and c9==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c2==100 and c5==100 and c8==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c3==100 and c5==100 and c7==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c3==100 and c6==100 and c9==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c4==100 and c5==100 and c6==100:
        print (f"{n2} a gagné!")
        sys.exit()
    elif c7==100 and c8==100 and c9==100:
        print (f"{n2} a gagné!")
        sys.exit()
#9eme coup
ja9= int(input(f"{n1} entrez la case que vous voulez jouer: "))


if a==1:
    if ja9==1:
        if c1==0:
            croix1()
            c1=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    
    elif ja9==2:
        if c2==0:
            croix2()
            c2=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
        
    elif ja9==3 :
        if c3==0:
            croix3()
            c3=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
   
    elif ja9==4:
        if c4==0:
            croix4()
            c4=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja9==5 :
        if c5==0:
            croix5()
            c5=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
            
    elif ja9==6:
        if c6==0:
            croix6()
            c6=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja9==7 :
        if c7==0:
            croix7()
            c7=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja9==8 :
        if c8==0:
            croix8()
            c8=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja9==9 :
        if c9==0:
            croix9()
            c9=50
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
if a==2:
    if ja9==1:
        if c1==0:
            cercle1()
            c1=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja9==2 :
        if c2==0:
            cercle2()
            c2=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    
    elif ja9==3 :
        if c3==0:
            cercle3()
            c3=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()

    
    elif ja9==4:
        if c4==0:
            cercle4()
            c4=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja9==5:
        if c5==0:
            cercle5()
            c5=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
        
    elif ja9==6 :
        if c6==0:
            cercle6()
            c6=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja9==7:
        if c7==0:
            cercle7()
            c7=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja9==8:
        if c8==0:
            cercle8()
            c8=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
    
    elif ja9==9 :
        if c9==0:
            cercle9()
            c9=100
        else:
            print("Casse déjà occupée, veulliez recommencer le jeux.")
            sys.exit()
#Verification du resultat
if a == 1:
    if c1==50 and c2==50 and c3==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==50 and c4==50 and c7==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==50 and c5==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c2==50 and c5==50 and c8==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==50 and c5==50 and c7==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==50 and c6==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c4==50 and c5==50 and c6==50:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c7==50 and c8==50 and c9==50:
        print (f"{n1} a gagné!")
        sys.exit()
if a == 2:
    if c1==100 and c2==100 and c3==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==100 and c4==100 and c7==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c1==100 and c5==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c2==100 and c5==100 and c8==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==100 and c5==100 and c7==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c3==100 and c6==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c4==100 and c5==100 and c6==100:
        print (f"{n1} a gagné!")
        sys.exit()
    elif c7==100 and c8==100 and c9==100:
        print (f"{n1} a gagné!")
        sys.exit()
    else:
        print(f"Dommage! Égalité, faites une autre partie {n1} et {n2}")


