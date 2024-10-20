from time import sleep
from random import shuffle, choice, randint
from Player import Player
from Labyrinth import Labyrinth, Room, shapePreset

running = True

# Donnée globale, dont les paramétres de base sont facilement changés.
size_preset = {'1': 5, '2': 10, '3': 20, '4': 50}

# Donne l'effet de Digitation au texte
def typewriter(string):
    for c in string:
        print(c, end="")
        sleep(0.005)
    print("")

def placeholder():
    pass

# Une donnée negative convient à donner du gold
def steal(name, amount):
    hasChoice = choice([True, False])
    if hasChoice:
        typewriter('Choose a person:')
        options = {}
        counter = 0
        for i in range(len(playerNames)):
            if name != playerNames[i]:
                counter += 1
                typewriter(f'[{counter}] {playerNames[i]}')
                options[f'{counter}'] = playerNames[i]
        answer = input('> ')
        try:
            assert int(answer) <= len(playerNames)
            victimName = options[answer]
        except:
            typewriter('Invalid Answer\n')
            steal(name, amount)
    else:
        victimName = choice(playerNames)
        while victimName == name:
            victimName = choice(playerNames)
    player_list[name].gain(amount)
    player_list[victimName].gain(-amount)

# le paramètre name ici est seulement présent car tous les autres evenements ont ce paramètre, et ont besoin de lui pour l'utiliser.
def emptyRoom(name):
    typewriter('Nothing Happens!')
    input('<Press ENTER to continue>')
    typewriter('')

# Choix des evenements possibles d'une salle Good
def goodWheel(name):
    # Gain 3 gold, Gain 5 gold, Double gold, Steal 3 gold, Free Item, Move Again, Bad Wheel 
    goodOptions = [lambda: player_list[name].gain(3),
                   lambda: player_list[name].gain(5),
                   lambda: player_list[name].multiplyGold(2),
                   lambda: steal(name, 3),
                   lambda: player_list[name].acquire(choice(list(itemList.keys()))),
                   lambda: playerMove(name),
                   lambda: badWheel(name)
                  ]
    typewriter('Something good is happenning...')
    input('<Press ENTER to continue>')
    typewriter('')
    idx = randint(0, len(goodOptions)-1)
    goodOptions[idx]()
    flavorText = [f'{name} found 3 gold. {name} now has {player_list[name].showGold()}.',
                  f'{name} found 5 gold. {name} now has {player_list[name].showGold()}.',
                  f"{name}'s gold was magically DOUBLED! {name} now has {player_list[name].showGold()}!",
                  f"{name} 'found' 3 gold. {name} now has {player_list[name].showGold()}. Someone's wallet feels lighter.",
                  f"{name} has gained a new item! {name}'s backpack now has: {player_list[name].showPack()}.",
                  f'{name} has a sudden burst of energy!',
                  f"{name}'s fortune turned bad."
                 ]
    typewriter(flavorText[idx])
    input('<Press ENTER to continue>')
    typewriter('')

# Change la position du joueur aléatoirement. Il est possible qu'il revienne au même endroit, mais improbable.
def teleport(name):
    playerPositions[name] = choice(board.rooms)
    typewriter(f'{name} was teleported to a {playerPositions[name].roomType} room.')
    if duplicate(playerPositions, name) != []:
        for name2 in duplicate(playerPositions, name):
            typewriter(f'{name2} is in this room.')
        input('<Press ENTER to continue>')
        typewriter('')
        if name == hunterName:
            for player in duplicate(playerPositions, name):
                catchPlayer(player)
        elif hunterName in duplicate(playerPositions, name):
            catchPlayer(name)
            return None
    # Garantit qu'il reste au moins 2 joueurs pour un evenement quelconque.
    if not isJover:
        for i in range(len(trapPositions.keys())):
            if list(trapPositions.values())[i] == playerPositions[name]:
                typewriter(f"Bear Trap> {list(trapPositions.keys())[i]}! I got 'em! I got 'em!")
                goldAmount = randint(1, player_list[name].gold)
                player_list[name].gain(-goldAmount)
                typewriter(f"{name} lost {goldAmount} to {list(trapPositions.keys())[i]}'s Bear Trap. {name} now has {player_list[name].showGold()}")
                typewriter("Bear Trap> Ma work 'ere s'done.")
        playerEvent[playerPositions[name].roomType](name)

