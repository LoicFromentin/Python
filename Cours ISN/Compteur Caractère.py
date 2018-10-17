#Entrée: Chaîne de caractères
#Sortie: Nombre
#Renvoie le nombre de fois qu'un caractère est présent dans une chaîne.

def compteurCaractere(caractere,chaine):
    compteur = 0
    for position in range (len(chaine)):
        if (chaine[position] == caractere) :
            compteur = compteur+1
    return (compteur)

