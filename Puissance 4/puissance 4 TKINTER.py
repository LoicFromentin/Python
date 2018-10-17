from tkinter import*

#---------------# FONCTIONS #---------------#

#Affiche les Règles du jeu
def Regles(FenetreRegles):
    Puissance4 = Label(FenetreRegles, text = "Règles du Puissance 4", fg = "DarkRed", font =("Yu Mincho Demibold",30)).pack(pady=25, side=TOP)
    Titre1 = Label(FenetreRegles, text = "Comment jouer :", fg = "blue", font =("Yu Mincho Demibold",20)).pack(pady=5, side=TOP)
    Texte1 = Label(FenetreRegles, text = "Cliquer sur une case de la première ligne du plateau de jeu pour faire glisser votre pion.",fg="#800080", font=("Constantia",14)).pack(padx=40,side=TOP)
    Titre2 = Label(FenetreRegles, text = "\n\nDéroulement de la partie:",fg = "blue", font=("Yu Mincho Demibold",20)).pack(pady=5, side=TOP)
    Texte2 = Label(FenetreRegles, text = "Chaque joueur a 21 pions.\nTour à tour, les joueurs vont placer leur pion sur la première ligne,\npuis ce pion va glisser jusqu'à la position la plus basse de la colonne.", fg="#800080", font=("Constantia",14)).pack(side=TOP)
    Titre3 = Label(FenetreRegles, text = "\n\nBut du jeu:",fg = "blue", font=("Yu Mincho Demibold",20)).pack(side=TOP)
    Texte3 = Label(FenetreRegles, text = "Aligner 4 pions horizontalement, verticalement ou diagonalement pour gagner.\n", fg="#800080", font=("Constantia",14)).pack(pady=5,side=TOP)

#Remet le jeu à 0, MàJ victoires BLUE/PINK
def Recommencer ():
    global tour, listeCasesPlateau, Message
    
    Plateau.delete(ALL)                                                             #Efface le contenu de la fenêtre
    Lignes()                                                                        #Crée les lignes qui délimitent les 9 cases
    listeCasesPlateau = []                                                          #Crée la liste
    for case in range (42):                                                         #Pour chaque case (42)
        listeCasesPlateau.append(" ")                                               #Ajoute une case vide à la liste
    tour = 1                                                                        #Crée variable "tour" égale à 1
    Texte = "C'est au tour des BLUE de jouer."                                      #Texte au tour 1
    ColorBg = ColorBgBlue                                                           #Couleur de fond au tour 1
    ColorFg = ColorFgBlue                                                           #Couleur d'écriture au tour 1
    Message.config(text = Texte, bg = ColorBg, fg = ColorFg)                        #Remet le Message au tour 1

#Dessine les lignes pour délimiter les cases
def Lignes ():
    #Horizontales
    Plateau.create_line(0,100,700,100,width = 2)
    Plateau.create_line(0,200,700,200,width = 2)
    Plateau.create_line(0,300,700,300,width = 2)
    Plateau.create_line(0,400,700,400,width = 2)
    Plateau.create_line(0,500,700,500,width = 2)
    #Verticales
    Plateau.create_line(100,0,100,600,width = 2)
    Plateau.create_line(200,0,200,600,width = 2)
    Plateau.create_line(300,0,300,600,width = 2)
    Plateau.create_line(400,0,400,600,width = 2)
    Plateau.create_line(500,0,500,600,width = 2)
    Plateau.create_line(600,0,600,600,width = 2)

#Affiche un message Texte
def Affichage (tour,Message):
    if tour < 60:                                                                   #Si la partie n'est pas finie
        if tour % 2 != 0:                                                           #Si c'est aux Blue de jouer:
            Texte = "C'est au tour des  BLUE  de jouer."                            #Change le Texte
            ColorBg = ColorBgBlue                                                   #Change la couleur de fond
            ColorFg = ColorFgBlue                                                   #Change la couleur du Texte
        else:                                                                       #Si c'est aux Pink de jouer:
            Texte = "C'est au tour des  PINK  de jouer."                            #Change le texte
            ColorBg = ColorBgPink                                                   #Change la couleur de fond
            ColorFg = ColorFgPink                                                   #Change la couleur du Texte
        Message.config(text = Texte, bg = ColorBg, fg = ColorFg)                    #Met à jour le Message
        return (Message)                                                            #Renvoie le Message

