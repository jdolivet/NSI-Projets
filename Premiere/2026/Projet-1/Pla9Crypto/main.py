"""
main app: orchestre les différents modes de chiffrement.
"""

from affine_cypher import affine_encrypt, affine_decrypt
from xorencrypt import encrypt
from chiffrementcharles import *

def affine_cypher() -> None:
    choix = int(input(
        "Chiffrement affine :\n"
        "  1 — Chiffrer\n"
        "  2 — Déchiffrer\n"
        "Votre choix : "
    ))

    if choix == 1:
        text = input("Texte à chiffrer : ")
        a = int(input("Clé a : "))
        b = int(input("Clé b : "))

        print(affine_encrypt(text, a, b))

    elif choix == 2:
        text = input("Texte à déchiffrer : ")
        a = int(input("Clé a : "))
        b = int(input("Clé b : "))
        
        print(affine_decrypt(text, a, b))
    else:
        print("Option invalide.")

def xor_cypher() -> None:
    choix = int(input(
        "Chiffrement XOR :\n"
        "  1 — Chiffrer\n"
        "  2 — Déchiffrer\n"
        "Votre choix : "
    ))

    if choix == 1:
        text = input("Texte à chiffrer : ")
        a = int(input("Clé a : "))
        print(encrypt(text, a))

    elif choix == 2:
        text = input("Texte à déchiffrer : ")
        a = int(input("Clé a : "))
        print(encrypt(text, a))

    else:
        print("Option invalide.")

def encryptcharles():
    choix = int(input(
        "Chiffrement Charles :\n"
        "  1 — Chiffrer\n"
        "  2 — Déchiffrer\n"
        "Votre choix : "
    ))

    if choix == 1:
        text = input("Texte à chiffrer : ")
        print(encryptC(text))

    elif choix == 2:
        text = input("Texte à déchiffrer : ")
        print(decodeC(text))

    else:
        print("Option invalide.")

def main() -> None:
    option = int(input(
        "\nCRIPTO NSI — Choisissez le mode de chiffrement :\n"
        "  1 — XOR Encryption\n"
        "  2 — Chiffrement affine\n"
        "  3 — Chiffrement de César\n"
        "Votre choix : "
    ))

    match option:
        case 2:
            affine_cypher()
        case 1:
            xor_cypher()
        case 3:
            encryptcharles()
        case _:
            print("Option invalide.")

main()
