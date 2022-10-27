from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button import MDIconButton
from kivymd.uix.snackbar import Snackbar
from generateur_de_mdp import *
from pyperclip import copy

"""
Lancer le programme avec:  python main.py -m screen:s3,portrait
Cela renvoie l'application en format d'un Samsung S3.
"""


class GenerateurDeMdpApp(MDApp):
    # dialog = None pour que la fenêtre n'aparaisse pas
    dialog = None

    def build(self):  # On implemente la méthode build()
        # On dit a Kivy de charger le fichier en format .kv 'generateurdemdp.kv'
        return Builder.load_file('generateurdemdp.kv')

    # Crée une fenetre qui affiche le MOT DE PASSE, le Bouton de COPIER et le Bouton FERMER
    def generer_mdp(self):
        """Renvoie une fenêtre qui superpose l'écran principale qui affiche le mot de passe générer, le bouton
        de copier qui permet de copier le mot de passe et le bouton de fermer qui ferme la fenêtre."""
        # On attribue des widgets à notre fenêtre
        if not self.dialog:
            self.dialog = MDDialog(
                title="",  # Affiche le mot de passe générer
                buttons=[
                    MDIconButton(  # Bouton de copier
                        icon='content-copy',  # nom de l'image
                        on_press=self.copy_code,  # quand presser il copie le mot de passe afficher
                    ),
                    MDFlatButton(  # Bouton de fermer
                        text="FERMER",  # texte du bouton
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        # détermine la couleur du bouton, dans notre cas la couleur primaire est bleu
                        on_release=self.ferme_fenetre_mdp,  # quand appuyer le bouton ferme la fenêtre
                    ),
                ],
            )
        self.dialog.open()  # ouvre la fenetre

    # Ferme la fenetre du mot de passe
    def ferme_fenetre_mdp(self, obj):
        """Ferme la fenêtre ouverte par la fonction generer_mdp()"""
        self.dialog.dismiss()

    # Permet de copié le mot de passe générer
    def copy_code(self, instance):
        """Copie le mot de passe générer qui correspond au titre de la fenêtre ouverte par generer_mdp()"""
        copy(self.dialog.title)  # copie le titre de la fenêtre
        # Affiche une notification type android à la partie inférieur de l'application qui montre à l'utilisateur qu'il a bien copie le code
        Snackbar(
            text="Mot de passe copier!",  # Texte de la notification
            snackbar_x="10dp",
            # Distance du rectangle de notification par rapport au bord de l'écran sur l'axe des abscisses
            snackbar_y="10dp",
            # Distance du rectangle de notification par rapport au bord de l'écran sur l'axe des ordonnées
            size_hint_x=0.94
        ).open()

    # Verifie les conditions du mot de passe et le renvoie
    def verifie_mdp(self, taille):
        """Verifie si le mot de passe comporte bien au moins 5 caractères et renvoie la fonction
        du fichier generateur_de_mdp() en dépéndent des conditions (les cases qui sont cochés)"""
        # Vérifie se l'utilisateur a choisi au moins 5 comme taille du mot de passe
        if taille == '' or int(taille) < 5:
            # Affiche un message si la taille n'est pas supporter par l'application
            self.dialog.title = "Taille insérer n'est pas supporté."
        else:
            # Si toute les checkbox sont activées
            if self.root.ids.box_majuscules.active and self.root.ids.box_minuscules.active and self.root.ids.box_chiffres.active and self.root.ids.box_caractere_speciaux.active:
                # Renvoi un mot de passe avec tout les éléments
                self.dialog.title = mdp_complet(int(taille))
            # Si la checkbox des Majuscules n'est pas activée
            elif not self.root.ids.box_majuscules.active:
                # Renvoie un mot de passe sans lettres majuscules
                self.dialog.title = sans_majuscules(int(taille))
            # Si la checkbox des Minuscules n'est pas activée
            elif not self.root.ids.box_minuscules.active:
                # Renvoie un mot de passe sans lettres minuscules
                self.dialog.title = sans_minuscules(int(taille))
            # Si la checkbox des Chiffres n'est pas activée
            elif not self.root.ids.box_chiffres.active:
                # Renvoie un mot de passe sans chiffres
                self.dialog.title = sans_chiffres(int(taille))
            # Si la checkbox des Caractère Speciaux n'est pas activée
            elif not self.root.ids.box_caractere_speciaux.active:
                # Renvoie un mot de passe sans caractères spéciaux
                self.dialog.title = sans_caractere_speciaux(int(taille))

    # L'utilisateur ne peut désactiver qu'une des options
    # Quand la checkbox des lettres majuscules est désactiver elle ne permet pas de desactiver les autres
    def box_majuscules_desactiver(self):
        """Quand la case des majuscules n'est pas coché, les autres cases sont automatiquement interdite
        d'être changer car l'utilisateur ne peut qu'enlever une des options"""
        if not self.root.ids.box_majuscules.active:
            self.root.ids.box_minuscules.disabled = True
            self.root.ids.box_chiffres.disabled = True
            self.root.ids.box_caractere_speciaux.disabled = True
        else:
            self.root.ids.box_minuscules.disabled = False
            self.root.ids.box_chiffres.disabled = False
            self.root.ids.box_caractere_speciaux.disabled = False

    # Quand la checkbox des lettres minuscules est désactiver elle ne permet pas de desactiver les autres
    def box_minuscules_desactiver(self):
        """Quand la case des minuscules n'est pas coché, les autres cases sont automatiquement interdite
                d'être changer car l'utilisateur ne peut qu'enlever une des options"""
        if not self.root.ids.box_minuscules.active:
            self.root.ids.box_majuscules.disabled = True
            self.root.ids.box_chiffres.disabled = True
            self.root.ids.box_caractere_speciaux.disabled = True
        else:
            self.root.ids.box_majuscules.disabled = False
            self.root.ids.box_chiffres.disabled = False
            self.root.ids.box_caractere_speciaux.disabled = False

    # Quand la checkbox des chiffres est désactiver elle ne permet pas de desactiver les autres
    def box_chiffres_desactiver(self):
        """Quand la case des chiffres n'est pas coché, les autres cases sont automatiquement interdite
                d'être changer car l'utilisateur ne peut qu'enlever une des options"""
        if not self.root.ids.box_chiffres.active:
            self.root.ids.box_majuscules.disabled = True
            self.root.ids.box_minuscules.disabled = True
            self.root.ids.box_caractere_speciaux.disabled = True
        else:
            self.root.ids.box_majuscules.disabled = False
            self.root.ids.box_minuscules.disabled = False
            self.root.ids.box_caractere_speciaux.disabled = False

    # Quand la checkbox des caractères spéciaux est désactiver elle ne permet pas de desactiver les autres
    def box_caractere_speciaux_desactiver(self):
        """Quand la case des caractères spéciaux n'est pas coché, les autres cases sont automatiquement interdite
        d'être changer car l'utilisateur ne peut qu'enlever une des options"""
        if not self.root.ids.box_caractere_speciaux.active:
            self.root.ids.box_majuscules.disabled = True
            self.root.ids.box_minuscules.disabled = True
            self.root.ids.box_chiffres.disabled = True
        else:
            self.root.ids.box_majuscules.disabled = False
            self.root.ids.box_minuscules.disabled = False
            self.root.ids.box_chiffres.disabled = False


# Démarre l'application
GenerateurDeMdpApp().run()
