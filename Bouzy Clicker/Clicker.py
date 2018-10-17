from tkinter import *

#----------------------------------------# FONCTIONS #----------------------------------------#

#--------------------# COIN #--------------------#
def FonctionCoin():
    global GoldTotal,GoldCoin,TexteGoldTotal

    #----------         MàJ Variables
    GoldTotal = GoldTotal + GoldCoin
    #----------         MàJ Textes
    PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
    TexteGoldTotal.set(PhraseTexteGoldTotal)

def FonctionAmeliorerCoin():
    global LvlCoin,GoldTotal,GoldCoin,BonusGoldCoin,PrixAmeliorerGoldCoin
    
    if GoldTotal >= PrixAmeliorerGoldCoin:
        #----------         MàJ Variables
        GoldTotal = GoldTotal - PrixAmeliorerGoldCoin
        GoldCoin = GoldCoin + BonusGoldCoin
        LvlCoin = LvlCoin +1
        PrixAmeliorerGoldCoin = int(PrixAmeliorerGoldCoin*(6/5))
        if LvlCoin in (listeLvlUp):
            GoldCoin = GoldCoin *2
            BonusGoldCoin = BonusGoldCoin *2
        #----------         MàJ Textes
        PhraseTexteCoin = "(+"+str(GoldCoin)+" pièces)"
        TexteCoin.set(PhraseTexteCoin)
        PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
        TexteGoldTotal.set(PhraseTexteGoldTotal)
        PhraseTexteAmeliorerCoin = "(coûte "+str(PrixAmeliorerGoldCoin)+" pièces)"
        TexteAmeliorerCoin.set(PhraseTexteAmeliorerCoin)
        PhraseTexteBouttonCoin ="       Coin - lvl "+str(LvlCoin)+"       "  
        TexteBouttonCoin.set(PhraseTexteBouttonCoin)

#--------------------# PLUME SACREE #--------------------#

def FonctionPlumeSacree():
    global GoldTotal,GoldPlumeSacree
    if AchatPlumeSacree == True:
        #----------         MàJ Variables
        GoldTotal = GoldTotal + GoldPlumeSacree
        #----------         MàJ Textes
        PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
        TexteGoldTotal.set(PhraseTexteGoldTotal)

def FonctionAmeliorerPlumeSacree ():
    global LvlPlumeSacree,AchatPlumeSacree,GoldTotal,PrixAmeliorerGoldPlumeSacree,TexteBouttonAmeliorerPlumeSacree,GoldPlumeSacree,BonusGoldPlumeSacree,TexteAmeliorerPlumeSacree
    if AchatPlumeSacree==False and GoldTotal>= PrixAmeliorerGoldPlumeSacree:
        #----------         MàJ Variables
        GoldTotal = GoldTotal - PrixAmeliorerGoldPlumeSacree
        PrixAmeliorerGoldPlumeSacree = int(PrixAmeliorerGoldPlumeSacree *(6/5))
        AchatPlumeSacree = True
        LvlPlumeSacree = LvlPlumeSacree +1
        #----------         MàJ Textes
        PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
        TexteGoldTotal.set(PhraseTexteGoldTotal)
        TexteBouttonAmeliorerPlumeSacree.set("Améliorer Plume Sacrée")
        PhraseTexteAmeliorerPlumeSacree = "(coûte "+str(PrixAmeliorerGoldPlumeSacree)+" pièces)"
        TexteAmeliorerPlumeSacree.set(PhraseTexteAmeliorerPlumeSacree)
        PhraseTexteBouttonPlumeSacree = "Plume Sacrée - lvl "+str(LvlPlumeSacree)
        TexteBouttonPlumeSacree.set(PhraseTexteBouttonPlumeSacree)
    elif AchatPlumeSacree == True:
        if GoldTotal >= PrixAmeliorerGoldPlumeSacree:
            #----------         MàJ Variables
            GoldTotal = GoldTotal-PrixAmeliorerGoldPlumeSacree
            PrixAmeliorerGoldPlumeSacree = int(PrixAmeliorerGoldPlumeSacree *(6/5))
            GoldPlumeSacree = GoldPlumeSacree +BonusGoldPlumeSacree
            LvlPlumeSacree = LvlPlumeSacree +1
            if LvlPlumeSacree in (listeLvlUp):
                GoldPlumeSacree = GoldPlumeSacree *2
                BonusGoldPlumeSacree = BonusGoldPlumeSacree *2
            #----------         MàJ Textes
            PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
            TexteGoldTotal.set(PhraseTexteGoldTotal)
            PhraseTextePlumeSacree = "(+"+str(GoldPlumeSacree)+" pièces)"
            TextePlumeSacree.set(PhraseTextePlumeSacree)
            PhraseTexteAmeliorerPlumeSacree = "(coûte "+str(PrixAmeliorerGoldPlumeSacree)+" pièces)"
            TexteAmeliorerPlumeSacree.set(PhraseTexteAmeliorerPlumeSacree)
            PhraseTexteBouttonPlumeSacree = "Plume Sacrée - lvl "+str(LvlPlumeSacree)
            TexteBouttonPlumeSacree.set(PhraseTexteBouttonPlumeSacree)
            
