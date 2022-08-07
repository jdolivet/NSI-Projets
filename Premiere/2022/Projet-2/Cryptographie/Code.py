import tkinter as tk  #on importe la bibliothèque Tkinter sous le nom de tk
from tkinter import filedialog #module Tkinter pour ouvrir et sauver des fichiers

fenetre = tk.Tk() #crée une fenêtre principale
fenetre.title("Chiffrer et déchiffrer un fichier") #titre de la fenêtre

base_bouton_fichier = tk.Canvas(fenetre, width=400, height=2, background="grey") #définition des dimensions de la base du bouton du fichier
base_bouton_fichier.pack(padx=8, pady=8, side=tk.LEFT)
base_boutons = tk.Canvas(fenetre, width= 400, height= 20, background="grey") #définition des dimensions de la base des boutons 
base_boutons.pack(padx=8, pady=8, side=tk.LEFT)

btn_fichier = tk.Button(base_bouton_fichier, text="Sélectionner fichier") #bouton pour que l'utilisateur sélectionne un fichier
btn_fichier.pack(fill=tk.X) #dispose le bouton dans la base_bouton_fichier automatiquement

btn_code_cesar = tk.Button(base_boutons, text="Code César") #bouton pour le code César
btn_code_cesar.pack(fill=tk.X) #dispose le bouton dans la base_boutons automatiquement
l_code_cesar = tk.Label(base_boutons, text=" ↓ Entrer votre clé (un nombre de 1 à 25) ↓ ") #étiquette qui signale où rentrer la clé
l_code_cesar.pack(fill=tk.X) #dispose l'étiquette dans la base_boutons automatiquement
ent_cesar = tk.Entry(base_boutons) #champ de saisie de texte pour rentrer la clé
ent_cesar.pack(fill=tk.X) #dispose le champ de saisie de texte dans la base_boutons automatiquement

btn_dechif_cesar = tk.Button(base_boutons, text="Déchiffrement du Code César") #bouton pour le déchiffrement du code César
btn_dechif_cesar.pack(fill=tk.X) #dispose le bouton dans la base_boutons automatiquement
l_dechif_cesar = tk.Label(base_boutons, text=" ↓ Entrer votre clé (un nombre de 1 à 25) ↓ ") #étiquette qui signale où rentrer la clé
l_dechif_cesar.pack(fill=tk.X) #dispose l'étiquette dans la base_boutons automatiquement
ent_dechif_cesar = tk.Entry(base_boutons) #champ de saisie de texte pour rentrer la clé
ent_dechif_cesar.pack(fill=tk.X) #dispose le champ de saisie de texte dans la base_boutons automatiquement

btn_casser_cesar = tk.Button(base_boutons, text="Casser le Code César") #bouton pour casser le code César
btn_casser_cesar.pack(fill=tk.X) #dispose le bouton dans la base_boutons automatiquement
l_casse_cesar = tk.Label(base_boutons, text='') #étiquette sans texte qui sera remplie après
l_casse_cesar.pack(fill=tk.X) #dispose l'étiquette dans la base_boutons automatiquement

btn_chif_vigenere = tk.Button(base_boutons, text="Chiffrement de Vigenère") #bouton pour le chiffrement de Vigenère
btn_chif_vigenere.pack(fill=tk.X) #dispose le bouton dans la base_boutons automatiquement
l_chif_vigenere = tk.Label(base_boutons, text=" ↓ Entrer votre clé (un ou plusieurs mots) ↓ ") #étiquette qui signale où rentrer la clé
l_chif_vigenere.pack(fill=tk.X) #dispose l'étiquette dans la base_boutons automatiquement
ent_chif_vigenere = tk.Entry(base_boutons) #champ de saisie de texte pour rentrer la clé
ent_chif_vigenere.pack(fill=tk.X) #dispose le champ de saisie de texte dans la base_boutons automatiquement

btn_dechif_vigenere = tk.Button(base_boutons, text="Déchiffrement du chiffrement de Vigenère") #bouton pour le déchiffrement du chiffrement de Vigenère
btn_dechif_vigenere.pack(fill=tk.X) #dispose le bouton dans la base_boutons automatiquement
l_dechif_vigenere = tk.Label(base_boutons, text=" ↓ Entrer votre clé (un ou plusieurs mots) ↓ ") #étiquette qui signale où rentrer la clé
l_dechif_vigenere.pack(fill=tk.X) #dispose l'étiquette dans la base_boutons automatiquement
ent_dechif_vigenere = tk.Entry(base_boutons) #champ de saisie de texte pour rentrer la clé
ent_dechif_vigenere.pack(fill=tk.X) #dispose le champ de saisie de texte dans la base_boutons automatiquement

