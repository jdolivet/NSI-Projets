import random 

#Liste des questions
quiz = [
    {"question": "Un pays asiatique avec un cercle rouge sur fond blanc.",
     "options": ["Japon", "Chine", "Corée du Sud", "Vietnam"],
     "reponse": "Japon",
     "niveau": "facile"},

    {"question": "Ce pays a des étoiles et des rayures.",
     "options": ["Canada", "États-Unis", "Mexique", "Brésil"],
     "reponse": "États-Unis",
     "niveau": "facile"},

    {"question": "Drapeau vert avec un losange jaune.",
     "options": ["Brésil", "Argentine", "Chili", "Pérou"],
     "reponse": "Brésil",
     "niveau": "facile"},
    
    {"question": "Drapeau avec une feuille d'érable rouge.",
     "options": ["Canada", "États-Unis", "Australie", "Nouvelle-Zélande"],
     "reponse": "Canada",
     "niveau": "facile"},
    
    {"question": "Drapeau bleu et blanc avec un soleil.",
     "options": ["Argentine", "Uruguay", "Paraguay", "Chili"],
     "reponse": "Argentine",
     "niveau": "moyen"},

    {"question": "Croix blanche sur fond rouge.",
     "options": ["Suisse", "Danemark", "Autriche", "Pologne"],
     "reponse": "Suisse",
     "niveau": "moyen"},

    {"question": "Trois couleurs noir, rouge et jaune à l'horizontale.",
     "options": ["Allemagne", "Belgique", "Espagne", "Italie"],
     "reponse": "Allemagne",
     "niveau": "moyen"},
    
    {"question": "Drapeau rouge avec une étoile jaune.",
     "options": ["Chine", "Vietnam", "Turquie", "Maroc"],
     "reponse": "Vietnam",
     "niveau": "moyen"},

    {"question": "Drapeau avec un dragon rouge.",
     "options": ["Pays de Galles", "Bhoutan", "Chine", "Mongolie"],
     "reponse": "Pays de Galles",
     "niveau": "difficile"},

    {"question": "Drapeau vert avec triangle jaune et étoile rouge.",
     "options": ["Guyana", "Suriname", "Ghana", "Mali"],
     "reponse": "Guyana",
     "niveau": "difficile"},
    
    {"question": "Drapeau possèdent les couleurs rouge, bleu, blanc, à l'horizontal.",
     "options": ["Indonésie", "Portugal", "Butan", "Thailand"],
     "reponse": "Thailand",
     "niveau": "difficile"},
    
    {"question": "Drapeau possèdent deux couleurs, rouge et blanc avec un cercle .",
     "options": ["Indonésie", "Pologne", "Groenland", "Autriche"],
     "reponse": "Groenland",
     "niveau": "difficile"}] 



random.shuffle(quiz)  #Les questions sont aléatoires
quiz = quiz[:6]   #Nombre de questions 

score = 0             

print("QUIZ DES PAYS!")

#Boucle principale
for question_actuelle in quiz:

    print(f"Niveau :",question_actuelle["niveau"])  #afficher le niveau
    print(question_actuelle["question"])            #afficher la question

    lettres = ["A", "B", "C", "D"]  #lettres à choisir

    options = question_actuelle["options"].copy()  #copier les options
    random.shuffle(options)                        #mélanger les options

    #afficher les options
    for i in range(4):
        print(lettres[i] + ")", options[i])

    #lire la réponse de l'utilisateur
    choix = input("Choisissez entre (A, B, C, D): ").upper().strip() #Choisir les options 

#vérification
    if choix == "A" or choix == "B" or choix == "C" or choix == "D":

        #transformer la lettre en réponse réelle
        reponse_choisie = options[lettres.index(choix)]

        #vérifier si c'est correct
        if reponse_choisie == question_actuelle["reponse"]:
            print("Correct !")

            #ajouter des points selon le niveau
            if question_actuelle["niveau"] == "facile":
                score += 1
            elif question_actuelle["niveau"] == "moyen":
                score += 2
            else:
                score += 3

            print()
        else:
            print("Faux ! Réponse :", question_actuelle["reponse"], "\n")
    
    else:
        print("Entrée invalide !\n")


#Score Final
print("Score final :", score)

if score >= 9:
    print("Excellent !")
elif score >= 5:
    print("Bien joué !")
else:
    print("À améliorer !")