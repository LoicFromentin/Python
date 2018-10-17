from random import*

#---------- Programme principal ----------#

ListeAdversaire=['joueur','autre joueur','autre','ordinateur',"l'ordinateur","l'ordi",'ordi',]
adversaire = 'adversaire'
while (adversaire not in (ListeAdversaire)):
    adversaire = input("Vous pouvez jouer contre [ORDINATEUR] ou contre [AUTRE JOUEUR]. \nVeuillez taper votre choix: ")
    adversaire = adversaire.lower()

#---------- Contre l'ordinateur ----------#

if (adversaire in ('ordinateur',"l'ordinateur","l'ordi",'ordi')):
    niveau='niveau'
    while niveau not in('facile','difficile'):
        niveau = input ("\nVeuillez tout d'abord choisir entre le niveau [Facile] ou [Difficile]: ")
        niveau = niveau.lower()

#---------- Niveau Facile ----------#

    if (niveau == 'facile'):
        allumettes = int (input ("\nVeuillez entrer le nombre d'allumettes de départ: "))
        tour = 0
        while (allumettes > 0):
            if (tour%2 == 0):
                if allumettes == 1:
                    nombreOrdi = 1
                elif allumettes == 2:
                    nombreOrdi = randint(1,2)
                else:
                    nombreOrdi = randint(1,3)
                print ("L'ordinateur a décidé d'enlever",nombreOrdi,"allumettes.")
                allumettes = allumettes - nombreOrdi
                if (allumettes == 0):
                   print ("L'ordinateur a gagné en",tour//2,"tours!")
            else:
                nombreJoueur = 0
                while (nombreJoueur not in (1,2,3)):
                    nombreJoueur = int (input ("Veuillez entrer le nombre d'allumettes à enlever (entre 1 et 3): "))
                allumettes = allumettes - nombreJoueur
                if (allumettes == 0):
                    print ("Vous avez gagné en",tour//2,"tours!")
            tour = tour + 1
            if (allumettes > 0):
                print ("Il reste",allumettes,"allumettes.")

#---------- Niveau Difficile ----------#

    elif (niveau == 'difficile'):
        allumettes = int (input ("\nVeuillez entrer le nombre d'allumettes de départ: "))
        tour = 1
        while (allumettes > 0):
            if (tour%2 == 0):
                if allumettes == (1,2,3):
                    nombreOrdi = allumettes
                elif ((allumettes%4) != 0):
                    if ((allumettes-1)%4 == 0):
                        nombreOrdi = 1
                    elif ((allumettes-2)%4 == 0):
                        nombreOrdi = 2
                    elif ((allumettes-3)%4 == 0):
                        nombreOrdi = 3
                else:
                    nombreOrdi= randint(1,3)
                print ("\nL'ordinateur a décidé d'enlever",nombreOrdi,"allumettes.")
                allumettes = allumettes - nombreOrdi
                if (allumettes == 0):
                    print ("L'ordinateur vous a battu en",tour//2,"tours!")
            else:
                nombreJoueur = 0
                while (nombreJoueur not in (1,2,3)):
                    nombreJoueur = float(input("\nVeuillez entrer le nombre d'allumettes à enlever (entre 1 et 3): "))
                allumettes = allumettes - nombreJoueur
                if (allumettes == 0):
                    print ("\n\nVous avez gagné en",tour//2,"tours!")
            tour = tour + 1
            if (allumettes > 0):
                print ("Il reste",int(allumettes),"allumettes.")

#---------- Contre Joueur ----------#

if (adversaire in ('joueur','autre joueur','autre')):
    Personnalisation = "personnalisation"
    while Personnalisation not in ('oui','Oui','OUI','non','Non','NON'):
        Personnalisation = input ("\nSouhaitez vous oui ou non utiliser des pseudos personnalisés? ")
        Personnalisation = Personnalisation.lower()

    #---------- PSEUDOS PERSONNALISES ----------#
    if Personnalisation == 'oui':
        PseudoJoueur1 = input ("Veuillez entrer le pseudo du JOUEUR 1: ")
        PseudoJoueur2 = input ("Veuillez entrer le pseudo du JOUEUR 2: ")
        allumettes = int (input ("Veuillez entrer le nombre d'allumettes de départ: "))
        tour = 0
        while (allumettes > 0):
            if (tour%2 == 0):
                Joueur1 = 0
                while (Joueur1 not in (1,2,3)):
                    print ("[",PseudoJoueur1,"] doit entrer le nombre d'allumettes à enlever (entre 1 et 3): ")
                    Joueur1 = float (input(""))
                allumettes = allumettes - Joueur1
                if (allumettes == 0):
                    print ("[",PseudoJoueur1,"] a gagné en",(tour+1)//2,"tours!")
            else:
                Joueur2 = 0
                while (Joueur2 not in (1,2,3)):
                    print ("[",PseudoJoueur2,"] doit entrer le nombre d'allumettes à enlever (entre 1 et 3): ")
                    Joueur2 = float (input(""))
                allumettes = allumettes - Joueur2
                if (allumettes == 0):
                    print ("[",PseudoJoueur2,"] a gagné en",(tour+1)//2,"tours!")
            tour = tour + 1
            print ("Il reste",allumettes,"allumettes.")

    #---------- PSEUDOS NON PERSONNALISES ----------#
            
    if Personnalisation == 'non':
        allumettes = int (input ("Veuillez entrer le nombre d'allumettes de départ: "))
        tour = 0
        while (allumettes > 0):
            if (tour%2 == 0):
                Joueur1 = 0
                while (Joueur1 not in (1,2,3)):
                    Joueur1 = float (input("Le Joueur1 doit entrer le nombre d'allumettes à enlever (entre 1 et 3): "))
                allumettes = allumettes - Joueur1
                if (allumettes == 0):
                    print ("Le Joueur1 a gagné en",(tour+1)//2,"tours!")
            else:
                Joueur2 = 0
                while (Joueur2 not in (1,2,3)):
                    Joueur2 = float (input("Le Joueur2 doit entrer le nombre d'allumettes à enlever (entre 1 et 3): "))
                allumettes = allumettes - Joueur2
                if (allumettes == 0):
                    print ("Le Joueur2 a gagné en",(tour+1)//2,"tours!")
            tour = tour + 1
            print ("Il reste",allumettes,"allumettes.")         
