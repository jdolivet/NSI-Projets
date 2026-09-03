import pyxel as px
from random import randint
import sys

#====================INITIALISATION=================

px.init(256, 256, title="puzzle-odyssee")
px.load("musica_game_ulysse.pyxres")
px.playm(1, loop=True)
px.load("res.pyxres")
px.mouse(True)

#===============VARIABLES(globales)=================
with open("donnees.txt", 'r') as file:
    v = {
       "argent" : int(file.readline()),
       "points_de_vie" : int(file.readline()),
       "depl" : int(file.readline()),
       "localisation" : list(map(int, file.readline().split())),
       "case1" : int(file.readline()),
       "case2" : int(file.readline()),
       "case3" : int(file.readline()),
       "case4" : int(file.readline()),
       "case5" : int(file.readline()),
       "case6" : int(file.readline()),
       "case7" : int(file.readline()),
       "case8" : int(file.readline()),
       "case9" : int(file.readline()),
       "bateau_x" : int(file.readline()),
       "bateau_y" : int(file.readline()),
       "en_mer" : file.readline()=="True\n",
       "end_of_turn" : file.readline()=="True\n",
       "map1" : [[int(file.readline()) for _ in range(30)] for _ in range(30)],
       "nb_destination" : int(file.readline()),
       "liste_destin" : [list(map(int, file.readline().split())) for _ in range(3)],
        "phrases" : [],
        "reponse" : '',
        "persos" : ["John", "Alex", "Francois"],
        "touche" : False,
        "perso_choisi" : '',
        "correct" : 2,
        "direction" : ''
        }
        
#====================FONCTIONS======================
def retour_map():
    if px.btnp(px.KEY_Q):
        sys.exit(255)
  
    

def copier_tab_2d(tab : list) -> list:
    """Prend en argument un tableau supposé être de 2 dimensions avec 2 sous-éléments et renvoie une copie"""
    copie = [[0, 0] for _ in range(len(tab))]
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            copie[i][j] = tab[i][j]
    return copie

