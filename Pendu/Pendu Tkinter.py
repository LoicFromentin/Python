from tkinter import *
from tkinter.messagebox import * # boîte de dialogue

Fenetre = Tk()
Fenetre.title("Jeu du Pendu")

Plateau = Canvas(Fenetre, height=700, width=500)
Plateau.pack(side=TOP,padx=5,pady=5)

Texte = Label(Fenetre, text="Entrez une lettre à tester:")
Texte.pack(side=LEFT, padx=5,pady=5)

LettreTest = StringVar()
Champ = Entry(Fenetre, textvariable=LettreTest, bg="pink")
Champ.focus_set()
Champ.pack(side=LEFT, padx=5,pady=5)

Fenetre.mainloop()
