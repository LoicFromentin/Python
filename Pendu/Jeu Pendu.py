#################### FONCTIONS ####################
from random import *

def cacherMot ():
    for lettre in range(len(motDeviner)):
        if motDeviner[lettre] in separateurs:
            motCache.append(motDeviner[lettre])
        else:
            motCache.append("_")
    return(motCache)

def afficherMotCache ():
    print("\nVoici le mot à deviner: ")
    print(" ".join(motCache))
    print("\n")

def afficherLettreTest ():
    if len(essais)>0:
        print ("Liste des lettres testées ne faisant pas partie du mot:")
        print (' | '.join(essais))

def jouer (lettreDansMot,vie):
    for lettre in range(len(motDeviner)):
        if lettreTest == motDeviner[lettre]:
            motCache[lettre] = motDeviner[lettre]
            lettreDansMot = True
    if lettreDansMot == True:       #Si hypothèse fait partie du motDeviner
        print("La lettre [",lettreTest,"] fait partie du mot à deviner.\n")
    if lettreDansMot == False:      #Si hypothèse ne fait pas partie du motDeviner
        lettreDejaTest = 0
        for element in range (len(essais)):
            if essais[element] == lettreTest:
                lettreDejaTest+=1
        if lettreDejaTest == 0:     #Si la lettre fausse n'a pas déjà été entrée:
            essais.append(lettreTest)
            vie = vie-1
            print ("La lettre [",lettreTest,"] ne fait pas partie du mot à deviner.\nVous avez perdu une vie.\n")
        elif lettreDejaTest > 0:    #Si la lettre fausse a déjà été entrée:
            print ("Vous avez déjà essayé la lettre [",lettreTest,"], elle ne fait pas partie du mot.\n")
    return(vie)

