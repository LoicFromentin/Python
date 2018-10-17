from tkinter import*

#---------------# FONCTIONS #---------------#

#Affiche les Règles du jeu
def Regles(FenetreRegles):
    TicTacToe = Label(FenetreRegles, text = "Règles du Tic Tac Toe", fg = "DarkRed", font =("Yu Mincho Demibold",30)).pack(pady=25, side=TOP)
    Titre1 = Label(FenetreRegles, text = "Comment jouer :", fg = "blue", font =("Yu Mincho Demibold",20)).pack(pady=5, side=TOP)
    Texte1 = Label(FenetreRegles, text = "Cliquer sur une case pour y placer votre pion.",fg="#800080", font = ("Constantia",14)).pack(side=TOP)
    Titre2 = Label(FenetreRegles, text = "\n\nDéroulement de la partie:",fg = "blue", font =("Yu Mincho Demibold",20)).pack(pady=5, side=TOP)
    Texte2 = Label(FenetreRegles, text = "Tour à tour, les joueurs vont placer leur pion sur une case du plateau.",fg="#800080", font = ("Constantia",14)).pack(side=TOP)
    Titre3 = Label(FenetreRegles, text = "\n\nBut du jeu:",fg = "blue", font =("Yu Mincho Demibold",20)).pack(side=TOP)
    Texte3 = Label(FenetreRegles, text = "Aligner 3 pions horizontalement, verticalement ou diagonalement pour gagner.\n",fg="#800080", font = ("Constantia",14)).pack(padx=30,pady=5,side=TOP)

#Remet le jeu à 0, MàJ victoires X/O
def Recommencer ():
    global tour, listeCasesPlateau, Message
    
    Plateau.delete(ALL)                                             #Efface le contenu de la fenêtre
    Lignes()                                                        #Crée les lignes qui délimitent les 9 cases
    listeCasesPlateau = [" "," "," "," "," "," "," "," "," "]       #Contenu des 9 Cases
    tour = 1                                                        #Set up variable "tour"
    Texte = "C'est au tour des  X  de jouer."                       #Texte
    ColorBg = ColorBgX                                              #Couleur du fond
    ColorFg = ColorFgX                                              #Couleur du Texte
    Message.config(text = Texte,bg= ColorBg, fg = ColorFg)          #Affiche le Message

def Quitter():
    global Fenetre
    Fenetre.destroy()
    print("Vous avez quitté le jeu.")

#Dessine les lignes pour délimiter les cases
def Lignes ():
    LigneHorizontale1 = Plateau.create_line(0,120,360,120,width=2)
    LigneHorizontale2 = Plateau.create_line(0,240,360,240,width=2)
    LigneVerticale1 =   Plateau.create_line(120,0,120,360,width=2)
    LigneVerticale2 =   Plateau.create_line(240,0,240,360,width=2)

#Test en Booléen si les X ont win
def VictoireX ():
    if (listeCasesPlateau[0]=='X' and listeCasesPlateau[1]=='X' and listeCasesPlateau[2]=='X'): return (True)
    if (listeCasesPlateau[3]=='X' and listeCasesPlateau[4]=='X' and listeCasesPlateau[5]=='X'): return (True)
    if (listeCasesPlateau[6]=='X' and listeCasesPlateau[7]=='X' and listeCasesPlateau[8]=='X'): return (True)
    if (listeCasesPlateau[0]=='X' and listeCasesPlateau[3]=='X' and listeCasesPlateau[6]=='X'): return (True)
    if (listeCasesPlateau[1]=='X' and listeCasesPlateau[4]=='X' and listeCasesPlateau[7]=='X'): return (True)
    if (listeCasesPlateau[2]=='X' and listeCasesPlateau[5]=='X' and listeCasesPlateau[8]=='X'): return (True)
    if (listeCasesPlateau[0]=='X' and listeCasesPlateau[4]=='X' and listeCasesPlateau[8]=='X'): return (True)
    if (listeCasesPlateau[2]=='X' and listeCasesPlateau[4]=='X' and listeCasesPlateau[6]=='X'): return (True)
    else: return(False)

