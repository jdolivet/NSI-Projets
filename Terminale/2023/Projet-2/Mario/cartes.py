import classes

def carte1_1_blocs() -> list[classes.Bloc]:
    """Renvoie une liste contenant tous les blocs
    du monde 1_1"""
    carte = []
    carte += [classes.Bloc(-16, 16*i, 240, 240) for i in range(15)]
    carte += [classes.Bloc(16*i, 208 + (16* j), 16, 0) for i in range(70) for j in range(2)]
    carte += [classes.Bloc(256, 144, 48, 16)]
    carte += [classes.Bloc(336, 144, 48, 16, contenu=[1, "champignon"])]
    carte += [classes.Bloc(336 + 32, 144, 48, 16)]
    carte += [classes.Bloc(320 + 32*i, 144, 32, 16) for i in range(3)]
    carte += [classes.Bloc(352, 80, 48, 16)]
    
    carte += [classes.Bloc(448, 176, 72, 16)] # Tuyau petit
    carte += [classes.Bloc(464, 176, 88, 16)]
    carte += [classes.Bloc(448, 192, 72, 32)]
    carte += [classes.Bloc(464, 192, 88, 32)]
    
    carte += [classes.Bloc(608, 160, 72, 16)] #Tuyau moyen
    carte += [classes.Bloc(624, 160, 88, 16)]
    carte += [classes.Bloc(608, 176, 72, 32)]
    carte += [classes.Bloc(624, 176, 88, 32)]
    carte += [classes.Bloc(608, 192, 72, 48)]
    carte += [classes.Bloc(624, 192, 88, 48)]
    
    carte += [classes.Bloc(736, 144, 72, 16)] #Tuyau grand
    carte += [classes.Bloc(752, 144, 88, 16)]
    carte += [classes.Bloc(736, 160, 72, 32)]
    carte += [classes.Bloc(752, 160, 88, 32)]
    carte += [classes.Bloc(736, 176 + (16*i), 72, 48) for i in range(2)]
    carte += [classes.Bloc(752, 176 + (16*i), 88, 48) for i in range(2)]
    
    carte += [classes.Bloc(736 + (16*11), 144, 72, 16)] #Tuyau 4
    carte += [classes.Bloc(752 + (16*11), 144, 88, 16)]
    carte += [classes.Bloc(736 + (16*11), 160, 72, 32)]
    carte += [classes.Bloc(752 + (16*11), 160, 88, 32)]
    carte += [classes.Bloc(736 + (16*11), 176 + (16*i), 72, 48) for i in range(2)]
    carte += [classes.Bloc(752 + (16*11), 176 + (16*i), 88, 48) for i in range(2)]
    
    carte += [classes.Bloc(1152 + (16*i), 208 + (16* j), 16, 0) for i in range(15) for j in range(2)] #Plateforme 2
    carte += [classes.Bloc(1248 + (32*i), 144, 32, 16) for i in range(2)]
    carte += [classes.Bloc(1264, 144, 48, 16, contenu=[1, "champignon"])]
    carte += [classes.Bloc(1296 + (16*i), 80, 32, 16) for i in range(8)]
    carte += [classes.Bloc(1472 + (16*i), 80, 32, 16) for i in range(3)]
    
    carte += [classes.Bloc(1520, 144, 32, 16)]
    carte += [classes.Bloc(1520, 80, 48, 16)]
    carte += [classes.Bloc(1440 + (16*i), 208 + (16* j), 16, 0) for i in range(63) for j in range(2)] #Plateforme 3
    carte += [classes.Bloc(1600 + (16*i), 144, 32, 16) for i in range(2)]
    carte += [classes.Bloc(1696 + (48*i), 144, 48, 16) for i in range(3)]
    carte += [classes.Bloc(1744, 80, 48, 16, contenu=[1, "champignon"])]
    carte += [classes.Bloc(1888, 144, 32, 16)]
    carte += [classes.Bloc(1936 + (16*i), 80, 32, 16) for i in range(3)]
    carte += [classes.Bloc(2048 + (48*i), 80, 32, 16) for i in range(2)]
    carte += [classes.Bloc(2064 + (16*i), 80, 48, 16) for i in range(2)]
    carte += [classes.Bloc(2064 + (16*i), 144, 32, 16) for i in range(2)]
    
    carte += [classes.Bloc(2196 - (16*j), 144 + (16*i), 16, 16)  for i in range(4) for j in range(i+1)] #Echelle droite
    carte += [classes.Bloc(2240 + (16*j), 144 + (16*i), 16, 16)  for i in range(4) for j in range(i+1)] #Echelle gauche
    carte += [classes.Bloc(2416 - (16*j), 144 + (16*i), 16, 16)  for i in range(4) for j in range(i+1)] #Echelle droite 2
    carte += [classes.Bloc(2432, 144 + (16*i), 16, 16) for i in range(4)]
    
    carte += [classes.Bloc(2480 + (16*i), 208 + (16* j), 16, 0) for i in range(53) for j in range(2)] #Plateforme 4
    carte += [classes.Bloc(2480 + (16*j), 144 + (16*i), 16, 16)  for i in range(4) for j in range(i+1)] #Echelle gauche 2
    
    carte += [classes.Bloc(2608, 176, 72, 16)] # Tuyau
    carte += [classes.Bloc(2624, 176, 88, 16)]
    carte += [classes.Bloc(2608, 192, 72, 32)]
    carte += [classes.Bloc(2624, 192, 88, 32)]
    
    carte += [classes.Bloc(2864, 176, 72, 16)] # Tuyau
    carte += [classes.Bloc(2880, 176, 88, 16)]
    carte += [classes.Bloc(2864, 192, 72, 32)]
    carte += [classes.Bloc(2880, 192, 88, 32)]
    
    carte += [classes.Bloc(2688 + (16*i), 144, 32, 16) for i in range(2)]
    carte += [classes.Bloc(2720, 144, 48, 16)]
    carte += [classes.Bloc(2736, 144, 32, 16)]
    
    carte += [classes.Bloc(3008 - (16*j), 80 + (16*i), 16, 16)  for i in range(8) for j in range(i+1)] #Grande echelle droite
    carte += [classes.Bloc(3024, 80 + (16*i), 16, 16)  for i in range(8)]
    carte += [classes.Bloc(3168, 192, 16, 16)]
    
    carte += [classes.Bloc(3328 + (16*i), 208 + (16* j), 48, 0) for i in range(16) for j in range(2)]
    carte += [classes.Bloc(3328, 32 + (16* i), 64, 0) for i in range(11)]
    carte += [classes.Bloc(3392 + (16*i), 32, 64, 0) for i in range(7)]
    carte += [classes.Bloc(3392 + (16*i), 160 + (16*j), 64, 0) for i in range(7) for j in range(3)]
    
    carte += [classes.Bloc(3168, 176 - 16*i, 200, 120, contenu=["victoire"]) for i in range(7)]
    carte += [classes.Bloc(3160, 64 , 192, 83, contenu=["victoire"])]
    
    return carte

