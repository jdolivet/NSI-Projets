class Player:
    def __init__(self, isCPU: bool):
        self.isCPU = isCPU

        self.gold = 5
        self.items = []

    # Representation de self.gold
    def showGold(self):
        if self.gold > 0:
            return f'{self.gold} gold'
        if self.gold == 0:
            return 'no gold'
        return f'{-self.gold} debt'

    # Representation de self.items
    def showPack(self):
        string = ''
        if self.items == []:
            return 'nothing'
        if len(self.items) == 1:
            return f'{self.items[0]}'
        for item in self.items[:-2]:
            string += f'{item}, '
        return string + f'{self.items[-2]} and {self.items[-1]}'

    # Additione du gold. Accepte des données négatives.
    def gain(self, goldAmount):
        self.gold += goldAmount

    # Multiplie de l'or. Seulement utilisé pour x2.
    def multiplyGold(self, amount):
        self.gold *= amount
    
    # Aditionne un item à self.items
    def acquire(self, item):
        self.items.append(item)