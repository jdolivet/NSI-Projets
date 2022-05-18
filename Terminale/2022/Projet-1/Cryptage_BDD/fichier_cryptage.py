import easygui, sys, sqlite3 #import les modules
from cles import cryptage, e, d, n #importe le fichier où se trouve les clés et algorithme rsa

tables = []
resultats_requetes = []
fichier = easygui.fileopenbox() # ouvre l'interface graphique permettant de chosir un fichier dans le repertoire

print('\nLa clé publique est', e)
cle_publique = int(input("Quelle est la clé publique?: "))

if cle_publique == e:
    acces = True 
    print("\nAccès vérifié")
else:
    acces = False
    print("\nMauvaise clé.")
    sys.exit("Executez le programme a nouveau.")
    
    
def applique(op: callable, tab: list, cle: int, n: int): #fonction qui prend une fonction en paramètre
    return op(tab, cle, n)
    
if acces == True: #execute seulement le code si acces reste True tout au long
    connexion = sqlite3.connect(fichier) #etablit la connexion avec le fichier
    cursor = connexion.execute("SELECT name FROM sqlite_master WHERE type = 'table';") #requete SQL permettant de recuperer le noms des tables des bases de données
    tab =  list(cursor.fetchall()) #.fetchall est un tableau de tuples, on convertis cela dans un tableau à 2d
    for i in range(len(tab)):
        tables += [tab[i][0]] #nettoye le tableau car il n'était pas clair
    for i in range(len(tables)):
            cursor = connexion.execute(f"SELECT * FROM {tables[i]};") #pour chaque table de la base de donnée
            resultats_requetes = list(cursor.fetchall()) #prend toutes les données de la table sous forme d'un tableau de tuple et les stocke sur python
            connexion.execute(f"DELETE FROM {tables[i]}") #supprime les donnés de la table sans supprimer la table elle-même
            resultats_requetes = applique(cryptage, resultats_requetes, e, n) #crypte le tableau de tuples
            for j in range(len(resultats_requetes)):
                connexion.execute(f"INSERT INTO {tables[i]} VALUES {tuple(resultats_requetes[j])}")
    print("Cryptage éffectuer.")
    connexion.commit() #execute toutes les commandes
    connexion.close()

print("\nPour décrypter la base de données, garder la clé privée pour l'insérer dans le fichier decryptage.")
print(f"Votre clé privée est {d}.")

