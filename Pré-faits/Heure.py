from tkinter import *

import time

def maj():
    # on arrive ici toutes les 1000 ms
    heure.set(time.strftime('%H:%M:%S'))
    Mafenetre.after(1000,maj)

Mafenetre = Tk()
Mafenetre.title("Heure courante")

Largeur = Mafenetre.winfo_screenwidth()
Hauteur = Mafenetre.winfo_screenheight()
    #----------             Crée la position
positionFenetre = "200x80+"+str(3*(Largeur//7))+"+"+str(3*(Hauteur//7))
    #----------             Positionne
Mafenetre.geometry(positionFenetre)


# Création d'un widget Label
heure = StringVar()
Label(Mafenetre,textvariable=heure).pack(side='top',padx=10,pady=30)

maj()

Mafenetre.mainloop()
