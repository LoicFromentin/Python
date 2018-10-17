from tkinter import *

#--------------------# FONCTIONS #--------------------#

def SeparationMilieu():
    y=0
    longueur=50
    for tiret in range (5):
        Plateau.create_line(Largeur//2,y,Largeur//2,y+longueur,width=2,fill='white')
        y=y+(2*longueur)
    
def Clavier(event):
    global PosGaucheX,PosGaucheY,PosDroitY,PosDroitX
    touche = event.char
    #----- Deplacement Pion Gauche
    if touche == 'z': PosGaucheY -=20
    if touche == 's': PosGaucheY +=20
    #----- Deplacement Pion Droit
    if touche == 'o': PosDroitY -=20
    if touche == 'l': PosDroitY +=20
    #----- Empêche Pion Gauche de sortir
    if PosGaucheY>420: PosGaucheY = 420
    if PosGaucheY<30: PosGaucheY = 30
    #----- Empêche Pion Droit de sortir
    if PosDroitY<30: PosDroitY = 30
    if PosDroitY>420: PosDroitY = 420
    #----- MàJ Coords
    Plateau.coords(PionGauche,PosGaucheX-LargeurBatonnet,PosGaucheY-HauteurBatonnet,PosGaucheX+LargeurBatonnet,PosGaucheY+HauteurBatonnet)
    Plateau.coords(PionDroit,PosDroitX-LargeurBatonnet,PosDroitY-HauteurBatonnet,PosDroitX+LargeurBatonnet,PosDroitY+HauteurBatonnet)

#--------------------# PROGRAMME #--------------------#

Fenetre = Tk()
Fenetre.title ("Pong")

#----------# Valeurs #----------#

HauteurBatonnet = 30                        #Taille Pion
LargeurBatonnet = 4                         #Taille Pion
Hauteur = 450                               #Taille Fenetre
Largeur = 900                               #Taille Fenetre
#----- Pion Gauche
PosGaucheX = 100                            #Position Start Pion Gauche
PosGaucheY = 225                            #Position Start Pion Gauche
#----- Pion Droit
PosDroitX = 800                             #Position Start Pion Droit
PosDroitY = 225                             #Position Start Pion Droit

#----------#

Plateau = Canvas(Fenetre, width=Largeur, height=Hauteur,bg='black')
PionGauche = Plateau.create_rectangle(PosGaucheX-LargeurBatonnet,PosGaucheY-HauteurBatonnet,PosGaucheX+LargeurBatonnet,PosGaucheY+HauteurBatonnet,fill="white")
PionDroit = Plateau.create_rectangle(PosDroitX-LargeurBatonnet,PosDroitY-HauteurBatonnet,PosDroitX+LargeurBatonnet,PosDroitY+HauteurBatonnet,fill="white")
SeparationMilieu()                          #Pointillés de séparation au centre

#----------# NE PAS TOUCHER #----------#

Plateau.focus_set()
Plateau.bind('<Key>',Clavier)
Plateau.pack(padx=5,pady=5)
Fenetre.mainloop()
