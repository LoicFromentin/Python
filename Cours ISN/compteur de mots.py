#Entrée: Mots
#Sortie: Nombre
#Compte combien il y a de mots dans une suite de mots.

def compteurMots (phrase):
    compteur = 0
    separateurs = [" ",",",".",";",":","'",'"',"/","*","+","!","?"]
    for i in range(len(phrase)):
        if phrase[i] not in (separateurs):
            if phrase[i+1] in (separateurs):
                compteur = compteur+1
    return (compteur)