# Fonctionne aussitôt comme 2 evenements Bad ou 1 evenement Bad à 2 joueurs. Peut être chaîné.
def doubleBadWheel(name1, isDouble):
    if isDouble:
        typewriter(f'Something bad will happen one more time to {name1}...')
        badWheel(name1)
        badWheel(name1)
    else:
        name2 = choice(playerNames)
        while name2 == name1:
            choice(playerNames)
        typewriter(f'Something bad will also happen to {name2}')
        badWheel(name1)
        badWheel(name2)

# Choix des evenements Bad. Recycle beaucoup de mécaniques.
def badWheel(name):
    # Give 3 gold, Give 5 gold, Teleport, Board Shift, Suffer Together, Suffer Twice 
    badOptions = [lambda: steal(name, -3),
                  lambda: steal(name, -5),
                  lambda: teleport(name),
                  placeholder, # Difficile il est difficile à voir qu'elle n'existe pas vraiment car il est difficile de voir la totalité de la carte.
                  lambda: doubleBadWheel(name, False),
                  lambda: doubleBadWheel(name, True),
                 ]
    typewriter('Something bad is happenning...')
    input('<Press ENTER to continue>')
    typewriter('')
    idx = randint(0, len(badOptions)-1)
    badOptions[idx]()
    flavorText = [f"{name} lost 3 gold. {name} now has {player_list[name].showGold()}. Someone's wallet feels heavier",
                  f"{name} lost 5 gold. {name} now has {player_list[name].showGold()}. Someone's wallet feels heavier",
                  f"{name}'s map is useless now.",
                  f"The mansion trembles and creaks. Something has changed.",
                  f"{name} drags someone along the misfortune.",
                  f'{name} is hated by fate.'
                 ]
    typewriter(flavorText[idx])
    input('<Press ENTER to continue>')
    typewriter('')

# Événnement Shop, seule manière de retirer du gold de l'économie globale.
# Les prix se balancent tout seuls (les items populaires deviennent vite les plus chers).
def shop(name):
    typewriter(f'{name} finds a vending machine in the room.')
    typewriter('Vending Machine> Hello [HELLO!!] prized customer! It is I, Vending Machine! [VENDING MACHINE?!]')
    typewriter('Vending Machine> Would you like to buy? [BUY!!]')
    typewriter('[1] Yes!')
    typewriter('[2] Absolutely!')
    typewriter('[3] For sure!')
    typewriter('[4] Yes please!')
    typewriter('[5] No')
    answer = input('> ')
    typewriter('')
    if answer == '5':
        typewriter('Vending Machine> Disappointing. [DISAPPOINTING?!] Disappointing!')
    else:
        if answer not in '1234':
            typewriter('Vending Machine> I will take that as a yes! [INVALID ANSWER?!]')
        doneShopping = False
        while not doneShopping:
            answered = False
            while not answered:
                options = {}
                typewriter('Vending Machine> Check out [CHECK IT OUT!!] my stock:')
                for i in range(len(list(itemList.keys()))):
                    typewriter(f'[{i+1}] {list(itemList.keys())[i]} - {itemList[list(itemList.keys())[i]]} gold ({randint(1, 100)}% off [100% NOT A LIE!!])')
                    options[i+1] = list(itemList.keys())[i]
                typewriter(f'[{len(list(itemList.keys()))+1}] Nevermind')
                answer = input('> ')
                try:
                    answer = int(answer)
                    assert answer <= len(list(itemList.keys()))+1 and answer > 0
                    answered = True
                except:
                    typewriter(f'Vending Machine> Item n{answer}[INVALID ANSWER!!] is not on the menu!!!\n')
            if answer == len(list(itemList.keys()))+1:
                typewriter('Vending Machine> Disappointing! [VERY!!]')
                doneShopping = True
            else:
                if player_list[name].gold >= itemList[options[answer]]:
                    player_list[name].acquire(options[answer])
                    player_list[name].gain(-itemList[options[answer]])
                    typewriter('Vending Machine> Gr-Gre-[GREAT CHOICE!!]!')
                    typewriter(f'{name} has bought {options[answer]} for {itemList[options[answer]]} gold, {name} now has {player_list[name].showGold()}\n')
                    purchased[options[answer]] += 1
                    if purchased[options[answer]] >= len(player_list) // 2:
                        typewriter('Vending Machine> HAHAHA! Business is booming! Time to increase the market price! [SUCKERS!!]')
                        itemList[options[answer]] += 1
                        purchased[options[answer]] = 0
                else:
                    typewriter(f"Vending Machine> Sorry {name}, but I don't do credit (unlike a certain gambling addict~).\nVending Machine> Just come back when you're a little richer. [NO GOLD?!]")
                typewriter(f'Vending Machine> Still got any gold? [BUY MORE!!]')
                typewriter('[1] Yes!')
                typewriter('[2] Absolutely!')
                typewriter('[3] For sure!')
                typewriter('[4] Yes please!')
                typewriter('[5] No')
                answer = input('> ')
                typewriter('')
                if answer == '5':
                    typewriter('Vending Machine> Tsk. Come back with more gold next time! [AND AFTER THAT!!]')
                    doneShopping = True
                elif answer not in '1234':
                    typewriter('Vending Machine> Translating Invalid Answer.... "Take all my gold machine overlord."')
                    typewriter('Vending Machine> I will for sure! [GIMME GOLD!!]')