def attribuer_valeurs_knk() -> tuple[list, int, str]:
    """Fonction complètement faite pour le puzzle de knights and knaves (chevaliers et fripons) du jeu principal
    Ne prend aucun argument. Fonctionne avec la fonction vérificateur_knk.
    vvv FONCTIONNEMENT vvv
    Atribue aléatoirement des phrases à caractère booléan à des listes de personnages décidés comme menteurs ou pas aléatoirement.
    Teste s'il est possible de résoudre qui est en train de mentir et qui a le trésor.
    Renvoie le nombre de solutions, les phrases crées et le ersonnage avec la réponse"""
    adresses_persos = ["John", "Alex", "Francois"]
    fripons = []
    chevaliers =[]
    cibles = []
    qualifications = []
    adresse_reponse = adresses_persos[randint(0, 2)]
    binarite = ('la verite', 'le mensonge')
    forme_etre = ('est', "n'est pas")
    forme_garder = ('garde', "ne garde pas")
    phrases_verite = ("{cible} dit {binarite}", "{cible} {forme_etre} de mon type", "{cible} dit {binarite} et {cible} dit {binarite}", "soit {cible} dit {binarite} soit {cible} dit {binarite}", "{cible} dit {binarite} ou {cible} dit {binarite}")
    phrases_reponse = ("{cible} {forme_garder} la reponse","La reponse est avec celui qui dit {binarite}", "{cible} {forme_garder} la reponse et {cible} la {forme_garder}", "soit {cible} {forme_garder} la reponse soit {cible} la {forme_garder}", "{cible} {forme_garder} la reponse ou {cible} la {forme_garder}")
    phrases = []
    phrases_formees = []


    nb_fripons = randint(1, 2)
    
    for _ in range(nb_fripons):
        fripon = adresses_persos[randint(0, len(adresses_persos)- 1)]
        adresses_persos.remove(fripon)
        fripons.append(fripon)
        
    for perso in adresses_persos[:]:
        chevaliers.append(perso)
        
    adresses_persos = ["John", "Alex", "Francois"]
    
    nb_phrases_verite = randint(1, 2)
    
    for _ in range(nb_phrases_verite):
        perso_choisi = adresses_persos[randint(0, len(adresses_persos)- 1)]
        adresses_persos.remove(perso_choisi)
        phrases.append([phrases_verite[randint(0, len(phrases_verite)- 1)], perso_choisi])
        
    for _ in range(3 - nb_phrases_verite):
        perso_choisi = adresses_persos[randint(0, len(adresses_persos)- 1)]
        adresses_persos.remove(perso_choisi)
        phrases.append([phrases_reponse[randint(0, len(phrases_reponse)- 1)], perso_choisi])
            
    adresses_persos = ["John", "Alex", "Francois"]
    
    phrases_formees = copier_tab_2d(phrases)
    
    j = 0
    tmp = ''
    for perso in adresses_persos[:]:
        cible = adresses_persos[randint(0, len(adresses_persos)- 1)]
        adresses_persos.remove(cible)
        cibles.append([cible])
        for i in range(len(phrases)):
            if perso == phrases[i][1]:
                #Phrases sur qui dit la vérité =========================================================
                if (cible == perso) and (phrases[i][0] == phrases_verite[1]):
                    phrases[i][0] = phrases_verite[0]
                
                if phrases[i][0] in phrases_verite:
                    if ((perso in fripons) and (cible in fripons)) or ((perso in chevaliers) and (cible in chevaliers)):
                        tmp = binarite[0]
                    else:
                        tmp = binarite[1]
                
                phrases_formees[i][0] = phrases[i][0].replace('{binarite}', tmp, 1)
                
                #Celui-ci est un cas spécifique des phrases où binarité est utilisé pour donner la réponse
                if phrases[i][0] == phrases_reponse[1]:    
                    if ((perso in fripons) and (adresse_reponse in fripons)) or ((perso in chevaliers) and (adresse_reponse in chevaliers)):
                        tmp = binarite[0]
                    else:
                        tmp = binarite[1]
                        
                    phrases_formees[i][0] = phrases[i][0].replace('{binarite}', tmp, 1)
                
                #Phrases de localisation de la réponse ================================================
                if (phrases[i][0] in phrases_reponse) and (phrases[i][0] != phrases_reponse[1]):
                    if ((perso in fripons) and (adresse_reponse != cible)) or ((perso in chevaliers) and (adresse_reponse == cible)):
                        tmp = forme_garder[0]
                    else:
                        tmp = forme_garder[1]

                phrases_formees[i][0] = phrases_formees[i][0].replace('{forme_garder}', tmp, 1)    
                    
                #Phrase de même type ================================================================
                if phrases[i][0] == phrases_verite[1]:
                    if ((perso in fripons) and (cible in fripons)) or ((perso in chevaliers) and (cible in fripons)):
                        tmp = forme_etre[1]
                    elif ((perso in fripons) and (cible in chevaliers)) or ((perso in chevaliers) and (cible in chevaliers)):
                        tmp = forme_etre[0]
                        
                    phrases_formees[i][0] = phrases_formees[i][0].replace('{forme_etre}', tmp)
                
                # Attribue la cible et sauvegarde qualifications =====================================
                if (cible == perso):
                    cible = "je"
                phrases_formees[i][0] = phrases_formees[i][0].replace('{cible}', cible, 1)
                qualifications.append([tmp])
                
                #Phrases composées (plusieurs cibles et binarités) ====================================
                if (phrases[i][0] in phrases_verite[2:]) or (phrases[i][0] in phrases_reponse[2:]):
                    cible = adresses_persos[randint(0, len(adresses_persos)- 1)]
                    cibles[j].append(cible)
                    
                    #Phrases avec "et" ================================================================
                    if (phrases[i][0] == phrases_verite[2]):
                        #Phrases sur lequel dit la vérité ======================(et)===================
                        if (perso in chevaliers) and (cible in chevaliers):
                            tmp = binarite[0]
                        elif ((perso in chevaliers) and (cible in fripons)):
                            tmp = binarite[1]
                        else:
                            tmp = binarite[randint(0, 1)]
                            
                        phrases_formees[i][0] = phrases_formees[i][0].replace('{binarite}', tmp)
                          
                        #Phrases sur l'adresse de la réponse ===================(et)===================
                    elif (phrases[i][0] == phrases_reponse[2]):
                        if (perso in chevaliers) and (cible == adresse_reponse):
                            tmp = forme_garder[0]
                        elif (perso in chevaliers) and (cible != adresse_reponse):
                            tmp = forme_garder[1]
                        else:
                            tmp = forme_garder[randint(0, 1)]
                            
                        phrases_formees[i][0] = phrases_formees[i][0].replace('{forme_garder}', tmp)
                            
                    #Phrases avec "soit" ==============================================================        
                    elif (phrases[i][0] == phrases_verite[3]):
                        #Phrases sur lequel dit la vérité ===============(soit)====================
                        if ((cibles[j][0] in fripons) and (cibles[j][1] in chevaliers)) or ((cibles[j][0] in chevaliers) and (cibles[j][1] in chevaliers)):
                            tmp = binarite[1]
                        else:
                            tmp = binarite[0]
                            
                        phrases_formees[i][0] = phrases_formees[i][0].replace('{binarite}', tmp)
                            
                        #Phrases sur l'adresse de la réponse ============(soit)====================
                    elif (phrases[i][0] == phrases_reponse[3]):
                        if ((cibles[j][0] != adresse_reponse) and (cibles[j][1] == adresse_reponse)) or ((cibles[j][0] == adresse_reponse) and (cibles[j][1] == adresse_reponse)):
                            tmp = forme_garder[1]
                        else:
                            tmp = forme_garder[0]
                            
                        phrases_formees[i][0] = phrases_formees[i][0].replace('{forme_garder}', tmp)
                                                                
                    #Phrases avec "ou" ================================================================
                    elif (phrases[i][0] == phrases_verite[4]):
                        #Phrases sur lequel dit la vérité ======================(ou)===================
                        if (perso in fripons) and (cible in fripons):
                            tmp = binarite[0]
                        elif ((perso in fripons) and (cible in chevaliers)):
                            tmp = binarite[1]
                        else:
                            tmp = binarite[randint(0, 1)]
                        
                        phrases_formees[i][0] = phrases_formees[i][0].replace('{binarite}', tmp)
                     
                    elif (phrases[i][0] == phrases_reponse[4]):
                        #Phrases sur l'adresse de la réponse ===================(ou)===================
                        if (perso in fripons) and (cible != adresse_reponse):
                            tmp = forme_garder[0]
                        elif ((perso in fripons) and (cible == adresse_reponse)):
                            tmp = forme_garder[1]
                        else:
                            tmp = forme_garder[randint(0, 1)]
                        
                        phrases_formees[i][0] = phrases_formees[i][0].replace('{forme_garder}', tmp)
        
                    if (cible == perso):
                        cible = "je"
                    phrases_formees[i][0] = phrases_formees[i][0].replace('{cible}', cible, 1)
                    qualifications[j].append(tmp)
                    
                    
        adresses_persos = ["John", "Alex", "Francois"]
        j += 1
        
    phrases_copie: list = [[] for _ in range(3)]
    for i in range(len(phrases)):
        if phrases[i][1] == "John":
            phrases_copie[0] = phrases[i]
        if phrases[i][1] == "Alex":
            phrases_copie[1] = phrases[i]
        if phrases[i][1] == "Francois":
            phrases_copie[2] = phrases[i]
    phrases = phrases_copie[:]
        
    #SECONDE PARTIE (VÉRIFICATEUR DE RÉSOLUBILITÉ) ===========================================================
    
    
    solutions = 0
    concordances = 0
    alternative: list = [[], []] 
    #alternative[0] chevaliers hypothetiques / alternative[1] fripons hypnothetiques
    
    
    for l in range(2):
        for perso in adresses_persos[:]:
            alternative[l].append(perso)
            adresses_persos.remove(perso)
            alternative[(l + 1) % 2] = adresses_persos[:]
            adresses_persos = ["John", "Alex", "Francois"]
            
            for j in range(len(adresses_persos)):
                tresor = adresses_persos[j]
                
                for i in range(len(phrases)):
                    #Phrases "simples" ==========================================================================
                    if phrases[i][0] == phrases_verite[0]:
                        if ((cibles[i][0] in alternative[0]) and (qualifications[i][0] == binarite[1])) or ((cibles[i][0] in alternative[1]) and (qualifications[i][0] == binarite[0])):
                        #Si c'est le cas au dessus, l'affirmation est fausse, on va alors tester si son locuteur est un sale fripon ou pas
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                                
                    elif phrases[i][0] == phrases_reponse[0]:
                        if ((cibles[i][0] == tresor) and (qualifications[i][0] == forme_garder[1])) or ((cibles[i][0] != tresor) and (qualifications[i][0] == forme_garder[0])):
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                                
                    # Phrases "speciales" ========================================================================            
                    elif phrases[i][0] == phrases_verite[1]:
                        proposition1 = ((cibles[i][0] in alternative[0]) and (phrases[i][1] in alternative[0])) and qualifications[i][0] == forme_etre[0]
                        proposition2 = ((cibles[i][0] in alternative[1]) and (phrases[i][1] in alternative[0])) and qualifications[i][0] == forme_etre[1]
                        if proposition1 or proposition2:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                                
                    elif phrases[i][0] == phrases_reponse[1]:
                        if ((tresor in alternative[1]) and (qualifications[i][0] == binarite[0])) or ((tresor not in alternative[1]) and (qualifications[i][0] == binarite[1])):
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                                
                    # Phrases "et" ========================================================================            
                    elif phrases[i][0] == phrases_verite[2]:
                        proposition1 = ((cibles[i][0] in alternative[0]) and (qualifications[i][0] == binarite[0])) or ((cibles[i][0] in alternative[1]) and (qualifications[i][0] == binarite[1]))
                        proposition2 = ((cibles[i][1] in alternative[0]) and (qualifications[i][1] == binarite[0])) or ((cibles[i][1] in alternative[1]) and (qualifications[i][1] == binarite[1]))
                        
                        if proposition1 and proposition2:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                                
                    elif phrases[i][0] == phrases_reponse[2]:
                        proposition1 = ((cibles[i][0] == tresor) and (qualifications[i][0] == forme_garder[0])) or ((cibles[i][0] != tresor) and (qualifications[i][0] == forme_garder[1]))
                        proposition2 = ((cibles[i][1] == tresor) and (qualifications[i][1] == forme_garder[0])) or ((cibles[i][1] != tresor) and (qualifications[i][1] == forme_garder[1]))
                        
                        if proposition1 and proposition2:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                                
                    # Phrases "soit" ======================================================================
                    elif phrases[i][0] == phrases_verite[3]:
                        proposition1 = ((cibles[i][0] in alternative[0]) and (qualifications[i][0] == binarite[0])) or ((cibles[i][0] in alternative[1]) and (qualifications[i][0] == binarite[1]))
                        proposition2 = ((cibles[i][1] in alternative[0]) and (qualifications[i][1] == binarite[0])) or ((cibles[i][1] in alternative[1]) and (qualifications[i][1] == binarite[1]))
                        
                        if proposition1 != proposition2:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                                
                    elif phrases[i][0] == phrases_reponse[3]:
                        proposition1 = ((cibles[i][0] == tresor) and (qualifications[i][0] == forme_garder[0])) or ((cibles[i][0] != tresor) and (qualifications[i][0] == forme_garder[1]))
                        proposition2 = ((cibles[i][1] == tresor) and (qualifications[i][1] == forme_garder[0])) or ((cibles[i][1] != tresor) and (qualifications[i][1] == forme_garder[1]))
                        
                        if proposition1 != proposition2:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                    
                    #Phrases "ou" =======================================================================
                    elif phrases[i][0] == phrases_verite[4]:
                        proposition1 = ((cibles[i][0] in alternative[0]) and (qualifications[i][0] == binarite[0])) or ((cibles[i][0] in alternative[1]) and (qualifications[i][0] == binarite[1]))
                        proposition2 = ((cibles[i][1] in alternative[0]) and (qualifications[i][1] == binarite[0])) or ((cibles[i][1] in alternative[1]) and (qualifications[i][1] == binarite[1]))
                        
                        if proposition1 or proposition2:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                                
                    elif phrases[i][0] == phrases_reponse[4]:
                        proposition1 = ((cibles[i][0] == tresor) and (qualifications[i][0] == forme_garder[0])) or ((cibles[i][0] != tresor) and (qualifications[i][0] == forme_garder[1]))
                        proposition2 = ((cibles[i][1] == tresor) and (qualifications[i][1] == forme_garder[0])) or ((cibles[i][1] != tresor) and (qualifications[i][1] == forme_garder[1]))
                        
                        if proposition1 or proposition2:
                            if phrases[i][1] in alternative[0]:
                                concordances += 1
                        else:
                            if phrases[i][1] in alternative[1]:
                                concordances += 1
                            
                if concordances == 3:
                    solutions += 1
                concordances = 0
                
            alternative = [[], []]
            
        
    
    return phrases_formees, solutions, adresse_reponse
        
