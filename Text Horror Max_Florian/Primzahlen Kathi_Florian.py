import colorama
from colorama import Fore
a = True
primzahl = int(input(Fore.CYAN + 'Gib eine Zahl ein um zu überprüfen ob es eine Primzahl ist'))
primzahlliste = []
nichtprimzahlliste = []
if primzahl == 2:
    print(Fore.GREEN + 'Deine Zahl ist eine Primzahl')
elif primzahl <= 1:
    print(Fore.RED + 'Deine Zahl ist keine Primzahl')
else:
    for i in range (2, primzahl):
        if primzahl % i == 0:
            a = False
            nichtprimzahlliste.append(i)
        elif nichtprimzahlliste == []:
            pass
    if a == False:
        print(primzahl, 'ist durch', nichtprimzahlliste, 'teilbar, ist somit keine primzahl')
    if a == True:
        print(primzahl, 'ist eine Primzahl')
