###################################### JEU DE DAMES ######################################

#Crée le tableau de jeu de 100 cases (10x10) vides
#Sortie: le tableau de jeu
def tableauStart ():                                    #Crée le plateau de jeu VIDE
    tableau = []
    for i in range (100):                               #100 cases (10x10)
        tableau.append ("     ")
    return (tableau)

#Affiche le plateau de jeu
def afficherTableau ():
    print("Voici le Plateau de jeu:")
    tableauPlace = 0
    for ligne in range (10):                            #Balaye les lignes
        afficherLigne = []
        for colonne in range (10):                      #Balaye les colonnes
            afficherLigne.append(tableau[tableauPlace])
            tableauPlace = tableauPlace+1
        print("    --------------------------------------------------------------------------------    ") #séparations horizontales
        print('   | ',' | '.join(afficherLigne),'|   ')                                                   #Affiche le contenu de chaque case + une barre verticale entre chaque case
    print("    --------------------------------------------------------------------------------    ")     #Dernière ligne du tableau
    print("\n")

#Permet de définir les cases jouables du tableau
#Sortie: liste des cases jouables
def caseJouable ():
    listeCasesJouables = []
    case = 1                                    #Première case jouable
    for i in range (50):                        #50 cases jouables
        listeCasesJouables.append(case)
        if case in (9,29,49,69,89):             #Dernière colonne
            case = case + 1
        elif case in (18,38,58,78):             #Avant dernière colonne
            case = case + 3
        else:                                   #Autres colonnes
            case = case + 2
    return(listeCasesJouables)

#Place les 20 pions Noirs et 20 Blancs dans le tableau (pour le début de la partie
#Sortie: le tableau de jeu
def pionsStart ():
    for pion in range (0,20):                   #20 pions Noirs
        tableau[listeCasesJouables[pion]] = "BLACK"
    for pion in range (30,50):                  #20 pions Blancs
        tableau[listeCasesJouables[pion]] = "WHITE"
    return (tableau)

#Test s'il est possible de créer une dame Blanche (ligne haut)
#Sortie: le tableau de jeu
def dameBlanche():  
    tableauPlace = 0
    for case in range (5):
        if tableau [tableauPlace] == "WHITE":
            tableau[tableauPlace] = "DameWHITE"
        tableauPlace = tableauPlace+2
    return (tableau)

#Test s'il est possible de créer une dame Noire (ligne bas)
#Sortie: le tableau de jeu
def dameNoire ():   
    tableauPlace = 90
    for case in range  (5): 
        if tableau [tableauPlace] == "BLACK": 
            tableau[tableauPlace] = "DameBLACK"
            tableauPlace = tableauPlace+2
    return (tableau)

#Demande si les joueurs veulent rejouer.
#Sortie: Booléen
def rejouer ():
    replay = ""
    while replay not in ("oui","yes","no","non","nope","nop"):
        replay = input("Souhaitez-vous rejouer? ")
        replay = replay.lower()
    if replay in ("oui","yes"):
        return (True)
    else:
        return(False)

#Permet au joueur de choisir le pion avec lequel il va jouer.
def choixCase ():
    case = 42
    while case not in listeCasesJouables and tableau[case] != joueur:
        case = int(input("Veuillez choisir un pion à déplacer: "))
        if case not in listeCasesJouables:
            print("Cette case n'est pas valide.")
            case = 42
        if tableau[case] != joueur:
            print("Le pion choisi n'est pas à vous.")
            case = 42
    return(case)

