from tkinter import *

#--------------------       Fonctions

def fonctionHein():
    global compteurHein, Debut
    compteurHein = compteurHein +1
    TexteHein.set ("Nombre de HEIN = " + str(compteurHein))

def fonctionDaccord():
    global compteurDaccord, Debut
    compteurDaccord = compteurDaccord +1
    TexteDaccord.set ("Nombre de D'ACCORD = " + str(compteurDaccord))

#--------------------       Crée la fenêtre
fenetre = Tk()
fenetre.title("Compteur Histoire")
#--------------------       Position de la fenêtre
Largeur = fenetre.winfo_screenwidth()
Hauteur = fenetre.winfo_screenheight()
    #----------             Crée la position
positionFenetre = "300x130+"+str(3*(Largeur//7))+"+"+str(3*(Hauteur//7))
    #----------             Positionne
fenetre.geometry(positionFenetre)
#--------------------       Compteurs variables
compteurHein = 0
compteurDaccord = 0
#--------------------       Message HEIN
TexteHein = StringVar()
TexteHein.set ("Nombre de HEIN = " + str(compteurHein))
    #----------
MessageHein = Label(fenetre, textvariable = TexteHein, font=("Gentium Book Basic",14),fg="red")
MessageHein.pack(side=TOP,padx=5,pady=5)
#--------------------       Message D'ACCORD
TexteDaccord = StringVar()
TexteDaccord.set ("Nombre de D'ACCORD = " + str(compteurDaccord))
    #----------
MessageDaccord = Label(fenetre, textvariable = TexteDaccord, font=("Gentium Book Basic",14),fg="blue")
MessageDaccord.pack(side=TOP,padx=5,pady=5)
#--------------------       Boutton HEIN
BouttonHein = Button(fenetre, text="HEIN", command=fonctionHein,fg="red")
BouttonHein.pack(side=LEFT,padx=20,pady=5)
#--------------------       Boutton D'ACCORD
BouttonDaccord = Button(fenetre, text="D'ACCORD", command=fonctionDaccord,fg="blue")
BouttonDaccord.pack(side="left",padx=40,pady=5)
#--------------------
Button(fenetre, text="Quitter",command=fenetre.destroy).pack(side="right",padx=5,pady=5)
#--------------------
fenetre.mainloop()
