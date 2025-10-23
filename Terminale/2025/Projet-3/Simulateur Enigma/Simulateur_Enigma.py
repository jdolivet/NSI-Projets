import tkinter as tk
import string

# ---------------------------
# Initialisation
# ---------------------------

alphabet = string.ascii_uppercase

rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotors = [rotor1, rotor2, rotor3]
positions = [0, 0, 0]

reflecteur = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# ---------------------------
# Fonction de chiffrement
# ---------------------------

def enigma(message):
    global positions
    message = message.upper().replace(" ", "")
    resultat = ""

    for lettre in message:
        if lettre not in alphabet:
            resultat += lettre
            continue

        code = ord(lettre) - ord('A')
        for i, rotor in enumerate(rotors):
            pos = (code + positions[i]) % 26
            code = (ord(rotor[pos]) - ord('A') - positions[i]) % 26

        code = ord(reflecteur[code]) - ord('A')

        for i, rotor in reversed(list(enumerate(rotors))):
            index = rotor.find(chr((code + positions[i]) % 26 + ord('A')))
            code = (index - positions[i]) % 26

        resultat += chr(code + ord('A'))

        # Avancer les rotors
        positions[0] = (positions[0] + 1) % 26
        if positions[0] == 0:
            positions[1] = (positions[1] + 1) % 26
            if positions[1] == 0:
                positions[2] = (positions[2] + 1) % 26

    return resultat

# ---------------------------
# Interface Tkinter
# ---------------------------

def chiffrer_message():
    global positions
    positions = [0,0,0]  # Reset positions
    message = entry.get()
    code = enigma(message)
    result_label.config(text=f"Message chiffré : {code}")

# Fenêtre principale
root = tk.Tk()
root.title("Simulateur Enigma")
root.geometry("600x300")

# Butons et messages
tk.Label(root, text="Entrez le message :", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(root, width=50, font=("Arial", 14))
entry.pack(pady=10)

tk.Button(root, text="Chiffrer", font=("Arial", 14), command=chiffrer_message).pack(pady=15)
result_label = tk.Label(root, text="Message chiffré : ", font=("Arial", 14))
result_label.pack(pady=10)

# Lancer l'application
root.mainloop()

