import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import copy
import sys
import numpy as np
from PIL import Image, ImageTk, ImageEnhance


# Fonctions
def open_image():
    """Ouvre une image avec le gestionnaire de fichiers."""
    global img, tk_image, file_path
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    tk_image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=tk_image)
    canvas.config(scrollregion=(0, 0, img.width, img.height))

def save_image():
    """Sauvegarde l'image avec le gestionnaire de fichiers."""
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    img = ImageTk.getimage(tk_image)
    if file_path:
        img.save(file_path)
        

def update_image():
    """Met à jour l'image."""
    global img, tk_image
    # Update du coupage
#    img = ImageTk.getimage(tk_image)
    tk_image = ImageTk.PhotoImage(img)
    # Update de la saturation
    enhancer = ImageEnhance.Color(img)
    saturated_img = enhancer.enhance(saturation_level)
    tk_image = ImageTk.PhotoImage(saturated_img)
    text_saturation.delete(0, END)
    text_saturation.insert(0, saturation_level)
    # Update du contrast
    enhancer = ImageEnhance.Contrast(saturated_img)
    contrasted_img = enhancer.enhance(contrast_level)
    tk_image = ImageTk.PhotoImage(contrasted_img)
    text_contrast.delete(0, END)
    text_contrast.insert(0, contrast_level)
    # Update de la luminosité
    enhancer = ImageEnhance.Brightness(contrasted_img)
    bright_img = enhancer.enhance(brightness_level)
    tk_image = ImageTk.PhotoImage(bright_img)
    text_luminosite.delete(0, END)
    text_luminosite.insert(0, brightness_level)
    # Update de la sharpness
    enhancer = ImageEnhance.Brightness(bright_img)
    sharp_img = enhancer.enhance(sharpness_level)
    tk_image = ImageTk.PhotoImage(sharp_img)
    text_sharpness.delete(0, END)
    text_sharpness.insert(0, sharpness_level)
    # Update de la rotation
    rotated_img = sharp_img.rotate(angle, expand=True)
    tk_image = ImageTk.PhotoImage(rotated_img)
    canvas.create_image(0, 0, anchor=NW, image=tk_image)



