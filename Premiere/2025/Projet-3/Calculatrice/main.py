import tkinter as tk

def main():
    """
    Démarre la calculatrice graphique simple.
    
    L’utilisateur peut saisir des nombres, choisir une opération (+, -, *, /)
    puis cliquer sur « = » pour voir le résultat ou « C » pour effacer.
    """
    def ajouter_valeur(valeur):
        """Ajoute un caractère (chiffre ou opérateur) à l’entrée."""
        entrée.insert(tk.END, str(valeur))
    
    def effacer():
        """Efface le champ d’entrée."""
        entrée.delete(0, tk.END)
    
    def calculer():
        """Évalue l’expression saisie et affiche le résultat ou 'Erreur'."""
        try:
            résultat = eval(entrée.get())
            entrée.delete(0, tk.END)
            entrée.insert(tk.END, str(résultat))
        except Exception:
            entrée.delete(0, tk.END)
            entrée.insert(tk.END, "Erreur")

    # fenêtre principale
    fenêtre = tk.Tk()
    fenêtre.title("Calculatrice Simple")

    # champ d’entrée
    entrée = tk.Entry(fenêtre, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
    entrée.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # boutons
    boutons = [
        ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
        ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
        ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
        ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ]

    for (texte, ligne, colonne) in boutons:
        if texte == '=':
            cmd = calculer
        else:
            cmd = lambda v=texte: ajouter_valeur(v)
        tk.Button(fenêtre, text=texte, width=4, height=2, font=('Arial', 18),
                  command=cmd).grid(row=ligne, column=colonne, padx=5, pady=5)

    # bouton « Effacer » (C)
    tk.Button(fenêtre, text='C', width=4, height=2, font=('Arial', 18),
              command=effacer).grid(row=5, column=0, columnspan=4, sticky='we', padx=5, pady=5)

    fenêtre.mainloop()

if __name__ == "__main__":
    main()