#--------------------# BEC POILU #--------------------#

def FonctionBecPoilu():
    global GoldTotal,GoldBecPoilu
    if AchatBecPoilu == True:
        #----------         MàJ Variables
        GoldTotal = GoldTotal + GoldBecPoilu
        #----------         MàJ Textes
        PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
        TexteGoldTotal.set(PhraseTexteGoldTotal)

def FonctionAmeliorerBecPoilu ():
    global LvlBecPoilu,AchatBecPoilu,GoldTotal,PrixAmeliorerGoldBecPoilu,TexteBouttonAmeliorerBecPoilu,GoldBecPoilu,BonusGoldBecPoilu,TexteAmeliorerBecPoilu
    if AchatBecPoilu==False and GoldTotal>= PrixAmeliorerGoldBecPoilu:
        #----------         MàJ Variables
        GoldTotal = GoldTotal - PrixAmeliorerGoldBecPoilu
        PrixAmeliorerGoldBecPoilu = int(PrixAmeliorerGoldBecPoilu *(6/5))
        AchatBecPoilu = True
        LvlBecPoilu = LvlBecPoilu +1
        #----------         MàJ Textes
        PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
        TexteGoldTotal.set(PhraseTexteGoldTotal)
        TexteBouttonAmeliorerBecPoilu.set("    Améliorer Bec Poilu    ")
        PhraseTexteAmeliorerBecPoilu = "(coûte "+str(PrixAmeliorerGoldBecPoilu)+" pièces)"
        TexteAmeliorerBecPoilu.set(PhraseTexteAmeliorerBecPoilu)
        PhraseTexteBouttonBecPoilu = "   Bec Poilu - lvl "+str(LvlBecPoilu)+"    "
        TexteBouttonBecPoilu.set(PhraseTexteBouttonBecPoilu)
    elif AchatBecPoilu == True:
        if GoldTotal >= PrixAmeliorerGoldBecPoilu:
            #----------         MàJ Variables
            GoldTotal = GoldTotal-PrixAmeliorerGoldBecPoilu
            PrixAmeliorerGoldBecPoilu = int(PrixAmeliorerGoldBecPoilu *(6/5))
            GoldBecPoilu = GoldBecPoilu +BonusGoldBecPoilu
            LvlBecPoilu = LvlBecPoilu +1
            if LvlBecPoilu in (listeLvlUp):
                GoldBecPoilu = GoldBecPoilu *2
                BonusGoldBecPoilu = BonusGoldBecPoilu *2
            #----------         MàJ Textes
            PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
            TexteGoldTotal.set(PhraseTexteGoldTotal)
            PhraseTexteBecPoilu = "(+"+str(GoldBecPoilu)+" pièces)"
            TexteBecPoilu.set(PhraseTexteBecPoilu)
            PhraseTexteAmeliorerBecPoilu = "(coûte "+str(PrixAmeliorerGoldBecPoilu)+" pièces)"
            TexteAmeliorerBecPoilu.set(PhraseTexteAmeliorerBecPoilu)
            PhraseTexteBouttonBecPoilu = "   Bec Poilu - lvl "+str(LvlBecPoilu)+"    "
            TexteBouttonBecPoilu.set(PhraseTexteBouttonBecPoilu)

