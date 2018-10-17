###################################### JEU DE DAMES ######################################

#Crée le tableau de jeu de 100 cases (10x10) vides
#Sortie: le tableau de jeu
def tableauStart ():
    tableau = []                                                            #Crée la liste
    for i in range (100):                                                   #100 cases (10x10)
        tableau.append ("     ")                                            #Ajoute une case vide à la liste
    return (tableau)                                                        #Return le plateau rempli de cases vides

#Place les 20 pions Noirs et 20 Blancs dans le tableau (pour le début de la partie)
#Sortie: le tableau de jeu
def pionsStart (tableau):
    for pion in range (0,20):                                               #20 pions Noirs
        tableau[listeCasesJouables[pion]] = "BLACK"                         #Place un pion noir sur la case
    for pion in range (30,50):                                              #20 pions Blancs
        tableau[listeCasesJouables[pion]] = "WHITE"                         #Place un pion blanc sur la case
    return (tableau)

#Permet de définir les cases jouables du tableau
#Sortie: liste des cases jouables
def caseJouable ():
    listeCasesJouables = []                                                 #Crée la liste
    case = 1                                                                #Première case jouable
    for i in range (50):                                                    #50 cases jouables
        listeCasesJouables.append(case)                 	            #Ajoute la case dans la liste
        if case in (9,29,49,69,89):                                         #Dernière colonne
            case = case + 1                                                 #Passe à la case suivante
        elif case in (18,38,58,78):                                         #Avant dernière colonne
            case = case + 3                                                 #Passe à la case suivante
        else:                                                               #Autres colonnes
            case = case + 2                                                 #Passe à la case suivante
    return(listeCasesJouables)                                              #Return la liste remplie

#Affiche le plateau de jeu
def afficherTableau ():
    print("Voici le Plateau de jeu:")
    tableauPlace = 0                                                        #Crée la variable
    for ligne in range (10):                                                #Balaye les lignes
        afficherLigne = []                                                  #Liste contenant une ligne du plateau de jeu
        for colonne in range (10):                                          #Balaye les colonnes
            afficherLigne.append(tableau[tableauPlace])                     #Ajoute la case dans la liste
            tableauPlace = tableauPlace+1                                   #Avance d'une case
        print("    --------------------------------------------------------------------------------    ")#Séparations horizontales
        print('   | ',' | '.join(afficherLigne),'|   ')                                                  #Affiche le contenu de chaque case + une barre verticale entre chaque case
    print("    --------------------------------------------------------------------------------    ")    #Dernière ligne du tableau
    print("\n")

#Test s'il est possible de créer une dame
#Sortie: le tableau de jeu
def transformationDame():  
    tableauPlace = 1                                                        #Crée la variable
    for case in range (5):                                                  #Balaye les 5 cases jouables de la première ligne
        if tableau [tableauPlace] == "WHITE":                               #Si il y a un pion blanc
            tableau[tableauPlace] = "DameW"                                 #Le transforme en dame
        tableauPlace = tableauPlace+2                                       #Avance de case
        
    tableauPlace = 90                                                       #Crée la variable             
    for case in range  (5):                                                 #Balaye les 5 cases jouables de la première ligne
        if tableau [tableauPlace] == "BLACK":                               #Si il y a un pion blanc
            tableau[tableauPlace] = "DameB"                                 #Le transforme en dame
            tableauPlace = tableauPlace+2                                   #Avance de case
    return (tableau)

#Demande si les joueurs veulent rejouer.
#Sortie: Booléen
def rejouer ():
    replay = ""                                                             #Crée la variable
    while replay not in ("oui","yes","no","non","nope","nop"):              #Tant que la réponse est incorrecte:
        replay = input("Souhaitez-vous rejouer? ")                          #Demande à l'utilisateur
        replay = replay.lower()                                             #Met la variable en minuscule
    if replay in ("oui","yes"):                                             #Si la réponse est positive:
        return (True)                                                       #Renvoie TRUE
    else:                                                                   #Si la réponse est négative:
        return(False)                                                       #Renvoie FALSE

#Permet au joueur de choisir le pion avec lequel il va jouer.
def choixCase ():
    case = 42                                                               #Crée la variable (qui rentre dans la boucle)
    while case not in listeCasesJouables and (tableau[case] != Joueur or tableau[case] != DameJoueur):
        #Tant que ce n'est pas une case jouable ou que le pion n'est pas à lui:
        case = int(input("Veuillez choisir un pion à déplacer: "))
        if case not in listeCasesJouables:                                  #Tant que le joueur ne choisi pas une case jouable:
            print("Cette case n'est pas valide.")                           #Informe le joueur
            case = 42                                                       #Réinitialise la variable
        if tableau[case] != Joueur and tableau[case] != DameJoueur:         #Si le pion sur la case n'est pas à lui:
            print("Le pion choisi n'est pas à vous.")                       #Informe le joueur
            case = 42                                                       #Réinitialise la variable
    return(case)