def carte1_1_entites() -> list[classes.Entite]:
    """Renvoie une liste contenant tous les entites
    du monde 1_1"""
    carte = []
    carte += [classes.Entite(256, 192, -1, "goomba")]
    carte += [classes.Entite(640, 192, 1, "goomba")]
    carte += [classes.Entite(768, 192, 1, "goomba")]
    carte += [classes.Entite(896, 192, -1, "goomba")]
    carte += [classes.Entite(1296, 64, -1, "goomba")]
    carte += [classes.Entite(1312, 64, -1, "goomba")]
    carte += [classes.Entite(2736, 192, -1, "goomba")]
    carte += [classes.Entite(2754, 192, -1, "goomba")]
    carte += [classes.Entite(2090, 192, -1, "goomba")]
    carte += [classes.Entite(2060, 192, -1, "goomba")]
    carte += [classes.Entite(2020, 192, -1, "goomba")]
    carte += [classes.Entite(1900, 192, -1, "goomba")]
    carte += [classes.Entite(1685, 192, -1, "goomba")]
    carte += [classes.Entite(1714, 192, -1, "goomba")]
    carte += [classes.Entite(1816, 192, -1, "goomba")]
    carte += [classes.Entite(1840, 192, -1, "goomba")]
    carte += [classes.Entite(1750, 192, -1, "koopa troopa")]
    return carte