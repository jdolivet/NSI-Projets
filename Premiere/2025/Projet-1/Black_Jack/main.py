from random import randint

def carta():
    return randint(1, 11)

def jogador():
    cartas = [carta(), carta()]
    total = sum(cartas)
    
    print(f"Tu as tiré: {cartas} (total = {total})")
    
    while total < 21:
        r = input("Prendre plus une carte? (oui/non): ")
        if r == "oui" or r == "Oui" or r == "OUI":
            nova = carta()
            cartes_nouvelle = [nova]
            cartas = cartas + cartes_nouvelle
            total += nova
            print(f"Tu as tiré: {nova}. Tes cartes: {cartas} (total = {total})")
        else:
            break
    return total, cartas

def robo():
    cartas = [carta(), carta()]
    total = sum(cartas)
    
    while total < 15:
        nova = carta()
        cartes_nouvelle = [nova]
        cartas = cartas + cartes_nouvelle
        total += nova
    return total, cartas

def resultat(pontos_jogador, cartas_jogador, pontos_robo, cartas_robo):
    print("\n=== Résultat final ===")
    print(f"Tes cartes: {cartas_jogador} (total = {pontos_jogador})")
    print(f"Cartes du robot: {cartas_robo} (total = {pontos_robo})")
    
    if pontos_jogador > 21:
        print("Tu as perdu, tu as dépassé 21.")
    elif pontos_robo > 21:
        print("Tu as gagné! Le robot a dépassé 21.")
    elif pontos_robo > pontos_jogador:
        print("Tu as perdu. Le robot a eu un meilleur score.")
    elif pontos_jogador > pontos_robo:
        print("Tu as gagné! Ton score est meilleur.")
    else:
        print("Match nul.")

# Início do jogo
print("=== Blackjack ===")
pontos_jogador, cartas_jogador = jogador()
pontos_robo, cartas_robo = robo()
resultat(pontos_jogador, cartas_jogador, pontos_robo, cartas_robo)

#Credits:
#Lucas Arias et André Sequeira