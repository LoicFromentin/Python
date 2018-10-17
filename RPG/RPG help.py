def NombreMonstreATuer_Lvl50 ():
    ''' 1176 '''
    n = 48 #Car on est lvl 49
    NombreATuer = (n*(n+1))/2
    print(NombreATuer)

def CalculXpDonneMonstre ():
    ''' Dans le cas où on doit gagner 200xp en tuant 8 monstres '''
    MonstreEtXp = []
    XpDonne = 0
    NombreMonstreATuer = 8
    XpToLvlUp = 200
    NumeroMonstre = 1
    S = (NombreMonstreATuer*(NombreMonstreATuer+1))/2
    print("S =",S)
    for i in range (NombreMonstreATuer):
        XpDonne = NumeroMonstre*XpToLvlUp
        listeTemporaire = [NumeroMonstre,XpDonne]
        MonstreEtXp.append(listeTemporaire)
        NumeroMonstre += 1
    print(MonstreEtXp)

def CalculHpLvl_50():
    ''' HP_LVL_50 = 758 369 '''
    HP = 100
    Multiplicateur = 1.2
    for i in range (49):
        NewHP = HP*Multiplicateur
        HP = NewHP
    print(int(HP))