#----------------------------------------# PROGRAMME PRINCIPAL #----------------------------------------#
            
#--------------------           Variables
listeLvlUp = [10,25,50,100,200,500,1000]
    #Total
GoldTotal = 0
    #Coin
LvlCoin = 1
GoldCoin = 1
BonusGoldCoin = 2
PrixAmeliorerGoldCoin = 20
    #Plume Sacrée
LvlPlumeSacree = 0
GoldPlumeSacree = 105
BonusGoldPlumeSacree = 5
PrixAmeliorerGoldPlumeSacree = 15000
AchatPlumeSacree = False
    #Bec Poilu
LvlBecPoilu = 0
GoldBecPoilu = 710
BonusGoldBecPoilu = 10
PrixAmeliorerGoldBecPoilu = 20000000
AchatBecPoilu = False
#--------------------           Fenêtre
fenetre = Tk()
fenetre.title("Coin Clicker")
#--------------------           Position de la fenêtre
Largeur = fenetre.winfo_screenwidth()
Hauteur = fenetre.winfo_screenheight()
    #Crée la position
positionFenetre = "530x180+"+str(3*(Largeur//7))+"+"+str(3*(Hauteur//7))
    #Positionne la fenêtre
fenetre.geometry(positionFenetre)
#--------------------           Texte Golds Total
TexteGoldTotal = StringVar()
PhraseTexteGoldTotal = "Vous  avez  "+str(GoldTotal)+"  pieces"
TexteGoldTotal.set(PhraseTexteGoldTotal)
MessageGoldTotal = Label(fenetre, textvariable = TexteGoldTotal,fg="#EEE2AF",bg="#533007",font = ("Karmatic Arcade",14))
MessageGoldTotal.pack(side="top",fill=X)

#--------------------           Coin
    #Boutton Coin
PhraseTexteBouttonCoin ="       Coin - lvl "+str(LvlCoin)+"       "
TexteBouttonCoin = StringVar()
TexteBouttonCoin.set(PhraseTexteBouttonCoin)
BouttonCoin = Button(fenetre, textvariable=TexteBouttonCoin,command=FonctionCoin)
BouttonCoin.place(x="15",y="40")
    #Message Coin
PhraseTexteCoin = "(+"+str(GoldCoin)+" pièces)"
TexteCoin = StringVar()
TexteCoin.set(PhraseTexteCoin)
MessageCoin = Label(fenetre, textvariable = TexteCoin)
MessageCoin.place(x="135",y="42")

#--------------------           Améliorer Coin
    #Boutton Améliorer Coin
BouttonAmeliorerCoin = Button(fenetre, text="       Améliorer Coin        ",command = FonctionAmeliorerCoin)
BouttonAmeliorerCoin.place(x="230",y="40")
    #Message Améliorer Coin
PhraseTexteAmeliorerCoin = "(coûte "+str(PrixAmeliorerGoldCoin)+" pièces)"
TexteAmeliorerCoin = StringVar()
TexteAmeliorerCoin.set(PhraseTexteAmeliorerCoin)
MessageAmeliorerCoin = Label(fenetre, textvariable = TexteAmeliorerCoin)
MessageAmeliorerCoin.place(x="380",y="42")

#--------------------           Plume Sacrée
    #Boutton Plume Sacrée
PhraseTexteBouttonPlumeSacree = "Plume Sacrée - lvl "+str(LvlPlumeSacree)
TexteBouttonPlumeSacree = StringVar()
TexteBouttonPlumeSacree.set(PhraseTexteBouttonPlumeSacree)
BouttonPlumeSacree = Button(fenetre, textvariable=TexteBouttonPlumeSacree,command=FonctionPlumeSacree)
BouttonPlumeSacree.place(x="15",y="90")
    #Message Plume Sacrée
PhraseTextePlumeSacree = "(+"+str(GoldPlumeSacree)+" pièces)"
TextePlumeSacree = StringVar ()
TextePlumeSacree.set(PhraseTextePlumeSacree)
MessagePlumeSacree = Label(fenetre, textvariable = TextePlumeSacree)
MessagePlumeSacree.place(x="135",y="92")

#--------------------           Améliorer Plume Sacrée
    #Boutton Améliorer Plume Sacrée
TexteBouttonAmeliorerPlumeSacree = StringVar()
TexteBouttonAmeliorerPlumeSacree.set("Débloquer Plume Sacrée")
BouttonAmeliorerPlumeSacree = Button(fenetre, textvariable=TexteBouttonAmeliorerPlumeSacree,command=FonctionAmeliorerPlumeSacree)
BouttonAmeliorerPlumeSacree.place(x="230",y="90")
    #Message Améliorer Plume Sacrée
PhraseTexteAmeliorerPlumeSacree = "(coûte "+str(PrixAmeliorerGoldPlumeSacree)+" pièces)"
TexteAmeliorerPlumeSacree = StringVar()
TexteAmeliorerPlumeSacree.set(PhraseTexteAmeliorerPlumeSacree)
MessageAmeliorerPlumeSacree = Label(fenetre, textvariable = TexteAmeliorerPlumeSacree)
MessageAmeliorerPlumeSacree.place(x="380",y="92")

#--------------------           Bec poilu
    #Boutton Bec Poilu
PhraseTexteBecPoilu = "   Bec Poilu - lvl "+str(LvlBecPoilu)+"    "
TexteBouttonBecPoilu = StringVar()
TexteBouttonBecPoilu.set(PhraseTexteBecPoilu)
BouttonBecPoilu = Button(fenetre, textvariable=TexteBouttonBecPoilu,command=FonctionBecPoilu)
BouttonBecPoilu.place(x="15",y="140")
    #Message Bec Poilu
PhraseTexteBecPoilu = "(+"+str(GoldBecPoilu)+" pièces)"
TexteBecPoilu = StringVar()
TexteBecPoilu.set(PhraseTexteBecPoilu)
MessageBecPoilu = Label(fenetre,textvariable=TexteBecPoilu)
MessageBecPoilu.place(x="135",y="142")

#--------------------           Améliorer Bec Poilu
    #Boutton Améliorer Bec Poilu
TexteBouttonAmeliorerBecPoilu = StringVar()
TexteBouttonAmeliorerBecPoilu.set("   Débloquer Bec Poilu    ")
BouttonAmeliorerBecPoilu = Button(fenetre, textvariable=TexteBouttonAmeliorerBecPoilu,command=FonctionAmeliorerBecPoilu)
BouttonAmeliorerBecPoilu.place(x="230",y="140")
    #Message Améliorer Bec Poilu
PhraseTexteAmeliorerBecPoilu = "(coûte "+str(PrixAmeliorerGoldBecPoilu)+" pièces)"
TexteAmeliorerBecPoilu = StringVar()
TexteAmeliorerBecPoilu.set(PhraseTexteAmeliorerBecPoilu)
MessageAmeliorerBecPoilu = Label(fenetre, textvariable = TexteAmeliorerBecPoilu)
MessageAmeliorerBecPoilu.place(x="380",y="142")
