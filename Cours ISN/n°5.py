print ("Ce programme calculera les 50 premiers termes de la table de multiplication par 13, mais n'affichera que ceux qui sont multiple de 7.")
boucle = 1
while boucle != 0 :
    premierTerme = input("Tapez 0 si vous considérez que la table de 13 commence à 13*0, ou tapez 1 si vous considérez qu'elle commence à 13*1: ")
    if premierTerme == '0':
        boucle = 0
        for i in range (0,50):
            if ((13*i)%7==0):
                print ("13 x",i,"=",13*i,(" <-- Multiple de 7"))
            else:
                print ("13 x",i,"=",13*i)
    elif premierTerme == '1':
        boucle = 0
        for i in range (1,51):
            if ((13*i)%7==0):
                print ("13 x",i,"=",13*i,(" <-- Multiple de 7"))
            else:
                print ("13 x",i,"=",13*i)
    else:
        print ("\nIL FAUT TAPER 0 OU 1!\n")
