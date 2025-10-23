import time 
import matplotlib.pyplot as plt  # Pour le graphique

def afficher_temps_depuis_secondes(s): 
    """Convertit secondes en un format lisible"""
    if s == "Instantané" or s == "instantané":
        return "instantané"
    try:
        s = float(s)
    except:
        return str(s)
    if s < 1:
        return f"{s:.2f} seconde(s)"
    if s < 60:
        return f"{s:.2f} seconde(s)"
    if s < 3600:
        return f"{s/60:.2f} minute(s)"
    if s < 24*3600:
        return f"{s/3600:.2f} heure(s)"
    if s < 365*24*3600:
        return f"{s/(24*3600):.2f} jour(s)"
    return f"{s/(365*24*3600):.2f} an(s)"

# Tableau des mots de passe
table_mots_de_passe = {
    4:  "Instantané",
    5:  4 * 3600,                  # 4 heures
    6:  14 * 24 * 3600,            # 14 jours
    7:  2 * 365 * 24 * 3600,       # 2 ans
    8:  164 * 365 * 24 * 3600,     # 164 ans
    9:  11000 * 365 * 24 * 3600,   # 11k ans
    10: 803000 * 365 * 24 * 3600,  # 803k ans
    11: 56000000 * 365 * 24 * 3600,# 56M ans
    12: 3_000_000_000 * 365 * 24 * 3600, # 3Md ans
    13: 275_000_000_000 * 365 * 24 * 3600, # 275Md ans
    14: 19_000_000_000 * 365 * 24 * 3600 # 19Bn ans
}

# Météo: 1 journée ou 1 semaine
table_meteo = {
    "1": {"sec": 1 * 3600, "label": "1 heure"},
    "7": {"sec": 7 * 3600, "label": "7 heures"}
}

# Molécules
table_molecules = {
    "simple":   {"sec": 73 * 3600, "label": "73 heures"},
    "complexe": {"sec": 2 * 365 * 24 * 3600, "label": "2 ans"}
}

# Ordinateur quantique
def temps_quantique(t_super_secondes, qubits):
    if t_super_secondes == "Instantané" or t_super_secondes == "instantané":
        return "instantané"
    try:
        t = float(t_super_secondes)
    except:
        return "instantané"
    if qubits <= 0:
        return t
    facteur = 1.0 + (qubits / 10.0)
    temps_calcul = t / facteur
    if temps_calcul < 0.5:
        temps_calcul = 0.5
    return temps_calcul

# Pour numéroté 1 a 1
def mon_enumerate_liste(sequence, début=0):
    resultat = []
    index = début
    for element in sequence:
        resultat.append((index, element))
        index += 1
    return resultat

# Intro animé
print("Chargement du simulateur", end="")
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print("\n")

# Liste pour le graphique 
liste_qubits = []
liste_temps_quantique = []

