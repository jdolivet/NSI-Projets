from random import randint
from hashlib import sha256
from math import gcd

#from time import perf_counter
  
def est_premier(n: int, k: int) -> bool:
    """Renvoie true si n est probablement premier et false sinon. Utilise le petit théorème de Fermat.
    La fiabilité de la primalité de n depend de la grandeur de k."""
    if n % 2 == 0 and n != 2: #Le seul nombre premier pair est 2.
        return False
    for i in range(k):
        a = randint(2, n-2)   #Génère k eléments compris dans [2,n-1[
        if pow(a,n-1,n) != 1:  #pour tout a < n-1, a^(n-1) mod n = 1 (si n est premier).
            return False
    return True

def genere_premier(debut: int, fin:int, k: int) -> int:
    """Renvoie un nombre premier aléatoire compris entre l'intervalle [debut,fin].
    Un plus grand k génère un nombre plus probablement premier mais prendra plus de temps pour la génération.
    Le fonctionnement de la fonction dépend également des valeurs passés en paramètre. Il est convenable
    de choisir un intervalle suffisamment grand pour assurer la bonne démarche et ne pas se rendre dans une boucle infinie."""
    a = randint(debut, fin)
    while not est_premier(a, k):
        a = randint(debut, fin)
    return a

def generateur(n: int):
    """Renvoie un générateur aléatoire du Groupe Cyclique d'ordre n, si n est premier."""
    ordre = set(range(1, n))
    if est_premier(n,1000): #Éxécute le code uniquement si n est premier
        while True:
            a = randint(1,n-1)
            g = set()
            for x in ordre:
                g.add(pow(a,x,n)) #Si g est generateur du groupe d'ordre n,
            if g == ordre: #alors pour tout 1 < a <= n-1, l'ensemble a**1, a**2, ..., a**(n-1)
                return a #contient tout les élément du groupe Z_n, soit tout nombre entier inférieur à n.

def est_generateur(g:int, G:int) -> bool:
    """Renvoie True si g est générateur du groupe G (G est en fait l'ordre du Groupe)"""
    ordre = set(range(1,G))
    valeurs = set()
    for x in ordre:
        valeurs.add(pow(g,x,G))  #Marche similairement a la fonction generateur(n).
    if valeurs != ordre:   
        return False
    else:
        return True

def hachage(r: int, M: str) -> int:
    """Applique la fonction de hachage sha256 en concatenant r et M."""
    #On choisit sha256 car elle est parmis les fonctions de hachage les plus fiables et rapides.
    #Il est connu par l'équilibre entre sécurité et coût en temps. "cout x bénéfice"
    hash=sha256();  #La fonction de hachage est définie comme sha256.
    r_M = str(r) + M
    hash.update(r_M.encode()); 
    return int(hash.hexdigest(),16); #hexdigest() renvoie un str haché avec des nombres hexadécimaux.
    #On le converti un un entier en base 10.


#Tests de coût: temps algorithmique

# time = 0
# n = 1
# 
# for i in range(n):
#     debut = perf_counter()
#     nb_premier = genere_premier(100000,1000000)
#     generateur(nb_premier)
#     fin = perf_counter()
#     time += (fin-debut)
# 
# print(time/n, 's')
# 
# nb = 999979
# temps = 0 
# for i in range(10):
#     debut = perf_counter()
#     generateur(nb)
#     fin = perf_counter()
#     temps += fin-debut
# print(temps/10,'s')
        