def VerificationChoixCase ():
    testVerification = False                                                #Crée la variable
    impossibleDroite = [29,49,69,89]                                        #Liste des 2 colonnes de droite
    impossibleGauche = [10,30,50,70]                                        #Liste des 2 colonnes de gauche
    impossibleHaut = [1,3,5,7]                                              #Liste des 2 lignes du haut
    impossibleBas = [92,94,96,98]                                           #Liste des 2 lignes du bas
    impossibleBasGauche = 90                                                #Place du coin bas gauche
    impossibleHautDroite = 9                                                #Place du coin haut droite
#--------------------------------------------------------------------------    
    if case == impossibleHautDroite:                                        #Si le pion choisi est dans le coin haut droit
        diagonale = case + 9                                                #Diagonale directe
        if tableau[diagonale] == Joueur or tableau[diagonale] == DameJoueur:#S'il y a un pion allié
            testVerification = True                                         #testVerification = True
#--------------------------------------------------------------------------
    if case == impossibleBasGauche:                                         #Si le pion est dans le coin bas gauche
        diagonale = case - 9                                                #Diagonale directe
        if tableau[diagonale] == Joueur or tableau[diagonale] == DameJoueur:#S'il y a un pion allié
            testVerification = True                                         #testVerification = True
#--------------------------------------------------------------------------      
    if case in (impossibleDroite):                                          #Si le pion choisi est sur une des 2 colonnes de Droite
        diagonale = [case+9,case-11]                                        #Liste diagonales directes
        place = 0                                                           #Place dans la liste diagonales directes
        compteur = 0                                                        #Crée la variable
        for i in range (len(diagonale)):                                    #Test pour toutes les diagonales
            if tableau[diagonale[place]] == Joueur or tableau[diagonale[place]] == DameJoueur:#S'il y a un pion allié:
                compteur = compteur+1                                       #Le compteur de case pleine augmente
            place = place + 1                                               #On avance dans la liste
        if compteur == len(diagonale):                                      #Si il n'y a que des pions alliés autour:
            testVerification = True                                         #testVerification = True
#--------------------------------------------------------------------------
    if case in (impossibleGauche):                                          #Si le pion choisi est sur une des 2 colonnes de Gauche
        diagonale = [case-9,case+11]                                        #Liste diagonales directes
        place = 0                                                           #Place dans la liste diagonales directes
        compteur = 0                                                        #Crée la variable
        for i in range (len(diagonale)):                                    #Test pour toutes les diagonales
            if tableau[diagonale[place]] == Joueur or tableau[diagonale[place]] == DameJoueur:  #S'il y a un pion allié:
                compteur = compteur+1                                       #Le compteur de case pleine augmente
            place = place + 1                                               #On avance dans la liste
        if compteur == len(diagonale):                                      #Si il n'y a que des pions alliés autour:
            testVerification = True                                         #testverification = True
#--------------------------------------------------------------------------
    if case in (impossibleHaut):                                            #Si le pion choisi est sur une des 2 lignes du haut
        diagonale = [case+9,case+11]                                        #Liste des diagonales directes
        place = 0                                                           #Place dans la liste diagonales directes
        compteur = 0                                                        #Crée la variable
        for i in range (len(diagonale)):                                    #Test pour toutes les diagonales
            if tableau[diagonale[place]] == Joueur or tableau[diagonale[place]] == DameJoueur:  #S'il y a un pion allié:
                compteur = compteur+1                                       #Le compteur de case pleine augmente
            place = place + 1                                               #On avance dans la liste
        if compteur == len(diagonale):                                      #Si il n'y a que des pions alliés autour:
            testVerification = True                                         #testVerification = True
#--------------------------------------------------------------------------
    if case in (impossibleBas):                                             #Si le pion choisi est sur une des 2 lignes du bas
        diagonale = [case-9,case-11]                                        #Liste  des diagonales directes
        place = 0                                                           #Place dans la liste diagonales directes
        compteur = 0                                                        #Crée la variable
        for i in range (len(diagonale)):                                    #Test pour toutes les diagonales
            if tableau[diagonale[place]] == Joueur or tableau[diagonale[place]] == DameJoueur:  #S'il y a un pion allié:
                compteur = compteur+1                                       #Le compteur de case pleine augmente
            place = place + 1                                               #On avance dans la liste
        if compteur == len(diagonale):                                      #Si il n'y a que des pions alliés autour:
            testVerification = True                                         #testVerification = True
