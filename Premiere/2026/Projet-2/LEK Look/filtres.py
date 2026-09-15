"""Fonctions qui modifient une image avec Pillow."""

from PIL import Image, ImageEnhance, ImageFilter


def creer_table_gamma(gamma):
    """Crée une table de conversion pour le réglage gamma."""
    table = []

    for valeur in range(256):
        couleur = valeur / 255
        nouvelle_valeur = round(255 * (couleur ** (1 / gamma)))
        table.append(nouvelle_valeur)

    return table


def creer_table_facteur(facteur):
    """Crée une table de conversion avec un facteur de couleur."""
    table = []

    for valeur in range(256):
        nouvelle_valeur = int(valeur * facteur)
        nouvelle_valeur = max(0, min(255, nouvelle_valeur))
        table.append(nouvelle_valeur)

    return table


def appliquer_luminosite(image, luminosite):
    """Modifie la luminosité de l'image."""
    facteur = 1 + luminosite / 100
    return ImageEnhance.Brightness(image).enhance(facteur)


def appliquer_contraste(image, contraste):
    """Modifie le contraste de l'image."""
    facteur = 1 + contraste / 100
    return ImageEnhance.Contrast(image).enhance(facteur)


def appliquer_saturation(image, saturation):
    """Modifie la saturation des couleurs."""
    facteur = 1 + saturation / 100
    return ImageEnhance.Color(image).enhance(facteur)


def appliquer_nettete(image, nettete):
    """Modifie la netteté de l'image."""
    facteur = nettete / 100
    return ImageEnhance.Sharpness(image).enhance(facteur)


def appliquer_gamma(image, gamma):
    """Éclaircit ou assombrit les tons moyens avec le gamma."""
    table = creer_table_gamma(gamma)
    return image.point(table * 3)


def appliquer_exposition(image, exposition):
    """Modifie l'exposition de l'image en valeurs photographiques."""
    facteur = 2 ** exposition
    return ImageEnhance.Brightness(image).enhance(facteur)


def appliquer_temperature(image, temperature):
    """Réchauffe ou refroidit les couleurs de l'image."""
    facteur_rouge = 1 + temperature / 250
    facteur_bleu = 1 - temperature / 250
    table_rouge = creer_table_facteur(facteur_rouge)
    table_bleu = creer_table_facteur(facteur_bleu)
    rouge, vert, bleu = image.split()
    rouge = rouge.point(table_rouge)
    bleu = bleu.point(table_bleu)
    return Image.merge("RGB", (rouge, vert, bleu))


def appliquer_teinte(image, teinte):
    """Décale légèrement la teinte de toutes les couleurs."""
    if teinte == 0:
        return image

    image_tsv = image.convert("HSV")
    teinte_actuelle, saturation, valeur = image_tsv.split()
    decalage = int(teinte * 127 / 100)
    table = []

    for couleur in range(256):
        table.append((couleur + decalage) % 256)

    teinte_actuelle = teinte_actuelle.point(table)
    return Image.merge("HSV", (teinte_actuelle, saturation, valeur)).convert("RGB")


def appliquer_vibrance(image, vibrance):
    """Renforce doucement les couleurs de l'image."""
    facteur = 1 + vibrance / 200
    return ImageEnhance.Color(image).enhance(facteur)


def appliquer_noir_blanc(image, noir_blanc):
    """Mélange progressivement l'image couleur et son gris."""
    image_grise = image.convert("L").convert("RGB")
    proportion = noir_blanc / 100
    return Image.blend(image, image_grise, proportion)


def appliquer_flou(image, flou):
    """Applique un flou gaussien sur l'image."""
    return image.filter(ImageFilter.GaussianBlur(flou))


def filtre_photomaton(image_originale, nombre_copies):
    """Réorganise les pixels de l'image avec un effet Photomaton."""
    image_modifiee = image_originale.copy()
    pixels_originaux = image_originale.load()
    pixels_modifies = image_modifiee.load()
    largeur, hauteur = image_modifiee.size

    for abscisse in range(largeur):
        for ordonnee in range(hauteur):
            nouvelle_abscisse = (nombre_copies * abscisse) % largeur
            nouvelle_ordonnee = (nombre_copies * ordonnee) % hauteur
            pixels_modifies[abscisse, ordonnee] = pixels_originaux[
                nouvelle_abscisse, nouvelle_ordonnee
            ]

    return image_modifiee


def filtre_inverse_video(image_originale):
    """Inverse les trois couleurs de tous les pixels de l'image."""
    image_modifiee = image_originale.copy()
    pixels_originaux = image_originale.load()
    pixels_modifies = image_modifiee.load()
    largeur, hauteur = image_modifiee.size

    for abscisse in range(largeur):
        for ordonnee in range(hauteur):
            rouge, vert, bleu = pixels_originaux[abscisse, ordonnee]
            pixels_modifies[abscisse, ordonnee] = (255 - rouge, 255 - vert, 255 - bleu)

    return image_modifiee


def appliquer_tous_les_reglages(image, reglages):
    """Applique tous les réglages dans un ordre toujours identique."""
    image_modifiee = image.copy()
    image_modifiee = appliquer_luminosite(image_modifiee, reglages["luminosite"])
    image_modifiee = appliquer_contraste(image_modifiee, reglages["contraste"])
    image_modifiee = appliquer_saturation(image_modifiee, reglages["saturation"])
    image_modifiee = appliquer_nettete(image_modifiee, reglages["nettete"])
    image_modifiee = appliquer_gamma(image_modifiee, reglages["gamma"])
    image_modifiee = appliquer_exposition(image_modifiee, reglages["exposition"])
    image_modifiee = appliquer_temperature(image_modifiee, reglages["temperature"])
    image_modifiee = appliquer_teinte(image_modifiee, reglages["teinte"])
    image_modifiee = appliquer_vibrance(image_modifiee, reglages["vibrance"])
    image_modifiee = appliquer_noir_blanc(image_modifiee, reglages["noir_blanc"])
    image_modifiee = appliquer_flou(image_modifiee, reglages["flou"])
    return image_modifiee
