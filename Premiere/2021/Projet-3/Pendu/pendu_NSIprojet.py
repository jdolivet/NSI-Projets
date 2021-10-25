# Pendu - Projet NSI

from tkinter import *
from tkinter import messagebox
from liste_mots import prendre_mots

mot = prendre_mots() # word = get_words()
victoire = False # win
mauvaise_reponse = 0 # wrong_guesses
bonne_reponse = 0 # correct_guesses
lettres = ""
tentative = ""
liste_mots = list(mot)
bonne_lettre = [' '] * len(mot)

fenetre = Tk()
fenetre.title("Pendu")

fond = PhotoImage(file = "feuille_pendu.png")
menu = Label(fenetre, image=fond).pack()
img_regles = PhotoImage(file = "feuille_pendu_regles.png")
# img_jeu = PhotoImage(file = "feuille_pendu.png")


def ouvrir_nouveau_jeu():
    """La fonction 'ouvrir_nouveau_jeu()', démare un nouveau jeu quand le joueur
    clique sur le bouton 'Nouveau Jeu' sur le menu du jeu. Il met en place une nouvelle fenêtre
    où les éléments du jeu seront projeté."""
    fenetre_jeu = Toplevel()
    fenetre_jeu.title("Jeu en cours")
    fenetre_jeu.geometry("900x600")
    bord_jeu = Canvas(fenetre_jeu, width = 900, height = 700, bg = "#4169E1")
    bord_jeu.pack(padx = 1, pady = 1)
    ecran_jeu = Canvas(bord_jeu, width = 900, height = 600, bg = "white")
    ecran_jeu.pack(padx = 5, pady = 5)
    
    # StringVar nous permet de créer une chaîne de caractère dynamique. On les atributs au Label.
    chaine_a = StringVar(ecran_jeu)
    chaine_b = StringVar(ecran_jeu)
    chaine_c = StringVar(ecran_jeu)
    
    # Label qui montre les lettres déjà essayer du côté supérieure droit
    label_txt1 = Label(ecran_jeu, height = 2, bg = "yellow", text = "Lettres utilisés:", font = 200)
    label_txt1.place(x = 340, y = 40)
    label_mots_utiliser = Label(ecran_jeu, width = 55, height = 2, bg = "light grey", textvariable = chaine_a, font = 200)
    label_mots_utiliser.place(x = 450, y = 40)
    # label qui montre 
    label_txt = Label(ecran_jeu, width = 15, height = 2, text = "Lettre ou Mot: ", font = "Arial, 15", bg = "light grey")
    label_txt.place(x = 2, y = 500)
    # Label qui montre les lettres correctes qui sont dans le mot
    label_bonne_lettre = Label(ecran_jeu, width = int(4 * (len(mot)+5)), height = 2, bg = "white", textvariable = chaine_b)
    label_bonne_lettre.place(x = 385, y = 400)
    # Label qui montre le message final en cas de VICTOIRE ou DEFAITE
    label_message_final = Label(ecran_jeu, width = 50, height = 2, bg = "white", textvariable = chaine_c, font = 300)
    label_message_final.place(x = 425, y = 200)
    # Boîte qui sert à mettre la lettre pour la tentative
    entrer_tentative = Entry(ecran_jeu, bg = "orange", font = 40)
    entrer_tentative.place(x = 170, y = 500, width = 100, height = 53)
    
    def dessiner_traits():
        """La fonction 'dessiner_traits()', déssine la guillotine et sa base.
        De plus, elle déssine les traits correspondant à la quantité de lettre dans le mot choisi."""
        ecran_jeu.create_line(0, 500, 150, 500, width = 10)
        ecran_jeu.create_line(40, 500, 40, 110, 180, 110, 180, 150, width = 10)
        for i in range(0, len(mot)):
            ecran_jeu.create_line(450 + i * 45, 450, 420 + i * 45, 450)
    
    def verifie_tentative():
        """La fonction 'verifie_tentative()', identifie les cas où la tentative de l'utilisateur
        correspond à un MOT ou à une LETTRE."""
        global mauvaise_reponse, lettres, bonne_reponse, bonne_lettre, victoire 
        # Si la TENTATIVE correspond à un MOT
        if len(tentative) > 1:
            if tentative == mot:
                victoire = True
            elif tentative != mot:
                mauvaise_reponse += 1
        # Si la TENTATIVE correspond à une LETTRE
        if len(tentative) == 1:
            if tentative not in lettres:
                lettres += tentative
                if tentative in mot:
                    compteur = liste_mots.count(tentative)
                    for i in range(compteur):
                        bonne_lettre[liste_mots.index(tentative)] = tentative
                        liste_mots[liste_mots.index(tentative)] = ''
                    bonne_reponse += compteur
                    if bonne_reponse == len(mot):
                        victoire = True
                elif tentative not in mot:
                    mauvaise_reponse += 1
                    
    def partie_corps():
        # Renvoie la tête
        if mauvaise_reponse == 1:
            ecran_jeu.create_oval(138, 150, 228, 230, width = 2)
        # corpo
        elif mauvaise_reponse == 2:
            ecran_jeu.create_line(183, 230, 183, 380, width = 2)
        # Renvoie le bras gauche
        elif mauvaise_reponse == 3:
            ecran_jeu.create_line(183, 270, 130, 260, width = 2)
        # Renvoie le bras droit
        elif mauvaise_reponse == 4:
            ecran_jeu.create_line(183, 270, 236, 260)
        # Renvoie la jambe gauche
        elif mauvaise_reponse == 5:
            ecran_jeu.create_line(183, 380, 130, 410, width = 2)
        # Renvoie la jambe droite
        elif mauvaise_reponse == 6:
            ecran_jeu.create_line(183, 380, 236, 410, width = 2)
            chaine_c.set(f'Vous avez perdu! La bonne réponse était "{mot}".')
            messagebox.showwarning("Pendu", "Game Over")
            fenetre_jeu.destroy()
            fenetre.destroy()
            
            
    def registrer_tentative(event):
        global tentative
        tentative = entrer_tentative.get()
        verifie_tentative()
        chaine_a.set(' '.join(lettres))
        chaine_b.set('           '.join(bonne_lettre))
        entrer_tentative.delete(0, END)
        partie_corps()
    
        if victoire:
            chaine_c.set("Bravo! Vous avez trouver la bonne réponse.")
            messagebox.showinfo("Pendu", "Bravo!")
            fenetre_jeu.destroy()
            fenetre.destroy()
            
            
    fenetre_jeu.bind("<Return>", registrer_tentative)
    dessiner_traits()
    
