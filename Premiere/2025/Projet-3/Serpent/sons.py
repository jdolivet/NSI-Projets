import numpy as np
import wave

def creer_son(nom_fichier, frequence, duree, volume=0.5, type_ondes="carree"):
    taux_echantillonnage = 44100
    t = np.linspace(0, duree, int(taux_echantillonnage * duree), False)

    if type_ondes == "carree":
        onde = np.sign(np.sin(2 * np.pi * frequence * t))
    elif type_ondes == "sinus":
        onde = np.sin(2 * np.pi * frequence * t)
    else:
        onde = np.sign(np.sin(2 * np.pi * frequence * t))  # forme par défaut

    audio = (onde * volume * 32767).astype(np.int16)
    with wave.open(nom_fichier, "w") as fichier:
        fichier.setnchannels(1)
        fichier.setsampwidth(2)
        fichier.setframerate(taux_echantillonnage)
        fichier.writeframes(audio.tobytes())

# Création des sons rétro simples
creer_son("manger.wav", frequence=880, duree=0.1)       # petit "blip"
creer_son("gameover.wav", frequence=220, duree=0.4)     # "bip" grave
creer_son("musique_fond.wav", frequence=440, duree=1.5) # ton moyen simple
