#Entrée: 1 liste de nombres
#Sorties: 1 nombre
#Cette fonction sert à renvoyer l'index de l'élément ayant la plus grande valeur dans une liste.
def indexMax(liste):
    a,b = 0,0    
    while a < len(liste):
        if (liste[a] > b):
            b,maximum = liste[a],a
        a = a+1
    return maximum