#--------------------------------------------------------------------------
    else:                                                                   #Si le pion pas dans 2 colonnes droite ou gauche
        diagonale = [case+9,case-9,case+11,case-11]                         #Liste diagonales directes
        place = 0                                                           #Place dans la liste diagonales directes
        compteur = 0                                                        #Crée la variable
        for i in range (len(diagonale)):                                    #Test pour toutes les diagonales
            if tableau[diagonale[place]] == Joueur or tableau[diagonale[place]] == DameJoueur:  #S'il y a un pion allié:
                compteur = compteur+1                                       #Le compteur de case pleine augmente
            place = place + 1                                               #On avance dans la liste
        if compteur == len(diagonale):                                      #Si il n'y a que des pions alliés autour:
            testVerification = True                                         #testVerification = True
            
    if testVerification == True:                                            #Si testVerification = True
        print("Ce pion ne peut pas bouger.")                                #Affiche un message d'erreur
    return(testVerification)                                                #Renvoie True ou False


#Permet au joueur de choisir la case où déplacer son pion et le déplace.
def deplacement (case):
    if case % 10 == 0:                                                      #Si la case choisie est dans la colonne de gauche
        direction = ""                                                      #Crée la variable
        while direction !="d":                                              #Si la direction choisie est "d" (droite):
            direction = input("Veuillez saisir une direction avec 'Q' ou 'D': ")#Demande la direction à l'utilisateur
            direction=direction.lower()                                     #Met la direction en minuscule
            if direction == "q":                                            #Si la direction choisie est "q" (gauche):
                print("Vous ne pouvez pas vous déplacer en dehors du plateau")#Affiche un message d'erreur
    elif case in (9,29,49,69,89):                                           #Si la case choisie est dans la colonne de droite:
        direction = ""                                                      #Crée la variable
        while direction !="q":                                              #Si la direction choisie est "q" (gauche):
            direction = input("Veuillez saisir une direction avec 'Q' ou 'D': ")#Demande la direction à l'utilisateur
            direction=direction.lower()                                     #Met la direction en minuscule
            if direction == "d":                                            #Si la direction choisie est "d" (droite):
                print("Vous ne pouvez pas vous déplacer en dehors du plateau")#Affiche un message d'erreur
    else:                                                                   #Colonnes centrales
        direction = ""                                                      #Crée la variable
        while direction not in ("q","d"):                                   #Tant qu'il ne choisit pas une direction valable:
            direction = input("Veuillez saisir une direction avec 'Q' ou 'D': ")#Demande la direction à l'utilisateur
            direction=direction.lower()                                     #Met la réponse en minuscule
    if direction == "q":                                                    #Si la direction choisie est "q" (gauche):
        if Joueur == "BLACK":                                               #Si c'est au tour des BLACK:
            tableau[case],tableau[case+9] = tableau[case+9],tableau[case]   #Déplace le pion et vide la case d'origine
        if Joueur == "WHITE":                                               #Si c'est au tour des WHITE:
            tableau[case],tableau[case-11] = tableau[case-11],tableau[case] #Déplace le pion et vide la case d'origine
    else:                                                                   #Si la direction choisie est "d" (droite):
        if Joueur == "BLACK":                                               #Si c'est au tour des BLACK:
            tableau[case],tableau[case+11] = tableau[case+11],tableau[case] #Déplace le pion et vide la case d'origine
        if Joueur == "WHITE":                                               #Si c'est au tour des WHITE:
            tableau[case],tableau[case-9] = tableau[case-9],tableau[case]   #Déplace le pion et vide la case d'origine

#Test la diagonale directe (si ennemie) et diagonale+1 (si vide). (True / False)
#Sortie: Booléen (True / False)
def verificationManger (tableau,case):
    testVerification = False                                                #Création de la variable
    testDiagonale = False                                                   #Création de la variable
    impossibleDroite = [18,29,38,49,58,69,78]                               #Liste des 2 colonnes de droite
    impossibleGauche = [21,30,41,50,61,70,81]                               #Liste des 2 colonnes de gauche
    impossibleHaut = [3,5,7,12,14,16,18]                                    #Liste des 2 lignes du haut
    impossibleBas = [81,83,85,87,92,94,96]                                  #Liste des 2 lignes du bas
    impossibleBasDroite = [89,98]                                           #Liste du coin bas droite
    impossibleHautGauche = [1,10]                                           #Liste du coin haut gauche
    impossibleBasGauche = 90                                                #Place du coin bas gauche
    impossibleHautDroite = 9                                                #Place du coin haut droite
