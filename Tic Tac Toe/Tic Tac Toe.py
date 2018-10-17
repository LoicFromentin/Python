from tkinter import*

def Effacer ():
    Plateau.delete(ALL)

def Lignes ():
    LigneHorizontale1 = Plateau.create_line(0,120,360,120)
    LigneHorizontale2 = Plateau.create_line(0,240,360,240)
    LigneVerticale1 = Plateau.create_line(120,0,120,360)
    LigneVerticale2 = Plateau.create_line(240,0,240,360)
        
def clic(event):
    X = event.x
    Y = event.y
    r=80
    hautY = 0
    basY = 119
    for ligne in range(3):
        gaucheX = 0
        droiteX = 119
        for case in range (3):
            if gaucheX<X<droiteX and hautY<Y<basY:
                if tour%2 == 0:
                    Plateau.create_oval(gaucheX+10,hautY+10,gaucheX+110,hautY+110, outline="red")
                else:
                    Plateau.create_line(gaucheX+10,hautY+10,gaucheX+110,hautY+110)
                    Plateau.create_line(gaucheX+10,hautY+110,gaucheX+110,hautY+10)
            gaucheX,droiteX=droiteX+2,droiteX+120
        hautY,basY=basY+2,basY+120

tour = 0
Fenetre = Tk()
Fenetre.title ("Tic Tac Toe")
Largeur = 360
Hauteur = 360
Plateau = Canvas(Fenetre, width = Largeur, height = Hauteur, bg = "white")
Plateau.focus_set()
Plateau.pack(padx = 5, pady = 5)
Lignes()
Button(Fenetre, text = "Recommencer", command = Effacer).pack(side = LEFT, padx = 5, pady = 5)
Button(Fenetre, text = "Quitter", command = Fenetre.destroy).pack(side=RIGHT, padx = 5, pady = 5)

while tour-9 != 0:
    Plateau.bind("<Button-1>", clic)
    tour = tour+1    
    Fenetre.mainloop()