#Test si le joueur a gagné et stock les cases des pions gagnant dans une liste
def TestWin(joueur):
    global ListeCasesWin
    ListeHaut = []                                                                  #Crée la liste des cases à tester vers le haut
    for i in range (21,41):                                                         #Pour les cases de 21 à 41
        ListeHaut.append(i)                                                         #Ajouter la case à la liste
    ListeBas = []                                                                   #Crée la liste des cases à tester vers le bas
    for i in range (0,20):                                                          #Pour les cases de 0 à 20
        ListeBas.append(i)                                                          #Ajouter la case à la liste
    ListeDroite = [0,1,2,3,7,8,9,10,14,15,16,17,21,22,23,24,28,29,30,31,35,36,37,38]#Liste des cases à tester à droite
    ListeGauche = [3,4,5,6,10,11,12,13,17,18,19,20,24,25,26,27,31,32,33,34,38,39,40,41]#Liste des cases à tester à gauche
    ListeHD = [21,22,23,24,28,29,30,31,35,36,37,38]                                 #Liste des cases à tester en Haut Droite
    ListeHG = [24,25,26,27,31,32,33,34,38,39,40,41]                                 #Liste des cases à tester en Haut Gauche
    ListeBG = [3,4,5,6,10,11,12,13,17,18,19,20]                                     #Liste des cases à tester en Bas Gauche
    ListeBD = [0,1,2,3,7,8,9,10,14,15,16,17]                                        #Liste des cases à tester en Bas Droite
    Win = False                                                                     #Crée la variable Win
    for case in range (0,41):                                                       #Balaye toutes les cases (0 à 41)
        if listeCasesPlateau[case] == joueur:                                       #S'il y a un pion du joueur qui joue:
        #----- Test Droite
            if Win == False and case in ListeDroite:                                #Si on peut tester les cases de droites:
                CaseTest = case                                                     #Crée la variable CaseTest
                ListeCasesWin.append(CaseTest)                                      #On ajoute la case à la liste
                TestJuste = 0                                                       #Crée la variable TestJuste
                Continue = True                                                     #Crée la variable Continue
                while Continue == True and TestJuste<3 :                            #Si on continue et qu'on a pas testé 3 cases:
                    if listeCasesPlateau[CaseTest+1] == listeCasesPlateau[case]:    #Si la prochaine case est occupée par joueur:
                        CaseTest = CaseTest +1                                      #On passe à la case suivante à tester
                        ListeCasesWin.append(CaseTest)                              #On ajoute la case à la liste
                        TestJuste = TestJuste +1                                    #On augmente le compteur de Test justes
                    else:                                                           #Sinon:
                        Continue = False                                            #On sort de la boucle
                        ListeCasesWin = []                                          #On vide la liste
                        
                if TestJuste == 3:                                                  #Si les 3 cases suivantes sont joueur
                    Win = True                                                      #Le joueur a gagné
                    
        #----- Test Gauche
            if Win == False and case in ListeGauche:
                CaseTest = case                                                     #Crée la variable CaseTest
                ListeCasesWin.append(CaseTest)                                      #On ajoute la case à la liste
                TestJuste = 0                                                       #Crée la variable TestJuste
                Continue = True                                                     #Crée la variable Continue
                while Continue == True and TestJuste<3 :                            #Si on continue et qu'on a pas testé 3 cases:
                    if listeCasesPlateau[CaseTest-1] == listeCasesPlateau[case]:    #Si la prochaine case est occupée par joueur:
                        CaseTest = CaseTest -1                                      #On passe à la case suivante à tester
                        ListeCasesWin.append(CaseTest)                              #On ajoute la case à la liste
                        TestJuste = TestJuste +1                                    #On augmente le compteur de Test justes
                    else:                                                           #Sinon:
                        Continue = False                                            #On sort de la boucle
                        ListeCasesWin = []                                          #On vide la liste
                if TestJuste == 3:                                                  #Si les 3 cases suivantes sont joueur
                    Win = True                                                      #Le joueur a gagné

        #----- Test Haut
            if Win == False and case in ListeHaut:
                CaseTest = case                                                     #Crée la variable CaseTest
                ListeCasesWin.append(CaseTest)                                      #On ajoute la case à la liste
                TestJuste = 0                                                       #Crée la variable TestJuste
                Continue = True                                                     #Crée la variable Continue
                while Continue == True and TestJuste<3 :                            #Si on continue et qu'on a pas testé 3 cases:
                    if listeCasesPlateau[CaseTest-7] == listeCasesPlateau[case]:    #Si la prochaine case est occupée par joueur:
                        CaseTest = CaseTest -7                                      #On passe à la case suivante à tester
                        ListeCasesWin.append(CaseTest)                              #On ajoute la case à la liste
                        TestJuste = TestJuste +1                                    #On augmente le compteur de Test justes
                    else:                                                           #Sinon:
                        Continue = False                                            #On sort de la boucle
                        ListeCasesWin = []                                          #On vide la liste
                if TestJuste == 3:                                                  #Si les 3 cases suivantes sont joueur
                    Win = True                                                      #Le joueur a gagné

        #----- Test Bas
            if Win == False and case in ListeBas:
                CaseTest = case                                                     #Crée la variable CaseTest
                ListeCasesWin.append(CaseTest)                                      #On ajoute la case à la liste
                TestJuste = 0                                                       #Crée la variable TestJuste
                Continue = True                                                     #Crée la variable Continue
                while Continue == True and TestJuste<3 :                            #Si on continue et qu'on a pas testé 3 cases:
                    if listeCasesPlateau[CaseTest+7] == listeCasesPlateau[case]:    #Si la prochaine case est occupée par joueur:
                        CaseTest = CaseTest +7                                      #On passe à la case suivante à tester
                        ListeCasesWin.append(CaseTest)                              #On ajoute la case à la liste
                        TestJuste = TestJuste +1                                    #On augmente le compteur de Test justes
                    else:                                                           #Sinon:
                        Continue = False                                            #On sort de la boucle
                        ListeCasesWin = []                                          #On vide la liste
                if TestJuste == 3:                                                  #Si les 3 cases suivantes sont joueur
                    Win = True                                                      #Le joueur a gagné
                    
        #----- Test Haut Droite
            if Win == False and case in ListeHD:
                CaseTest = case                                                     #Crée la variable CaseTest
                ListeCasesWin.append(CaseTest)                                      #On ajoute la case à la liste
                TestJuste = 0                                                       #Crée la variable TestJuste
                Continue = True                                                     #Crée la variable Continue
                while Continue == True and TestJuste<3 :                            #Si on continue et qu'on a pas testé 3 cases:
                    if listeCasesPlateau[CaseTest-6] == listeCasesPlateau[case]:    #Si la prochaine case est occupée par joueur:
                        CaseTest = CaseTest -6                                      #On passe à la case suivante à tester
                        ListeCasesWin.append(CaseTest)                              #On ajoute la case à la liste
                        TestJuste = TestJuste +1                                    #On augmente le compteur de Test justes
                    else:                                                           #Sinon:
                        Continue = False                                            #On sort de la boucle
                        ListeCasesWin = []                                          #On vide la liste
                if TestJuste == 3:                                                  #Si les 3 cases suivantes sont joueur
                    Win = True                                                      #Le joueur a gagné
        #----- Test Haut Gauche
            if Win == False and case in ListeHG:
                CaseTest = case                                                     #Crée la variable CaseTest
                ListeCasesWin.append(CaseTest)                                      #On ajoute la case à la liste
                TestJuste = 0                                                       #Crée la variable TestJuste
                Continue = True                                                     #Crée la variable Continue
                while Continue == True and TestJuste<3 :                            #Si on continue et qu'on a pas testé 3 cases:
                    if listeCasesPlateau[CaseTest-8] == listeCasesPlateau[case]:    #Si la prochaine case est occupée par joueur:
                        CaseTest = CaseTest -8                                      #On passe à la case suivante à tester
                        ListeCasesWin.append(CaseTest)                              #On ajoute la case à la liste
                        TestJuste = TestJuste +1                                    #On augmente le compteur de Test justes
                    else:                                                           #Sinon:
                        Continue = False                                            #On sort de la boucle
                        ListeCasesWin = []                                          #On vide la liste
                if TestJuste == 3:                                                  #Si les 3 cases suivantes sont joueur
                    Win = True                                                      #Le joueur a gagné
        #----- Test Bas Droite
            if Win == False and case in ListeBD:
                CaseTest = case                                                     #Crée la variable CaseTest
                ListeCasesWin.append(CaseTest)                                      #On ajoute la case à la liste
                TestJuste = 0                                                       #Crée la variable TestJuste
                Continue = True                                                     #Crée la variable Continue
                while Continue == True and TestJuste<3 :                            #Si on continue et qu'on a pas testé 3 cases:
                    if listeCasesPlateau[CaseTest+8] == listeCasesPlateau[case]:    #Si la prochaine case est occupée par joueur:
                        CaseTest = CaseTest +8                                      #On passe à la case suivante à tester
                        ListeCasesWin.append(CaseTest)                              #On ajoute la case à la liste
                        TestJuste = TestJuste +1                                    #On augmente le compteur de Test justes
                    else:                                                           #Sinon:
                        Continue = False                                            #On sort de la boucle
                        ListeCasesWin = []                                          #On vide la liste
                if TestJuste == 3:                                                  #Si les 3 cases suivantes sont joueur
                    Win = True                                                      #Le joueur a gagné
        #----- Test Bas Gauche
            if Win == False and case in ListeBG:
                CaseTest = case                                                     #Crée la variable CaseTest
                ListeCasesWin.append(CaseTest)                                      #On ajoute la case à la liste
                TestJuste = 0                                                       #Crée la variable TestJuste
                Continue = True                                                     #Crée la variable Continue
                while Continue == True and TestJuste<3 :                            #Si on continue et qu'on a pas testé 3 cases:
                    if listeCasesPlateau[CaseTest+6] == listeCasesPlateau[case]:    #Si la prochaine case est occupée par joueur:
                        CaseTest = CaseTest +6                                      #On passe à la case suivante à tester
                        ListeCasesWin.append(CaseTest)                              #On ajoute la case à la liste
                        TestJuste = TestJuste +1                                    #On augmente le compteur de Test justes
                    else:                                                           #Sinon:
                        Continue = False                                            #On sort de la boucle
                        ListeCasesWin = []                                          #On vide la liste
                if TestJuste == 3:                                                  #Si les 3 cases suivantes sont joueur
                    Win = True                                                      #Le joueur a gagné
    return (Win)                                                                    #Renvoie le Test: gagné ou non