#--------------------------------------------------------------------------
    if case == impossibleHautDroite:                                        #Si le pion choisi est dans le coin haut droit
        diagonale = case + 9                                                #Diagonale directe
        if tableau[diagonale] == Adversaire or tableau[diagonale[place]] == DameAdversaire :    #S'il y a un pion ennemie
            testDiagonale = True                                            #testDiagonale = True
        if testDiagonale == True:                                           #Si testDiagonale = True
            diagonale2 = case - 9                                           #Diagonale indirecte
            if tableau[diagonale2] == '     ':                              #Si la diagonale indirecte est vide
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------       
    elif case in (impossibleHautGauche):                                    #Si le pion est dans le coin haut gauche
        diagonale = case + 11                                               #Diagonale directe
        if tableau[diagonale] == Adversaire or tableau[diagonale] == DameAdversaire :           #S'il y a un pion ennemie
            testDiagonale = True                                            #testDiagonale = True
        if testDiagonale == True:                                           #Si testDiagonale = True
            diagonale2 = case+11                                            #Diagonale indirecte
            if tableau[diagonale2] == '     ':                              #Si la diagonale indirecte est vide
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------                
    elif case == impossibleBasGauche:                                       #Si le pion est dans le coin bas gauche
        diagonale = case - 9                                                #Diagonale directe
        if tableau[diagonale] == Adversaire or tableau[diagonale[place]] == DameAdversaire :    #S'il y a un pion ennemie:
            testDiagonale = True                                            #testDiagonale = True
        if testDiagonale == True:                                           #Si testDiagonale = True:
            diagonale2 = case - 18                                          #Diagonale indirecte
            if tableau[diagonale2] == '     ':                              #Si la diagonale indirecte est vide:
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------          
    elif case in (impossibleBasDroite):                                     #Si le pion est dans le coin bas droite
        diagonale = case - 11                                               #Diagonale directe
        if tableau[diagonale] == Adversaire or tableau[diagonale[place]] == DameAdversaire :    #S'il y a un pion ennemie:
            testDiagonale = True                                            #testDiagonale = True
        if testDiagonale == True:                                           #Si testDiagonale = True
            diagonale2 = case-11                                            #Diagonale indirecte
            if tableau[diagonale2] == '     ':                              #Si la diagonale indirecte est vide
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------          
    elif case in (impossibleDroite):                                        #Si le pion est dans les 2 colonnes de droite
        diagonale = [case+9,case-11]                                        #Liste des diagonales directes
        place = 0                                                           #Place dans la liste des diagonales directes
        while testDiagonale == False and place < 2:                         #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes:
            if tableau[diagonale[place]] == Adversaire or tableau[diagonale[place]] == DameAdversaire : #S'il y a un pion ennemie:
                TestDiagonale = True                                        #testDiagonale = True
            else:                                                           #S'il n'y a pas de pion ennemie:                                                      
                place = place + 1                                           #On avance dans la liste
        if testDiagonale == True:                                           #S'il y a un ennemie sur une diagonale directe:
            diagonale2 = [case+18,case-22]                                  #Liste des diagonales indirectes
            if tableau[diagonale2[place]] != '     ':                       #Si la diagonale indirecte n'est pas libre:
                place += 1                                                  #On avance dans la liste
            else:                                                           #Si la diagonale indirecte est libre:
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------               
    elif case in (impossibleGauche):                                        #Si le pion est dans 2 colonnes de gauche
        diagonale = [case-9,case+11]                                        #Liste des diagonales directes
        place = 0                                                           #Place dans la liste des diagonales directes
        while testDiagonale == False and place < 2:                         #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes:
            if tableau[diagonale[place]] == Adversaire or tableau[diagonale[place]] == DameAdversaire : #S'il y a un pion ennemie:
                testDiagonale = True                                        #testDiagonale = True
            else:                                                           #S'il n'y a pas de pion ennemie:
                place = place + 1                                           #On avance dans la liste            
        if testDiagonale == True:                                           #S'il y a un ennemie sur une diagonale directe:
            diagonale2 = [case-18,case+22]                                  #Liste des diagonales indirectes
            if tableau[diagonale2[place]] != '     ':                       #Si la diagonale indirecte n'est pas libre:
                place += 1                                                  #On avance dans la liste
            else:                                                           #Si la diagonale indirecte est libre:
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------       
    elif case in (impossibleHaut):                                          #Si le pion choisi est sur une des 2 lignes du haut
        diagonale = [case+9,case+11]                                        #Liste des diagonales directes
        place = 0                                                           #Place dans la liste diagonales directes
        while testDiagonale == False and place < 2:                         #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes:
            if tableau[diagonale[place]] == Adversaire or tableau[diagonale[place]] == DameAdversaire : #S'il y a un pion ennemie:
                testDiagonale = True                                        #testDiagonale = True
            else:                                                           #S'il n'y a pas de pion ennemie:
                place = place + 1                                           #On avance dans la liste
        if testDiagonale == True:                                           #S'il y a un ennemie sur une diagonale directe:
            diagonale2 = [case+18,case+22]                                  #Liste des diagonales indirectes
            if tableau[diagonale2[place]] != '     ':                       #Si la diagonale indirecte n'est pas libre:
                place = place + 1                                           #On avance dans la liste
            else:                                                           #Si la diagonale indirecte est libre:
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------   
    elif case in (impossibleBas):                                           #Si le pion choisi est sur une des 2 lignes du bas
        diagonale = [case-9,case-11]                                        #Liste des diagonales directes
        place = 0                                                           #Place dans la liste diagonales directes
        while testDiagonale == False and place < 2:                         #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes
            if tableau[diagonale[place]] == Adversaire or tableau[diagonale[place]] == DameAdversaire : #S'il y a un pion ennemie:
                testDiagonale = True                                        #testDiagonale = True
            else:                                                           #S'il n'y a pas de pion ennemie:
                place = place + 1                                           #On avance dans la liste
        if testDiagonale == True:                                           #S'il y a un ennemie sur une diagonale directe:
            diagonale2 = [case-18,case-22]                                  #Liste des diagonales indirectes
            if tableau[diagonale2[place]] != '     ':                       #Si la diagonale indirecte n'est pas vide:
                place = place + 1                                           #On avance dans la liste
            else:                                                           #Si la diagonale indirecte est libre:
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------   
    else:                                                                   #Si pion est dans le centre du plateau
        diagonale = [case+9,case-9,case+11,case-11]                         #Liste des diagonales directes
        place = 0                                                           #Place dans la liste diagonales directes
        while testDiagonale == False and place < 4:                         #Tant que pas ennemie sur diago directe / pas balayé toutes diago directes
            if tableau[diagonale[place]] == Adversaire or tableau[diagonale[place]] == DameAdversaire : #S'il y a un pion ennemie:
                testDiagonale = True                                        #testDiagonale = True
            else:                                                           #S'il n'y a pas de pion ennemie:
                place = place + 1                                           #On avance dans la liste
        if testDiagonale == True:                                           #S'il y a un ennemie sur une diagonale directe:
            diagonale2 = [case+18,case-18,case+22,case-22]                  #Liste des diagonales indirectes
            if tableau[diagonale2[place]] != '     ':                       #Si la diagonale indirecte n'est pas vide:
                place += 1                                                  #On avance dans la liste
            else:                                                           #Si la diagonale indirecte est libre:
                testVerification = True                                     #testVerification = True