def ouvrir_fichier(event):
    """Gestionnaire d'évènement qui permet d'ouvrir un fichier"""
    global fichier_texte
    filename = filedialog.askopenfilename()
    fichier_texte = filename

def chiffrer_lettre_fct(lettre: str, clef: int):
    """ Fonction qui effectue le chiffrement de César sur une lettre supposée non accentuée.
    Prend pour paramètres la lettre à chiffrer et une clef entre 1 et 25 """
    if lettre.isupper() == True:
        return chr(ord('A') + (ord(lettre) - ord('A') + clef) % 26)
    else:
        return chr(ord('a') + (ord(lettre) - ord('a') + clef) % 26)
    
def code_cesar(event):
    """ Gestionnaire d'évènement qui effectue le chiffrement de cesar sur un message dépourvu
    de lettres accentuées et supposé non ponctué. 
    Prend pour paramètres un message de type str et une clef entre 1 et 25 """
    global fichier_texte
    clef = int(ent_cesar.get()) #recupère la clé rentrée par l'utilisateur 
    with open(fichier_texte, 'r') as f: #ouvre le fichier sélectionner par l'utilisateur et le lis
        message = f.read() #stocke le texte dans la variable message
    res = ""
    for i in message:
        if i == " ":
            res += " "
        else:
            i = chiffrer_lettre_fct(i, clef)
            res += i
    with open("Code_Cesar.txt", 'w+') as f2: #crée un fichier en mode écriture + lecture
        f2.write(res) #écrit le résultat dans le fichier
    l_code_cesar.config(text="Le résultat est disponible dans le fichier texte nommé Code_Cesar.txt") #change le texte de l'étiquette pour signaler l'utilisateur
        
def dechiffrer_lettre_fct(lettre: str, clef: int):
    """ Fonction qui effectue le chiffrement de César sur une lettre supposée non accentuée.
    Prend pour paramètres la lettre à déchiffrer et une clef entre 1 et 25 """
    if lettre.isupper() == True:
        return chr(ord('A') + (ord(lettre) - ord('A') + clef) % 26)
    else:
        return chr(ord('a') + (ord(lettre) - ord('a') + clef) % 26)
    
def dechif_cesar(event):
    """ Gestionnaire d'évènement qui déchiffre un message supposé chiffré grâce au chiffrement de césar
    Suppose que l'on connaît la clef avec laquelle il fut chiffré """
    global fichier_texte
    clef = int(ent_dechif_cesar.get()) #recupère la clé rentrée par l'utilisateur
    with open(fichier_texte, 'r') as f: #ouvre le fichier sélectionner par l'utilisateur et le lis
        message = f.read() #stocke le texte dans la variable message
    res = ""
    for i in message:
        if i == " ":
            res += " "
        else:
            i = dechiffrer_lettre_fct(i, -(clef))
            res += i
    with open("Déchiffrement_Code_Cesar.txt", 'w+') as f2: #crée un fichier en mode écriture + lecture
         f2.write(res) #écrit le résultat dans le fichier
    l_dechif_cesar.config(text="Le résultat est disponible dans le fichier texte nommé Déchiffrement_Code_Cesar.txt") #change le texte de l'étiquette pour signaler l'utilisateur
    
def chiffrer_lettre(lettre: str, clef: int):
    """ Fonction qui effectue le chiffrement de César sur une lettre supposée non accentuée.
    Prend pour paramètres la lettre à chiffrer et une clef entre 1 et 25
    Servira pour le gestionnaire d'évènement qui casse le code César"""
    if lettre.isupper() == True:
        return chr(ord('A') + (ord(lettre) - ord('A') + clef) % 26)
    else:
        return chr(ord('a') + (ord(lettre) - ord('a') + clef) % 26)
             
def dechiffrer_cesar(message: str, clef: int) -> str :
    """ Fonction qui déchiffre un message supposé chiffré grâce au chiffrement de César
    suppose que l'on connaît la clef avec laquelle il fut chiffré
    Servira pour le gestionnaire d'évènement qui casse le code César"""
    res = ""
    for i in message:
        if i == " ":
            res += " "
        else:
            i = chiffrer_lettre(i, -(clef))
            res += i
    return res
        
