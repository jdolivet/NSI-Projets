import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import filtres


# 1. Variables du programme

image_originale = None
image_transforme = None
image_originale_affichage = None
image_transforme_affichage = None
photomaton_actif = False
inverse_video_actif = False
historique = []
position_historique = -1


# 2. Ouvrir et afficher une image

def ouvrir_fichier(evenement=None):
    """Ouvre une image choisie par l'utilisateur."""
    global image_originale, image_transforme
    global historique, position_historique

    nom_fichier = filedialog.askopenfilename(filetypes=[("Fichiers image", "*.png *.jpg *.jpeg *.bmp *.gif")])

    if nom_fichier != "":
        with Image.open(nom_fichier) as img:
            image_originale = img.convert("RGB")

        image_transforme = image_originale.copy()
        historique = []
        position_historique = -1
        restaurer_reglages_defaut()
        afficher_image_originale()
        mise_a_jour_images()
        ajouter_historique()


def afficher_image_originale():
    """Affiche l'image originale à gauche."""
    global image_originale_affichage

    apercu = image_originale.copy()
    apercu.thumbnail((360, 500))
    image_originale_affichage = ImageTk.PhotoImage(apercu)
    canevas_gauche.delete("all")
    canevas_gauche.create_image(180, 250, image=image_originale_affichage)


def afficher_image_modifiee():
    """Affiche l'image modifiée à droite."""
    global image_transforme_affichage

    apercu = image_transforme.copy()
    apercu.thumbnail((360, 500))
    image_transforme_affichage = ImageTk.PhotoImage(apercu)
    canevas_droite.delete("all")
    canevas_droite.create_image(180, 250, image=image_transforme_affichage)


# 3. Lire les curseurs et modifier l'image

def obtenir_reglages():
    """Récupère les valeurs des onze curseurs."""
    reglages = {}
    reglages["luminosite"] = curseur_luminosite.get()
    reglages["contraste"] = curseur_contraste.get()
    reglages["saturation"] = curseur_saturation.get()
    reglages["nettete"] = curseur_nettete.get()
    reglages["gamma"] = curseur_gamma.get()
    reglages["exposition"] = curseur_exposition.get()
    reglages["temperature"] = curseur_temperature.get()
    reglages["teinte"] = curseur_teinte.get()
    reglages["vibrance"] = curseur_vibrance.get()
    reglages["noir_blanc"] = curseur_noir_blanc.get()
    reglages["flou"] = curseur_flou.get()
    return reglages


def mise_a_jour_images(valeur=None):
    """Applique les réglages et affiche l'image modifiée."""
    global image_transforme

    if image_originale == None:
        return

    reglages = obtenir_reglages()
    image_transforme = filtres.appliquer_tous_les_reglages(image_originale, reglages)

    if photomaton_actif:
        nombre_copies = int(entree_photomaton.get())
        image_transforme = filtres.filtre_photomaton(image_transforme, nombre_copies)

    if inverse_video_actif:
        image_transforme = filtres.filtre_inverse_video(image_transforme)

    afficher_image_modifiee()


def memoriser_modification(evenement=None):
    """Met à jour l'image et garde les réglages."""
    if image_originale != None:
        mise_a_jour_images()
        ajouter_historique()


def restaurer_reglages_defaut():
    """Replace les curseurs sur leurs valeurs de départ."""
    global photomaton_actif, inverse_video_actif

    curseur_luminosite.set(0)
    curseur_contraste.set(0)
    curseur_saturation.set(0)
    curseur_nettete.set(100)
    curseur_gamma.set(1)
    curseur_exposition.set(0)
    curseur_temperature.set(0)
    curseur_teinte.set(0)
    curseur_vibrance.set(0)
    curseur_noir_blanc.set(0)
    curseur_flou.set(0)
    entree_photomaton.delete(0, tk.END)
    entree_photomaton.insert(0, "4")
    photomaton_actif = False
    inverse_video_actif = False
    bouton_photomaton.configure(text="Photomaton : non")
    bouton_inverse_video.configure(text="Inverse vidéo : non")