#Test en Booléen si les O ont win
def VictoireO ():
    if (listeCasesPlateau[0]=='O' and listeCasesPlateau[1]=='O' and listeCasesPlateau[2]=='O'): return (True)
    if (listeCasesPlateau[3]=='O' and listeCasesPlateau[4]=='O' and listeCasesPlateau[5]=='O'): return (True)
    if (listeCasesPlateau[6]=='O' and listeCasesPlateau[7]=='O' and listeCasesPlateau[8]=='O'): return (True)
    if (listeCasesPlateau[0]=='O' and listeCasesPlateau[3]=='O' and listeCasesPlateau[6]=='O'): return (True)
    if (listeCasesPlateau[1]=='O' and listeCasesPlateau[4]=='O' and listeCasesPlateau[7]=='O'): return (True)
    if (listeCasesPlateau[2]=='O' and listeCasesPlateau[5]=='O' and listeCasesPlateau[8]=='O'): return (True)
    if (listeCasesPlateau[0]=='O' and listeCasesPlateau[4]=='O' and listeCasesPlateau[8]=='O'): return (True)
    if (listeCasesPlateau[2]=='O' and listeCasesPlateau[4]=='O' and listeCasesPlateau[6]=='O'): return (True)
    else: return(False)

#Test en Booléen s'il y a match nul
def MatchNul ():
    if VictoireO() == False and VictoireX() == False:               #Si personne n'a gagné
        CasePleine = 0
        for i in range (0,9):                                       #Balaye toutes les cases
            if listeCasesPlateau[i] != ' ':                         #Si la case est occupée
                CasePleine = CasePleine +1                          #Ajoute 1 au compteur
        if CasePleine == 9: return (True)                           #Si les 9 cases sont occupées renvoie True
        else: return (False)                                        #Sinon, renvoie False
    else: return(False)                                             #Si quelqu'un a gagné, renvoie False

#Affiche s'il y a VictoireX, VictoireO ou MatchNul
def TestWinOrNul ():
    global Message,Texte,Color, tour, VictoiresX, VictoiresO
    
    if tour < 60:
        if VictoireX()== True:                                      #Si les X gagnent
            tour = 65                                               #Arrêter le jeu
            Texte = "Les  X  ont gagné !"                           #Change le Texte
            ColorBg = ColorBgX                                      #Change la couleur du fond
            ColorFg = ColorFgX       	                            #Change la couleur du Texte
            Message.config(text = Texte, bg = ColorBg, fg = ColorFg)#Affiche qu'ils ont gagnés
            VictoiresX = VictoiresX +1                              #Ajoute 1 au compteur VictoiresX
            
        if VictoireO()== True:                                      #Si les O gagnent
            tour = 65                                               #Arrêter le jeu
            Texte = "Les  O  ont gagné !"                           #Change le Texte
            ColorBg = ColorBgO                                      #Change la couleur du fond
            ColorFg = ColorFgO                                      #Change la couleur du Texte
            Message.config(text = Texte, bg = ColorBg, fg = ColorFg)#Affiche qu'ils ont gagnés
            VictoiresO = VictoiresO +1                              #Ajoute 1 au compteur VictoiresO
            
        elif MatchNul() == True:                                    #S'il y a Match Nul
            tour = 65                                               #Arrêter le jeu
            Texte = "Match nul !"                                   #Change le Texte
            ColorBg = "#533007"                                     #Change la couleur du fond
            ColorFg = "#E6E2AF"                                     #Change la couleur du Texte
            Message.config(text = Texte, bg = ColorBg, fg = ColorFg)#Affiche qu'il y a match nul
        MessageVictoiresX.config(text= TextVictoiresX (VictoiresX)) #Met à jour le nombre de VictoiresX
        MessageVictoiresO.config(text= TextVictoiresO (VictoiresO)) #Met à jour le nombre de VictoiresO

#Affiche un message Texte
def Affichage (tour,Message):
    if tour < 65:                                                   #Si la partie n'est pas finie
        if tour % 2 != 0:                                           #Si c'est au tour des X de jouer
            Texte = "C'est au tour des  X  de jouer."               #Change le Texte
            ColorBg = ColorBgX                                      #Change la couleur de fond
            ColorFg = ColorFgX                                      #Change la couleur du Texte
        else: 
            Texte = "C'est au tour des  O  de jouer."               #Change le texte
            ColorBg = ColorBgO                                      #Change la couleur de fond
            ColorFg = ColorFgO                                      #Change la couleur du Texte
        Message.config(text = Texte, bg = ColorBg, fg = ColorFg)    #Met à jour le Message
        return (Message)

