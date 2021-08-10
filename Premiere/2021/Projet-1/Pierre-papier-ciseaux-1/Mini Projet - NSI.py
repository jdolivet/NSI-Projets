"""
Mini Projet - NSI | Jokenpo
Theo, Felipe et Gabriel
"""

from random import randint

jokenpo = ["Pierre", "Papier", "Ciseaux"]
ordinateur = randint(0, 2)
print("""Vos choix:
[ 0 ] Pierre
[ 1 ] Papier
[ 2 ] Ciseaux""")
joueur = int(input("Quel est votre choix? "))

print("JO")
print("KEN")
print("PO!!!")

print("-=-" * 9)

print(f"L'Ordinateur a choisi {jokenpo[ordinateur]}.")
print(f"Vous avez choisi {jokenpo[joueur]}.")
print("-=-" * 9)

# ORDINATEUR a choisi [0] = PIERRE
if ordinateur == 0:
    if joueur == 0:
        print("Match nul!")
    elif joueur == 1:
        print("Vous avez GAGNÉ!")
    elif joueur == 2:
        print("L'ORDINATEUR a gagné.")
    else:
        print("ERREUR! Jouer a nouveau!")
# ORDINATEUR a choisi [1] =  PAPIER
elif ordinateur == 1:
    if joueur == 0:
        print("L'ORDINATEUR a gagné.")
    elif joueur == 1:
        print("Match nul!")
    elif joueur == 2:
        print("Vous avez GAGNÉ!")
    else:
        print("ERREUR! Jouer a nouveau!")
# ORDINATEUR a choisi [2] = CISEAUX
elif ordinateur == 2:       
    if joueur == 0:
        print("Vous avez GAGNÉ!")
    elif joueur == 1:
        print("L'ORDINATEUR a gagné.")
    elif joueur == 2:
        print("Match nul!")
    else:
        print("ERREUR! Jouer a nouveau!")
        