def update_image_zoom():
    """Met à jour le zoom de l'image."""
    global tk_image
    img_zoome = img.resize((int(img.width * zoom_level), int(img.height * zoom_level)), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(img_zoome)
    canvas.config(scrollregion=(0, 0, img_zoome.width, img_zoome.height))
    canvas.create_image(0, 0, anchor=NW, image=tk_image)

rect_id = None
def appui_coupage(event):
    """Initie le rectangle de coupage."""
    global debut_x, debut_y, rect_id
    debut_x, debut_y = event.x, event.y
    if rect_id: 
        canvas.delete(rect_id)
    rect_id = canvas.create_rectangle(debut_x, debut_y, debut_x, debut_y, outline='red', width=2)

def rectangle_coupage(event):
    """Manipule le rectangle de coupage pour qu'il soit cohérent avec la position de la souris."""
    global rect_id
    fin_x, fin_y = event.x, event.y
    if rect_id:
        canvas.delete(rect_id)
    rect_id = canvas.create_rectangle(debut_x, debut_y, fin_x, fin_y, outline = 'red', width = 5)

image_coupe = None
def finalizer_coupage(event):
    """Finalize le coupage selon la position de la souris et met l'image à jour."""
    global img, tk_image, image_coupe
    fin_x, fin_y = event.x, event.y
    limite_debut_x = max(0, min(debut_x, img.width))
    limite_debut_y = max(0, min(debut_y, img.height))
    limite_fin_x = max(0, min(fin_x, img.width))
    limite_fin_y = max(0, min(fin_y, img.height))
    aire_decoupage = ((min(limite_debut_x, limite_fin_x)) / zoom_level, min(limite_debut_y, limite_fin_y) / zoom_level,
                       max(limite_debut_x, limite_fin_x) / zoom_level, max(limite_debut_y, limite_fin_y) / zoom_level)
    img = ImageTk.getimage(tk_image)
#    image_coupe = img.crop(aire_decoupage)
    img = img.crop(aire_decoupage)
    canvas.delete(rect_id)
    update_image()
#    tk_image = ImageTk.PhotoImage(image_coupe)


angle = 0
def rotation(angle_r):
    """Tourne l'image."""
    global angle
    angle = float(angle_r)
    update_image()

debut_nav_x = 0
debut_nav_y = 0
def appui_nav(event):
    """Définit la position de la souris comme le 0 du déplacement."""
    global debut_nav_x, debut_nav_y
    debut_nav_x = event.x
    debut_nav_x = event.y

def nav(event):
    """Déplace l'image."""
    global debut_nav_x, debut_nav_y
    delta_x = debut_nav_x - event.x
    delta_y = debut_nav_y - event.y
    canvas.xview_scroll(int(delta_x)//3, "units")
    canvas.yview_scroll(int(delta_y)//3, "units")
    debut_nav_x, debut_nav_y = event.x, event.y

zoom_level = 1
def zoom(event):
    """Zoome l'image"""
    global zoom_level
    if event.delta > 0:
        zoom_level *= 1.2 ** (event.delta / 120.0)
    zoom_level /= 1.1 ** abs(event.delta / 120.0)
    zoom_level = max(0.1, min(zoom_level, 10))
#    print(f"Event Delta: {event.delta}, Zoom Level: {zoom_level}")
    update_image_zoom()


saturation_level = 1.0
def saturation(pourcentage):
    """Change le niveau de saturation de l'image."""
    global saturation_level
    saturation_level = float(pourcentage)
    update_image()

def saturation_entry(event):
    """Récupère le niveau de saturation inséré par l'utilisateur."""
    global saturation_level
    entree = text_saturation.get()
    if entree.isdigit():
        entree = int(entree)
        if entree >= -10 and entree <= 10:
            slider_saturation.set(entree)
    update_image()

contrast_level = 1.0
def contrast(pourcentage):
    """Change le niveau de contrast de l'image."""
    global contrast_level
    contrast_level = float(pourcentage)
    update_image()

def contrast_entry(event):
    """Récupère le niveau de contrast inséré par l'utilisateur."""
    global contrast_level
    entree = text_contrast.get()
    if entree.isdigit():
        entree = int(entree)
        if entree >= -10 and entree <= 10:
            slider_contrast.set(entree)
    update_image()

brightness_level = 1.0
def brightness(pourcentage):
    """Change le niveau d'illumination de l'image."""
    global brightness_level
    brightness_level = float(pourcentage)
    update_image()

def brightness_entry(event):
    """Récupère le niveau d'illumination inséré par l'utilisateur."""
    global brightness_level
    entree = text_luminosite.get()
    if entree.isdigit():
        entree = int(entree)
        if entree >= -10 and entree <= 10:
            slider_luminosite.set(entree)
    update_image()


sharpness_level = 1.0
def sharpness(pourcentage):
    """Change le niveau de netteté de l'image."""
    global sharpness_level
    sharpness_level = float(pourcentage)
    update_image()

def sharpness_entry(event):
    """Récupère le niveau de netteté inséré par l'utilisateur."""
    global sharpness_level
    entree = text_sharpness.get()
    if entree.isdigit():
        entree = int(entree)
        if entree >= -10 and entree <= 10:
            slider_sharpness.set(entree)
    update_image()

'''
def dematricage():
    """Applique le dématriçage à l'image en cours."""
    global img, tk_image
    largeur, hauteur = img.size 
    img_rgb = np.zeros((hauteur, largeur, 3), dtype=np.uint8)  # Crée un tableau pour stocker l'image RGB

    for y in range(1, hauteur-1):
        for x in range(1, largeur-1):
            if y % 2 == 0 and x % 2 == 0:  # Interpolation aux pixels rouges
                img_rgb[y, x, 0] = img.getpixel((x, y))  # Rouge
                img_rgb[y, x, 1] = int((img.getpixel((x, y - 1)) + img.getpixel((x, y + 1)) +
                                         img.getpixel((x - 1, y)) + img.getpixel((x + 1, y))) / 4)  # Vert
                img_rgb[y, x, 2] = int((img.getpixel((x - 1, y - 1)) + img.getpixel((x - 1, y + 1)) +
                                         img.getpixel((x + 1, y - 1)) + img.getpixel((x + 1, y + 1))) / 4)  # Bleu

            elif y % 2 == 1 and x % 2 == 1:  # Interpolation aux pixels bleus
                img_rgb[y, x, 2] = img.getpixel((x, y))  # Bleu
                img_rgb[y, x, 1] = int((img.getpixel((x, y - 1)) + img.getpixel((x, y + 1)) +
                                         img.getpixel((x - 1, y)) + img.getpixel((x + 1, y))) / 4)  # Vert
                img_rgb[y, x, 0] = int((img.getpixel((x - 1, y - 1)) + img.getpixel((x - 1, y + 1)) +
                                         img.getpixel((x + 1, y - 1)) + img.getpixel((x + 1, y + 1))) / 4)  # Rouge

            else:  # Interpolation aux pixels verts
                img_rgb[y, x, 1] = img.getpixel((x, y))  # Vert
                if y % 2 == 0:
                    img_rgb[y, x, 0] = int((img.getpixel((x - 1, y)) + img.getpixel((x + 1, y))) / 2)  # Rouge
                    img_rgb[y, x, 2] = int((img.getpixel((x, y - 1)) + img.getpixel((x, y + 1))) / 2)  # Bleu
                else:
                    img_rgb[y, x, 0] = int((img.getpixel((x, y - 1)) + img.getpixel((x, y + 1))) / 2)  # Rouge
                    img_rgb[y, x, 2] = int((img.getpixel((x - 1, y)) + img.getpixel((x + 1, y))) / 2)  # Bleu

    img = Image.fromarray(img_rgb, 'RGB')
    update_image()
'''


# Fenêtre de display d'image
fenetre = tk.Tk()
fenetre.title("Image display")
fenetre.geometry('1920x1080')
canvas = tk.Canvas(fenetre, width=1920, height=1080)
canvas.pack()

# Fenêtre de l'éditeur d'image
fenetre_editeur = tk.Tk()
fenetre_editeur.title("Éditeur")
canvas_editeur = tk.Frame(fenetre_editeur, width=600, height=400)





# Contrôles

# Bouton d'ouverture d'image
open_button = Button(fenetre_editeur, text='Ouvrir', command=open_image)
open_button.grid(column=1, row=1)
# Bouton de sauvegarde d'image        
save_button = Button(fenetre_editeur, text="Save", command=save_image)
save_button.grid(column=2, row=1)
# Découpage de l'image
canvas.bind("<ButtonPress-1>", appui_coupage)
canvas.bind("<B1-Motion>", rectangle_coupage)
canvas.bind("<ButtonRelease-1>", finalizer_coupage)
# Rotation de l'image
slider_rotation = Scale(fenetre_editeur, from_=0, to=360, resolution=1, command=rotation, label='Rotation')
slider_rotation.set(angle)
slider_rotation.grid(column=1, row=2)
# Bouton de dématricage
#bouton_dematricage = Button(fenetre_editeur, text='Dématricage', command=dematricage)
#bouton_dematricage.grid(column=2, row=2)
# Navigation de l'image
canvas.bind("<ButtonPress-3>", appui_nav)
canvas.bind("<B3-Motion>", nav)
# Scrollbar
x_scrollbar = Scrollbar(fenetre, orient=HORIZONTAL, command=canvas.xview)
x_scrollbar.pack(side=BOTTOM, fill=X)
y_scrollbar = Scrollbar(fenetre, orient=VERTICAL, command=canvas.yview)
y_scrollbar.pack(side=RIGHT, fill=Y)
# Zoom
canvas.bind("<MouseWheel>", zoom)
# Saturation
slider_saturation = Scale(fenetre_editeur, from_=-10, to=10, resolution=0.01, orient=HORIZONTAL, command=saturation, label='Saturation')
slider_saturation.set(saturation_level)
slider_saturation.grid(column=1, row=3)
text_saturation = Entry(fenetre_editeur)
text_saturation.grid(column=1, row=4)
text_saturation.bind("<Return>", saturation_entry)
# Contrast
slider_contrast = Scale(fenetre_editeur, from_=-10, to=10, resolution=0.01, orient=HORIZONTAL, command=contrast, label='Contrast')
slider_contrast.set(contrast_level)
slider_contrast.grid(column=2, row=3)
text_contrast = Entry(fenetre_editeur)
text_contrast.grid(column=2, row=4)
text_contrast.bind("<Return>", contrast_entry)
# Luminosité
slider_luminosite = Scale(fenetre_editeur, from_=-10, to=10, resolution=0.01, orient=HORIZONTAL, command=brightness, label='Luminosité')
slider_luminosite.set(brightness_level)
slider_luminosite.grid(column=3, row=3)
text_luminosite = Entry(fenetre_editeur)
text_luminosite.grid(column=3, row=4)
text_luminosite.bind("<Return>", brightness_entry)
# Sharpness
slider_sharpness = Scale(fenetre_editeur, from_=-10, to=10, resolution=0.01, orient=HORIZONTAL, command=sharpness, label='Sharpness'    )
slider_sharpness.set(sharpness_level)
slider_sharpness.grid(column=4, row=3)
text_sharpness = Entry(fenetre_editeur)
text_sharpness.grid(column=4, row=4)
text_sharpness.bind("<Return>", sharpness_entry)









# Loops
fenetre.mainloop()
fenetre_editeur.mainloop()