#Permet au joueur de choisir la case où déplacer son pion et le déplace.
def deplacement (case):
    if case % 10 == 0:              #Colonne de gauche
        direction = ""
        while direction !="d":
            direction = input("Veuillez saisir une direction avec 'Q' ou 'D': ")
            direction=direction.lower()
            if direction == "q":
                print("Vous ne pouvez pas vous déplacer en dehors du plateau")
    elif case in (9,29,49,69,89):   #colonne de droite
        direction = ""
        while direction !="q":
            direction = input("Veuillez saisir une direction avec 'Q' ou 'D': ")
            direction=direction.lower()
            if direction == "d":
                print("Vous ne pouvez pas vous déplacer en dehors du plateau")
    else:                           #autres colonnes
        direction = ""
        while direction not in ("q","d"):
            direction = input("Veuillez saisir une direction avec 'Q' ou 'D': ")
            direction=direction.lower()
    if direction == "q":
        if joueur == "BLACK":
            tableau[case],tableau[case+9] = tableau[case+9],tableau[case]
        if joueur == "WHITE":
            tableau[case],tableau[case-11] = tableau[case-11],tableau[case]
    else:
        if joueur == "BLACK":
            tableau[case],tableau[case+11] = tableau[case+11],tableau[case]
        if joueur == "WHITE":
            tableau[case],tableau[case-9] = tableau[case-9],tableau[case]
    return(case)