# Principal
while True:
    print("=== Simulateur : Supercalculateur vs Ordinateur quantique ")
    print("Choisissez un scénario :")
    print("1 - Mots de passe ")
    print("2 - Prévision météo")
    print("3 - Simulation de molécule ")

    choix = input("Choisissez entre (1/2/3) : ").strip() # demande choisir l'option de calcul

    qubits = int(input("Combien de qubits pour l'ordinateur quantique ? (exemple: 10, 100, 1000) : ").strip()) # Demande le nombre de qubit a utilisé

    if choix == "1": # Les mots de passe
        longueur = int(input("Longueur du mot de passe (entre 4 et 14) : ").strip())
        if longueur not in table_mots_de_passe:
            print("Les données pour les mots de passe sont comprises entre 4 et 14 caractères.")
        else:
            temps_supercalculateur = table_mots_de_passe[longueur]
            print("\n--- Résultats : mots de passe ---")
            if isinstance(temps_supercalculateur, str):
                print("Supercalculateur :", temps_supercalculateur)
                print("Ordinateur quantique :", temps_supercalculateur)
            else:
                print("Supercalculateur :", afficher_temps_depuis_secondes(temps_supercalculateur))
                temps_calcul = temps_quantique(temps_supercalculateur, qubits)
                print(f"Ordinateur quantique ({qubits} qubits) :", afficher_temps_depuis_secondes(temps_calcul))

    elif choix == "2": # La météo
        print("\n--- Prévision météo ---")
        print("Choisissez la quantité de calcul :")
        print("1 - 1 journée")
        print("2 - 1 semaine")
        duree_prevision = input("Choisissez entre (1/2) : ").strip()
        if duree_prevision == "1":
            cle = "1"
        elif duree_prevision == "2":
            cle = "7"
        else:
            print("Choix invalide.")
            cle = None
        if cle:
            entree = table_meteo[cle]
            temps_supercalculateur = entree["sec"]
            temps_calcul = temps_quantique(temps_supercalculateur, qubits)
            print("\n--- Résultats : météo ---")
            print("Supercalculateur :", entree["label"])
            print(f"Ordinateur quantique ({qubits} qubits) :", afficher_temps_depuis_secondes(temps_calcul))

    elif choix == "3": # Les molécules
        print("\n--- Simulation de molécule  ---")
        print("Choisissez la complexité :")
        print("1 - Calcul réalisable (simple)")
        print("2 - Calcul trop long pour un supercalculateur (complexe)")
        c = input("Choisissez entre (1/2) : ").strip()
        if c == "1":
            entree = table_molecules["simple"]
        elif c == "2":
            entree = table_molecules["complexe"]
        else:
            print("Choix invalide.")
            entree = None
        if entree:
            temps_supercalculateur = entree["sec"]
            temps_calcul = temps_quantique(temps_supercalculateur, qubits)
            print("\n--- Résultats : simulations de molécule ---")
            print("Supercalculateur :", entree["label"])
            print(f"Ordinateur quantique ({qubits} qubits) :", afficher_temps_depuis_secondes(temps_calcul))
    else:
        print("Choix invalide. Fin.") # EN cas d'entré éronné
        temps_calcul = None

    # Sauvegarde des résultats dans un fichier texte
    if 'temps_calcul' in locals() and temps_calcul is not None:
        try:
            with open("resultats.txt", "a", encoding="utf-8") as f:
                f.write(f"{choix} | {qubits} qubits | Supercalculateur : {afficher_temps_depuis_secondes(temps_supercalculateur)} | Quantique : {afficher_temps_depuis_secondes(temps_calcul)}\n")
        except Exception as e:
            print("Erreur lors de la sauvegarde :", e)

        # Données pour le graphique 
        if isinstance(temps_calcul, (int, float)):
            liste_qubits.append(qubits)
            liste_temps_quantique.append(temps_calcul)

    # Relance le simulateur
    relancer = input("\nVoulez-vous relancer le simulateur ? (oui/non/graphique) : ").strip().lower()
    if relancer == "graphique":
        # Affiche le graphique 
        if liste_qubits and liste_temps_quantique:
            # Conversion du temps en heures ou jours 
            temps_affichage = []
            for t in liste_temps_quantique:
                if t < 24*3600:
                    temps_affichage.append(t/3600)  # heures
                else:
                    temps_affichage.append(t/(24*3600))  # jours

            plt.figure()
            plt.scatter(liste_qubits, temps_affichage, c='blue')  # points seulement
            plt.title("Temps de calcul quantique en fonction du nombre de qubits")
            plt.xlabel("Nombre de qubits")
            plt.ylabel("Temps (heures ou jours)")
            plt.grid(True)

            # Numérotation des points dans l’ordre de création
            for idx, (x_val, y_val) in mon_enumerate_liste(zip(liste_qubits, temps_affichage), début=1):
                plt.text(x_val, y_val, str(idx), fontsize=9, ha='left', va='bottom')

            plt.show()
        else:
            print("Aucune donnée pour le graphique.")
    elif relancer != "oui":
        print("Aurevoir.")
        break
