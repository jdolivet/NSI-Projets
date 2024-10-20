from random import choice, randint

# Valeurs globales inchangeables
dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
shapePreset = {'Dead End': 1, 'Corridor': 2, 'T-Intersection': 3, 'Square': 4, 'Hexagon': 6, 'Octagon': 8}
# Les répétitions d'une même valeur affectent le poid de cette valeur.
nodeTypes = ['Empty', 'Empty', 'Empty', 'Good', 'Good', 'Bad', 'Bad', 'Shop', 'Shop', 'Gamble', 'Gold', 'Teleport']
nodeShapes = ['Corridor', 'Corridor', 'Corridor', 'Corridor', 'Corridor', 'Corridor', 'T-Intersection', 'T-Intersection', 'T-Intersection', 'T-Intersection', 'T-Intersection', 'Square', 'Square', 'Square', 'Square', 'Hexagon', 'Hexagon', 'Octagon']
doorType = ['Exit', 'Exit', 'Exit', 'Exit', 'Entrance'] 

# Valeurs globales changeables
loneDoorsR = []
loneDoorsD = []
loneDoorsT = []

# Équivaut à un Noeud
class Room:
    def __init__(self, type=None, shape=None):
        if type == None:
            self.roomType = choice(nodeTypes)
        else:
            self.roomType = type
        if shape == None and self.roomType != 'Teleport': # Un teleport ne peut pas servir de lien entre 2 parties du labytinthe, car il envoie à un noeud aléatoire.
            self.shape = choice(nodeShapes)
        elif self.roomType == 'Teleport':
            self.shape = 'Dead End'
        else:
            self.shape = shape

        # Correspond à la liste d'adjacence
        # {dir: (room, destDir)}
        self.doors = {}

        # Crée les portes
        taken = set()
        for i in range(shapePreset[self.shape]):
            dir = choice(dirs)
            while dir in taken:
                dir = choice(dirs)
            if i+1 == shapePreset[self.shape]:
                dType = 'Exit'
            else:
                dType = choice(doorType)
            self.doors[dir] = None
            loneDoorsR.append(self)
            loneDoorsD.append(dir)
            loneDoorsT.append(dType)
            taken.add(dir)

# Parcours le labyrinthe et place les noeuds passés en 'seen'
def roam(start: Room, seen:set):
    if start in seen:
        return None
    seen.add(start)
    for key in start.doors.keys():
        if start.doors[key] != None:
            roam(start.doors[key][0], seen)

# Équivaut à un graphe
class Labyrinth:
    def __init__(self, size):
        self.size = size
        self.generate()

    # Crée le labyrinthe
    def generate(self):
        global loneDoorsD, loneDoorsR, loneDoorsT
        # Recomence les données globales
        self.rooms = []
        loneDoorsR = []
        loneDoorsD = []
        loneDoorsT = []
        # Crée les sales
        for i in range(self.size):
            self.rooms.append(Room())
        self.rooms.append(Room('Escape', 'Dead End'))
        if len(loneDoorsD) % 2 == 1:
            self.rooms.append(Room('Empty', 'T-Intersection'))
        
        #Connecte les portes (crée les arcs)
        #Sens unique
        for i in range(len(loneDoorsT)):
            if i < len(loneDoorsT) and loneDoorsT[i] == 'Entrance':
                idx = randint(0, len(loneDoorsT)-1)
                while loneDoorsT[idx] != 'Exit' or idx == i:
                    idx = randint(0, len(loneDoorsT)-1)
                loneDoorsR[idx].doors[loneDoorsD[idx]] = (loneDoorsR[i], loneDoorsD[i])

                loneDoorsD.pop(i) 
                loneDoorsR.pop(i)
                loneDoorsT.pop(i)
                if i < idx:
                    idx -= 1
                loneDoorsR.pop(idx)
                loneDoorsD.pop(idx)
                loneDoorsT.pop(idx)
        # Double sens
        while loneDoorsD != []:
            idx1 = randint(0, len(loneDoorsD)-1)
            idx2 = randint(0, len(loneDoorsD)-1)
            while idx1 == idx2:
                idx2 = randint(0, len(loneDoorsD)-1)
            loneDoorsR[idx1].doors[loneDoorsD[idx1]] = (loneDoorsR[idx2], loneDoorsD[idx2])
            loneDoorsR[idx2].doors[loneDoorsD[idx2]] = (loneDoorsR[idx1], loneDoorsD[idx1])
            
            loneDoorsR.pop(idx1)
            loneDoorsD.pop(idx1)
            loneDoorsT.pop(idx1)
            if idx1 < idx2:
                idx2 -= 1
            loneDoorsR.pop(idx2)
            loneDoorsD.pop(idx2)
            loneDoorsT.pop(idx2)

        # Vérifie que le graphe soit connexe, si il ne l'est pas, regénére (force brute) 
        success = set()
        for r in self.rooms:
            success.add(r)
        for start in self.rooms:
            seen = set()
            roam(start, seen)
            if len(seen) != len(success):
                self.generate()
                break