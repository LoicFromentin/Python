#Table de multiplication

Table = int(input("Quel nombre souhaitez-vous multiplier? "))
nombrePremier = int(input("Entrez le premier multiplicateur: "))
nombreFinal = nombrePremier - 1
while (nombreFinal < nombrePremier) :
    nombreFinal = int(input("Entrez le dernier multiplicateur: "))

for nombre in range (nombrePremier,(nombreFinal+1)):
    resultat = Table*nombre
    print(Table,"x",nombre,"=",resultat)