# Evenement Gamble, mesure de secours pour un joueur qui perd. Facile à s'en débarasser des dettes (si on essaye pas de faire le malin).
def gamble(name):
    typewriter(f'{name} finds a Slot Machine in this room.')
    typewriter(f"Slot Machine> Greetings {name}. Did you know that you miss 100% of the shots you don't take?")
    answered = False
    if player_list[name].gold == 0:
        typewriter("Slot Machine> Oh. You don't have gold do you? Then...")
        input("<Press Enter to continue>")
        typewriter("\nSlot Machine> GET YOUR BROKE [CHA-CHING!] out of here!!!")
    else:
        while not answered:
            typewriter(f'Slot Machine> Would you like to gamble? You currently have {player_list[name].showGold()}.')
            typewriter('[1] Yes')
            typewriter("[2] I'm a scared little baby")
            answer = input('> ')
            typewriter('')
            if answer == '1':
                typewriter("Slot Machine> I knew I could count on you!")
                while not answered:
                    typewriter("Slot Machine> How much gold are you gambling? I only have energy for 1 spin!")
                    goldAmount = input("> ")
                    try:
                        goldAmount = int(goldAmount)
                        if goldAmount > 0:
                            assert player_list[name].gold >= goldAmount
                            answered = True
                        elif goldAmount < 0:
                            assert player_list[name].gold <= goldAmount
                            typewriter("Slot Machine> Trying to gamble away your debt huh. I'll take it. Only a fool would not see the opportunity!")
                            answered = True
                        elif goldAmount == 0:
                            typewriter("What's the fun in gambling if there are no stakes?")
                            typewriter("C'mon for real this time!")
                        else:
                            typewriter("Slot Machine> Do you take me for a fool?! You don't have enough!")
                            typewriter("Slot Machine> C'mon for real this time!")
                    except:
                        typewriter("Slot Machine> That's not how it works around here.")
                answered = False
                while not answered:
                    typewriter("Slot Machine> All that's left is for you to pick your color!!!")
                    typewriter("[1] Yellow - x10 (8% Chance)")
                    typewriter("[2] Red - x2 (46% Chance)")
                    typewriter("[3] Black - x2 (46% Chance)")
                    answer = input('> ')
                    if answer in '123':
                        answered = True
                    else:
                        typewriter("Slot Machine> Don't try to get smart here. C'mon there are only 3 colors to choose from.")
                typewriter("\nSlot Machine> Alright! Let's get it spinning!")
                input('<Press ENTER to continue>')
                typewriter("\nSlot Machine> What do you mean I'm not supposed to work like a roulette. How rude!")
                typewriter('Slot Machine> What matters in gambling is the thrill of the game, not the form!')
                input('<Press ENTER to continue>')
                typewriter("\nSlot Machine> HO HO! IT'S COMING! I CAN FEEL IT! IT'S...")
                input('<Press ENTER to continue>')
                typewriter('')
                result = randint(1, 100)
                if goldAmount > 0:
                    if result <= 8:
                        if answer == '1':
                            typewriter(f'Slot Machine> Oh no. YELLOW?! JACKPOT?! You lucky [CHA-CHING]!! Your {goldAmount} gold was increased by 10 times!!')
                            player_list[name].gain(goldAmount*10)
                            typewriter(f'{name} now has {player_list[name].showGold()}')
                        else:
                            typewriter(f'Slot Machine> Oh no~ It was Yellow! You missed a jackpot! Better luck next time!')
                            player_list[name].gain(-goldAmount)
                            typewriter(f'{name} now has {player_list[name].showGold()}')
                    else:
                        result = choice(['2', '3'])
                        if answer == result:
                            typewriter(f'Slot Machine> You win! Congratulations! Your {goldAmount} gold was doubled!')
                            player_list[name].gain(goldAmount*2)
                            typewriter(f'{name} now has {player_list[name].showGold()}')
                        else:
                            typewriter(f'Slot Machine> Oh no~ You lost. You lost {goldAmount} gold. Better luck next time.')
                            player_list[name].gain(-goldAmount)
                            typewriter(f'{name} now has {player_list[name].showGold()}')
                elif goldAmount < 0:
                    if answer == '1':
                        if result <= 50:
                            typewriter(f'Slot Machine> YELLOW! JACKPOT! YOUR {-goldAmount} DEBT WAS INCREASED BY 10 TIMES!!!')
                            player_list[name].gain(goldAmount*10)
                            typewriter(f'{name} now has {player_list[name].showGold()}')
                        else:
                            typewriter(f"Slot Machine> Tsk. It was {choice(['Red', 'Black'])}. You lose {-goldAmount} debt.")
                            player_list[name].gain(-goldAmount)
                            typewriter(f'{name} now has {player_list[name].showGold()}')
                    else:
                        if result <= 50:
                            typewriter(f"Slot Machine> {['YELLOW', 'RED', 'BLACK'][int(answer)]}! YOUR {-goldAmount} DEBT IS DOUBLED!")
                            player_list[name].multiplyGold(2)
                            typewriter(f'{name} now has {player_list[name].showGold()}')
                        else:
                            if answer == '2':
                                answer = 3
                            else:
                                answer = 2
                            typewriter(f"Slot Machine> Tsk. It was {['YELLOW', 'RED', 'BLACK'][answer]}. You lose {-goldAmount} debt.")
                            player_list[name].gain(-goldAmount)
                            typewriter(f'{name} now has {player_list[name].showGold()}.')
                input('<Press ENTER to continue>')
                typewriter('\nSlot Machine> Remember: 99% of gamblers quit before making it big! Come back again!')    
            elif answer == '2':
                typewriter("Slot Machine> This is a mistake! And the only real mistake is not learning from one's mistakes.")
                typewriter("Slot Machine> See you next time.")
                answered = True