#Test la diagonale directe (si ennemie) et diagonale+1 (si vide). (True / False)
#Sortie: Booléen (True / False)
def verification (listeCasesJouables):
    listeReturn = []
    compteur = 0
    testVerification = False                            #set up
    testDiagonale = False                               #set up
    impossibleDroite = [18,29,38,49,58,69,78]           #liste 2 colonnes droite
    impossibleGauche = [21,30,41,50,61,70,81]           #liste 2 colonnes gauches
    impossibleHaut = [3,5,7,12,14,16,18]                #liste 2 lignes haut
    impossibleBas = [81,83,85,87,92,94,96]              #liste 2 lignes bas
    impossibleBasDroite = [89,98]                       #liste coin bas droite
    impossibleHautGauche = [1,10]                       #liste coin haut gauche
    impossibleBasGauche = 90                            #place coin bas gauche
    impossibleHautDroite = 9                            #place coin haut droite
    print("Case = ",case)
    #Si le pion choisi est dans le coin haut droit
    if case == impossibleHautDroite:
        diagonale = case + 9                            #diagonale directe
        if tableau[diagonale] != joueur and tableau[diagonale] != '     ':
            #S'il y a un pion ennemie
            testDiagonale = True                        #test = True
        if testDiagonale == True:                       #Si test = True
            diagonale2 = case - 9                       #diagonale indirecte
            if tableau[diagonale2] == '     ':          #Si diagonale indirecte vide
                testVerification = True                 #test = True
    #Si le pion est dans le coin haut gauche
    if case in (impossibleHautGauche):
        diagonale = case + 11
        if tableau[diagonale] != joueur and tableau[diagonale] != '     ':
            #S'il y a un pion ennemie
            testDiagonale = True                        #test = True
        if testDiagonale == True:                       #Si test = True
            diagonale2 = case+11                        #diagonale indirecte
            if tableau[diagonale2] == '     ':          #Si diagonale indirecte vide
                testVerification = True                 #test = True
    #Si le pion est dans le coin bas gauche
    if case == impossibleBasGauche:
        diagonale = case - 9                            #diagonale directe
        if tableau[diagonale] != joueur and tableau[diagonale] != '     ':
            #S'il y a un pion ennemie
            testDiagonale = True                        #test = True
        if testDiagonale == True:                       #Si test = True
            diagonale2 = case - 18                      #diagonale indirecte
            if tableau[diagonale2] == '     ':          #Si diagonale indirecte vide
                testVerification = True                 #test = True
    #Si le pion est dans le coin bas droite
    if case in (impossibleBasDroite):
        diagonale = case - 11
        if tableau[diagonale] != joueur and tableau[diagonale] != '     ':
            #S'il y a un pion ennemie
            testDiagonale = True                        #test = True
        if testDiagonale == True:                       #Si test = True
            diagonale2 = case-11                        #diagonale indirecte
            if tableau[diagonale2] == '     ':          #Si diagonale indirecte vide
                testVerification = True                 #test = True
    #Si le pion choisi est sur une des 2 colonnes de Droite
    if case in (impossibleDroite):                      #si le pion est dans les 2 colonnes de droite
        diagonale = [case+9,case-11]                    #liste diagonales directes
        place = 0                                       #place dans la liste diagonales directes
        while testDiagonale == False and place < 1:     #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes
            if tableau[diagonale[place]] == joueur or tableau[diagonale[place]] == '     ':
                #S'il n'ya a pas de pion ennemie:
                place += 1                              #on avance dans la liste
            else:
                testDiagonale = True                    #sinon, test=True
        if testDiagonale == True:                       #si un ennemie sur diagonales directes
            diagonale2 = [case+18,case-22]              #liste diagonales indirectes
            if tableau[diagonale2[place]] != '     ':   #Si la diagonale indirectes n'est pas vide
                place += 1                              #on avance dans la liste
            else:
                testVerification = True                 #sinon, test = True
    #Si le pion choisi est sur une des 2 colonnes de Gauche
    if case in (impossibleGauche):                      #si le pion est dans 2 colonnes de gauche
        diagonale = [case-9,case+11]                    #liste diagonales directes
        place = 0                                       #place dans la liste diagonales directes
        while testDiagonale == False and place < 1:     #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes
            if tableau[diagonale[place]] == joueur or tableau[diagonale[place]] == '     ':
                #S'il n'y a pas de pion ennemie:
                place += 1                              #on avance dans la liste
            else:
                testDiagonale = True                    #sinon, test=True
        if testDiagonale == True:                       #si un ennemie sur diagonales directes
            diagonale2 = [case-18,case+22]              #liste diagonales indirectes
            if tableau[diagonale2[place]] != '     ':   #Si la diagonale indirecte n'est pas vide
                place += 1                              #on avance dans la liste
            else:
                testVerification = True                 #sinon, test=True
    #Si le pion choisi est sur une des 2 lignes du haut
    if case in (impossibleHaut):
        diagonale = [case+9,case+11]                    #liste des diagonales directes
        place = 0                                       #place dans la liste diagonales directes
        while testDiagonale == False and place < 1:     #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes
            if tableau[diagonale[place]] == joueur or tableau[diagonale[place]] == '     ':
                #S'il n'y a pas d'ennemie:
                place = place + 1                       #On avance dans la liste
            else:
                testDiagonale = True                    #sinon, test=True
        if testDiagonale == True:                       #si un ennemie sur diagonales directes
            diagonale2 = [case+18,case+22]              #liste diagonales indirectes
            if tableau[diagonale2[place]] != '     ':   #Si la diagonale indirecte n'est pas vide
                place = place + 1                       #On avance dans la liste
            else:
                testVerification = True                 #Sinon, test = True
    
    #Si le pion choisi est sur une des 2 lignes du bas
    if case in (impossibleBas):
        diagonale = [case-9,case-11]                    #Liste diagonales directes
        place = 0                                       #Place dans la liste
        while testDiagonale == False and place < 1:     #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes
            if tableau[diagonale[place]] == joueur or tableau[diagonale[place]] == '     ':
                #S'il n'y a pas d'ennemie
                place = place + 1                       #On avance dans la liste
            else:
                testDiagonale = True                    #Sinon, test = True
        if testDiagonale == True:                       #Si ennemmie sur diagonale directe
            diagonale2 = [case-18,case-22]              #Liste diagonales indirectes
            if tableau[diagonale2[place]] != '     ':   #Si la diagonale indirecte n'est pas vide
                place = place + 1                       #On avance dans la liste
            else:
                testVerification = True                 #Sinon, test = True
                
    #Si le pion choisi est dans le carré central
    else:
        diagonale = [case+9,case-9,case+11,case-11]     #liste diagonales directes
        place = 0                                       #place dans la liste diagonales directes
        while testDiagonale == False and place < 4:     #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes
            print("place =",place)
            print("Diago =",diagonale[place])
            if tableau[diagonale[place]] == joueur or tableau[diagonale[place]] == '     ':
                #S'il n'y a pas de pion ennemie:
                place += 1                              #on avance dans la liste
            else:
                testDiagonale = True                    #sinon, test=True
        if testDiagonale == True:                       #si un ennemie sur diagonales directes
            diagonale2 = [case+18,case-18,case+22,case-22]  #Diagonales indirectes
            if tableau[diagonale2[place]] != '     ':   #si la 2° diagonale est vide
                place += 1                              #on avance dans la liste
            else:
                testVerification = True                 #sinon, test=True
    if testVerification == True:                    #Si test = True
        CaseEnnemie = diagonale[place]              #Position du pion ennemie à manger
        CaseVerifie = diagonale2[place]             #Position de la case où tu atteris après avoir manger
        print("Vous pouvez manger le pion sur la case",CaseEnnemie,"!")
        listeVariable = [testVerification,CaseEnnemie,CaseVerifie,case]
        listeReturn.append(listeVariable)
        compteur = compteur + 1
    elif testVerification == False:
        listeReturn = [testVerification]
    return(listeReturn)                             #True ou False