def restaurer_image(evenement=None):
    """Restaure l'image sans modification."""
    if image_originale != None:
        restaurer_reglages_defaut()
        mise_a_jour_images()
        ajouter_historique()


# 4. Les filtres spéciaux

def appliquer_photomaton(evenement=None):
    """Active ou désactive le filtre Photomaton."""
    global photomaton_actif

    if image_originale != None:
        photomaton_actif = not photomaton_actif

        if photomaton_actif:
            bouton_photomaton.configure(text="Photomaton : oui")
        else:
            bouton_photomaton.configure(text="Photomaton : non")

        mise_a_jour_images()
        ajouter_historique()


def appliquer_inverse_video(evenement=None):
    """Active ou désactive le filtre Inverse vidéo."""
    global inverse_video_actif

    if image_originale != None:
        inverse_video_actif = not inverse_video_actif

        if inverse_video_actif:
            bouton_inverse_video.configure(text="Inverse vidéo : oui")
        else:
            bouton_inverse_video.configure(text="Inverse vidéo : non")

        mise_a_jour_images()
        ajouter_historique()


def changer_nombre_photomaton(evenement=None):
    """Met à jour le filtre Photomaton."""
    if photomaton_actif:
        mise_a_jour_images()


# 5. Annuler et rétablir

def creer_etat():
    """Crée un état pour Annuler et Rétablir."""
    etat = obtenir_reglages()
    etat["photomaton"] = photomaton_actif
    etat["inverse_video"] = inverse_video_actif
    etat["nombre_photomaton"] = entree_photomaton.get()
    return etat


def ajouter_historique():
    """Ajoute les réglages actuels dans l'historique."""
    global historique, position_historique

    etat = creer_etat()

    if position_historique == -1:
        historique.append(etat)
        position_historique = 0

    elif historique[position_historique] != etat:
        historique = historique[:position_historique + 1]
        historique.append(etat)
        position_historique += 1


def annuler_modification(evenement=None):
    """Revient à l'état précédent."""
    global position_historique

    if position_historique > 0:
        position_historique -= 1
        charger_historique()


def retablir_modification(evenement=None):
    """Revient à l'état suivant."""
    global position_historique

    if position_historique < len(historique) - 1:
        position_historique += 1
        charger_historique()


def charger_historique():
    """Replace les curseurs sur un ancien état."""
    global photomaton_actif, inverse_video_actif

    etat = historique[position_historique]
    curseur_luminosite.set(etat["luminosite"])
    curseur_contraste.set(etat["contraste"])
    curseur_saturation.set(etat["saturation"])
    curseur_nettete.set(etat["nettete"])
    curseur_gamma.set(etat["gamma"])
    curseur_exposition.set(etat["exposition"])
    curseur_temperature.set(etat["temperature"])
    curseur_teinte.set(etat["teinte"])
    curseur_vibrance.set(etat["vibrance"])
    curseur_noir_blanc.set(etat["noir_blanc"])
    curseur_flou.set(etat["flou"])
    entree_photomaton.delete(0, tk.END)
    entree_photomaton.insert(0, etat["nombre_photomaton"])
    photomaton_actif = etat["photomaton"]
    inverse_video_actif = etat["inverse_video"]

    if photomaton_actif:
        bouton_photomaton.configure(text="Photomaton : oui")
    else:
        bouton_photomaton.configure(text="Photomaton : non")

    if inverse_video_actif:
        bouton_inverse_video.configure(text="Inverse vidéo : oui")
    else:
        bouton_inverse_video.configure(text="Inverse vidéo : non")

    mise_a_jour_images()


# 6. Enregistrer et quitter

def enregistrer_image(evenement=None):
    """Enregistre l'image modifiée."""
    if image_transforme != None:
        nom_fichier = filedialog.asksaveasfilename(defaultextension=".png")

        if nom_fichier != "":
            image_transforme.save(nom_fichier)


def quitter_application(evenement=None):
    """Ferme la fenêtre."""
    fenetre.destroy()


# 7. Création de la fenêtre

