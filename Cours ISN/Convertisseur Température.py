#Entrée: 1 nombre
#Sortie: 1 nombre
#Convertit une température d'une unité à une autre.

def ConvertTempFahrenheit(a):
    return(1.8*a+32)


def ConvertTempCelsius (a):
    return((a-32)/1.8)


test = 'test'
possibilite = ['Celcius','celcius','c','C','F','f','fahrenheit','Fahrenheit']
while test not in (possibilite):
    test = input("Votre température est-elle en Celcius ou en Fahrenheit? ")
    if (test == 'Celcius') or (test == 'celcius') or (test == 'c') or (test == 'C'):
        temperature = float(input("Tapez la valeur de la température: "))
        print("La température correspondante en degré Fahrenheit est:",ConvertTempFahrenheit(temperature))
        
    elif (test == 'Fahrenheit') or (test == 'fahrenheit') or (test == 'f') or (test == 'F'):
        temperature = float(input("Tapez la valeur de la température: "))
        print("La température correspondante en degré Celsius est:",ConvertTempCelsius(temperature))
    else:
        print("Votre réponse ne fait pas partie des possibilités ci-dessous:\n[Celcius] [celcius] [c] [C] [F] [f] [fahrenheit] [Fahrenheit]\n\n")
             