# Evenement Gold, Sert à equilibrer. Donne un avantage au hunter, qui est beaucoup ciblé.
def goldSpace(name):
    typewriter(f'{name} finds an ATM Machine in the room.')
    if hunterName != name:
        typewriter(f'ATM Machine> Oh. Hi there little invader!')
        input('<Press ENTER to continue>')
        typewriter('')
        if player_list[name].gold <= 0:
            typewriter(f'ATM Machine> Oh you poor thing! What happened to you? If it was one of my Wretched Brothers they WILL pay for it.')
            typewriter(f"ATM Machine> Have a little something. Courtesy of my dear maker's bank account! I'm sure he won't miss this much!")
            goldAmount = randint(1, 10)
            player_list[name].gain(goldAmount)
            typewriter(f'{name} received {goldAmount} gold. {name} now has {player_list[name].showGold()}')
        elif player_list[name].gold >= 25:
            typewriter(f"ATM Machine> Oh my! Quite the hoarder aren't you? Did you beat my Brother at his own game?\nATM Machine> Ah, you remind me of Astorias in his early days.\nATM  Machine> Do you mind if add to your collection?")
            goldAmount = randint(1, 3)
            player_list[name].gain(goldAmount)
            typewriter(f'{name} received {goldAmount} gold. {name} now has {player_list[name].showGold()}')
        else:
            typewriter("ATM Machine> Have some gold, courtesy of my master's bank account! It'll be our little secret.")
            goldAmount = randint(1, 5)
            player_list[name].gain(goldAmount)
            typewriter(f'{name} received {goldAmount} gold. {name} now has {player_list[name].showGold()}')
    else:
        typewriter(f"ATM Machine> Oh. If it isn't our dear guardian! How are you doing, {name}?")
        if player_list[name].gold <= 0:
            typewriter(f"ATM Machine> Oh my! Those invaders really roughed you up! Or was it one of my brothers? I swear they don't know who they're working with.")
            typewriter(f"ATM Machine> Have this, courtesy of our master's bank account, and go get those invaders!")
            goldAmount = randint(1, 20)
            player_list[name].gain(goldAmount)
            typewriter(f'{name} received {goldAmount} gold. {name} now has {player_list[name].showGold()}')
        elif player_list[name].gold >= 50:
            typewriter(f"ATM Machine> Oh my! You've acquired quite the hoard! Taking after our master, huh? Well, mind if I pitch in?")
            goldAmount = randint(1, 5)
            player_list[name].gain(goldAmount)
            typewriter(f'{name} received {goldAmount} gold. {name} now has {player_list[name].showGold()}')
        else:
            typewriter(f"ATM Machine> You're struggling with those intruders, aren't you? Take this and go get them!")
            goldAmount = randint(1, 10)
            player_list[name].gain(goldAmount)
            typewriter(f'{name} received {goldAmount} gold. {name} now has {player_list[name].showGold()}')
    input('<Press ENTER to continue>')
    typewriter("")