#Test s'il y a match nul
def MatchNul ():
    if TestWin(joueur) == False and tour == 42:                                     #Si le joueur n'a pas gagné et que le plateau est rempli:
        return(True)                                                                #Il y a Match Nul
    else: return(False)                                                             #Sinon, il n'y a pas Match Nul

#Compte le nombre de victoires Blue
def TextVictoiresBlue (VictoiresBlue):
    nombre = str(VictoiresBlue)                                                     #Nombre de VictoiresBLUE
    blabla = "Victoires BLUE :  "                                                   #Début de la phrase
    TexteVictoiresBlue = str(" "+blabla+nombre+" ")                                 #Associe le contenu de nombre et blabla en chaîne de caractères
    return(TexteVictoiresBlue)                                                      #Renvoie cette chaîne de caractères

#Compte le nombre de victoires Pink
def TextVictoiresPink (VictoiresPink):
    nombre = str(VictoiresPink)                                                     #Nombre de VictoiresPINK
    blabla = "Victoires PINK :  "                                                   #Début de la phrase
    TexteVictoiresPink = str(" "+blabla+nombre+" ")                                 #Associe le contenu de nombre et blabla en chaîne de caractères
    return(TexteVictoiresPink)                                                      #Renvoie cette chaîne de caractères

#Affiche s'il y a VictoirePink, VictoireBlue ou MatchNul
def TestWinOrNul (joueur):
    global Message,Texte,Color,tour,VictoiresPink,VictoiresBlue,MessageVictoiresPink,MessageVictoiresBlue
    '''ListeCasesWin '''
    if tour < 60:
        if TestWin(joueur)== True:                                                  #Si le joueur a gagné:
            tour = 65                                                               #Arrêter le jeu
            if joueur == "P":                                                       #Si le joueur est PINK:
                Texte = "Les  PINK  ont gagné !"                                    #Change le Texte
                ColorBg = ColorBgPink                                               #Change la couleur du fond
                ColorFg = ColorFgPink    	                                    #Change la couleur du Texte
                Message.config(text = Texte, bg = ColorBg, fg = ColorFg)            #Affiche qu'ils ont gagnés
                rayon = 13                                                          #Rayon du cercle
                for case in range (0,4):                                            #4 Pions
                    X = coordCases[ListeCasesWin[case]][0]                          #X du centre du cercle
                    Y = coordCases[ListeCasesWin[case]][1]                          #Y du centre du cercle
                    Plateau.create_oval(X-rayon, Y-rayon, X+rayon, Y+rayon, width = 40, outline = "#800080")#Cercle plein
                VictoiresPink = VictoiresPink +1                                    #Ajoute 1 au compteur VictoiresPink
            elif joueur == "B":                                                     #Si le joueur est BLUE:
                Texte = "Les  BLUE  ont gagné !"                                    #Change le Texte
                ColorBg = ColorBgBlue                                               #Change la couleur du fond
                ColorFg = ColorFgBlue    	                                    #Change la couleur du Texte
                Message.config(text = Texte, bg = ColorBg, fg = ColorFg)            #Affiche qu'ils ont gagnés
                rayon = 13                                                          #Rayon du cercle
                for case in range (0,4):                                            #4 Pions
                    X = coordCases[ListeCasesWin[case]][0]                          #X du centre du cercle
                    Y = coordCases[ListeCasesWin[case]][1]                          #Y du centre du cercle
                    Plateau.create_oval(X-rayon, Y-rayon, X+rayon, Y+rayon, width = 40, outline = "blue")#Cercle plein
                VictoiresBlue = VictoiresBlue +1                                    #Ajoute 1 au compteur VictoiresBlue
                
        elif MatchNul() == True:                                                    #S'il y a Match Nul:
            tour = 65                                                               #Arrêter le jeu
            Texte = "Match nul !"                                                   #Change le Texte
            ColorBg = "#533007"                                                     #Change la couleur du fond
            ColorFg = "#E6E2AF"                                                     #Change la couleur du Texte
            Message.config(text = Texte, bg = ColorBg, fg = ColorFg)                #Affiche qu'il y a match nul
            
        MessageVictoiresBlue.config(text= TextVictoiresBlue (VictoiresBlue))        #Met à jour le nombre de VictoiresX
        MessageVictoiresPink.config(text= TextVictoiresPink (VictoiresPink))        #Met à jour le nombre de Victoires