#--------------------------------------------------------------------------   
    if testVerification == True:                                            #Si testVerification = True
        CaseEnnemie = diagonale[place]                                      #Position du pion ennemie à manger
        CaseVerifie = diagonale2[place]                                     #Position de la case où tu atteris après avoir manger
        print("Vous pouvez manger le pion sur la case",CaseEnnemie,"!")
        listeReturn = [True,CaseEnnemie,CaseVerifie]                        #Liste contenant le test si on peut manger, CaseEnnemie,CaseVerirife (là où on atteri)
    else:                                                                   #Si testVerification = False
        listeReturn=[False]                                                 #Liste contenant le test si on peut manger
    return(listeReturn)                                                     #True ou False

#Déplace le pion et le fait manger le pion adverse
def manger(case,vieBLACK,vieWHITE,listeVerification):
    choixCase = 666                                                         #Crée la variable (rentre dans la boucle
    while choixCase != listeVerification[1]:                                #Tant que la case choisie n'est pas celle où on peut manger un pion:
        choixCase = int(input("Veuillez saisir la case du pion à manger: "))#Demande la case
        if choixCase != listeVerification[1]:                               #Si elle ne convient pas au test:
            print("Vous n'avez pas saisi la case pion à manger.")           #Informe le joueur
    tableau[listeVerification[1]] = '     '                                 #La case "mangée" est vide
    tableau[listeVerification[2]] = Joueur                                  #Le pion du joueur va sur la case d'après
    tableau[case] = '     '                                                 #La case du pion avant de manger devient alors vide
    if Joueur == "BLACK":                                                   #Si c'est au tour des BLACK:
        vieWHITE -= 1                                                       #Les WHITE perdent une vie (pion mangé)
    if Joueur == "WHITE":                                                   #Si c'est au tour des WHITE:
        vieBLACK -= 1                                                       #Les BLACK perdent une vie (pion mangé)
    print("Félicitation, vous avez mangé un pion adverse!\n")               #Informe le joueur
    print("Les Blancs possèdent encore",vieWHITE,"pions.")                  #Informe le joueur
    print("Les Noirs possèdent encore",vieBLACK,"pions.\n")                 #Informe le joueur
    return(vieBLACK,vieWHITE)

def DéplacementDames() :   
#Les listes "caseVerif0" vont contenir les cases de déplacements possibles dans les diagonales de la Dame choisie ;
    caseVerif0HG = []   #HG pour Haut / Gauche
    caseVerif0HD = []   #HD pour Haut / Droite
    caseVerif0BG = []   #BG pour Bas / Gauche
    caseVerif0BD = []   #BD pour Bas / Droite
#Les listes "caseVerif1" vont ensuite servir à déterminer les éléments positionnés sur les cases des diagonales de la Dame choisie (Pion adverse, allié ou rien)
    caseVerif1HG = []   #HG pour Haut / Gauche
    caseVerif1HD = []   #HD pour Haut / Droite
    caseVerif1BG = []   #BG pour Bas / Gauche
    caseVerif1BD = []   #BD pour Bas / Droite