def dessin ():
    if vie == 10:
        print(" ------------------ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 9:
        print(" ------------------ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 8:
        print(" ------------------ ")
        print("|                  |")
        print("|                  |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 7:
        print(" ------------------ ")
        print("|                  |")
        print("|       ------     |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 6:
        print(" ------------------ ")
        print("|                  |")
        print("|       ------     |")
        print("|       |/         |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 5:
        print(" ------------------ ")
        print("|                  |")
        print("|       ------     |")
        print("|       |/   |     |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 4:
        print(" ------------------ ")
        print("|                  |")
        print("|       ------     |")
        print("|       |/   |     |")
        print("|       |    O     |")
        print("|       |          |")
        print("|       |          |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 3:
        print(" ------------------ ")
        print("|                  |")
        print("|       ------     |")
        print("|       |/   |     |")
        print("|       |    O     |")
        print("|       |    |     |")
        print("|       |          |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 2:
        print(" ------------------ ")
        print("|                  |")
        print("|       ------     |")
        print("|       |/   |     |")
        print("|       |    O     |")
        print("|       |   -|-    |")
        print("|       |          |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 1:
        print(" ------------------ ")
        print("|                  |")
        print("|       ------     |")
        print("|       |/   |     |")
        print("|       |    O     |")
        print("|       |   -|-    |")
        print("|       |   |      |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    if vie == 0:
        print(" ------------------ ")
        print("|                  |")
        print("|       ------     |")
        print("|       |/   |     |")
        print("|       |    O     |")
        print("|       |   -|-    |")
        print("|       |   | |    |")
        print("|       |          |")
        print("|    ----------    |")
        print("|                  |")
        print(" ------------------ ")
    
def finGame ():
    if vie == 0:
        print ("Dommage, vous avez perdu!\nLe mot à trouver était:",motDeviner,"\nVous y arriverez peut-être la prochaine fois :)")
    elif vie == 10:
        print ("Bravo! Vous avez trouvé le mot [",motDeviner,"] en un seul coup!\nVous êtes un être supérieur!")
    else:
        print ("Bravo! Vous avez trouvé le mot [",motDeviner,"] en",(10-vie),"coups!")

def replay (rejouer):
    question = ""
    while question not in ("oui","non","yes","no"):
        question = input("\nVoulez-vous rejouer? ")
        question = question.lower()
    if question in ("non","no"):
        rejouer = False
    return(rejouer)
        
#################### PROGRAMME PRINCIPAL ####################

dicoOrdiDifficile = ["lithosphérique","polymorphe","velocipede","metaphorique","haussebecquait","hedonisme","hirondelles","methylisothiazolinone","caiman","anatomocytopathologie","ornithorynque","zygomatique","qualification","coccyx","testosterone","zoocryptologie","whisky","carrousel","caparaconner"," bechamel","cuauhtemoc","dilemme","drolatique","exorbitant","etymologique","hyperthermie","mnemotechnique"]
dicoOrdiFacile = ["jazz","poulet","imprimante","ombrelle","table","chaise","porcelaine","pantalon","calculette","calculatrice","canard","coin","poney","cheval","bateau","carreau","gateau","ciel","nuage","bouteille","kiwi","ecouteur","porte-feuille","sexisme","biscuit","camera","wesh","tableau","bureau","nourriture","familial","difficile","camion poubelle","detritus","feministe","macho","manchot","pinguin","cardiaque"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
separateurs = [" ","-","'",'""']
ListeAdversaire = ['joueur','autre joueur','autre','ordinateur',"l'ordinateur","l'ordi",'ordi']
rejouer = True

while rejouer == True:
    vie = 10
    motDeviner = ""
    motCache=[]
    essais =[]
    ordiOuJoueur = ""
    while ordiOuJoueur not in ListeAdversaire:
        ordiOuJoueur = input ("Souhaitez vous jouer contre [Ordinateur] ou contre un [Autre Joueur]? ")
        ordiOuJoueur = ordiOuJoueur.lower()
        
    ##----------## CONTRE ORDINATEUR ##----------##
        
    if ordiOuJoueur in ('ordinateur',"l'ordinateur","l'ordi",'ordi'):
        niveau = ""
        while niveau not in ('facile','difficile'):
            niveau = input ("Veuillez tout d'abord choisir entre le niveau [Facile] ou [Difficile]: ")
            niveau = niveau.lower()
        print("\n"*40)
            
        #-----# NIVEAU FACILE #-----#
            
        if (niveau == 'facile'):
            randomNumber = randint (0,(len(dicoOrdiFacile)))
            motDeviner = dicoOrdiFacile[randomNumber]
            cacherMot()
            while (' '.join(motCache)) != (' '.join(motDeviner)) and (vie > 0) :
                lettreDansMot= False
                afficherMotCache ()
                afficherLettreTest()
                lettreTest = ""
                while lettreTest not in (alphabet):
                    lettreTest = input("\nVeuillez entrer une lettre à tester: ")
                    lettreTest = lettreTest.lower()
                    if lettreTest not in (alphabet):
                        print("\nVous n'avez pas entré une lettre de l'alphabet.")
                print("\n"*35)
                vie = jouer(lettreDansMot,vie)
                dessin ()

            #-----# NIVEAU DIFFICILE #-----#
                
        elif (niveau == 'difficile'):
            randomNumber = randint (0,(len(dicoOrdiDifficile)))
            motDeviner = dicoOrdiDifficile[randomNumber]
            cacherMot()
            while (' '.join(motCache)) != (' '.join(motDeviner)) and (vie > 0) :    
                lettreDansMot = False
                afficherMotCache()
                afficherLettreTest()
                lettreTest = ""
                while lettreTest not in (alphabet):
                    lettreTest = input("\nVeuillez entrer une lettre à tester: ")
                    lettreTest = lettreTest.lower()
                    if lettreTest not in (alphabet):
                        print("\nVous n'avez pas entré une lettre de l'alphabet.")
                print("\n"*35)
                vie = jouer(lettreDansMot,vie)
                dessin ()

    ##----------## CONTRE JOUEUR ##----------##
            
    if ordiOuJoueur in ('joueur','autre joueur','autre'):
        while motDeviner == "":
            motDeviner = input("\nVeuillez entrer  le mot à faire deviner: ")
            motDeviner = motDeviner.lower()
        for lettre in range(len(motDeviner)):
            if motDeviner[lettre] not in (alphabet) and motDeviner[lettre] not in (separateurs):
                print("Vous avez utilisé des caractères spéciaux (accents ou autre).")
                motDeviner = ""
        print("\n"*40)      #Cacher le mot à faire deviner
        cacherMot()
        while (' '.join(motCache)) != (' '.join(motDeviner)) and (vie > 0) :
            lettreDansMot = False
            afficherMotCache()
            afficherLettreTest()
            lettreTest = ""
            while lettreTest not in (alphabet):
                lettreTest = input("\nVeuillez entrer une lettre à tester: ")
                lettreTest = lettreTest.lower()
                if lettreTest not in (alphabet):
                    print("\nVous n'avez pas entré une lettre de l'alphabet.")
            print("\n"*35)
            vie = jouer(lettreDansMot,vie)
            dessin()
    finGame()
    rejouer = replay(rejouer)
print("\n"*3)
print("Votre partie est terminée, bonne journée :)")