def verificateur_knk() -> tuple[list, str]:
    """Fonction complètement faite pour le puzzle de knights and knaves (chevaliers et fripons) du jeu principal
    Ne prend aucun argument. Fonctionne avec la fonction attribuer_valeurs_knk.
    vvv FONCTIONNEMENT vvv
    Teste si le nombre de solutions renvoié par attribuer_valeurs_knk est égal à 1 e reffet le procès jusqu'a le résultat est satisfaisant
    renvoie les phrases crées par la première fonction, et le personnage qui a la réponse"""
    phr, sol, rep = attribuer_valeurs_knk()
    while sol != 1:
        phr, sol, rep = attribuer_valeurs_knk()
    return phr, rep

v['phrases'], v['reponse'] = verificateur_knk()

#=====================UPDATE========================
def update():
    if px.btnp(px.MOUSE_BUTTON_LEFT) and not v['touche']:
        for i in range(3):
            if (px.mouse_x > (10 + i * 90)) and (px.mouse_x < (70 + i * 90)) and (px.mouse_y > 30) and (px.mouse_y < 158):
                v['touche'] = True
                v['perso_choisi'] = v['persos'][i]
                
    if (v['touche'] and px.btnp(px.MOUSE_BUTTON_LEFT)) and (v['correct'] == 2):
        if (px.mouse_x > 40) and (px.mouse_x < 126) and (px.mouse_y > 148) and (px.mouse_y < 192):
            if v['reponse'] == v['perso_choisi']:
                v['correct'] = 1
            else:
                v['correct'] = 0
        if (px.mouse_x > 130) and (px.mouse_x < 216) and (px.mouse_y > 148) and (px.mouse_y < 192):
            v['touche'] = False
    
    retour_map()
    
