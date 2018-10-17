#Entrée: 1 mot
#Sortie: 1 mot en minuscule
#Remplace les majuscules d'un mot par des minuscules.

def Majuscule_To_Minuscule (mot):
    majuscules=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    minuscules=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for element in range (len(mot)):
        for i in range (26):
            if mot[element] == majuscules[i]:
                mot[element] = minuscules[i]
    return(mot)

