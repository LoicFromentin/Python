#Entrées: 3 nombres
#Sorties: 1 nombre
#Multiplie les 3 nombres
def Produit3Nombres (a,b,c):
    return(a*b*c)

#----- Calcule le volume d'un parallélépipède rectangle -----#

largeur=float(input("Entrer la valeur de la Longueur du parallélépipède rectangle: "))
hauteur=float(input("Entrer la valeur de la Hauteur du parallélépipède rectangle: "))
profondeur=float(input("Entrer la valeur de la Profondeur du parallélépipède rectangle: "))
print("\nLe volume du parallélépipère rectatgle est: ",Produit3Nombres(largeur,hauteur,profondeur))
