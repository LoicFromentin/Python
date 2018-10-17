#Entrées: 3 nombres
#Sorties: 3 nombres
#Fonction permettant de placer la plus grande valeur en 3° position.
def PlusGrand (a,b,c):
    if a>b and a>c:
        return (c,b,a)
    elif b>a and b>c:
        return (a,c,b)
    else:
        return (a,b,c)

#Entrées: 3 nombres
#Sorties: une phrase et un test
def Existe (a,b,c): #Avec c plus grand que a et b.
    if (a+b)>=c:
        return True

#Entrées: 3 nombres
#Sorties: 3 nombres
def Rectangle (a,b,c):
    if ((b**2)+(a**2)==(c**2)):
        print ("Ce triangle est rectangle.")

#Entrées: 3 nombres
#Sorties: 3 nombres
def IsoceleRectangle (a,b,c):
    if ((c*c) == (b*b)+(a*a)):
        if (a==b) or (b==c) or (a==c):
          print ("Ce triangle est isocèle et rectangle.")

#Entrées: 3 nombres
#Sorties: 3 nombres
def Isocele (a,b,c):
    if ((a==b) or (a==c) or (b==c)) and ((a!=b) or (a!=c) or (b!=c)):
        print ("Ce triangle est isocèle.")

#Entrées: 3 nombres
#Sorties: 3 nombres
def Equilateral (a,b,c):
    if (a==b==c):
        print ("Ce triangle est équilatéral.")

#Entrées: 3 nombres
#Sorties: 3 nombres
def Quelconque (a,b,c):
    if ((c**2)!=(b**2)+(a**2)) and (a!=b) and (b!=c) and (a!=c):
        print("Ce triangle est quelconque.")

#---------------# Programme principal #---------------#
#--- IL NE MARCHE PAS ---#
print("Afin procéder au test sur la nature du triangle, veuillez entrer les longueurs des 3 côtés.")
boucle = 1
while (boucle != 0):
    a=float(input("Première longueur: "))
    b=float(input("Deuxième longueur: "))
    c=float(input("Troisième longueur: "))
    PlusGrand (a,b,c)
    if Existe (a,b,c) == True:
        Rectangle (a,b,c)
        IsoceleRectangle (a,b,c)
        Isocele (a,b,c)
        Equilateral (a,b,c)
        Quelconque (a,b,c)
        boucle = 0
    else:
        print ("On ne peut pas former de triangle avec ces mesures.")

