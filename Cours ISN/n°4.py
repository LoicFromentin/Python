print ("Ce programme affichera les 20 premiers termes de la table de multiplication par 7 et mettra une astérisque si ce sont des multiples de 3.")
boucle = 1
while boucle != 0 :
    premierTerme = input("Tapez 0 si vous considérez que la table de 7 commence à 7*0, ou tapez 1 si vous considérez qu'elle commence à 7*1: ")
    if premierTerme == '0':
        boucle = 0
        for i in range (0,20):
            if ((7*i)%3==0):
                print ("7 x",i,"=",7*i,(" <-- Multiple de 3"))
            else:
                print ("7 x",i,"=",7*i)
    elif premierTerme == '1':
        boucle = 0
        for i in range (1,21):
            if ((7*i)%3==0):
                print ("7 x",i,"=",7*i,(" <-- Multiple de 3"))
            else:
                print ("7 x",i,"=",7*i)
    else:
        print ("\nIL FAUT TAPER 0 OU 1!\n")
