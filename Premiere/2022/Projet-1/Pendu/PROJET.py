import random

tab1 = ["concatenation", "python", "ascii", "fonction", "procedure", "variable", "nsi", "dolivet", "thonny", "encodage"]
tab2 = ["repertoire", "script", "binaire", "turtle", "random", "randint", "unicode", "programme", "range", "while", "break"]
tab3 = ["ordinateur", "ubuntu", "windows", "linux", "terminal", "console", "assistant"]
tab_max = tab1 + tab2+ tab3 #cela pourrait etre fait dans un seul tableau mais on decide de ne pas avoir une ligne trop grande

def table_de_mots(i):
    return tab_max[i] #fonction pour pouvoir utiliser le randint
    

mot_secret = table_de_mots(random.randint(0, len(tab_max)-1)) #aleatoirite du mot_secret avec le module random dans le tableau tab_max
tab_mot_secret = [0] * len(mot_secret)
for i in range(len(mot_secret)):
    tab_mot_secret[i] = mot_secret[i] #on cree un tableau avec le mot secret pour une plus facile manipulation
    
decouvert = ["_ "] * len(mot_secret)

erreurs = 0 #variable qui compte les erreurs
max_erreurs = 8 #variable pour changer les erreurs maximales
repetitions_lettres = 0 #variable pour voir si une erreur est comise
tests_rates = "" #variable qui garde les erreurs

print("Les mots secrets ont un lien avec le cours de NSI, bonne chance! ")

while decouvert != tab_mot_secret: #on compare le tableau vide avec le tableau du mot, si les deux sont egaux le jeu se finit
    
    decouvert_2 = ""
    for i in range(len(decouvert)):
        decouvert_2 = decouvert_2 + decouvert[i] #on concatene les lettres decouvertes pour un meilleur affichage
    print(decouvert_2)
    print()
    print(f"Vous avez {max_erreurs-erreurs} tentatives")
    print(f"Tentatives: {tests_rates}")
    print()
    
    repetitions_lettres = 0 #on reinitie cette variable toujours quand il y a un nouveau essai
    validite_test = 0 #variable pour voir si une erreur est comise
    
    essai = input("Tenter une lettre: ")
    print()
    for i in range(len(mot_secret)):
        if essai == mot_secret: #test pour savoir si le essai est le mot_secret en entier
            decouvert = tab_mot_secret #cette ligne fait le jeu se terminer car on sort de la condition du while
            repetitions_lettres += -1 #cette ligne enleve un a la variable car le joueur a eu la bonne reponse
            validite_test = 1
        if essai == mot_secret[i]: #test pour savoir si la lettre est dans le mot_secret
            decouvert[i] = essai
            repetitions_lettres += -1
            validite_test = 1
        repetitions_lettres += 1 #cette ligne est pour savoir si le joueur rate
    
    
    if repetitions_lettres == len(mot_secret): #ici c'est quand le joueur rate car la variable 
        erreurs += 1
    if erreurs == max_erreurs: #ici le joueur perd et le jeu ce fini
        decouvert = tab_mot_secret
        
    if validite_test == 0:
        tests_rates = tests_rates + essai + ", " #ici on concatene les erreurs
    
    for i in range(4): #espace vide pour un meilleur affichage apres un input
        print()
                
if erreurs == max_erreurs: #affichage quand on perd
    print(f"Vous êtes morts, {max_erreurs-erreurs} erreurs vous ont restés")
else: #affichage quand on gagne et avec les tentatives qui restent
    print(f"Vous avez réussi avec {max_erreurs-erreurs} erreurs qui restent. Bravo!") 
print(f"Le mot était: {mot_secret}") 
        
    