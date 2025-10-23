# Projet : Analyseur de mot de passe
def verifier_mot_de_passe(mdp: str) -> str:
    """Vérifie si un mot de passe est fort selon la présence de minuscules, majuscules,
    chiffres, longueur du mot de passe et encore la présence de caractères spéciaux."""
    
    score = 0

    # Vérifie la longueur
    if len(mdp) >= 8:
        score += 1

    # Vérifie la présence de minuscules
    for c in mdp:
        if c.islower():
            score += 1
            break

    # Vérifie la présence de majuscules
    for c in mdp:
        if c.isupper():
            score += 1
            break

    # Vérifie la présence de chiffres
    for c in mdp:
        if c.isdigit():
            score += 1
            break

    # Vérifie la présence de caractères spéciaux
    caracteres_speciaux = "!@#$%^&*()_+-=[]{};:,<.>/?|"
    for c in mdp:
        if c in caracteres_speciaux:
            score += 1
            break

    # Évaluation finale
    if score <= 2:
        return "Mot de passe FAIBLE – Vous devez l'améliorer!"
    elif score == 3 or score == 4:
        return "Mot de passe MOYEN – C'est améliorable, mais c'est déjà plûtot bien."
    else:
        return "Mot de passe FORT – Bonne sécurité."

def main(): #Interface initialle
    print("Analyseur de mot de passe")
    mdp = input("Entrez un mot de passe à tester : ")
    resultat = verifier_mot_de_passe(mdp)
    print(resultat)

main() #Éxécution du programme