# Les Invaders peuvent s'échaper mais pas le hunter.
def escape(name):
    typewriter(f'{name} is blinded by sunlight. After hours of roaming through the manor. {name} could have never seen it again.')
    if name != hunterName:
        typewriter(f'{name} escaped.')
        playerNames.remove(name)
    else:
        typewriter(f"As {name} stepped foward, {name} started to feel a sharp pain. It was Astoria's curse. {name} could not leave. {name} still had work to do.")
    input('<Press ENTER to continue>')
    typewriter('')

# les evenements sont tous des fonctions avec un seul paramètre 'name'.
playerEvent = {'Empty': emptyRoom, 
         'Good': goodWheel,
         'Bad': badWheel,
         'Shop': shop,
         'Gamble': gamble,
         'Gold': goldSpace,
         'Teleport': teleport,
         'Escape': escape
        }

# Selectione la taille du labyrinthe
def sizeSelect():
    typewriter('Select the size of the labyrinth:')
    typewriter('[1] Small')
    typewriter('[2] Medium')
    typewriter('[3] Big')
    typewriter('[4] Humongous')
    answer = input('> ')
    typewriter('')
    if answer not in size_preset.keys():
        typewriter('Invalid answer')
        typewriter('')
        return sizeSelect()
    else:
        return size_preset[answer]

# Crée le chasseur
def hunterSelect():
    typewriter("Select the Hunter's name:")
    name = input('> ')
    typewriter('')
    #typewriter(f'Is {name} a computer?')
    #typewriter('[1] Yes')
    #typewriter('[2] No')
    #answer = input('> ')
    #typewriter('')
    #if answer == '1':
    #    player_list[name] = Player(True)
    #elif answer == '2':
    #    player_list[name] = Player(False)
    #else:
    #    typewriter('Invalid Answer')
    #    typewriter('')
    #    hunterSelect()
    player_list[name] = Player(False)
    return name

# Crée les invaseurs
def playerSelect():
    answered = False
    while not answered:
        typewriter('Select the number of invaders:')
        try:
            playerNb = int(input('> '))
            typewriter('')
            assert playerNb > 0
            answered = True
        except:
            typewriter('Invalid Answer')
            typewriter('')
    for i in range(playerNb):
        answered = False
        while not answered:
            typewriter(f"Select Invader #{i+1}'s name:")
            name = input('> ')
            typewriter('')
            if name in player_list.keys():
                typewriter("Name already used.")
            else:
                answered = True
        #answered = False
        #while not answered:
        #    typewriter(f'Is {name} a Computer?')
        #    typewriter('[1] Yes')
        #    typewriter('[2] No')
        #    answer = input('> ')
        #    typewriter('')
        #    if answer == '1':
        #        answered = True
        #        player_list[name] = Player(True)
        #    elif answer == '2':
        #        answered = True
        #        player_list[name] = Player(False)
        #    else:
        #        typewriter('Invalid Answer')
        #        typewriter('')
        player_list[name] = Player(False)

# Renvoie toutes les clés de dict qui ont la même valeur que key1
def duplicate(dict: dict, key1):
    out = []
    for key, value in dict.items():
        if value == dict[key1] and key != key1:
            out.append(key)
    return out

