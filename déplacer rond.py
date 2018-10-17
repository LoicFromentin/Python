from tkinter import *

#---------------# FONCTIONS #---------------#

#Place le cercle à sa position de départ
#La couleur du cercle est Noir
def StartRond ():
    global Cercle,xCercle,yCercle,PlaceListeCouleurs
    PlaceListeCouleurs = 1
    xCercle = 60
    yCercle = 60 
    Cercle = Plateau.create_oval(xCercle-Rayon,yCercle-Rayon,xCercle+Rayon,yCercle +Rayon, fill=ListeCouleurs[0], width=3, outline='black')

#Replace le cercle à sa position de départ
#Re setup le cercle en Noir
def Recommencer ():
    Plateau.delete(Cercle)
    StartRond()

#Quitte le jeu et en informe l'utilisateur que le programme
def Quitter ():
    global Fenetre
    Fenetre.destroy()
    print("Vous avez quitté le programme.")

#Empêche le cercle de sortir du Canvas
def PasDepasser (X,Y,Largeur,Hauteur,Rayon):
    Marge = 2
    if X > (Largeur - Rayon):   X = Largeur - (Rayon + Marge)   #S'il est trop à droite
    if X < (0 + Rayon):         X = 0 + (Rayon + Marge)   #S'il est trop à gauche
    if Y > (Hauteur - Rayon):   Y = Hauteur - (Rayon + Marge)   #S'il est trop en bas
    if Y < (0 + Rayon):         Y = 0 + (Rayon + Marge)   #S'il est trop en haut
    return(X,Y)

def clic (event):
    global Selection, Cercle, xCercle, yCercle,PlaceListeCouleurs
    X = event.x
    Y = event.y
    X,Y = PasDepasser (X,Y,Largeur,Hauteur,Rayon)               #Empêche le cercle de sortir du Canvas
    
    if (xCercle-30<X<xCercle+30 and yCercle-30<Y<yCercle+30):     #S'il clique sur le cercle
        Selection = True                                        #Il tient le cercle
    
    if Selection == True:                                       #S'il a déjà cliqué sur le cercle
        if not (xCercle-30<X<xCercle+30 and  yCercle-30<Y<yCercle+30): #S'il ne clique pas sur le cercle
            Plateau.delete(Cercle)                              #Supprime l'ancien cercle
            xCercle = X                                         #Définit le centre du cercle (X)
            yCercle = Y                                         #Définit le centre du cercle (Y)
            Cercle = Plateau.create_oval(xCercle-Rayon,yCercle-Rayon,xCercle+Rayon,yCercle+Rayon,fill=ListeCouleurs[PlaceListeCouleurs],width=3,outline='black')
            Selection = False                                   #Il ne tient plus le cercle
            PlaceListeCouleurs = PlaceListeCouleurs + 1         #Avance dans la liste des couleurs  
    
    if PlaceListeCouleurs > (len(ListeCouleurs)-1) :            #Si on a fait toutes les couleurs de la liste
        PlaceListeCouleurs = 0                                  #Revient à la première couleur de la liste

#---------------# VARIABLES #---------------#
        
PlaceListeCouleurs = 1
ListeCouleurs = ["grey","pink","red","magenta","blue","cyan","green"]      
Selection = False
Rayon = 30
xCercle = 60
yCercle = 60

#---------------# FENÊTRE #---------------#

Fenetre = Tk ()
Fenetre.title ("Déplacer un rond")
Largeur = 650
Hauteur = 450
Plateau = Canvas (Fenetre, width=Largeur, height=Hauteur, bg="white")
Plateau.focus_set()
Plateau.pack(padx = 5,pady = 5)

#----------------------

StartRond()                                                     #Place le rond de départ
Button (Fenetre, text = "Recommencer", command = Recommencer).pack(side = LEFT, padx = 5, pady = 5)
Button (Fenetre, text = "Quitter", command = Quitter).pack(side = RIGHT, padx = 5, pady = 5)
Plateau.bind("<Button-1>", clic)

Fenetre.mainloop()