#Compte le nombre de victoires X
def TextVictoiresX (VictoiresX):
    nombre = str(VictoiresX)                                        #Nombre de VictoiresX
    blabla = "           Victoires X :  "                           #Début de la phrase
    TexteVictoiresX = str(blabla+nombre+"           ")              #Associe le contenu de nombre et blabla en chaîne de caractères
    return(TexteVictoiresX)                                         #Renvoie cette chaîne de caractères

#Compte le nombre de victoires O
def TextVictoiresO (VictoiresO):
    nombre = str(VictoiresO)                                        #Nombre de VictoiresO
    blabla = "           Victoires O :  "                           #Début de la phrase
    TexteVictoiresO = str(blabla+nombre+"           ")              #Associe le contenu de nombre et blabla en chaîne de caractères
    return(TexteVictoiresO)                                         #Renvoie cette chaîne de caractères
    
    
#Faire en sorte qu'à chaque clic ça enregistre dans une liste qu'il y a un signe sur cette case afin de ne pas superposer les signes X/O.
def clic(event):
    global tour, Message, Gagne
    
    FinTour = False    
    X = event.x
    Y = event.y
    rayon = 46                                                      #Rayon du cerle / moitié de la taille des lignes

    #---------- Balayage des Cases ----------#
    hautY = 0                                                       #Coordonnée en haut de la case à tester
    basY =  120                                                     #Coordonnée en bas de la case à tester
    for ligne in range(3):                                          #Teste les 3 lignes
        gaucheX = 0                                                 #Coordonnée à gauche de la case à tester
        droiteX = 120                                               #Coordonnée à droite de la case à tester
        for case in range (3):                                      #Teste les 3 colonnes
            if gaucheX<X<droiteX and hautY<Y<basY:                  #S'il a cliqué dans la case
                X = gaucheX + 60                                    #Centre le clic au mileu de la case
                Y = hautY + 60                                      #Centre le clic au mileu de la case

    #---------- Tour des O ----------#
                if tour%2 == 0 and tour<60:                         #Si la partie n'est pas finie:
                    position = [X,Y]                                #Range les coordonnées du clic dans une liste
                    for i in range(0,9):                            #Balaye les 9 cases
                        if coordCases[i] == position:               #Si clic dans case correspondante à ses coord
                            if listeCasesPlateau[i] == " ":         #Si la case est vide
                                Plateau.create_oval(X-rayon, Y-rayon, X+rayon, Y+rayon, width = 8, outline = "blue")
                                listeCasesPlateau[i] = "O"          #Remplie la case DANS LA LISTE
                                FinTour = True                      #Le joueur a fini son tour
                            else:                                   #Sinon:
                                FinTour = False                     #C'est encore aux O de jouer
                
    #---------- Tour des X ----------#
                if tour%2 != 0 and tour<60:                         #Si la partie n'est pas finie:
                    position = [X,Y]                                #Range les coordonnées du clic dans une liste
                    for i in range(0,9):                            #Balaye les 9 cases
                        if coordCases[i] == position:               #Si clic dans la case correspondante à ses coord
                            if listeCasesPlateau[i] == " ":         #Si la case est vide
                                Plateau.create_line(X-rayon, Y-rayon, X+rayon, Y+rayon, width = 8, fill = "#800080")
                                Plateau.create_line(X-rayon, Y+rayon, X+rayon, Y-rayon, width = 8, fill = "#800080")
                                listeCasesPlateau[i] = "X"          #Remplie la case DANS LA LISTE
                                FinTour = True                      #Le joueur a fini son tour
                            else:                                   #Sinon:
                                FinTour = False                     #C'est encore aux X de jouer
                                
            #Retour à la boucle:                    
            gaucheX,droiteX = droiteX,droiteX+120                   #Passe à la case de droite
        hautY,basY = basY,basY+120                                  #Passe à la colonne d'en bas
        
    #Sorti de la boucle:
        TestWinOrNul ()                                             #Test s'il y a Win / MatchNul
    if FinTour == True:                                             #Si le joueur a fini son tour
        tour = tour + 1                                             #Passe au tour adverse
    if tour<60:                                                     #Si la partie n'est pas finie
        Message = Affichage(tour,Message)                           #Actualise le nom du joueur


