from random import randint

def pgcd(a: int, b: int) -> int:
    """Renvoie le PGCD entre deux entiers"""
    r = a % b
    if r == 0:
        return b
    else:
        return pgcd(b, r)

def creer_cle_publique(n: int) -> int:
    """Renvoie la clé publique"""
    while True:
        e = randint(2, n)
        if pgcd(e, n) == 1:
            return e
        
def creer_cle_privee(lim: int, e: int) -> int:
    """Renvoie la clé privée"""
    d = 0
    while((d * e) % lim != 1):
        d += 1
    return d

def cryptage(tableau: list, e: int, n: int) -> list:
    """Prend la liste avec les données, les cryptes et les renvoies cryptés dans un
    tableau de tableaux"""
    for i in range(len(tableau)):
        tableau[i] = list(tableau[i])
        for j in range(len(tableau[i])):
            mot_crypte = ''
            for k in range(len(str(tableau[i][j]))):
                tableau[i][j] = str(tableau[i][j])
                C = str(chr(ord(tableau[i][j][k])**e % n))
                mot_crypte += C
            tableau[i][j] = mot_crypte
    return tableau

def decryptage(tableau, d, n):
    """Prend le message crypté par la fonction cryptage() et récupere l'information
    crypter"""
    for i in range(len(tableau)):
        tableau[i] = list(tableau[i])
        for j in range(len(tableau[i])):
            mot_crypte = ''
            for k in range(len(str(tableau[i][j]))):
                tableau[i][j] = str(tableau[i][j])
                C = str(chr(ord(tableau[i][j][k])**d % n))
                mot_crypte += C
            tableau[i][j] = mot_crypte
    return tableau

p = 17
q = 19
n = p * q
lim = (p - 1) * (q - 1)
e = creer_cle_publique(lim)
d = creer_cle_privee(lim, e)

    