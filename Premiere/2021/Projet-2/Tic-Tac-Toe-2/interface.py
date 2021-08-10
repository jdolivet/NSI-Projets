# Importations
import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk, Image
import pygame

# Variables  
clique = True
compteur = 0

# Création du menu et des fenêtres
fenetre = tk.Tk()
fenetre.title("TicTacToe")

canevas_fond_fond = tk.Canvas(fenetre, width = 600, height = 600, background = "grey")
canevas_fond_fond.pack(padx = 8, pady = 8, side = tk.LEFT)

canevas_fond = tk.Canvas(canevas_fond_fond, width = 600, height = 600, background = "white")
canevas_fond.pack(padx = 8, pady = 8, side = tk.LEFT)

canevas_menu = tk.Canvas(canevas_fond, width = 600, height = 600, background = "black")
canevas_menu.pack(padx = 12, pady = 12, side = tk.LEFT)

label_titre = tk.Label(canevas_menu, width = 20, text = "TIC TAC TOE", fg = "white", font = "Comic, 25", background = "black")
label_titre.place(x = 130, y = 20)

label_menu = tk.Label(canevas_menu, width = 20, text = "MENU", fg = "white", font = "Comic, 25", background = "black")
label_menu.place(x = 130, y = 100)

label_credits = tk.Label(canevas_menu, width = 40, text = "Réalisé par Baudoin, Luca, Bruno et Theo", fg = "white", font = "Comic, 10", background = "black")
label_credits.place(x = 275, y = 560)

# Musique du jeu
pygame.mixer.init()

def jouer_musique():
    """ Fonction 'jouer_musique()'.
    Cette function lance la musique au démmarage du jeu. """
    pygame.mixer.music.load("battle_pokemon.mp3")     
    pygame.mixer.music.play(loops = 10)       
    
def arreter_musique():
    """ Fonction 'arreter_musique()'.
    Cette function sert a arrêter la musique. """
    pygame.mixer.music.stop()
    
def jouer_musique_vainqueur():
    """ Fonction 'jouer_musique_vainqueur()'.
    Cette fonction lance une musique pour déclarer le vainqueur du match. """
    pygame.mixer.music.load("pokemon_captured.mp3")
    pygame.mixer.music.play(loops = 1)
    
    
def ouvrir_jeu_1():
    global nouvelle_fenetre
    nouvelle_fenetre = tk.Toplevel()
    nouvelle_fenetre.title('Jeu')
    nouvelle_fenetre.geometry("600x600")
    
    global btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9

# Dimensions des carrés
    btn_1 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_1))
    btn_2 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_2))
    btn_3 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_3))
    
    btn_4 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_4))
    btn_5 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_5))
    btn_6 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_6))
    
    btn_7 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_7))
    btn_8 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_8))
    btn_9 = tk.Button(nouvelle_fenetre, width = 12, height = 6, text = " ", font = "Comic, 20", borderwidth = 7, background = "SystemButtonFace", command = lambda: btn_clique(btn_9))
    
# Position des carrés
    btn_1.place(x = 0, y = 0)
    btn_2.place(x = 200, y = 0)
    btn_3.place(x = 400, y = 0)
    
    btn_4.place(x = 0, y = 200)
    btn_5.place(x = 200, y = 200)
    btn_6.place(x = 400, y = 200)
    
    btn_7.place(x = 0, y = 400)
    btn_8.place(x = 200, y = 400)
    btn_9.place(x = 400, y = 400)

# Boutons pour les OPTIONS du jeu
    options = Menu(nouvelle_fenetre)
    nouvelle_fenetre.config(menu = options)
 
    options_du_menu = Menu(options, tearoff = False)
    options.add_cascade(label = "Options", menu = options_du_menu)
    options_du_menu.add_command(label = "Rejouer", command = lambda:[arreter_musique(), fenetre.destroy()])
    options_du_menu.add_command(label = "Couper la musique", command = arreter_musique)
    options_du_menu.add_command(label = "Remettre la musique", command = jouer_musique)
    
        
def tout_annuler():
    """ Fonction 'tout_annuler()'.
    Cette fonction sert a annuler les carrés déjà selectionnés. """
    btn_1.config(state="disabled")
    btn_2.config(state="disabled")
    btn_3.config(state="disabled")
    btn_4.config(state="disabled")
    btn_5.config(state="disabled")
    btn_6.config(state="disabled")
    btn_7.config(state="disabled")
    btn_8.config(state="disabled")
    btn_9.config(state="disabled")

    