#Programme principal du jeu
def clic(event):
    global tour, Message,joueur
    
    FinTour = False    
    X = event.x                                                                     #X = X du clic
    Y = event.y                                                                     #Y = Y du clic
    rayon = 35                                                                      #Rayon du cerle / moitié de la taille des lignes

    #---------- Balayage des Cases ----------#
    
    gaucheX = 0                                                                     #Point le plus à gauche de la case
    droiteX = 100                                                                   #Point le plus à droite de la case
    for colonne in range (7):
        if gaucheX<X<droiteX and 0<Y<100:                                           #S'il a cliqué dans la case
            X = gaucheX + 50                                                        #Centre le clic au mileu de la case
            Y = 50                                                                  #Centre le clic au mileu de la case

    #---------- Tour des PINK ----------#
            if tour%2 == 0 and tour<60:                                             #Si la partie n'est pas finie:
                joueur = "P"                                                        #C'est au tour des PINK
                position = [X,Y]                                                    #Range X,Y du clic dans cette liste
                placeListe = 0                                                      #Place dans coordCases (numéro de colonne)
                for i in range(8):                                                  #Balaye les 7 colonnes (0 à 7 car (1-1) à (8-1))
                    if coordCases[placeListe-1] == position:                        #Si clic dans case correspondante à ses coord
                        if listeCasesPlateau[placeListe-1] == " ":                  #Si la case est vide
                            case = placeListe-1                                     #On ce place sur cette case vide
                            NextCase = True                                         #Set up variable
                            while NextCase == True and case < 35:                   #Si la prochaine case est vide et qu'on dépasse pas
                                if listeCasesPlateau[case+7]== " ":                 #Si la case d'en dessous est vide
                                    case = case+7                                   #On avance de case à tester
                                else: NextCase = False                              #Sinon, la prochaine case n'est pas vide
                            X = coordCases[case][0]                                 #On change les coordonnées du clic (X)
                            Y = coordCases[case][1]                                 #On change les coordonnées du clic (Y)
                            Plateau.create_oval(X-rayon, Y-rayon, X+rayon, Y+rayon, width = 10, outline = "#800080")
                            listeCasesPlateau[case] = joueur                        #Remplie la case DANS LA LISTE
                            FinTour = True                                          #Le joueur a fini son tour
                        else:                                                       #Sinon:
                            FinTour = False                                         #C'est encore aux PINK de jouer
                    placeListe = placeListe +1                                      #On avance dans la liste
                
    #---------- Tour des BLUE ----------#
            if tour%2 != 0 and tour<60:                                             #Si la partie n'est pas finie:
                joueur = "B"                                                        #C'est au tour des BLUE
                position = [X,Y]                                                    #Range X,Y du clic dans cette liste
                placeListe = 0                                                      #Place dans coordCases (numéro de colonne)
                for i in range(8):                                                  #Balaye les 7 colonnes (0 à 7 car (1-1) à (8-1))
                    if coordCases[placeListe-1] == position:                        #Si clic dans case correspondante à ses coord
                        if listeCasesPlateau[placeListe-1] == " ":                  #Si la case est vide
                            case = placeListe-1                                     #On ce place sur cette case vide
                            NextCase = True                                         #Set up variable
                            while NextCase == True and case < 35:                   #Si la prochaine case est vide et qu'on dépasse pas
                                if listeCasesPlateau[case+7]== " ":                 #Si la case d'en dessous est vide
                                    case = case+7                                   #On avance de case à tester
                                else: NextCase = False                              #Sinon, la prochaine case n'est pas vide
                            X = coordCases[case][0]                                 #On change les coordonnées du clic (X)
                            Y = coordCases[case][1]                                 #On change les coordonnées du clic (Y)
                            Plateau.create_oval(X-rayon, Y-rayon, X+rayon, Y+rayon, width = 10, outline = "blue")
                            listeCasesPlateau[case] = joueur                        #Remplie la case DANS LA LISTE
                            FinTour = True                                          #Le joueur a fini son tour
                        else:                                                       #Sinon:
                            FinTour = False                                         #C'est encore aux BLUE de jouer
                    placeListe = placeListe +1                                      #On avance dans la liste
            
        gaucheX,droiteX = droiteX,droiteX+100                                       #Passe à la case de droite
    TestWinOrNul (joueur)                                                           #Regarde si la partie est finie
    if FinTour == True:                                                             #Si le joueur a fini son tour
        tour = tour + 1                                                             #Passe au tour adverse
    if tour<60:                                                                     #S'il n'y a pas encore de gagnant:
        Message = Affichage (tour,Message)                                          #Change le message affiché

