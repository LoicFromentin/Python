#Entrée: 2 listes de nombres dans l'ordre croissant
#Sortie: 1 liste de nombres dans l'ordre croissant
#Fusionne 2 listes croissantes en une seule liste croissante.

def fusionCroissant (liste1,liste2):
    listeFusion=[]
    i2=0
    i=0
    while (i<=len(liste1)-1) and (i2<=len(liste2)-1):
        if liste1[i] < liste2[i2] :
            listeFusion.append(liste1[i])
            i=i+1
        else :
            listeFusion.append(liste2[i2])
            i2=i2+1
    if (i>len(liste1)-1):
        listeFusion.append(liste2[i2])
    elif (i2>len(liste2)-1):
        listeFusion.append(liste1[i])
    return(listeFusion)