#=====================DRAW==========================    
def draw():
    px.cls(1)
    for i in range(3):
        px.rect(10 + i * 90, 30, 60, 128, [11, 9, 12][i])
        px.blt(20 + i * 95, 75, 0, 32*i, 0, 32, 32)
        
    for i in range(3):
        px.text(30 + i * 90, 20, str(v['persos'][i]), [11, 9, 12][i])
        
    for i in range(len(v['persos'])):
        h = 0
        x = 0
        l = 0
        for indice in v['phrases']:
            if v['persos'][i] == indice[1]:
                mots = indice[0].split()
                for j in range(len(mots)):
                    if (j > 0) and (j % 3 == 0):
                        x = 0
                        h += 10
                    if mots[j] == "je":
                        px.text(10 + x + (i * 87), 172 + h, str(mots[j]), [11, 9, 12][i])
                    elif mots[j] == "John":
                        px.text(10 + x + (i * 87), 172 + h, str(mots[j]), 11)
                    elif mots[j] == "Alex":
                        px.text(10 + x + (i * 87), 172 + h, str(mots[j]), 9)
                    elif mots[j] == "Francois":
                        px.text(10 + x + (i * 87), 172 + h, str(mots[j]), 12)
                    elif mots[j] == "verite":
                        px.text(10 + x + (i * 87), 172 + h, str(mots[j]), 3)
                    elif mots[j] == "mensonge":
                        px.text(10 + x + (i * 87), 172 + h, str(mots[j]), 8)
                    else:
                        px.text(10 + x + (i * 87), 172 + h, str(mots[j]), 7)
                    
                    x += (len(mots[j]) * 5) + 1
                    
                    
    px.text(10, 220, "Un de nous dit forcement la verite", 7)
    px.text(10, 230, "Un de nous dit forcement le mensonge", 7)
    px.text(10, 240, "Mais un seul de nous sait ou est vraiment la reponse", 7)
    px.text(10, 250, 'P.S. "ou" = ou inclusif', 7)
    
    if v['touche']:
        px.rect(32, 20, 192, 192, 0)
        px.rectb(32, 20, 192, 192, 7)
        for i in range(2):
            px.rect(40 + i * 90, 148, 86, 44, 0)
            px.rectb(40 + i * 90, 148, 86, 44, 7)
        px.text(45, 50, f"-etes vous surs que {v['perso_choisi']} a la reponse?", 7)
        px.text(35, 100, "Les apparences peuvent parfois etre trompeuses.", 7)
        px.text(128, 120, ";)", 7)
        px.text(80, 170, "OUI", 7)
        px.text(170, 170, "NON", 7)
        
    if v['correct'] == 1:
        if (v["liste_destin"][v["nb_destination"]][0]-v["localisation"][0])>0:
            direction1="a l'est"
        elif (v["liste_destin"][v["nb_destination"]][0]-v["localisation"][0])<0:
            direction1="a l'ouest"
        else:
            direction1='sur votre colonne'
        if (v["liste_destin"][v["nb_destination"]][1]-v["localisation"][1])>0:
            direction2='au sud '
        elif (v["liste_destin"][v["nb_destination"]][1]-v["localisation"][1])<0:
            direction2='au nord'
        else:
            direction2='sur votre ligne'
        px.cls(5)
        px.text(80, 104, "Bravo! vous avez reussi", 7)
        px.text(16, 128, "Vous devez maintenant atteindre la prochaine ile-drapeau,", 7)
        px.text(92, 148, f"qui est {direction1} et {direction2}.", 7)
        px.text(80, 168, 'Pressionez "q" pour quitter', 7)
    elif v['correct'] == 0:
        px.cls(2)
        px.text(92, 128, "Dommage! vous avez echoue!", 7)
        px.text(64, 168, 'Appuyez "q" pour quitter', 7)
    
        
    
        
#======================RUN==========================

px.run(update, draw)