def flash(btn):
    """ Fonction 'flash(btn)'.
    Cette fonction change la couleur des carrés lors d'une victoire,
    colorant ceux ultilisés par le vainqueur.
    Les carrés apparaissent en rouge et en jaune. """
    nouvelle_fenetre.after(200, lambda: btn.config(background="red"))
    nouvelle_fenetre.after(400, lambda: btn.config(background="yellow"))
    nouvelle_fenetre.after(600, lambda: btn.config(background="red"))
    nouvelle_fenetre.after(800, lambda: btn.config(background="yellow"))
    nouvelle_fenetre.after(1000, lambda: btn.config(background="red"))
    
def flash_egalite(btn):
    """ Fonction 'flash_egalite(btn)'.
    Cette fonction change la couleur des carrés lors d'une égalité.
    Les carrés apparaissent en rouge et en jaune. """
    nouvelle_fenetre.after(200, lambda: btn.config(background="red"))
    nouvelle_fenetre.after(400, lambda: btn.config(background="yellow"))
    nouvelle_fenetre.after(600, lambda: btn.config(background="red"))

    
def verif_vainqueur():
    """ Fonction 'verif_vainqueur()'.
    Cette fonction verifie toutes les combinaisons possible pour désigner un
    vainqueur ('O' ou 'X') ou une égalité. """
    global vaincre
    vaincre = False
    
# Combinaisons de victoire du "X"   
    if btn_1["text"] == "X" and btn_2["text"] == "X" and btn_3["text"] == "X":
        btn_1.config(command = flash(btn_1))
        btn_2.config(command = flash(btn_2))
        btn_3.config(command = flash(btn_3))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! X a gagné!")
    
    elif btn_4["text"] == "X" and btn_5["text"] == "X" and btn_6["text"] == "X":
        btn_4.config(command = flash(btn_4))
        btn_5.config(command = flash(btn_5))
        btn_6.config(command = flash(btn_6))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! X a gagné!")

        
    elif btn_7["text"] == "X" and btn_8["text"] == "X" and btn_9["text"] == "X":
        btn_7.config(command = flash(btn_7))
        btn_8.config(command = flash(btn_8))
        btn_9.config(command = flash(btn_9))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! X a gagné!")

    
    elif btn_1["text"] == "X" and btn_4["text"] == "X" and btn_7["text"] == "X":
        btn_1.config(command = flash(btn_1))
        btn_4.config(command = flash(btn_4))
        btn_7.config(command = flash(btn_7))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! X a gagné!")
        
    elif btn_2["text"] == "X" and btn_5["text"] == "X" and btn_8["text"] == "X":
        btn_2.config(command = flash(btn_2))
        btn_5.config(command = flash(btn_5))
        btn_8.config(command = flash(btn_8))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! X a gagné!")
        
    elif btn_3["text"] == "X" and btn_6["text"] == "X" and btn_9["text"] == "X":
        btn_3.config(command = flash(btn_3))
        btn_6.config(command = flash(btn_6))
        btn_9.config(command = flash(btn_9))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! X a gagné!")
        
    elif btn_1["text"] == "X" and btn_5["text"] == "X" and btn_9["text"] == "X":
        btn_1.config(command = flash(btn_1))
        btn_5.config(command = flash(btn_5))
        btn_9.config(command = flash(btn_9))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! X a gagné!")

    elif btn_3["text"] == "X" and btn_5["text"] == "X" and btn_7["text"] == "X":
        btn_3.config(command = flash(btn_3))
        btn_5.config(command = flash(btn_5))
        btn_7.config(command = flash(btn_7))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! X a gagné!")

# Combinaisons de victoire du "O"
    elif btn_1["text"] == "O" and btn_2["text"] == "O" and btn_3["text"] == "O":
        btn_1.config(command = flash(btn_1))
        btn_2.config(command = flash(btn_2))
        btn_3.config(command = flash(btn_3))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! O a gagné!")
        
    elif btn_4["text"] == "O" and btn_5["text"] == "O" and btn_6["text"] == "O":
        btn_4.config(command = flash(btn_4))
        btn_5.config(command = flash(btn_5))
        btn_6.config(command = flash(btn_6))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! O a gagné!")
        
    elif btn_7["text"] == "O" and btn_8["text"] == "O" and btn_9["text"] == "O":
        btn_7.config(command = flash(btn_7))
        btn_8.config(command = flash(btn_8))
        btn_9.config(command = flash(btn_9))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! O a gagné!")
    
    elif btn_1["text"] == "O" and btn_4["text"] == "O" and btn_7["text"] == "O":
        btn_1.config(command = flash(btn_1))
        btn_4.config(command = flash(btn_4))
        btn_7.config(command = flash(btn_7))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! O a gagné!")
        
    elif btn_2["text"] == "O" and btn_5["text"] == "O" and btn_8["text"] == "O":
        btn_2.config(command = flash(btn_2))
        btn_5.config(command = flash(btn_5))
        btn_8.config(command = flash(btn_8))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! O a gagné!")
        
    elif btn_3["text"] == "O" and btn_6["text"] == "O" and btn_9["text"] == "O":
        btn_3.config(command = flash(btn_3))
        btn_6.config(command = flash(btn_6))
        btn_9.config(command = flash(btn_9))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! O a gagné!")
        
    elif btn_1["text"] == "O" and btn_5["text"] == "O" and btn_9["text"] == "O":
        btn_1.config(command = flash(btn_1))
        btn_5.config(command = flash(btn_5))
        btn_9.config(command = flash(btn_9))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! O a gagné!")
        
    elif btn_3["text"] == "O" and btn_5["text"] == "O" and btn_7["text"] == "O":
        btn_3.config(command = flash(btn_3))
        btn_5.config(command = flash(btn_5))
        btn_7.config(command = flash(btn_7))
        vaincre = True
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "Bravo! O a gagné!")
        
