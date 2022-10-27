from random import choice, shuffle

# Listes des différents types de caractères qui seront utiliser dans notre mot de passe
# Les éléments sont des chaine de caractères pour faciliter la concaténation

# Liste des lettres majuscules (A-Z)
lettres_majuscules = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                      'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                      'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                      'Z']

# Liste des lettres minuscules (a-z)
lettres_minuscules = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                      'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                      'z']

# Liste des chiffres (0-9)
chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Liste des caractères spéciaux
caractere_speciaux = ['@', '#', '$', '%', '=', ':', '?', '.',
                      '/', '|', '~', '>', '*', '(', ')', '<']


# Renvoie un mot de passe avec les quatres éléments
def mdp_complet(longueur):
    """Renvoie un mot de passe avec au moins un élément de chaque liste."""
    # Rassemble tout les éléments de toutes les listes en une seule liste
    liste_combiner = lettres_majuscules + lettres_minuscules + chiffres + caractere_speciaux
    # Selectionne aléatoirement un élément de chaque liste
    majuscule_aleatoire = choice(lettres_majuscules)  # Choisit une lettre majuscule aléatoire
    minuscule_aleatoire = choice(lettres_minuscules)  # Choisit une lettre minuscule aléatoire
    chiffre_aleatoire = choice(chiffres)  # Choisit un chiffre aléatoire
    cspecial_aleatoire = choice(caractere_speciaux)  # Choisit un caractère spécial aléatoire
    # Ajoute les éléments aléatoires choisit auparavant dans une liste temporaire
    # En ce moment, le mot de passe ne contient que les quatres caracteres choisit aléatoirement
    mdp_temp = []
    mdp_temp.append(majuscule_aleatoire)
    mdp_temp.append(minuscule_aleatoire)
    mdp_temp.append(chiffre_aleatoire)
    mdp_temp.append(cspecial_aleatoire)

    # Entre dans une boucle for qui tourne la longueur déterminer
    # du mot de passe moins les éléments aléatoires déjà déterminer
    for i in range(longueur - 4):
        mdp_temp.append(choice(liste_combiner))  # Ajoute les nouveaux éléments du mot de passe aussi choisi au hasard
    shuffle(mdp_temp)  # Mélange le mot de passe

    mot_de_passe = ""
    # Parcour la liste avec les éléments choisit aléatoirement et
    # les ajoutent dans la chaîne de caractère qui correspond à notre mot de passe finale.
    for elt in mdp_temp:
        mot_de_passe = mot_de_passe + elt

    return mot_de_passe


# Renvoie un mot de passe sans lettres majuscules
def sans_majuscules(longueur):
    """Renvoie un mot de passe sans lettre majuscule."""
    liste_combiner = lettres_minuscules + chiffres + caractere_speciaux
    minuscule_aleatoire = choice(lettres_minuscules)
    chiffre_aleatoire = choice(chiffres)
    cspecial_aleatoire = choice(caractere_speciaux)
    mdp_temp = []
    mdp_temp.append(minuscule_aleatoire)
    mdp_temp.append(chiffre_aleatoire)
    mdp_temp.append(cspecial_aleatoire)

    for i in range(longueur - 3):
        mdp_temp.append(choice(liste_combiner))
    shuffle(mdp_temp)

    mot_de_passe = ""
    for elt in mdp_temp:
        mot_de_passe = mot_de_passe + elt

    return mot_de_passe


# Renvoie un mot de passe sans lettres minuscules
def sans_minuscules(longueur):
    """Renvoie un mot de passe sans lettre minuscule."""
    liste_combiner = lettres_majuscules + chiffres + caractere_speciaux
    majuscule_aleatoire = choice(lettres_majuscules)
    chiffre_aleatoire = choice(chiffres)
    cspecial_aleatoire = choice(caractere_speciaux)
    mdp_temp = []
    mdp_temp.append(majuscule_aleatoire)
    mdp_temp.append(chiffre_aleatoire)
    mdp_temp.append(cspecial_aleatoire)

    for i in range(longueur - 3):
        mdp_temp.append(choice(liste_combiner))
    shuffle(mdp_temp)

    mot_de_passe = ""
    for elt in mdp_temp:
        mot_de_passe = mot_de_passe + elt

    return mot_de_passe


# Renvoie un mot de passe sans chiffres
def sans_chiffres(longueur):
    """Renvoie un mot de passe sans chiffre."""
    liste_combiner = lettres_majuscules + lettres_minuscules + caractere_speciaux
    majuscule_aleatoire = choice(lettres_majuscules)
    minuscule_aleatoire = choice(lettres_minuscules)
    cspecial_aleatoire = choice(caractere_speciaux)
    mdp_temp = []
    mdp_temp.append(majuscule_aleatoire)
    mdp_temp.append(minuscule_aleatoire)
    mdp_temp.append(cspecial_aleatoire)

    for i in range(longueur - 4):
        mdp_temp.append(choice(liste_combiner))
    shuffle(mdp_temp)

    mot_de_passe = ""
    for elt in mdp_temp:
        mot_de_passe = mot_de_passe + elt

    return mot_de_passe


# Renvoie un mot de passe sans carcteres speciaux
def sans_caractere_speciaux(longueur):
    """Renvoie un mot de passe sans caractère spécial."""
    liste_combiner = lettres_majuscules + lettres_minuscules + chiffres
    majuscule_aleatoire = choice(lettres_majuscules)
    minuscule_aleatoire = choice(lettres_minuscules)
    chiffre_aleatoire = choice(chiffres)
    mdp_temp = []
    mdp_temp.append(majuscule_aleatoire)
    mdp_temp.append(minuscule_aleatoire)
    mdp_temp.append(chiffre_aleatoire)

    for i in range(longueur - 3):
        mdp_temp.append(choice(liste_combiner))
    shuffle(mdp_temp)

    mot_de_passe = ""
    for elt in mdp_temp:
        mot_de_passe = mot_de_passe + elt

    return mot_de_passe
