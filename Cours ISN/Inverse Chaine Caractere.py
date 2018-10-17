#Entrée: Chaine de caractères
#Sortie: Chaine de caractères
#Inverse l'ordre des caracteres d'une chaine.

def inverse(chaine):
    chaineInverse=""
    for i in range (len(chaine)):
        chaineInverse = chaineInverse + chaine[(len(chaine)-1)-i]
    return(chaineInverse)