#---------------# VARIABLES / LISTES #---------------#

tour = 1                                                                            #Tour actuel
Largeur = 700                                                                       #Largeur du Plateau de jeu
Hauteur = 600                                                                       #Hauteur du Plateau de jeu
VictoiresPink = 0                                                                   #Nombre de Victoires Pink de base
VictoiresBlue = 0                                                                   #Nombre de Victoires Blue de base
ColorFgPink = "#FF75FF"                                                             #Couleur d'écriture Pink
ColorBgPink = "#2E0039"                                                             #Couleur de fond Pink
ColorFgBlue = "cyan"                                                                #Couleur d'écriture Blue
ColorBgBlue = "#0B1253"                                                             #Couleur de fond Blue
Texte = "C'est au tour des BLUE de jouer."                                          #Texte au tour 1
joueur = "B"                                                                        #Joueur au tour 1 (Blue)
ColorBg = ColorBgBlue                                                               #Couleur de fond au tour 1
ColorFg = ColorFgBlue                                                               #Couleur d'écriture au tour 1

#----------

coordCases = [[50,50],[150,50],[250,50],[350,50],[450,50],[550,50],[650,50],
              [50,150],[150,150],[250,150],[350,150],[450,150],[550,150],[650,150],
              [50,250],[150,250],[250,250],[350,250],[450,250],[550,250],[650,250],
              [50,350],[150,350],[250,350],[350,350],[450,350],[550,350],[650,350],
              [50,450],[150,450],[250,450],[350,450],[450,450],[550,450],[650,450],
              [50,550],[150,550],[250,550],[350,550],[450,550],[550,550],[650,550]] #42 cases