# def ouvrir_langue():
#     fenetre_langue = Toplevel()
#     fenetre_langue.title("Changer la langue")
#     fenetre_langue.geometry("400x400")
#     btn_english = Button(fenetre_langue, width = 10, height = 1, text = "English", font = "Arial, 20", borderwidth = 4, bg = "#4169E1", fg = "white", command = change_us)
#     btn_english.place(x = 120, y = 70)
#     btn_francais = Button(fenetre_langue, width = 10, height = 1, text = "Français", font = "Arial, 20", borderwidth = 4, bg = "#4169E1", fg = "white", command = change_fr)
#     btn_francais.place(x = 120, y = 140)
#     btn_portugues = Button(fenetre_langue, width = 10, height = 1, text = "Português", font = "Arial, 20", borderwidth = 4, bg = "#4169E1", fg = "white", command = change_br)
#     btn_portugues.place(x = 120, y = 210)
#     btn_fermer_langue = Button(fenetre_langue,  width = 5, height = 1, text = "OK", font = "Arial, 10", borderwidth = 4, bg = "white", fg = "black", command = fenetre_langue.destroy)
#     btn_fermer_langue.place(x = 120, y = 280)
    
def ouvrir_regles():
    fenetre_regles = Toplevel()
    fenetre_regles.title("Règles et commandes du jeu")
    regles = Label(fenetre_regles, image = img_regles).pack()

 # Les textes et boutons du menu
# Nom du jeu
txt_pendu = Label(menu, text = "PENDU", fg = "black", bg = "white", font = "Arial, 40")
txt_pendu.place(x = 225, y = 100)

liste_menu = ["Nouveau Jeu", "Langue", "Règles", "Projet réalisé par Theo et Gabriel"]
# Bouton 'Nouveau Jeu'
btn_nouveau_jeu = Button(menu, width = 18, height = 1, text = liste_menu[0], font = "Arial, 20", borderwidth = 4, bg = "#4169E1", fg = "white", command = ouvrir_nouveau_jeu)
btn_nouveau_jeu.place(x = 160, y = 250)
 # Bouton 'Langue'
# btn_langue = Button(menu, width = 18, height = 1, text = liste_menu[1], font = "Arial, 20", borderwidth = 4, bg = "#4169E1", fg = "white", command = ouvrir_langue)
# btn_langue.place(x = 160, y = 365)
# Bouton 'Langue'
btn_regles = Button(menu, width = 18, height = 1, text = liste_menu[2], font = "Arial, 20", borderwidth = 4, bg = "#4169E1", fg = "white", command = ouvrir_regles)
btn_regles.place(x = 160, y = 480)
# Auteurs du projet
txt_groupe = Label(menu, text = liste_menu[3], fg = "black", bg = "yellow", font = "Comic, 12")
txt_groupe.place(x = 350, y = 700)


fenetre.mainloop()