def manger(case,vieBLACK,vieWHITE):
    choixCase = 666
    while choixCase != listeVerification[1]:
        choixCase = int(input("Veuillez saisir la case du pion à manger: "))
        if choixCase != listeVerification[1]:
            print("Vous n'avez pas choisi le pion à manger!")
    tableau[listeVerification[1]] = '     '
    tableau[listeVerification[2]] = joueur
    tableau[case] = '     '
    print("Félicitation, vous avez mangé un pion adverse!")
    if joueur == "BLACK":
        vieWHITE -= 1
    if joueur == "WHITE":
        vieBLACK -= 1
    return(vieBLACK,vieWHITE)
    
############### PROGRAMME PRINCIPAL ###############

#---# Set up start #---#
    
vieBlack = 1                            #Création de la variable "vie" pour les Noirs
vieWhite = 1                            #Création de la variable "vie" pour les Blancs
tableau = tableauStart ()               #Crée le plateau de jeu VIDE
listeCasesJouables = caseJouable()      #Set up les cases jouables dans la liste: "listeCasesJouables"
pionsStart()                            #Place les pions noirs et blancs au début du jeu
afficherTableau()                       #Affiche le plateau de jeu
tour = 1                                #Set up variable
vieBLACK = 20
vieWHITE = 20

#---# Début du jeu #---#

rejouer = True
while vieBLACK != 0 and vieWHITE != 0 :  #Joue tant qu'il reste des pions et tant que l'utilisateur veut rejouer. 
    if (tour%2 == 0) :          #Si tour paire
        joueur = "BLACK"
        print("C'est au tour des [BLACK] de jouer.")
        #Boucle pour faire verification() pour tous les pions avant de jouer
        listePionJoueur = []
        for element in range (len(listeCasesJouables)):
            if tableau[listeCasesJouables[element-1]] == joueur:
                listePionJoueur.append(listeCasesJouables[element-1])
        for element in range (len(listePionJoueur)):
            case = listePionJoueur[element-1]
            listeVerification = verification(listeCasesJouables)        
        if listeVerification[0] == True:
            vieBLACK,vieWHITE = manger(case,vieBLACK,vieWHITE)
        if listeVerification[0] == False:
            case = choixCase()
            case = deplacement(case)
    if (tour%2 != 0) :          #Si tour impaire
        joueur = "WHITE"
        print("C'est au tour des [WHITE] de jouer.")
        #Boucle pour faire verification() pour tous les pions avant de jouer
        listePionJoueur = []
        for element in range (len(listeCasesJouables)):
            if tableau[listeCasesJouables[element-1]] == joueur:
                listePionJoueur.append(listeCasesJouables[element-1])
        print(listePionJoueur)
        for element in range (len(listePionJoueur)):
            case = listePionJoueur[element-1]
            listeVerification = verification(listeCasesJouables)        
        if listeVerification[0] == True:
            vieBLACK,vieWHITE = manger(case,vieBLACK,vieWHITE)
        if listeVerification[0] == False:
            case = choixCase()
            case = deplacement(case)
    print("Les Blancs possèdent encore",vieWHITE,"pions !")
    print("Les Noirs possèdent encore",vieBLACK,"pions !")
    print("\n")
    afficherTableau()           #Affiche le tableau
    tour = tour+1