#---------------# VARIABLES / LISTES #---------------#

tour = 1                                                            #Tour actuel
Largeur = 360                                                       #Largeur du Plateau de jeu
Hauteur = 360                                                       #Hauteur du Plateau de jeu
VictoiresX = 0                                                      #Nombre de départ de VictoiresX
VictoiresO = 0                                                      #Nombre de départ de VictoiresO
ColorFgX = "#FF75FF"                                                #Couleur d'écriture Pink
ColorBgX = "#2E0039"                                                #Couleur de fond Pink
ColorFgO = "cyan"                                                   #Couleur d'écriture Blue
ColorBgO = "#0B1253"                                                #Couleur de fond Blue
Texte = "C'est au tour des X de jouer."                             #Text pour le tour 1
ColorBg = ColorBgX                                                  #Color du Fond pour le tour 1
ColorFg = ColorFgX                                                  #Color du Texte pour le tour 1
''' + Voir dans la fonction "Commencer" '''

#----------

coordCases = [[60,60],[180,60],[300,60],
              [60,180],[180,180],[300,180],
              [60,300],[180,300],[300,300]]                         #9 Cases
listeCasesPlateau = [" "," "," "," "," "," "," "," "," "]           #9 Cases

#---------------# FENÊTRE REGLES#---------------#

FenetreRegles = Tk()                                                #Crée la fenêtre
FenetreRegles.title("Règles du jeu Tic Tac Toe")                    #Nomme la fenêtre
Regles(FenetreRegles)                                               #Affiche les Règles

#Crée un boutton Quitter qui ferme la Fenetre
BouttonQuitter = Button(FenetreRegles, text="Commencer à jouer", command=FenetreRegles.destroy).pack(side="right", padx=5, pady=5)

''' A NE PAS TOUCHER '''
FenetreRegles.mainloop()                                            #Affiche la fenêtre

#---------------# FENÊTRE #---------------#

#Création de la Fenetre
Fenetre = Tk()                                                      #Crée une Fenetre
Fenetre.title ("Tic Tac Toe")                                       #Nomme la Fenetre

#Affiche un message, ici "C'est au tour des X de jouer." en couleur "cyan"
Message = Label(Fenetre, text = Texte,bg= ColorBg, fg = ColorFg, font = ("Gentium Book Basic",14))
Message.pack(side = TOP, fill = X)

#Création du Plateau de jeu
Plateau = Canvas(Fenetre, width = Largeur, height = Hauteur, bg = "ivory", cursor="heart")
Plateau.focus_set()                                                 #Rend réactif le plateau
Plateau.pack(padx = 5, pady = 10)                                   #Place le plateau

#Association du Clic Gauche à la fonction clic
Plateau.bind("<Button-1>", clic)                                    #Associe le clic gauche à la fonction Clic

#Crée un message: Nombre de VictoiresX
MessageVictoiresX = Label(Fenetre, text=TextVictoiresX(VictoiresX), bg=ColorBgX, fg=ColorFgX, font=("Gentium Book Basic",12))
MessageVictoiresX.pack(side="right")

#Crée un message: Nombre de VictoiresO
MessageVictoiresO = Label(Fenetre, text=TextVictoiresO(VictoiresO), bg=ColorBgO, fg=ColorFgO, font=("Gentium Book Basic",12))
MessageVictoiresO.pack(side="left")

#Crée un menu
MenuFenetre = Menu(Fenetre)
MenuFenetre.add_command(label="Recommencer", command = Recommencer)
MenuFenetre.add_command(label="Quitter",command = Quitter)

#----------
''' A NE PAS TOUCHER '''
Recommencer()                                                       #Crée l'affichage de départ
Fenetre.config(menu = MenuFenetre)
Fenetre.mainloop()                                                  #Affiche la fenêtre