# Posicione les joueurs et decide l'ordre des tours. = Fase de préparation
def openingRound(board):
    typewriter('Deciding turn order...\n')
    input('<Press ENTER to continue>')
    typewriter('')
    shuffle(playerNames)
    typewriter('The players are shuffled.\n')
    input('<Press ENTER to continue>')
    typewriter('')
    playerPositions[hunterName] = choice(board.rooms)
    for name in playerNames:
        if name != hunterName:
            playerPositions[name] = choice(board.rooms)
            while playerPositions[name].roomType == 'Escape' or playerPositions[name] == playerPositions[hunterName]:
                playerPositions[name] = choice(board.rooms)
        typewriter(f'{name} was sent to a {playerPositions[name].roomType} room.')
        if duplicate(playerPositions, name) != []:
            for name2 in duplicate(playerPositions, name):
                typewriter(f'{name2} is also in this room.')
        playerEvent[playerPositions[name].roomType](name)

# Mouvement du joueur.
def playerMove(name):
    typewriter(f'{name} is in a {playerPositions[name].shape} room. There are {shapePreset[playerPositions[name].shape]} doors.')
    answered = False
    while not answered:
        typewriter(f'Which door would you like to open?')
        options = {}
        for i in range(shapePreset[playerPositions[name].shape]):
            if playerPositions[name].doors[list(playerPositions[name].doors.keys())[i]] is None:
                typewriter(f'[{i+1}] The {list(playerPositions[name].doors.keys())[i]} door is locked from outside.')
            else:
                typewriter(f'[{i+1}] {list(playerPositions[name].doors.keys())[i]} door')  
                options[f'{i+1}'] = list(playerPositions[name].doors.keys())[i]
        answer = input('> ')
        typewriter('')
        if answer in options:
            answered = True
    playerPositions[name], exitedDoor = playerPositions[name].doors[options[answer]]
    typewriter(f"On the other side of the door is a {playerPositions[name].roomType} room. You've entered through the {exitedDoor} door.")
    if duplicate(playerPositions, name) != []:
        for name2 in duplicate(playerPositions, name):
            typewriter(f'{name2} is in this room.')
    for i in range(len(trapPositions.keys())):
        if list(trapPositions.values())[i] == playerPositions[name]:
            typewriter(f"Bear Trap> {list(trapPositions.keys())[i]}! I got 'em! I got 'em!")
            goldAmount = randint(1, player_list[name].gold)
            player_list[name].gain(-goldAmount)
            typewriter(f"{name} lost {goldAmount} to {list(trapPositions.keys())[i]}'s Bear Trap. {name} now has {player_list[name].showGold()}")
            typewriter("Bear Trap> Ma work 'ere s'done.")
    input('<Press ENTER to continue>')
    typewriter('')
    if name == hunterName:
        for player in duplicate(playerPositions, name):
            catchPlayer(player)
    elif hunterName in duplicate(playerPositions, name):
        catchPlayer(name)
        return None
    if not isJover:
        playerEvent[playerPositions[name].roomType](name)

# Predicting Stone. En réalité elle trompe les joueurs. L'idée de base, est de les guider vers leurs objectifs.
def stonePredict(name): # Make the stone actually predict (sometimes)
    typewriter('Predicitng Stone> You should go...')
    input('<Press ENTER to continue>')
    typewriter(f'\nPredicting Stone> YES! You should go {choice(list(playerPositions[name].doors.keys()))}!')
    input('<Press ENTER to continue>')
    typewriter('Predicting Stone> FREEDOM!!!!!')

# Wizard's Eye. Regarde le types des sales où l'on peu aller. Très pratique pour trouver l'escape. Trop fort??
def seeRooms(name):
    for door in playerPositions[name].doors.keys():
        if not playerPositions[name].doors[door] is None:
            typewriter(f"Wizard's Eye> Behind the {door} door I see a {playerPositions[name].doors[door][0].roomType} room")
    input('<Press ENTER to continue>')
    typewriter("Wizard's Eye> Alas, the sweet embrace...")

# La Bear Trap est posée
def setTrap(name):
    typewriter(f"Bear Trap> Aye! I'ma bite 'em ankles!")
    trapPositions[name] = playerPositions[name]
    typewriter(f"Bear Trap> Time ta hide.")

