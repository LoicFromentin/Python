def ListeDansLordre(liste):                                                       
    i=0
    while (i<len(liste)-1 and liste[i]<liste[i+1]):
        i=i+1
        return (i=len(liste)-1)

def ListeDansLordre(liste):
    i=0
    ordre=True
    while (ordre and i<len(liste)-1):
        if liste[i]>liste[i+1]:
            ordre=False
        i=i+1
    return(ordre)

#Entrée: 1 liste
#Sortie: Test
#Cette fonction permet de vérifier si une liste est dans l'ordre croissant.

def TestCroissant (liste):
    ordre=True
    element=liste[0]
    for i in liste:
        if element>i :
            ordre=False
        element=i   
    return (ordre)