def casser_cesar(event):
    """ Gestionnaire d'évènement qui casse un message codé grâce au chiffrement de César
    en montrant les 25 message possibles """
    global fichier_texte
    with open(fichier_texte, 'r') as f: #ouvre le fichier sélectionner par l'utilisateur et le lis
        message = f.read() #stocke le texte dans la variable message
    solution = ['']*25 #crée un tableau 
    for i in range(0, 25):
        solution[i] = dechiffrer_cesar(message, i+1) #remplie le tableau avec les 25 possibilités
    with open("Possibilites_Code_Cesar.txt", 'w+') as f2: #crée un fichier en mode écriture + lecture
        f2.write("Les messages possibles sont: \n") 
        for i in range(len(solution)): 
            f2.write(solution[i]) #écrit chaque possibilité dans une ligne
            f2.write('\n')
    l_casse_cesar.config(text="Le résultat est disponible dans le fichier texte nommé Possibilites_Code_Cesar.txt") #change le texte de l'étiquette pour signaler l'utilisateur
    
def lettre_vigenere(i):
    """ Fonction qui vérifie si la lettre i est non accentuée
    (retourne True si la lettre est non accentuée)"""
    let = ord(i.upper()) #met la lettre en majuscule
    if let > 64 and let < 91:
        return True
    else:
        return False

def decalage_vigenere(i, idx):
    """ Fonction qui décale la lettre selon la lettre de la clé """
    let = ord(i.upper()) #met la lettre en majuscule
    let += idx
    while let > 90:
        let -= 26
    while let < 65:
        let += 26
    return chr(let)

def vigenere(event):
    """ Gestionnaire d'évènement qui effectue le chiffrement de Vigenère """
    global fichier_texte
    with open(fichier_texte, 'r') as f:  #ouvre le fichier sélectionner par l'utilisateur et le lis
        message = f.read() #stocke le texte dans la variable message
    clef = ent_chif_vigenere.get() #recupère la clé rentrée par l'utilisateur
    a = 0
    res = " "
    for i in message:
        if lettre_vigenere(i):
            idx = ord(clef[a % len(clef)])- 65
            res += decalage_vigenere(i, idx)
            a += 1
        else :
            res += i
    with open("Chiffrement_Vigenere.txt", 'w+') as f2:  #crée un fichier en mode écriture + lecture
         f2.write(res) #écrit le résultat dans le fichier
    l_chif_vigenere.config(text="Le résultat est disponible dans le fichier texte nommé Chiffrement_Vigenere.txt") #change le texte de l'étiquette pour signaler l'utilisateur
    
def dechif_vigenere(event):
    global fichier_texte
    with open(fichier_texte, 'r') as f: #ouvre le fichier sélectionner par l'utilisateur et le lis
        message = f.read()  #stocke le texte dans la variable message
    clef = ent_dechif_vigenere.get() #recupère la clé rentrée par l'utilisateur
    a = 0
    res = " "
    for i in message:
        if lettre_vigenere(i):
            idx = ord(clef[a % len(clef)]) - 65
            res += decalage_vigenere(i, -idx)
            a += 1
        else:
            res += i
    with open("Dechiffrement_Vigenere.txt", 'w+') as f2: #crée un fichier en mode écriture + lecture
         f2.write(res) #écrit le résultat dans le fichier
    l_dechif_vigenere.config(text="Le résultat est disponible dans le fichier texte nommé Dechiffrement_Vigenere.txt") #change le texte de l'étiquette pour signaler l'utilisateur
      
     
btn_fichier.bind("<Button-1>", ouvrir_fichier) #associe la fonction à un évènement déclenché pour le bouton
btn_code_cesar.bind("<Button-1>", code_cesar) #associe la fonction à un évènement déclenché pour le bouton
btn_dechif_cesar.bind("<Button-1>", dechif_cesar) #associe la fonction à un évènement déclenché pour le bouton
btn_casser_cesar.bind("<Button-1>", casser_cesar) #associe la fonction à un évènement déclenché pour le bouton
btn_chif_vigenere.bind("<Button-1>", vigenere) #associe la fonction à un évènement déclenché pour le bouton
btn_dechif_vigenere.bind("<Button-1>", dechif_vigenere) #associe la fonction à un évènement déclenché pour le bouton

fenetre.mainloop() #fonction qui crée la fenêtre jusqu'à ce que l'utilisateur ferme la fenêtre