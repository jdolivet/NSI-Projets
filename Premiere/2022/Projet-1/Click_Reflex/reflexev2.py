import tkinter as tk
import random
import time
import keyboard

print("choisissez la difficulté: 1, 2, 3")
diff = input("entrez la difficulté ")

perf_ordi = 0

if diff =="1":
    perf_ordi = random.uniform(3, 4)
if diff =="2":
    perf_ordi = random.uniform(2.8, 3.5)
if diff =="3":
    perf_ordi = random.uniform(1.7, 2.5)
    
    
#on initie les variables dont nous aurons besoin plus tard
temps_initial = random.randint(1, 5) # ici, le temps que mettra la fenetre pour apparaitre est aléatoire, pour que le jeu soit imprévisible et dépende vraiment des réflexes
debut = time.perf_counter()

fenetre = tk.Tk() #on crée une fenetre
fenetre.title("Jeu de relexe") #le nom de la fenetre est: "Jeu de reflexe"
fenetre.geometry("800x400") #la dimmension de la fenetree est de 800 de pixels de long sur 400 pixels de large
fenetre.configure(bg = 'green') #l'arriere plan de la fenetre sera vert


regles = tk.Label(fenetre, text = "une fois l'ecran vert veuillez appuyer sur le bouton",font=("sans-serif", 10), bg = 'green')
regles.pack() #on inidque les regles du jeu a l'utilisateur



#while True:
    
#    try:  
#         if keyboard.is_pressed('s'):  
#             fin = time.perf_counter()
#             if fin > temps_initial: 
#                 score = fin - temps_initial
#                 print("vous avez un temps de réaction de ", score, "secondes")
#             else:
#                 print("attendez la fenetre verte") 
#                 break  
#         apparition()
#         fenetre.mainloop()
#cette boucle ne marchait pas car python ne détectait pas que nous avions appuyé sur une touche une fois la fenetre ouverte


score1 = [0] # on crée ce tableau pour sauvegarder la variable de score qui est crée dans la fonciton

def temps():
    fin = time.perf_counter()
    score = fin - temps_initial - 6 #le 6 correspond au temps que met l'ordinateur à calculer et afficher, et au temps de saisie de la difficulté qui nuisent à la précision
    for i in range(1):
        score1[i] = score
    print("vous avez un temps de réaction de",score,"secondes")
    
    return fin


bouton = tk.Button(fenetre, height= 40, width=80, bg = 'green', command = temps) #ce bouton apelle la fonction temps qui arrete le chrono et calcule le temps de réaction
bouton.pack()


time.sleep(temps_initial) #on attends un nombre de secondes entier compris entre 1 et 5
fenetre.mainloop() #on affiche la fenetre

print(perf_ordi)
if perf_ordi > score1[0]:
    print("Vous avez gagné")
else:
    print("Vous avez perdu")

# Veuillez ne pas mettre votre IDE en plein écran car la fenetre cliquable apparaitra en arriere plan
# il faut fermer la fenetre tkinter pour que le score de l´ordinateur soit affiche