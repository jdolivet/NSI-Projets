from tkinter import *
from math import *


"""Calculatrice simple avec interface graphique avec le module Tkinter"""

fenetre = Tk()
fenetre.title("Calculatrice")
fenetre.geometry("323x300")                             #creation et définition de l'interface graphique 
operation_ecrite = ""
premier_numero = ""
deuxieme_numero = ""                                 #définition des variables principales utilisées pour faire les opérations
position_signe = 0

def ecriture(nb):
    global operation_ecrite
    operation_ecrite += nb                      #fonction ecriture est lancee chaque foix qu'un nouveau caractère est ajouté pour l'afficher sur l'écran 
    ecran["text"] = operation_ecrite
    
def testage():
    global operation_ecrite
    global premier_numero
    global deuxieme_numero
    position_signe = 0                                                             #fonction testage, parcoure la chaine de caractères saisie par l'utilisateur quand la touche "=" est saisie 
    k = 0                                                                          #prend ainsi d'une chaine de caracteres deux valeurs et les transforment en un flottant et non pas un entier, nous permettant de faire des calculs avec des chifres décimaux.
    while operation_ecrite[k] != "+" and operation_ecrite[k] != "*" and operation_ecrite[k] != "/" and operation_ecrite[k] != "-":                       
        premier_numero += operation_ecrite[k]
        k += 1
    premier_numero = float(premier_numero)
    position_signe = k+1
    for j in range(position_signe, len(operation_ecrite)):
        deuxieme_numero += operation_ecrite[j]
    deuxieme_numero = float(deuxieme_numero)

def numero1():
    ecriture("1")

def numero2():
    ecriture("2")

def numero3():
    ecriture('3')

def numero4():
    ecriture("4")

def numero5():
    ecriture("5")

def numero6():
    ecriture("6")                               #fonctions numériques qui affichent le chiffre du bouton préssionné dans l'écran de la calculatrice

def numero7():
    ecriture("7")

def numero8():
    ecriture("8")

def numero9():
    ecriture("9")

def zero():
    ecriture("0")

def virgule():
    ecriture(".")

def numpi():
    ecriture(str(pi))      #utilisation du module math pour afficher la valeur de pi sur l'ecran quand la touche est saisie

def clear():
    global operation_ecrite
    operation_ecrite = ""                       #supprime tous les caracteres saisis
    ecran["text"] = ""
    
def delete():
    global operation_ecrite
    operation_ecrite = operation_ecrite[0:(len(operation_ecrite)-1)]  #supprime le dernier caractere saisi par l'utilisateur
    ecran["text"] = operation_ecrite

def addition():
    global op
    ecriture("+")      #ajoute le caractere + a l'écran et selectione le mode operation 1 (addition)
    op = 1

def soustraction():
    global op
    ecriture("-")      #ajoute le caractere - a l'écran et selectione le mode operation 2 (soustraction)
    op = 2

def multiplier():
    global op
    ecriture("*")   #ajoute le caractere * a l'écran et selectione le mode operation 3 (multiplication)
    op = 3

def diviser():
    global op
    ecriture("/")   #ajoute le caractere / a l'écran et selectione le mode operation 4 (division)
    op = 4

def execute():
    testage()
    global premier_numero
    global deuxieme_numero
    if op == 1:
        result = premier_numero + deuxieme_numero
    if op == 2:
        result = round(premier_numero - deuxieme_numero,10)         #fonction lancée quand la touche = est saisie, lance la fonction testage() pour
    if op == 3:                                                     #récuperer les valeurs et fait l'opération selon le mode d'opération choisi      
        result = round(premier_numero * deuxieme_numero ,10)
    if op == 4:
        result = round(premier_numero / deuxieme_numero,10)
    ecran["text"] = result
    operation_ecrite = ""
    premier_numero = ""
    deuxieme_numero = ""
    result = 0

def off():
    fenetre.destroy()            #fonction qui ferme la fenetre

    
ecran = Label(text="0")
ecran.place(x=10,y=10)
b0 = Button(fenetre, text = "0",width = 5,command=zero,background='#A9A9A9',borderwidth=1).place(x=10,y=230)
bvirgule = Button(fenetre, text = ".",width = 5,background='#A9A9A9', borderwidth=1,command=virgule).place(x=59,y= 230)
bpi = Button(fenetre, text= "π",width = 5,command=numpi,background = '#A9A9A9',borderwidth=1).place(x=108, y=230)
b1 = Button(fenetre, text = "1",width = 5,command=numero1,background='#A9A9A9', borderwidth=1).place(x=10,y=190)
b2 = Button(fenetre, text = "2",width = 5,command=numero2,background='#A9A9A9', borderwidth=1).place(x=59,y=190)
b3 = Button(fenetre, text = "3",width = 5,command=numero3,background='#A9A9A9', borderwidth=1).place(x=108,y=190)
b4 = Button(fenetre, text = "4",width = 5,command=numero4,background='#A9A9A9', borderwidth=1).place(x=10,y=150)       #Création de tous les boutons numériques (positionement, tailles, couleurs) avec leurs fonctions respectives
b5 = Button(fenetre, text = "5",width = 5,command=numero5,background='#A9A9A9', borderwidth=1).place(x=59,y=150)
b6 = Button(fenetre, text = "6",width = 5,command=numero6,background='#A9A9A9', borderwidth=1).place(x=108,y=150)
b7 = Button(fenetre, text = "7",width = 5,command=numero7,background='#A9A9A9', borderwidth=1).place(x=10,y=110)
b8 = Button(fenetre, text = "8",width = 5,command=numero8,background='#A9A9A9', borderwidth=1).place(x=59,y=110)                                                     
b9 = Button(fenetre, text = "9",width = 5,command=numero9,background='#A9A9A9', borderwidth=1).place(x=108,y=110) 

bclear = Button(fenetre, text = 'AC',width = 6,background = '#708090',borderwidth=1,command = clear).place(x=171, y=110)
bdelete = Button(fenetre, text = 'DEL',width = 6,background = '#708090',borderwidth=1,command = delete).place(x=225, y= 110)
baddition = Button(fenetre, text = "+",width = 6,background = '#696969',borderwidth=1,command=addition).place(x=171, y=190)
bsoustraction = Button(fenetre, text= "-",width = 6,background = '#696969',borderwidth=1,command=soustraction).place(x=225, y=190)    #Création des boutons non-numériques, opérations mathématiques, supprimer et touche étteinte de a calculatrice. (chaque bouton avec sa fonctions respective)
bmultiplication =Button(fenetre, text= "*",width = 6,background = '#696969',borderwidth=1,command=multiplier).place(x=171, y=150)
bdivision = Button(fenetre, text= "/",width = 6,background = '#696969',borderwidth=1,command=diviser).place(x=225, y=150)
bexecute = Button(fenetre, text = "=",width = 6,background = '#d9463d',borderwidth=1,command=execute).place(x=171, y=230)
boff = Button(fenetre, text= "OFF",width = 6,background = '#d9463d',borderwidth=1,command=off).place(x=225, y= 230)


fenetre.mainloop() #fin du cycle