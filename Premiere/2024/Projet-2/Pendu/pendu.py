import tkinter as tk
from tkinter import messagebox
import random

# Configuration initiale du jeu
mots = [
    "abimer", "action", "ancien", "ancrer", "ardent", "armure",
    "autant", "avenir", "ballet", "banque", "bateau", "batons", "berger",
    "biopic", "bonbon", "bonnet", "bouger", "bureau", "cacher",
    "camion", "carnet", "carton", "causer", "chance", "choyer", "choisi",
    "citron", "classe", "client", "clouer", "cocher", "coiffe", "coller",
    "cousin", "courir", "crayon", "curage", "danser", "devoir", "diner",
    "efface", "effort", "eluder", "epaule", "estime", "facies", "facteur",
    "fermer", "filmer", "flacon", "flamme", "flotter", "forage", "fraise",
    "gouter", "graver", "hocher", "ignore", "infini", "jauger",
    "joueur", "jouets", "lacher", "lavoir", "lettre",
    "lignee", "lisser", "maison", "manuel", "marine", "miroir", "modele",
    "nature", "navire", "ondule", "outils", "patine", "penser", "pierre",
    "plaire", "plante", "ployer", "poudre", "priere", "racler", "rappel",
    "rayons", "repond", "rincer", "sabler", "servir", "souris", "stable"
]

mot = random.choice(mots)  # Sélectionne un mot aléatoire pour le jeu

lettres_utilisateur = []
chances = 6

def mettre_a_jour_affichage():
    """Met à jour l'affichage du mot et des chances."""
    affichage = ""
    for lettre in mot:
        if lettre in lettres_utilisateur:
            affichage += lettre + " "
        else:
            affichage += "_ "
    label_mot.config(text=affichage.strip())
    label_chances.config(text=f"Vous avez {chances} chances restantes")

def deviner_lettre():
    """Gère la tentative de deviner une lettre."""
    global chances
    tentative = entree_lettre.get().lower()
    entree_lettre.delete(0, tk.END)  # Efface l'entrée après la tentative

    if tentative and tentative not in lettres_utilisateur:
        lettres_utilisateur.append(tentative)

        if tentative not in mot:
            chances -= 1

        if all(lettre in lettres_utilisateur for lettre in mot):
            messagebox.showinfo("Victoire!", f"Félicitations, vous avez gagné! Le mot était : {mot}")
            root.quit()

        if chances == 0:
            messagebox.showinfo("Perte!", f"Désolé, vous avez perdu! Le mot était : {mot}")
            root.quit()

        mettre_a_jour_affichage()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu du Pendu")

label_mot = tk.Label(root, font=("Helvetica", 24))
label_mot.pack(pady=20)

label_chances = tk.Label(root, font=("Helvetica", 16))
label_chances.pack(pady=10)

entree_lettre = tk.Entry(root, font=("Helvetica", 24))
entree_lettre.pack(pady=20)

button_valider = tk.Button(root, text="Deviner", command=deviner_lettre, font=("Helvetica", 16))
button_valider.pack(pady=10)

# Initialiser l'affichage
mettre_a_jour_affichage()

# Démarrer l'application
root.mainloop()
