#Entrée: Nombre
#Sortie: Booléen
#Dit si une année est bissextile ou non.

def anneeBissextile (annee):
    test = False
    if (annee % 100 == 0):
        if (annee % 400 == 0) :
            test = True
        else :
            test = False
    elif (annee % 4 == 0) :
        test = True
    else:
        test = False
    return (test)
    
