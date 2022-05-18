import easygui, sys, sqlite3
from cles import decryptage, n

tables = []
resultats_requetes = []
fichier = easygui.fileopenbox()

cle_privee = int(input("Quelle est la clé privée?: "))
    
    
def applique(op: callable, tab: list, cle: int, n: int):
    return op(tab, cle, n)
    

connexion = sqlite3.connect(fichier)
cursor = connexion.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tab =  list(cursor.fetchall())
for i in range(len(tab)):
    tables += [tab[i][0]]
for i in range(len(tables)):
        cursor = connexion.execute(f"SELECT * FROM {tables[i]};")
        resultats_requetes = list(cursor.fetchall())
        connexion.execute(f"DELETE FROM {tables[i]}")
        resultats_requetes = applique(decryptage, resultats_requetes, cle_privee, n)
        for j in range(len(resultats_requetes)):
            connexion.execute(f"INSERT INTO {tables[i]} VALUES {tuple(resultats_requetes[j])}")
print("Decryptage éffectuer.")
connexion.commit()
connexion.close()
    