# Tous les evenements sont des fonctions de paramètre 'name'
itemEvent = {'Predicting Stone': stonePredict, 
             "Wizard's Eye": seeRooms, 
             'Cursed Doll': lambda name: teleport(choice(playerNames)), 
             'Energy Drink': playerMove, 
             'Bear Trap': setTrap, 
             'Magic Die': lambda name: choice(list(itemEvent.values()))(name)
             }

# La majorité du jeu se passe dans cette fonction:
def round():
    for name in playerNames:
        if player_list[name].items != []:
            answered = False
            while not answered:
                typewriter(f'Would {name} like to use items?')
                typewriter('[1] Yes')
                typewriter('[2] No')
                answer = input('> ')
                typewriter('')
                if answer == '2':
                    answered = True
                elif answer == '1':
                    while not answered:
                        typewriter('Which item would you like to use?')
                        options = {}
                        for i in range(len(player_list[name].items)):
                            typewriter(f'[{i+1}] {player_list[name].items[i]}')
                            options[f'{i+1}'] = player_list[name].items[i]
                        typewriter(f'[{len(player_list[name].items)+1}] Nevermind')
                        answer = input('> ')
                        typewriter('')
                        if answer == f'{len(player_list[name].items)+1}':
                            answered = True
                        elif answer in options.keys():
                            itemEvent[options[answer]](name)
                            typewriter(f'The {options[answer]} turns into dust.')
                            player_list[name].items.remove(options[answer])
                        else:
                            typewriter('Invalid Answer\n')
                else:
                    typewriter('Invalid answer\n')
        playerMove(name)

# Elimination d'un invaseur.
def catchPlayer(name):
    global isJover
    typewriter(f'{name} was caught by {hunterName}. {name} was never heard of again.')
    playerNames.remove(name)
    if playerNames == [hunterName]:
        isJover = True
    input('<Press ENTER to continue>')
    typewriter('')

# Intro
typewriter("\nWelcome to Astorias's Confusion Mansion!")
typewriter('At least 2 players are required, but the more the better!')
typewriter('Making a map is highly advised!')
input('<Press ENTER to continue>')
typewriter('')
while running:
    # Données globales qui changent le long du jeu, et qui reviennent aux paramètres iniciaux à chaque fois.
    player_list = {}
    playerPositions = {}
    trapPositions = {}
    playerNames = []
    itemList = {'Predicting Stone': 1, "Wizard's Eye": 1, 'Cursed Doll': 1, 'Energy Drink': 1, 'Bear Trap': 1, 'Magic Die': 1}
    purchased = {'Predicting Stone': 0, "Wizard's Eye": 0, 'Cursed Doll': 0, 'Energy Drink': 0, 'Bear Trap': 0, 'Magic Die': 0}
    isJover = False
    size = sizeSelect()
    board = Labyrinth(size)
    hunterName = hunterSelect()
    playerSelect()
    playerNames = list(player_list.keys())
    typewriter(f"You have heard the legends of the Mad Wizard Astorias, locked in his mansion along with his riches. You decided to take your chance and steal the gold. As soon as you stepped foot in the mansion, the doors shut and all invaders were shuffled through the confusing manor. You heard the waking roar of Astorias's protector, {hunterName}, and knew you had to find an exit.")
    input("\n<Press ENTER to start>")
    typewriter('')
    # Totalité du jeu:
    openingRound(board)
    while len(playerNames) > 1:
        round()
    # Fin du jeu:
    typewriter(f"{hunterName} was alone again. All invaders had either fled or died to {hunterName}'s hand.")
    typewriter(f"{hunterName} was now alone again, with only the machines left by Astorias to keep him company.")
    input('<Press ENTER to continue>')
    typewriter("\nThank you for playing Astorias's Confusion Mansion!")
    typewriter("\n    A game by HazenLD")
    typewriter("    Special thanks to Magic The Noah")
    input('<Press ENTER to continue>')
    typewriter('\nWould you like to play again?')
    typewriter('[1] Yes')
    typewriter('[2] No')
    answer = input('> ')
    if answer == '1':
        typewriter('Restarting Game...')
        input('<Press ENTER to continue>')
        typewriter('')
    if answer == '2':
        typewriter('Closing Game...')
        input('<Press ENTER to continue>')
        running = False
    else:
        typewriter('HazenLD> HAVE YOU STILL NOT LEARNED HOW TO ANSWER???')
        typewriter('HazenLD> Get the [Cha-Ching!] out of here!')
        input('<Press ENTER to continue>')
        running = False