"""
Nous utilisons trois fonctions Python natives non vues en cours :

1 - isalpha():
    --vérifie si un caractère ou une chaîne ne contient que des lettres
2 - isupper():
    --vérifie si une lettre est en majuscule
3 - chr():
    --convertit un nombre en lettre correspondante
"""

def mod_inverse(a, m): #inverse de a modulo m
    for x in range(1, m):
        if a * x % m == 1 :
            return x
    return 'pas d\'inverse modulaire'

def affine_encrypt(text, a, b):
    encrypted_message = ''
    
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                reference_letter = ord('A')
            else :
                reference_letter = ord('a')
                
#le but de cette partie est de ramener la valeur unicode de la lettre à son indice dans l'alphabet, i.e., sa position
            x = ord(letter) - reference_letter
            y = (a * x + b) % 26 #en effet on travaille modulo 26 car on associe à chaque x \in Z/26Z une lettre, i.e., il y a 26 lettres dans l'alphabet
            encrypted_message += chr(y + reference_letter)
        else:
            encrypted_message += letter #si un élément de la chaîne n'est pas une lettre, i.e. une espace, une virgule, etc., il reste inchangé
    return encrypted_message

def affine_decrypt(text, a, b):
    decrypted_message = ''
    inverse_of_a = mod_inverse(a, 26)
    
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                reference_letter = ord('A')
            else :
                reference_letter = ord('a')
            y = ord(letter) - reference_letter
            x = (inverse_of_a * (y - b)) % 26
            decrypted_message += chr(x + reference_letter)
        else:
            decrypted_message += letter
    return decrypted_message