listeCasesPlateau = []                                                              #Crée la liste du contenu des cases
for case in range (42):                                                             #42 Cases
    listeCasesPlateau.append(" ")                                                   #Ajoute une case vide

ListeCasesWin = []                                                                  #Liste des cases des 4 pions qui win

#---------------# FENÊTRE REGLES#---------------#

FenetreRegles = Tk()                                                                #Crée une fenêtre
FenetreRegles.title("Règles du jeu Puissance 4")                                    #Nomme la fenêtre
Regles(FenetreRegles)                                                               #Affiche les règles

#Crée un boutton Quitter qui ferme la Fenetre
BouttonQuitter = Button(FenetreRegles, text="Commencer à jouer", command=FenetreRegles.destroy).pack(side="right", padx=5, pady=5)

''' A NE PAS TOUCHER '''
FenetreRegles.mainloop()                                                            #Affiche la fenêtre

#---------------# FENÊTRE #---------------#

#Création de la Fenetre
Fenetre = Tk()                                                                      #Crée une Fenetre
Fenetre.title ("Puissance 4")                                                       #Nomme la Fenetre

#Affiche un message, ce tour ci: "C'est au tour des Blue de jouer."
Message = Label(Fenetre, text=Texte, bg=ColorBg, fg=ColorFg, font=("Gentium Book Basic",12))
Message.pack(side=TOP, padx=5, pady=5, fill=X)

