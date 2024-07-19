# HUNDREGISTRET
# Ditt namn här

'''
********************
KLASSER
********************
'''

class Hund:
     
     def __init__(self, namn, ras, ålder):
          self.namn = namn
          self.ras = ras
          self.ålder = ålder


'''
********************
VARIABLER
********************
'''

# detta är en list av hundar
hundar = [Hund() for _ in range(0)]

'''
********************
FUNKTIONER
********************
'''

# Funktionen skrivInHund
# Här kan man skriva in en eller flera hundar, tills anv säger nej.

def skrivInHund():
    fortsätt = True

    while fortsätt:
         namn = input('Ange hundens namn: ')
         ras = input('Ange hundens ras: ')
         while True:
             try:
                 ålder = int(input('Ange hundens ålder: '))
             except ValueError:
                 print('Hundens ålder måste vara ett heltal.')
                 continue
             else:
                 break

         nyHund = Hund(namn, ras, ålder)
         hundar.append(nyHund)

         while True:
             janej = input('Vill du skriva in en till hund? (ja/nej)? ')
             if (janej.lower() == 'nej'):
                 fortsätt = False
                 break
             if (janej.lower() == 'ja'):
                 break
             else:
                 continue


# Funktionen yngstaHunden
# Hittar den yngsta hunden och skriver ut åldern.

def yngstaHunden():
    if not hundar:
        print('Det finns inga hundar i registret')
    else:
        yngst = min(hundar, key=lambda hund: hund.ålder)
        print('Den yngsta hunden heter ' + yngst.namn + ' som är ' + str(yngst.ålder) + ' år och är en ' + yngst.ras + '.')
    
     

# **********************************************
# **********************************************


# Här börjar själva programmet

print('Välkommen till hundregistret!')
fortsätt = True
while fortsätt:
    if len(hundar) == 1:
        hundEllerHundar = 'hund'
    else:
        hundEllerHundar = 'hundar'
    print('\nDet finns ' + str(len(hundar)) + ' ' + hundEllerHundar + ' i registret\n')

    while True:
        userInput = input('Skriv H för att lägga till en hund, Y för att hitta den yngsta hunden A för att avsluta programmet. ')
        if userInput.lower() == 'h':
            skrivInHund()
            break
        if userInput.lower() == 'y':
            yngstaHunden()
            break
        if userInput.lower() == 'a':
            fortsätt = False
            break
        else:
            continue

print('Tack för att du ville använda detta utmärkta program!')