#Les listes "caseVerif2" vont contenir les listes finales des éléments des cases de déplacements possibles
    caseVerif2HG = []   #HG pour Haut / Gauche
    caseVerif2HD = []   #HD pour Haut / Droite
    caseVerif2BG = []   #BG pour Bas / Gauche
    caseVerif2BD = []   #BD pour Bas / Droite
#Les listes "caseVerif3" vont contenir les listes finales des numéros des cases de déplacements possibles
    caseVerif3HG = []   #HG pour Haut / Gauche
    caseVerif3HD = []   #HD pour Haut / Droite
    caseVerif3BG = []   #BG pour Bas / Gauche
    caseVerif3BD = []   #BD pour Bas / Droite
#Les valeurs des "caseVerif" sont les cases de déplacements possibles qui vont être stockés dans les listes "caseVerif0" ;
    caseVerifHG = case  #HG pour Haut / Gauche
    caseVerifHD = case  #HD pour Haut / Droite
    caseVerifBG = case  #BG pour Bas / Gauche
    caseVerifBD = case  #BD pour Bas / Droite
    
    if (case % 10) != 9 and 0 :
            while (caseVerifHG % 10) != 0 :
                caseVerifHG = caseVerifHG - 11          #HG pour Haut / Gauche
                caseVerif0HG.append (caseVerifHG)
            while (caseVerifHD % 10) != 9 :
                caseVerifHD = caseVerifHD - 9           #HD pour Haut / Droite
                caseVerif0HD.append (caseVerifHD)
            while (caseVerifBG % 10) != 0 :
                caseVerifBG = caseVerifBG + 9           #BG pour Bas / Gauche
                caseVerif0BG.append (caseVerifBG)
            while (caseVerifBD % 10) != 9 :
                caseVerifBD = caseVerifHD + 11          #BD pour Bas / Droite
                caseVerif0BD.append (caseVerifBD)
    elif (case % 10) == 9 :
        while (caseVerifHG % 10) != 9 :
            caseVerifHG = caseVerifHG - 11              #HG pour Haut / Gauche
            caseVerif0HG.append (caseVerifHG)
        while (caseVerifBG % 10) != 0 :
            caseVerifBG = caseVerifBG + 9               #BG pour Bas / Gauche
            caseVerif0BG.append (caseVerifBG)
    elif (case % 10) == 0 :
        while (caseVerifHD % 10) != 9 :
            caseVerifHD = caseVerifHD - 9               #HD pour Haut / Droite
            caseVerif0HD.append (caseVerifHD)
        while (caseVerifBD % 10) != 9 :
            caseVerifBD = caseVerifHD + 11              #BD pour Bas / Droite
            caseVerif0BD.append (caseVerifBD)
            