fenetre = tk.Tk()
fenetre.title("LEK LOOK")
fenetre.geometry("1280x720")
fenetre.resizable(True, True)

# Les couleurs du logo LEK LOOK

couleur_jaune = "#ffc20e"
couleur_bleu = "#00071d"
couleur_fond = "#fff4d6"
couleur_panneau = "#ffffff"
couleur_canevas = "#f5f1e7"

fenetre.configure(background=couleur_fond)
fenetre.option_add("*background", couleur_fond)
fenetre.option_add("*foreground", couleur_bleu)
fenetre.option_add("*Label.background", couleur_panneau)
fenetre.option_add("*Label.foreground", couleur_bleu)

# Les boutons du haut

barre_actions = tk.Frame(fenetre, background=couleur_jaune)
barre_actions.pack(fill=tk.X, padx=8, pady=8)

nom_projet = tk.Label(barre_actions, text="LEK LOOK", background=couleur_jaune, foreground=couleur_bleu, font=("Arial", 18, "bold"))
nom_projet.pack(side=tk.LEFT, padx=12)

btn_ouvrir = tk.Button(barre_actions, text="Ouvrir", background=couleur_bleu, foreground=couleur_jaune, activebackground=couleur_jaune)
btn_ouvrir.pack(side=tk.LEFT, padx=3)
btn_ouvrir.bind("<Button-1>", ouvrir_fichier)

btn_enregistrer = tk.Button(barre_actions, text="Enregistrer", background=couleur_bleu, foreground=couleur_jaune, activebackground=couleur_jaune)
btn_enregistrer.pack(side=tk.LEFT, padx=3)
btn_enregistrer.bind("<Button-1>", enregistrer_image)

btn_restaurer = tk.Button(barre_actions, text="Restaurer", background=couleur_bleu, foreground=couleur_jaune, activebackground=couleur_jaune)
btn_restaurer.pack(side=tk.LEFT, padx=3)
btn_restaurer.bind("<Button-1>", restaurer_image)

btn_annuler = tk.Button(barre_actions, text="Annuler", background=couleur_bleu, foreground=couleur_jaune, activebackground=couleur_jaune)
btn_annuler.pack(side=tk.LEFT, padx=3)
btn_annuler.bind("<Button-1>", annuler_modification)

btn_retablir = tk.Button(barre_actions, text="Rétablir", background=couleur_bleu, foreground=couleur_jaune, activebackground=couleur_jaune)
btn_retablir.pack(side=tk.LEFT, padx=3)
btn_retablir.bind("<Button-1>", retablir_modification)

btn_quitter = tk.Button(barre_actions, text="Quitter", background=couleur_bleu, foreground=couleur_jaune, activebackground=couleur_jaune)
btn_quitter.pack(side=tk.LEFT, padx=3)
btn_quitter.bind("<Button-1>", quitter_application)

# Les réglages à gauche et les images à droite

cadre_principal = tk.Frame(fenetre, background=couleur_fond)
cadre_principal.pack(padx=8, pady=8)

cadre_image_gauche = tk.LabelFrame(cadre_principal, text="Image originale", background=couleur_panneau, foreground=couleur_bleu)
cadre_image_gauche.pack(side=tk.LEFT, padx=5)

canevas_gauche = tk.Canvas(cadre_image_gauche, width=360, height=500, background=couleur_canevas, highlightthickness=2, highlightbackground=couleur_jaune)
canevas_gauche.pack()

cadre_reglages = tk.LabelFrame(cadre_principal, text="Réglages", background=couleur_panneau, foreground=couleur_bleu)
cadre_reglages.pack(side=tk.LEFT, padx=5, before=cadre_image_gauche)

colonne_gauche = tk.Frame(cadre_reglages, background=couleur_panneau)
colonne_gauche.pack(side=tk.LEFT, padx=5)

colonne_droite = tk.Frame(cadre_reglages, background=couleur_panneau)
colonne_droite.pack(side=tk.LEFT, padx=5)

cadre_image_droite = tk.LabelFrame(cadre_principal, text="Image modifiée", background=couleur_panneau, foreground=couleur_bleu)
cadre_image_droite.pack(side=tk.LEFT, padx=5)

