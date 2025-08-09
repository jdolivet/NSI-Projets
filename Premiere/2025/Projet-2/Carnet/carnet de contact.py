# Carnet de contacts - Version simple

contacts = []

def menu():
    print("\n--- Menu ---")
    print("1. Ajouter un contact")
    print("2. Voir les contacts")
    print("3. Rechercher un contact")
    print("0. Quitter")
    return input("Choix : ")

def ajouter():
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    tel = input("Téléphone : ")
    email = input("Email : ")
    contact = {"prenom": prenom, "nom": nom, "tel": tel, "email": email}
    contacts.append(contact)
    print("Contact ajouté.")

def afficher():
    if not contacts:
        print("Aucun contact.")
    else:
        for c in contacts:
            print(f"{c['prenom']} {c['nom']} - {c['tel']} - {c['email']}")

def rechercher():
    nom = input("Nom à chercher : ").lower()
    trouvé = False
    for c in contacts:
        if nom in c["nom"].lower():
            print(f"{c['prenom']} {c['nom']} - {c['tel']} - {c['email']}")
            trouvé = True
    if not trouvé:
        print("Aucun résultat.")

# Boucle principale
while True:
    choix = menu()
    if choix == "1":
        ajouter()
    elif choix == "2":
        afficher()
    elif choix == "3":
        rechercher()
    elif choix == "0":
        print("Bye !")
        break
    else:
        print("Choix invalide.")
