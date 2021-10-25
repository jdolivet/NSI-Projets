# Liste de mots | PENDU - Projet NSI

from random import choice

def prendre_mots():
    mots = []
    with open("listeDeMots_pendu.txt") as liste:
        for line in liste:
            line = line.rstrip("\n").replace(' ','').split(',')
            for mot in line:
                mots.append(mot)
                
        return choice(mots)
        