#Création du Plateau de jeu
Plateau = Canvas(Fenetre, width = Largeur, height = Hauteur, cursor="target", bg='ivory')#Création du Plateau de jeu
Plateau.focus_set()                                                                 #Rend réactif le Plateau
Plateau.pack(side = TOP, padx = 10, pady = 10)                                      #Place le Plateau

#Crée un boutton qui utilise la fonction Recommencer                                                                  
Button(Fenetre, text = "Recommencer", command = Recommencer).pack(side = "left", padx = 5, pady = 5)

#Crée un boutton Quitter qui ferme la Fenetre
Button(Fenetre, text = "Quitter", command = Fenetre.destroy).pack(side = "right", padx = 5, pady = 5)

#Association du Clic Gauche à la fonction clic
Plateau.bind("<Button-1>", clic)                                                    #Associe le clic gauche à la fonction Clic

#Crée un message: Nombre de VictoiresBlue
MessageVictoiresBlue = Label(Fenetre, text=TextVictoiresBlue(VictoiresBlue), bg=ColorBgBlue, fg=ColorFgBlue, font=("Gentium Book Basic",12))
MessageVictoiresBlue.pack(side="right", padx=70, pady=5)

#Crée un message: Nombre de VictoiresPink
MessageVictoiresPink = Label(Fenetre, text=TextVictoiresPink(VictoiresPink), bg=ColorBgPink, fg=ColorFgPink, font=("Gentium Book Basic",12))
MessageVictoiresPink.pack(side="left", padx=70, pady=5)

#----------
''' A ne pas toucher: '''
Recommencer()                                                                       #Crée l'affichage de départ
Fenetre.mainloop()                                                                  #Affiche la fenêtre
