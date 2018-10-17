#Ce programme permet de convertur une note sous forme de points en note standardisé.

a=int(input("Entrez le nombre de points de l'élève: "))
b=int(input("Entrez le nombre maximal de points: "))

if (a>=0.8*b) :
    print ("L'élève a eu la note de",a,"sur",b,"ce qui correspond à l'appréciation A.")
elif (0.8*b>=a>=0.6*b):
    print ("L'élève a eu la note de",a,"sur",b,"ce qui correspond à l'appréciation B.")
elif (0.6*b>=a>=0.5*b):
    print ("L'élève a eu la note de",a,"sur",b,"ce qui correspond à l'appréciation C.")
elif (0.5*b>=a>=0.4*b):
    print ("L'élève a eu la note de",a,"sur",b,"ce qui correspond à l'appréciation D.")
elif (a<0.4*b):
    print ("L'élève a eu la note de",a,"sur",b,"ce qui correspond à l'appréciation E.")
