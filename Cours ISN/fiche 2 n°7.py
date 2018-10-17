#Entrée: Un nombre entier (1<=n<=12)
#Sortie: Une chaine de caractères
#Fonction qui renvoie le nom du n-ième mois de l'année

def nomMois(n):
    mois=[0,'Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
    return (mois[n])

print(nomMois(4))