#Le joeur va désormais choisir la diagonale dans laquelle sa Dame va se diriger
    DameDeplacement = ""
    print("Les directions possibles sont:\nHD pour Haut / Droite ; HG pour Haut / Gauche ; BD pour Bas / Droite ; BG pour Bas / Gauche")
    while DameDeplacement not in ("HD","HG","BD","BG"):
        DameDeplacement = input("Veuillez indiquer la direction dans laquelle vous souhaitez vous déplacer : ")
        if DameDeplacement not in ("HD","HG","BD","BG"):
            print("Vous n'avez pas saisi une direction correcte.")
    CDD = 0             #Compteur 1
    CDD2 = 0            #Compteur 2
    if DameDeplacement == "HD" :
        while (CDD <= len(caseVerif0HD)-1) and (tableau[caseVerif0HD[CDD]] != Joueur and tableau[caseVerif0HD[CDD]] != DameJoueur):
                caseVerif1HD.append (tableau[caseVerif0HD[CDD]])
                CDD = CDD + 1
        while (CDD2 <= len(caseVerif1HD)-1):
            if (caseVerif1HD[CDD2] == '     ') :
                caseVerif2HD.append (caseVerif1HD[i - 1])
            elif (caseVerif1HD[CDD2] == Adversaire) or (caseVerifHD[CDD2] == DameAdversaire) :
                if (caseVerif1HD[CDD2 + 1] != Adversaire) or (caseVerifHD[CDD2 + 1] != DameAdversaire) :
                    for i in range (CDD2):
                        caseVerif2HD.append (caseVerif1HD[i - 1])          
                else:  CDD2 = CDD2 + 666
            CDD2 = CDD2 + 1
        for z in range (len(caseVerif2HD)-1):
            caseVerif3HD.append (caseVerif0HD[z])
    elif DameDeplacement == "HG" :
        while (CDD <= len(caseVerif0HG - 1)) and (tableau[caseVerif0HG[CDD]] != Joueur and tableau[caseVerif0HG[CDD]] != DameJoueur):
                caseVerif1HG.append (tableau[caseVerif0HG[CDD]])
                CDD = CDD + 1
        while (CDD2 <= len(caseVerif1HG)-1):
            if (caseVerif1HG[CDD2] == '     ') :
                caseVerif2HG.append (caseVerif1HG[i - 1])
            elif (caseVerif1HG[CDD2] == Adversaire) or (caseVerifHG[CDD2] == DameAdversaire) :
                if (caseVerif1HG[CDD2 + 1] != Adversaire) or (caseVerifHG[CDD2 + 1] != DameAdversaire) :
                    for i in range (CDD2):
                        caseVerif2HG.append (caseVerif1HG[i - 1])
                else:  CDD2 = CDD2 + 666
            CDD2 = CDD2 + 1
        for z in range (len(caseVerif2HG)-1):
            caseVerif3HG.append (caseVerif0HG[z])
    elif DameDeplacement == "BD" :
        while (CDD <= len(caseVerif0BD)-1) and (tableau[caseVerif0BD[CDD]] != Joueur and tableau[caseVerif0BD[CDD]] != DameJoueur):
                caseVerif1BD.append (tableau[caseVerif0BD[CDD]])
                CDD = CDD + 1
        while (CDD2 <= len(caseVerif1BD)-1):
            if (caseVerif1BD[CDD2] == '     ') :
                caseVerif2BD.append (caseVerif1BD[i - 1])
            elif (caseVerif1BD[CDD2] == Adversaire) or (caseVerifBD[CDD2] == DameAdversaire) :
                if (caseVerif1BD[CDD2 + 1] != Adversaire) or (caseVerifBD[CDD2 + 1] != DameAdversaire) :
                    for i in range (CDD2):
                        caseVerif2BD.append (caseVerif1BD[i - 1])
                else:  CDD2 = CDD2 + 666
            CDD2 = CDD2 + 1
        for z in range (len(caseVerif2BD)-1):
            caseVerif3BD.append (caseVerif0BD[z])
    elif DameDeplacement == "BG" :
        while (CDD <= len(caseVerif0BG)-1) and (tableau[caseVerif0BG[CDD]] != Joueur and tableau[caseVerif0BG[CDD]] != DameJoueur):
                caseVerif1BG.append (tableau[caseVerif0BG[CDD]])
                CDD = CDD + 1
        while (CDD2 <= len(caseVerif1BG)-1):
            if (caseVerif1BG[CDD2] == '     ') :
                caseVerif2BG.append (caseVerif1BG[i - 1])
            elif (caseVerif1BG[CDD2] == Adversaire) or (caseVerifBG[CDD2] == DameAdversaire) :
                if (caseVerif1BG[CDD2 + 1] != Adversaire) or (caseVerifBG[CDD2 + 1] != DameAdversaire) :
                    for i in range (CDD2):
                        caseVerif2BG.append (caseVerif1BG[i - 1])
                else:  CDD2 = CDD2 + 666
            CDD2 = CDD2 + 1
        for z in range (len(caseVerif2BG)-1):
            caseVerif3BG.append (caseVerif0BG[z])
#Le joueur va désormais choisir sur quelle case il se déplacera
    if DameDeplacement == "HD" :
        if caseVerif2HD == [] :
            print("Vous pouvez vous déplacer sur les case suivantes : ", caseVerif2HD)
            DD = int(input("Veuillez séléctionner le numéro de l'élement dans la liste (ex : 1, 2, 3...)"))
            tableau[case] = '     '
            tableau[caseVerif3HD[DD - 1]] = Joueur
        for i in range (DD - 1):
            tableau[caseVerif3HD[i - 1]] = '     '
    elif DameDeplacement == "HG" :
        print("Vous pouvez vous déplacer sur les case suivantes : ", caseVerif2HG)
        DD = int(input("Veuillez séléctionner le numéro de l'élement dans la liste (ex : 1, 2, 3...)"))
        tableau[case] = '     '
        tableau[caseVerif3HG[DD - 1]] = Joueur
        for i in range (DD - 1):
            tableau[caseVerif3HG[i - 1]] = '     '
    elif DameDeplacement == "BD" :
        print("Vous pouvez vous déplacer sur les case suivantes : ", caseVerif2BD)
        DD = int(input("Veuillez séléctionner le numéro de l'élement dans la liste (ex : 1, 2, 3...)"))
        tableau[case] = '     '
        tableau[caseVerif3BD[DD - 1]] = Joueur
        for i in range (DD - 1):
            tableau[caseVerif3BD[i - 1]] = '     '
    elif DameDeplacement == "BG" :
        print("Vous pouvez vous déplacer sur les case suivantes : ", caseVerif2BG)
        DD = int(input("Veuillez séléctionner le numéro de l'élement dans la liste (ex : 1, 2, 3...)"))
        tableau[case] = '     '
        tableau[caseVerif3BG[DD - 1]] = Joueur
        for i in range (DD - 1):
            tableau[caseVerif3BG[i - 1]] = '     '
    