# Verifie si l'égalité existe
    # global compteur, vaincre, tout_annuler
    elif compteur == 9 and vaincre == False:
        btn_1.config(command = flash_egalite(btn_1))
        btn_2.config(command = flash_egalite(btn_2))
        btn_3.config(command = flash_egalite(btn_3))
        btn_4.config(command = flash_egalite(btn_4))
        btn_5.config(command = flash_egalite(btn_5))
        btn_6.config(command = flash_egalite(btn_6))
        btn_7.config(command = flash_egalite(btn_7))
        btn_8.config(command = flash_egalite(btn_8))
        btn_9.config(command = flash_egalite(btn_9))
        arreter_musique
        jouer_musique_vainqueur()
        tout_annuler()
        messagebox.showinfo("TicTacToe", "La partie a finie en égalité!")

# Fonction pour cliquer et mettre les X et O
def btn_clique(btn):
    """ Fonction 'btn_clique(btn)'.
    Cette fonction vérifie le clique et marque le carré séléctionner
    en vérifiant le vainqueur a chaque clique."""
    global clique, compteur
    
    if btn["text"] == " " and clique == True:
        btn["text"] = "X"
        clique = False
        compteur += 1
        verif_vainqueur()
    elif btn["text"] == " " and clique == False:
        btn["text"] = "O"
        clique = True
        compteur += 1
        verif_vainqueur()
    else:
        messagebox.showerror("TicTacToe", "Cet emplacement a déjà été séléctionné! Veillez choisir un autre vide...")


# Modes de jeu et leurs boutons sur le menu
btn_player_vs_ordi = tk.Button(canevas_menu, width = 40, text =  "Jouer player vs player", fg = "white", font = "Comic, 15", background = "black", command = lambda:[ouvrir_jeu_1(), jouer_musique()])
btn_player_vs_ordi.place(x = 100, y = 180)

btn_player_vs_player = tk.Button(canevas_menu, width = 40, text =  "Jouer player vs ordi (pas encore pret)", fg = "white", font = "Comic, 15", background = "black")
btn_player_vs_player.place(x = 100, y = 240)

btn_ordi_vs_ordi = tk.Button(canevas_menu, width = 40, text =  "Jouer ordi vs ordi (pas encore pret)", fg = "white", font = "Comic, 15", background = "black")
btn_ordi_vs_ordi.place(x = 100, y = 300)

btn_quit_game = tk.Button(fenetre, width = 20, text =  "Quit Game", fg = "white", font = "Comic, 10", background = "black", command = fenetre.destroy)
btn_quit_game.place(x = 100, y = 540)


def ouvrir_regles_et_commandes():
    """ Fonction 'ouvrir_regles_et_commandes()'.
    Cette fonction montre les règles et les commandes du 'Tic Tac Toe' au joueur(s).
    TRÈS IMPORTANT DE LES LIRES AVANT JOUER!!! """
    global img
    nouvelle_fenetre = tk.Toplevel()
    nouvelle_fenetre.title('Règles et commandes du jeu')
    img = ImageTk.PhotoImage(Image.open("regles.png"))
    label = tk.Label(nouvelle_fenetre, image = img).pack()
    btn_retour = tk.Button(nouvelle_fenetre, text = "Fermer les règles et commandes", command = nouvelle_fenetre.destroy).pack()

# Bouton pour les règles et commandes
btn_commandes_et_regles = tk.Button(canevas_menu, width = 40, text =  "Voir les règles et commandes (IMPORTANT!)", fg = "white",
font = "Comic, 15", background = "black", command = ouvrir_regles_et_commandes)
btn_commandes_et_regles.place(x = 100, y = 360)

fenetre.mainloop()