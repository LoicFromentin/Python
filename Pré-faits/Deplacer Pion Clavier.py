from tkinter import *

def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX,PosY
    touche = event.char
    # déplacement vers le haut
    if touche == 'z':
        PosY -= 20
    # déplacement vers le bas
    if touche == 's':
        PosY += 20
    # déplacement vers la droite
    if touche == 'd':
        PosX += 20
    # déplacement vers la gauche
    if touche == 'q':
        PosX -= 20
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Pion,PosX -10, PosY -10, PosX +10, PosY +10)
    # Création de la fenêtre principale

Mafenetre = Tk()
Mafenetre.title('Pion')

# position initiale du pion
PosX = 230
PosY = 150

# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
Pion = Canevas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2,fill='red')
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.pack(padx =5, pady =5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT)

Mafenetre.mainloop()