canevas_droite = tk.Canvas(cadre_image_droite, width=360, height=500, background=couleur_canevas, highlightthickness=2, highlightbackground=couleur_jaune)
canevas_droite.pack()

# Les filtres spéciaux

bouton_photomaton = tk.Button(colonne_gauche, text="Photomaton : non", background=couleur_jaune, foreground=couleur_bleu, activebackground=couleur_jaune)
bouton_photomaton.pack(fill=tk.X, pady=2)
bouton_photomaton.bind("<Button-1>", appliquer_photomaton)

tk.Label(colonne_gauche, text="Copies Photomaton").pack()
entree_photomaton = tk.Spinbox(colonne_gauche, from_=1, to=10, width=5, command=changer_nombre_photomaton, background=couleur_jaune, foreground=couleur_bleu, insertbackground=couleur_bleu)
entree_photomaton.delete(0, tk.END)
entree_photomaton.insert(0, "4")
entree_photomaton.pack()
entree_photomaton.bind("<KeyRelease>", changer_nombre_photomaton)

bouton_inverse_video = tk.Button(colonne_gauche, text="Inverse vidéo : non", background=couleur_jaune, foreground=couleur_bleu, activebackground=couleur_jaune)
bouton_inverse_video.pack(fill=tk.X, pady=2)
bouton_inverse_video.bind("<Button-1>", appliquer_inverse_video)

# Les curseurs de gauche

tk.Label(colonne_gauche, text="Luminosité").pack()
curseur_luminosite = tk.Scale(colonne_gauche, from_=-100, to=100, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_luminosite.pack()

tk.Label(colonne_gauche, text="Contraste").pack()
curseur_contraste = tk.Scale(colonne_gauche, from_=-100, to=100, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_contraste.pack()

tk.Label(colonne_gauche, text="Saturation").pack()
curseur_saturation = tk.Scale(colonne_gauche, from_=-100, to=100, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_saturation.pack()

tk.Label(colonne_gauche, text="Netteté").pack()
curseur_nettete = tk.Scale(colonne_gauche, from_=0, to=200, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_nettete.set(100)
curseur_nettete.pack()

tk.Label(colonne_gauche, text="Gamma").pack()
curseur_gamma = tk.Scale(colonne_gauche, from_=0.1, to=3, resolution=0.1, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_gamma.set(1)
curseur_gamma.pack()

# Les curseurs de droite

tk.Label(colonne_droite, text="Exposition").pack()
curseur_exposition = tk.Scale(colonne_droite, from_=-3, to=3, resolution=0.1, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_exposition.pack()

tk.Label(colonne_droite, text="Température").pack()
curseur_temperature = tk.Scale(colonne_droite, from_=-100, to=100, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_temperature.pack()

tk.Label(colonne_droite, text="Teinte").pack()
curseur_teinte = tk.Scale(colonne_droite, from_=-100, to=100, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_teinte.pack()

tk.Label(colonne_droite, text="Vibrance").pack()
curseur_vibrance = tk.Scale(colonne_droite, from_=-100, to=100, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_vibrance.pack()

tk.Label(colonne_droite, text="Noir et blanc").pack()
curseur_noir_blanc = tk.Scale(colonne_droite, from_=0, to=100, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_noir_blanc.pack()

tk.Label(colonne_droite, text="Flou").pack()
curseur_flou = tk.Scale(colonne_droite, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL, command=mise_a_jour_images)
curseur_flou.pack()

# Mémoriser les changements des curseurs

liste_curseurs = [curseur_luminosite, curseur_contraste, curseur_saturation, curseur_nettete, curseur_gamma, curseur_exposition, curseur_temperature, curseur_teinte, curseur_vibrance, curseur_noir_blanc, curseur_flou]

for curseur in liste_curseurs:
    curseur.configure(background=couleur_panneau, foreground=couleur_bleu, troughcolor=couleur_jaune, highlightthickness=0)
    curseur.bind("<ButtonRelease-1>", memoriser_modification)

fenetre.mainloop()
