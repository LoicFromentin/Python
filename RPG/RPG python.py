from random import *

#--------------------# AIDE #--------------------#

''' Voir dans le fichier RPG Help.py '''

#--------------------# FONCTIONS #--------------------#

def LvlUpPerso (LvlPerso,XP,HpPersoMax,HpPerso,PMMax,PM,DegatsPerso,DegatsSortPerso,XpLvlUp):
    LvlPerso = LvlPerso +1
    XP = 0
    HpPersoMax = HpPersoMax +50
    PMMax = int(PMMax *(1.4))
    DegatsPerso = int(DegatsPerso *(1.4))
    DegatsSortPerso = int(DegatsSortPerso*(1.4))
    XpLvlUp = XpLvlUp +20
    HpPerso = HpPersoMax
    PM = PMMax
    print("\n----------------------------------------------------------------------------\n")
    print("VOUS VENEZ DE LVL UP! Vous êtes maintenant lvl",LvlPerso,".\n")
    print("----------------------------------------------------------------------------\n")
    return(LvlPerso,XP,HpPersoMax,HpPerso,PMMax,PM,DegatsPerso,DegatsSortPerso,XpLvlUp)

def PasLvlUpPerso (HpPersoMax, HpPerso, XP):
    print("\n")
    print("----------------------------------------------------------------------------")
    print("\n")
    print("Vous mangez la dépouille du monstre et votre vie remonte de",int((1/5)*HpPersoMax),"!")
    print("\n")
    print("----------------------------------------------------------------------------")
    print("\n")
    HpPerso = HpPerso + int((1/5)*HpPersoMax)
    return(HpPerso)

def LvlUpMonstre (LvlMonstre,HpMonstreMax,HpMonstre,DegatsMonstre):
    LvlMonstre = LvlMonstre + 1
    print("Un monstre de lvl",LvlPerso,"vous attaque!\n")
    print("----------------------------------------------------------------------------\n")
    HpMonstreMax = HpMonstreMax + (10*LvlMonstre)
    DegatsMonstre = DegatsMonstre +2
    HpMonstre = HpMonstreMax
    return (LvlMonstre,HpMonstreMax,HpMonstre,DegatsMonstre)

def TourJoueur(PM):
    action = ""
    while action not in ("sort","attaque","a","s"):
        action = input("Vous avez le choix entre lancer un 'sort' ou une 'attaque': ")
        action.lower()
        if action == "a":action = "attaque"
        if action == "s": action = "sort"
        if action not in ("sort","attaque"):
            print("Vous n'avez pas choisi une action possible: 'sort' ou 'attaque'.\n")
        if action in ("sort") and PM < 5:
            print("Vous n'avez pas assez de Points de Mana pour lancer un sort.\n")
            action = ""
    return(action)

def Sort (HpMonstre,PM,DegatsSortPerso):
    PM = PM - 5
    HpMonstre = HpMonstre - DegatsSortPerso
    print("Vous lui avez enlevé 20 PV en dépit de 5 PM")
    return(HpMonstre,PM)

def Attaque (HpMonstre,DegatsPerso):
    DegatsAleatoire = randint(LvlPerso-1,LvlPerso+2)
    if DegatsAleatoire < 0:
        DegatsAleatoire = 0
    HpMonstre = HpMonstre - (DegatsPerso + DegatsAleatoire)
    print("Vous lui avez enlevé",(DegatsPerso + DegatsAleatoire),"PV")
    return(HpMonstre)

def AttaqueMonstre (HpPerso,DegatsMonstre,LvlMonstre):
    DegatsAleatoire = randint(LvlMonstre-1,LvlMonstre+2)
    if DegatsAleatoire < 0:
        DegatsAleatoire = 0
    HpPerso = HpPerso - (DegatsMonstre + DegatsAleatoire)
    print("Vous avez perdu",(DegatsMonstre + DegatsAleatoire),"PV")
    return(HpPerso)


#--------------------# Variables Perso #--------------------#

LvlPerso = 1
HpPersoMax = 100
HpPerso = 100
PMMax = 20
PM = 20
XP = 0
DegatsPerso = 10
DegatsSortPerso = 20
XpLvlUp = 10

#--------------------# Variables Monstre #--------------------#

LvlMonstre = 1
HpMonstreMax = 100
HpMonstre = 100
DegatsMonstre = 7

#--------------------# PROGRAMME PRINCIPAL #--------------------#

while HpPerso > 0:
    tour = 1
    
    while HpMonstre > 0 and HpPerso > 0:
        if tour%2 != 0:
            print("C'est à votre tour de jouer!")
            print("Vous avez",PM,"PM et",HpPerso,"PV")
            print("Le monstre a",HpMonstre,"PV\n")
            action = TourJoueur(PM)
            if action == "sort":
                HpMonstre,PM = Sort(HpMonstre,PM,DegatsSortPerso)
            elif action == "attaque":
                HpMonstre = Attaque(HpMonstre,DegatsPerso)
        #HpMonstre = 0
        if tour%2 == 0:
            print("Le monstre vous attaque!")
            HpPerso = AttaqueMonstre (HpPerso,DegatsMonstre,LvlMonstre)
        tour = tour+1
        print("\n")
        print("----------------------------------------------------------------------------")
        print("\n")
    if HpPerso > 0:
        XP = XP+(10*LvlMonstre)
        print("\n"*40)
        print("Bravo, vous avez tué le monstre!\nVous avez donc gagné",(10*LvlMonstre),"XP.")
        if XP < XpLvlUp:
            HpPerso = PasLvlUpPerso (HpPersoMax, HpPerso, XP)
        if XP >= XpLvlUp:
            LvlPerso,XP,HpPersoMax,HpPerso,PMMax,PM,DegatsPerso,DegatsSortPerso,XpLvlUp = LvlUpPerso (LvlPerso,XP,HpPersoMax,HpPerso,PMMax,PM,DegatsPerso,DegatsSortPerso,XpLvlUp)            
        LvlMonstre,HpMonstreMax,HpMonstre,DegatsMonstre = LvlUpMonstre (LvlMonstre,HpMonstreMax,HpMonstre,DegatsMonstre)

print("Vous avez succombé aux attaques du monstre...")