############### PROGRAMME PRINCIPAL ###############

replay = True                                                               #Crée la variable
while replay == True:                                                       #Tant que le joueur veut rejouer

    #---# VARIABLES DE DEBUT DE PARTIE #---#
    
    tableau = tableauStart ()                                               #Crée le plateau de jeu VIDE
    listeCasesJouables = caseJouable()                                      #Set up les cases jouables dans la liste: "listeCasesJouables"
    pionsStart(tableau)                                                     #Place les pions noirs et blancs au début du jeu
    tour = 1                                                                #Set up variable
    vieBLACK = 20                                                           #Création de la variable "vie" pour les Noirs
    vieWHITE = 20                                                           #Création de la variable "vie" pour les Blancs
    
    #---# POUR TESTER LES DAMES #---#
##    tableau[1] = "DameW"
##    tableau[23] = "     "
##    tableau[34] = "     "
##    tableau[34] = "     "
##    tableau[12] = "     "
##    tableau[67] = "     "
##    tableau[56] = "BLACK"
    
    #---# POUR CREER UNE DAME #---#
    tableau[3]="     "
    tableau[12]="WHITE"
    tableau[21]="     "
    tableau[32]="     "
    tableau[61]="     "
    tableau[54]="BLACK"
    tableau[50]="BLACK"
    
    
    afficherTableau()                                                       #Affiche le plateau de jeu

    #---# PARTIE EN COURS #---#
    
    while vieBLACK > 0 and vieWHITE > 0 :                                   #Joue tant qu'il reste des pions 
        if (tour%2 == 0) :                                                  #Si tour paire
            Joueur = "BLACK"                                                #Le joueur est BLACK
            DameJoueur = 'DameB'                                            #La dame du joueur est DameB
            Adversaire = 'WHITE'                                            #L'adversaire est WHITE
            DameAdversaire = "DameW"                                        #La dame adverse est DameW
            print("C'est au tour des [BLACK] de jouer.")                    #Informe le joueur
            case = 42                                                       #Crée la variable
            verification = False                                            #Crée la variable
            while verification == False:                                    #Tant le joueur n'a pas choisi une case possible à jouer:
                case = choixCase()                                          #Il choisi une case à jouer
                if VerificationChoixCase () == False:                       #Si il a choisi une case valide:
                    verification = True                                     #Sort de la boucle
            if tableau[case]=="DameB":                                      #Si son pion est une dame:
                DéplacementDames()                                          #Le déplace comme une dame
            if tableau[case]=="BLACK":                                      #Si son pion est basique:
                listeVerification = verificationManger(tableau,case)        #Test s'il y a un pion à manger
                if  listeVerification[0] == True:                           #S'il y a un pion à manger:
                    vieBLACK,vieWHITE = manger(case,vieBLACK,vieWHITE,listeVerification)#Fait manger
                else:                                                       #S'il n'y a pas de pion à manger:
                    case = deplacement(case)                                #Déplace le pion
        if (tour%2 != 0) :                                                  #Si tour impaire
            Joueur = "WHITE"                                                #Le joueur est WHITE
            DameJoueur = "DameW"                                            #La dame du joueur est DameW
            Adversaire = "BLACK"                                            #L'adversaire est BLACK
            DameAdversaire = "DameB"                                        #La dame adverse est DameB
            print("C'est au tour des [WHITE] de jouer.")                    #Informe le joueur
            case = 42                                                       #Crée la variable      
            verification = False                                            #Crée la variable
            while verification == False:                                    #Tant le joueur n'a pas choisi une case possible à jouer:
                case = choixCase()                                          #Il choisi une case à jouer
                if VerificationChoixCase () == False:                       #Si il n'y a pas de pion allié tout autour
                    verification = True                                     #Sort de la boucle
            if tableau[case]=="DameW":                                      #Si son pion est une dame:
                DéplacementDames()                                          #Le déplace comme une dame
            if tableau[case]=="WHITE":                                      #Si son pion est basique:
                listeVerification = verificationManger(tableau,case)        #Test s'il y a un pion à manger
                if  listeVerification[0] == True:                           #S'il y a un pion à manger:
                    vieBLACK,vieWHITE = manger(case,vieBLACK,vieWHITE,listeVerification)#Fait manger
                else:                                                       #S'il n'y a pas de pion à manger:
                    case = deplacement(case)                                #Déplace le pion
        print("\n")            
        transformationDame()                                                #Met une dame si possible
        afficherTableau()                                                   #Affiche le tableau de jeu
        tour = tour+1                                                       #Passe au tour suivant
        
    #---# FIN DE PARTIE #---#

    replay = rejouer()
    if replay == True:                                                      #Si la réponse est 'oui':
        print("\n"*30)                                                      #'vide' l'écran
    elif replay == False:                                                   #Si la réponse est 'non':
        print("\n"*5,"Votre partie est terminée!")                          #Informe le joueur
