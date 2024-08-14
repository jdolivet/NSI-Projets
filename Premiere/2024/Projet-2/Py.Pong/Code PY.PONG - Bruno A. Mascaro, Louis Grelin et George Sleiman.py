import tkinter as tk
from tkinter import messagebox
import datetime
import os
import csv
import pygame

# Initialiser le mixeur pygame pour jouer des sons
pygame.mixer.init()

# Constantes
SCORE_GAGNANT = 2
FICHIER_RANG = "classement.csv"
VITESSE_BALLE = 7
INTERVALLE_AUGMENTATION_VITESSE = 50000  # 5 secondes

# Charger les sons
son_rebond = pygame.mixer.Sound("rebond.mp3")
son_point = pygame.mixer.Sound("point.mp3")
son_victoire = pygame.mixer.Sound("victoire.mp3")

# Fonction pour enregistrer le classement
def enregistrer_classement(gagnant: str, perdant: str, score_joueur1: int, score_joueur2: int) -> None:
    """Enregistre les résultats des jeux dans un fichier CSV."""
    with open(FICHIER_RANG, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([gagnant, perdant, score_joueur1, score_joueur2, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

# Fonction pour charger le classement
def charger_classement() -> list:
    """Charge les données de classement à partir du fichier CSV."""
    if not os.path.exists(FICHIER_RANG):
        return []
    with open(FICHIER_RANG, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Ignorer l'en-tête
        return list(reader)

# Créer le fichier de classement s'il n'existe pas
if not os.path.exists(FICHIER_RANG):
    with open(FICHIER_RANG, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Gagnant", "Adversaire", "Score Joueur 1", "Score Joueur 2", "Date"])

# Fonction pour afficher les journaux de jeu
def afficher_journaux() -> None:
    """Affiche les journaux de jeu, triés par date."""
    for widget in cadre_principal.winfo_children():
        widget.destroy()
    classement = charger_classement()
    classement.sort(key=lambda x: x[4], reverse=True)  # Trier par date
    tk.Label(cadre_principal, text="Journaux", font=("Arial", 24)).pack(pady=10)
    cadre_journaux = tk.Frame(cadre_principal)
    cadre_journaux.pack()
    tk.Label(cadre_journaux, text="Gagnant", font=("Arial", 14)).grid(row=0, column=0)
    tk.Label(cadre_journaux, text="Adversaire", font=("Arial", 14)).grid(row=0, column=1)
    tk.Label(cadre_journaux, text="Score", font=("Arial", 14)).grid(row=0, column=2)
    tk.Label(cadre_journaux, text="Date", font=("Arial", 14)).grid(row=0, column=3)
    for i, (gagnant, perdant, s1, s2, date) in enumerate(classement, start=1):
        tk.Label(cadre_journaux, text=gagnant, font=("Arial", 12)).grid(row=i, column=0)
        tk.Label(cadre_journaux, text=perdant, font=("Arial", 12)).grid(row=i, column=1)
        tk.Label(cadre_journaux, text=f"{s1} - {s2}", font=("Arial", 12)).grid(row=i, column=2)
        tk.Label(cadre_journaux, text=date, font=("Arial", 12)).grid(row=i, column=3)
    tk.Button(cadre_principal, text="Retour", command=afficher_ecran_initial, font=("Arial", 14)).pack(pady=10)

# Fonction pour afficher le classement
def afficher_classement() -> None:
    """Affiche le classement des joueurs en fonction du nombre de victoires."""
    for widget in cadre_principal.winfo_children():
        widget.destroy()
    classement = charger_classement()
    
    gagnants = {}
    for row in classement:
        gagnant = row[0]
        if gagnant in gagnants:
            gagnants[gagnant] += 1
        else:
            gagnants[gagnant] = 1

    gagnants_tries = sorted(gagnants.items(), key=lambda x: x[1], reverse=True)
    
    tk.Label(cadre_principal, text="Classement", font=("Arial", 24)).pack(pady=10)
    cadre_classement = tk.Frame(cadre_principal)
    cadre_classement.pack()
    tk.Label(cadre_classement, text="Joueur", font=("Arial", 14)).grid(row=0, column=0)
    tk.Label(cadre_classement, text="Victoires", font=("Arial", 14)).grid(row=0, column=1)
    for i, (gagnant, victoires) in enumerate(gagnants_tries, start=1):
        tk.Label(cadre_classement, text=gagnant, font=("Arial", 12)).grid(row=i, column=0)
        tk.Label(cadre_classement, text=victoires, font=("Arial", 12)).grid(row=i, column=1)
    tk.Button(cadre_principal, text="Retour", command=afficher_ecran_initial, font=("Arial", 14)).pack(pady=10)

# Fonction pour afficher l'écran initial
def afficher_ecran_initial() -> None:
    """Affiche l'écran d'accueil avec le logo et les options pour voir les journaux et le classement, ou commencer le jeu."""
    for widget in cadre_principal.winfo_children():
        widget.destroy()
    
    # Charger le logo
    logo_image = tk.PhotoImage(file="logo.png")
    logo_label = tk.Label(cadre_principal, image=logo_image)
    logo_label.image = logo_image  # Conserver une référence à l'image pour éviter le ramassage de déchets
    logo_label.pack(pady=20)

    tk.Label(cadre_principal, text="PY.PONG", font=("Arial", 24)).pack(pady=20)
    tk.Label(cadre_principal, text="Appuyez sur la touche 'S' pour jouer", font=("Arial", 16)).pack(pady=20)
    tk.Button(cadre_principal, text="Voir les journaux", command=afficher_journaux, font=("Arial", 14)).pack(pady=10)
    tk.Button(cadre_principal, text="Voir le classement", command=afficher_classement, font=("Arial", 14)).pack(pady=10)
    root.bind("<KeyPress-s>", commencer_jeu)

# Fonction pour afficher l'écran de saisie des joueurs
def afficher_ecran_saisie_joueurs(nom_joueur1: str = "", nom_joueur2: str = "") -> None:
    """Affiche l'écran pour saisir les noms des joueurs avant de commencer le jeu."""
    for widget in cadre_principal.winfo_children():
        widget.destroy()
    tk.Label(cadre_principal, text="Joueur 1", font=("Arial", 14)).grid(row=0, column=0, padx=20, pady=10)
    tk.Label(cadre_principal, text="Joueur 2", font=("Arial", 14)).grid(row=0, column=2, padx=20, pady=10)
    saisie_joueur1 = tk.Entry(cadre_principal, font=("Arial", 14))
    saisie_joueur1.grid(row=1, column=0, padx=20, pady=10)
    saisie_joueur1.insert(0, nom_joueur1)
    saisie_joueur2 = tk.Entry(cadre_principal, font=("Arial", 14))
    saisie_joueur2.grid(row=1, column=2, padx=20, pady=10)
    saisie_joueur2.insert(0, nom_joueur2)
    bouton_commencer = tk.Button(cadre_principal, text="Commencer", font=("Arial", 14), command=lambda: lancer_jeu_pong(saisie_joueur1.get(), saisie_joueur2.get()))
    bouton_commencer.grid(row=2, column=1, pady=20)
    tk.Label(cadre_principal, text="Joueur 1: touches W et S", font=("Arial", 12)).grid(row=3, column=0, columnspan=3, pady=5)
    tk.Label(cadre_principal, text="Joueur 2: touches Flèche Haut et Flèche Bas", font=("Arial", 12)).grid(row=4, column=0, columnspan=3, pady=5)
    tk.Label(cadre_principal, text="Appuyez sur 'Espace' pour mettre en pause le jeu", font=("Arial", 12)).grid(row=5, column=0, columnspan=3, pady=5)
    tk.Button(cadre_principal, text="Retour", command=afficher_ecran_initial, font=("Arial", 14)).grid(row=6, column=1, pady=10)

# Fonction pour lancer le jeu de pong
def lancer_jeu_pong(nom_joueur1: str, nom_joueur2: str) -> None:
    """Démarre le jeu de pong dans une nouvelle fenêtre."""
    jeu_fenetre = tk.Toplevel(root)
    jeu_fenetre.title("PY.PONG")

    # État du jeu
    jeu_commence = False
    jeu_pause = False

    # Fonction pour basculer la pause du jeu
    def basculer_pause(event: tk.Event = None) -> None:
        """Gère la pause et la reprise du jeu."""
        nonlocal jeu_commence, jeu_pause
        if not jeu_commence:
            jeu_commence = True
            jeu_pause = False
            message_commencer.place_forget()
            mettre_a_jour_jeu()
        else:
            jeu_pause = not jeu_pause
            if not jeu_pause:
                cadre_pause.pack_forget()
                mettre_a_jour_jeu()
            else:
                cadre_pause.pack(fill="both", expand=True)

    # Fonction pour redémarrer le jeu
    def redemarrer_jeu() -> None:
        """Redémarre le jeu avec les mêmes joueurs."""
        jeu_fenetre.destroy()
        lancer_jeu_pong(nom_joueur1, nom_joueur2)

    # Fonction pour quitter le jeu
    def quitter_jeu() -> None:
        """Quitte le jeu et retourne à l'écran de saisie des joueurs."""
        jeu_fenetre.destroy()
        afficher_ecran_saisie_joueurs(nom_joueur1, nom_joueur2)

    cadre_pause = tk.Frame(jeu_fenetre, bg="black")

    etiquette_pause = tk.Label(cadre_pause, text="Jeu en Pause", font=("Arial", 24), fg="white", bg="black")
    etiquette_pause.pack(pady=20)

    bouton_reprendre = tk.Button(cadre_pause, text="Reprendre", font=("Arial", 14), command=basculer_pause)
    bouton_reprendre.pack(pady=10)

    bouton_redemarrer = tk.Button(cadre_pause, text="Recommencer", font=("Arial", 14), command=redemarrer_jeu)
    bouton_redemarrer.pack(pady=10)

    bouton_quitter = tk.Button(cadre_pause, text="Quitter", font=("Arial", 14), command=quitter_jeu)
    bouton_quitter.pack(pady=10)

    cadre_pause.pack_forget()

    # Configurations du canvas
    canvas = tk.Canvas(jeu_fenetre, width=600, height=400, bg="black")
    canvas.pack()

    # Message pour démarrer le jeu
    message_commencer = tk.Label(jeu_fenetre, text="Appuyez sur la touche 'Espace' pour commencer", font=("Arial", 16), fg="white", bg="black")
    message_commencer.place(relx=0.5, rely=0.5, anchor="center")

    # Dessiner les raquettes et la balle
    raquette1 = canvas.create_rectangle(20, 150, 30, 250, fill="white")
    raquette2 = canvas.create_rectangle(570, 150, 580, 250, fill="white")
    balle = canvas.create_oval(290, 190, 310, 210, fill="white")
    
    # Score
    score_joueur1 = 0
    score_joueur2 = 0
    score_joueur1_text = canvas.create_text(150, 20, text=f"{nom_joueur1}: {score_joueur1}", font=("Arial", 16), fill="white")
    score_joueur2_text = canvas.create_text(450, 20, text=f"{nom_joueur2}: {score_joueur2}", font=("Arial", 16), fill="white")

    # Variables de contrôle
    balle_dx = VITESSE_BALLE
    balle_dy = VITESSE_BALLE
    vitesse_raquette = 20
    raquette1_dy = 0
    raquette2_dy = 0

    # Fonction pour déplacer la raquette 1
    def deplacer_raquette1(event: tk.Event) -> None:
        """Déplace la raquette 1 vers le haut ou le bas."""
        nonlocal raquette1_dy
        if event.keysym == 'w':
            raquette1_dy = -vitesse_raquette
        elif event.keysym == 's':
            raquette1_dy = vitesse_raquette

    # Fonction pour arrêter la raquette 1
    def arreter_raquette1(event: tk.Event) -> None:
        """Arrête le mouvement de la raquette 1."""
        nonlocal raquette1_dy
        if event.keysym in ('w', 's'):
            raquette1_dy = 0

    # Fonction pour déplacer la raquette 2
    def deplacer_raquette2(event: tk.Event) -> None:
        """Déplace la raquette 2 vers le haut ou le bas."""
        nonlocal raquette2_dy
        if event.keysym == 'Up':
            raquette2_dy = -vitesse_raquette
        elif event.keysym == 'Down':
            raquette2_dy = vitesse_raquette

    # Fonction pour arrêter la raquette 2
    def arreter_raquette2(event: tk.Event) -> None:
        """Arrête le mouvement de la raquette 2."""
        nonlocal raquette2_dy
        if event.keysym in ('Up', 'Down'):
            raquette2_dy = 0

    # Fonction pour augmenter la vitesse de la balle
    def augmenter_vitesse() -> None:
        """Augmente progressivement la vitesse de la balle toutes les 10 secondes."""
        nonlocal balle_dx, balle_dy
        if not jeu_pause:
            balle_dx *= 1.1
            balle_dy *= 1.1
            jeu_fenetre.after(INTERVALLE_AUGMENTATION_VITESSE, augmenter_vitesse)

    # Fonction pour mettre à jour le jeu
    def mettre_a_jour_jeu() -> None:
        """Met à jour l'état du jeu, déplace les raquettes et la balle, vérifie les collisions et met à jour les scores."""
        nonlocal balle_dx, balle_dy, score_joueur1, score_joueur2

        if jeu_pause or not jeu_commence:
            return

        # Mouvement des raquettes
        canvas.move(raquette1, 0, raquette1_dy)
        canvas.move(raquette2, 0, raquette2_dy)

        # Limiter le mouvement des raquettes aux bords du canvas
        coords_raquette1 = canvas.coords(raquette1)
        coords_raquette2 = canvas.coords(raquette2)
        if coords_raquette1[1] < 0:
            canvas.move(raquette1, 0, -coords_raquette1[1])
        if coords_raquette1[3] > 400:
            canvas.move(raquette1, 0, 400 - coords_raquette1[3])
        if coords_raquette2[1] < 0:
            canvas.move(raquette2, 0, -coords_raquette2[1])
        if coords_raquette2[3] > 400:
            canvas.move(raquette2, 0, 400 - coords_raquette2[3])

        # Mouvement de la balle
        canvas.move(balle, balle_dx, balle_dy)
        coords_balle = canvas.coords(balle)

        # Collision avec les bords supérieur et inférieur
        if coords_balle[1] <= 0 or coords_balle[3] >= 400:
            balle_dy = -balle_dy

        # Collision avec les raquettes
        if (coords_balle[0] <= coords_raquette1[2] and coords_raquette1[1] < coords_balle[3] and coords_raquette1[3] > coords_balle[1]) or \
           (coords_balle[2] >= coords_raquette2[0] and coords_raquette2[1] < coords_balle[3] and coords_raquette2[3] > coords_balle[1]):
            balle_dx = -balle_dx
            son_rebond.play()

        # Mise à jour du score
        if coords_balle[0] <= 0:
            score_joueur2 += 1
            son_point.play()
            canvas.itemconfig(score_joueur2_text, text=f"{nom_joueur2}: {score_joueur2}")
            canvas.coords(balle, 290, 190, 310, 210)
            balle_dx = VITESSE_BALLE
            balle_dy = VITESSE_BALLE
        elif coords_balle[2] >= 600:
            score_joueur1 += 1
            son_point.play()
            canvas.itemconfig(score_joueur1_text, text=f"{nom_joueur1}: {score_joueur1}")
            canvas.coords(balle, 290, 190, 310, 210)
            balle_dx = -VITESSE_BALLE
            balle_dy = -VITESSE_BALLE

        # Vérifier si un joueur a gagné
        if score_joueur1 == SCORE_GAGNANT:
            enregistrer_classement(nom_joueur1, nom_joueur2, score_joueur1, score_joueur2)
            son_victoire.play()
            messagebox.showinfo("Fin du jeu", f"{nom_joueur1} a gagné!")
            jeu_fenetre.destroy()
            afficher_ecran_saisie_joueurs(nom_joueur1, nom_joueur2)
        elif score_joueur2 == SCORE_GAGNANT:
            enregistrer_classement(nom_joueur2, nom_joueur1, score_joueur1, score_joueur2)
            son_victoire.play()
            messagebox.showinfo("Fin du jeu", f"{nom_joueur2} a gagné!")
            jeu_fenetre.destroy()
            afficher_ecran_saisie_joueurs(nom_joueur1, nom_joueur2)
        else:
            jeu_fenetre.after(20, mettre_a_jour_jeu)

    # Liaison des touches pour les mouvements des raquettes
    jeu_fenetre.bind("<KeyPress-w>", deplacer_raquette1)
    jeu_fenetre.bind("<KeyPress-s>", deplacer_raquette1)
    jeu_fenetre.bind("<KeyRelease-w>", arreter_raquette1)
    jeu_fenetre.bind("<KeyRelease-s>", arreter_raquette1)
    jeu_fenetre.bind("<KeyPress-Up>", deplacer_raquette2)
    jeu_fenetre.bind("<KeyPress-Down>", deplacer_raquette2)
    jeu_fenetre.bind("<KeyRelease-Up>", arreter_raquette2)
    jeu_fenetre.bind("<KeyRelease-Down>", arreter_raquette2)
    jeu_fenetre.bind("<KeyPress-space>", basculer_pause)

    # Démarrer l'augmentation de la vitesse de la balle
    jeu_fenetre.after(INTERVALLE_AUGMENTATION_VITESSE, augmenter_vitesse)

# Fonction pour commencer le jeu
def commencer_jeu(event: tk.Event) -> None:
    """Défaire l'association pour éviter de recommencer le jeu et afficher l'écran de saisie des joueurs."""
    root.unbind("<KeyPress-s>")  # Défaire l'association pour éviter de recommencer
    afficher_ecran_saisie_joueurs()

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("PY.PONG")

# Cadre principal
cadre_principal = tk.Frame(root)
cadre_principal.pack(fill="both", expand=True)

# Afficher l'écran initial
afficher_ecran_initial()

# Boucle principale de l'application
root.mainloop()
