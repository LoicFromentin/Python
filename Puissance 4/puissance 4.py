######################################## PUISSANCE 4 ########################################
#7 large
#6 haut

def creerPlateau ():
    for case in range (42):
        plateau.append(" ")
    return(plateau)

def montrerPlateau ():
    print("\nVoici le plateau de jeu:\n")
    place = 0
    for ligne in range (6):                            #Balaye les lignes
        afficherLigne = []
        for colonne in range (7):                      #Balaye les colonnes
            afficherLigne.append(plateau[place])
            place = place+1
        print("    ---------------------------")
        print('   |',' | '.join(afficherLigne),'|')
    print("    ---------------------------")
    print("\n")

def jouer (plateau):
    casePrise = True
    while casePrise == True:
        case = 0
        while not 0<case<8:
            print("C'est au tour des",joueur,"de jouer.")
            case = int(input("Veuillez choisir dans quelle colonne placer votre pion: "))
            if not 0<case<8:
                print("\nVous n'avez pas choisi une colonne valide (1 à 7).\n\n")
        case = case-1
        if plateau[case]!='O' and plateau[case]!='X':
            casePrise = False
        else:
            print("Cette colonne est déjà pleine!")
    while case<35 and (plateau[case+7]==' '):
        case = case+7
    plateau[case] = joueur
    return(plateau)

def TestWin():
    ListeHaut = []
    for i in range (21,41):
        ListeHaut.append(i)
    ListeBas = []
    for i in range (0,20):
        ListeBas.append(i)
    ListeDroite = [0,1,2,3,7,8,9,10,14,15,16,17,21,22,23,24,28,29,30,31,35,36,37,38]
    ListeGauche = [3,4,5,6,10,11,12,13,17,18,19,20,24,25,26,27,31,32,33,34,38,39,40,41]
    ListeHD = [21,22,23,24,28,29,30,31,35,36,37,38]
    ListeHG = [24,25,26,27,31,32,33,34,38,39,40,41]
    ListeBG = [3,4,5,6,10,11,12,13,17,18,19,20]
    ListeBD = [0,1,2,3,7,8,9,10,14,15,16,17]
    Win = False
    for case in range (0,41):
        if plateau[case] == joueur:                             #S'il y a un pion du joueur à qui c'est le tour de jouer
        #----- Test Droite
            if Win == False and case in ListeDroite:
                CaseTest = case
                TestJuste = 0
                Continue = True
                while Continue == True and TestJuste<3 :
                    if plateau[CaseTest+1] == plateau[case]:
                        CaseTest = CaseTest +1
                        TestJuste = TestJuste +1
                    else: Continue = False #Sortir de la boucle
                if TestJuste == 3:
                    Win = True
                    
        #----- Test Gauche
            if Win == False and case in ListeGauche:
                CaseTest = case
                TestJuste = 0
                Continue = True
                while Continue == True and TestJuste<3 :
                    if plateau[CaseTest-1] == plateau[case]:
                        CaseTest = CaseTest -1
                        TestJuste = TestJuste +1
                    else: Continue = False #Sortir de la boucle
                if TestJuste == 3:
                    Win = True

        #----- Test Haut
            if Win == False and case in ListeHaut:
                CaseTest = case
                TestJuste = 0
                Continue = True
                while Continue == True and TestJuste<3 :
                    if plateau[CaseTest-7] == plateau[case]:
                        CaseTest = CaseTest -7
                        TestJuste = TestJuste +1
                    else: Continue = False #Sortir de la boucle
                if TestJuste == 3:
                    Win = True

        #----- Test Bas
            if Win == False and case in ListeBas:
                CaseTest = case
                TestJuste = 0
                Continue = True
                while Continue == True and TestJuste<3 :
                    if plateau[CaseTest+7] == plateau[case]:
                        CaseTest = CaseTest +7
                        TestJuste = TestJuste +1
                    else: Continue = False #Sortir de la boucle
                if TestJuste == 3:
                    Win = True
                    
        #----- Test Haut Droite
            if Win == False and case in ListeHD:
                CaseTest = case
                TestJuste = 0
                Continue = True
                while Continue == True and TestJuste<3 :
                    if plateau[CaseTest-6] == plateau[case]:
                        CaseTest = CaseTest -6
                        TestJuste = TestJuste +1
                    else:
                        Continue = False #Sortir de la boucle
                if TestJuste == 3:
                    Win = True
        #----- Test Haut Gauche
            if Win == False and case in ListeHG:
                CaseTest = case
                TestJuste = 0
                Continue = True
                while Continue == True and TestJuste<3 :
                    if plateau[CaseTest-8] == plateau[case]:
                        CaseTest = CaseTest -8
                        TestJuste = TestJuste +1
                    else: Continue = False #Sortir de la boucle
                if TestJuste == 3:
                    Win = True
        #----- Test Bas Droite
            if Win == False and case in ListeBD:
                CaseTest = case
                TestJuste = 0
                Continue = True
                while Continue == True and TestJuste<3 :
                    if plateau[CaseTest+8] == plateau[case]:
                        CaseTest = CaseTest +8
                        TestJuste = TestJuste +1
                    else: Continue = False #Sortir de la boucle
                if TestJuste == 3:
                    Win = True
        #----- Test Bas Gauche
            if Win == False and case in ListeBG:
                CaseTest = case
                TestJuste = 0
                Continue = True
                while Continue == True and TestJuste<3 :
                    if plateau[CaseTest+6] == plateau[case]:
                        CaseTest = CaseTest +6
                        TestJuste = TestJuste +1
                    else: Continue = False #Sortir de la boucle
                if TestJuste == 3:
                    Win = True
    return (Win)
    
def replay (recommencer):
    question = ""
    while question not in ("oui","non","yes","no"):
        question = input("\nVoulez-vous rejouer? ")
        question = question.lower()
        if question not in ("oui","non","yes","no"):
            print("Il faut répondre par oui ou par non.")
    if question in ("non","no"):
        recommencer = False
    return(recommencer)
    
####################################### PROGRAMME JEU #######################################
        
partiej1Win = 0
partiej2Win = 0
recommencer = True


#Insérer possibilités pseudo

while recommencer == True:
    Joueur1 = "X"
    Joueur2 = "O"
    plateau = []
    creerPlateau()
    tour = 0
    j1Win = False
    j2Win = False
    aucunGagnant = False
    while j1Win == j2Win and aucunGagnant == False:
        montrerPlateau()
        if tour == 42:
            aucunGagnant = True
        elif tour%2 == 0:
            joueur = Joueur1
            jouer(plateau)
            if TestWin() == True:
                j1Win = True
        elif tour%2 != 0:
            joueur = Joueur2
            jouer(plateau)
            if TestWin() == True:
                j2Win = True
        tour = tour +1
        print("\n"*40)
    
    if aucunGagnant == True: #si match nul
        print("Match nul, aucun joueur n'a gagné la partie!")
    elif j1Win == True: #si J1 win
        print ("les X ont gagné! BRAVO!")
        partiej1Win = partiej1Win + 1
    else: #si j2 Win
        print ("Les O ont gagné! BRAVO!")
        partiej2Win = partiej2Win + 1
    print("\n")
    montrerPlateau()
    if replay(recommencer) == False:
        recommencer = False
    print("\n"*40)

print("\n\nVoici les scores totaux:\n")
print("Le joueur des",Joueur1,"a gagné",partiej1Win,"parties.")
print("Le joueur des",Joueur2,"a gagné",partiej2Win,"parties.")
    
