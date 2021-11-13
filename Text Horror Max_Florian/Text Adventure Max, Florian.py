import random
import colorama
from colorama import Fore, Back, Style
import time
f1antwort1 = 'a'
f1antwort2 = 'b'
f1antwort3 = 'c'
a = 'Ich möchte Jagen!'
b = 'Ich suche mir lieber Holz und versuche mich warmzuhalten'
c = 'Ich renne irgendwo hin'

print(f'{Fore.MAGENTA}Du bist mit deinen Freunden wandern gegangen. Sie wollten kurz pinkeln gehen doch kamen nicht zurück.')
print(f' Es wurde schon dunkel und du hörst ein seltsames Geräusch. Irgendwo muss jemand geschrien haben. ')
print(f'Du hast ein Feuerzeug dabei doch kein Holz... Oh nein! Dein Magen tut schon weh...')
time.sleep(5)

weg = input(Fore.BLUE + '''Wie gehst du vor?
Ich möchte jagen gehen! [a]
cIch suche mir lieber Holz und versuche mich warmzuhalten! [b]
Ich renne irgendwo hin! [c]
''')
while True:
     if weg == f1antwort1:
          print(f'{Fore.RED}Du bist jagen gegangen, doch hattest keine Waffen. Die Wölfe hatten ein leichtes Spiel')
          quit()
     elif weg == f1antwort2:
          print(f'{Fore.CYAN}Du hast Holz gefunden und dir ein Lagerfeuer gemacht...Doch die Wölfe wittern dich schon...')
     elif weg == f1antwort3:
          print(f'{Fore.RED}Du Opfer bist gegen einen Baum gerannt, hingefallen und hast dir das Genick am einem Felsen gebrochen.')
          quit()
     else:
          print(Fore.RED + 'Keine Ahnung was mit deinem Gehirn los ist doch es ist ausgefallen... Die Wölfe haben dich gefressem.')
          quit()
     if weg == 'b':
      break

#Kapitel 2 Das Lagerfeuer
print(Fore.BLUE + 'Du sitzt schon eine Weile am Lagerfeuer')

#Speer
    #Speer Waffe Zum Geräusch
#sitzen
    #Geräusch lauter, verstecken , Geräusch läuft weg, du laufen nach. Start Kapitel 3
#zum Geräusch
    #Du wirst gegessen

#Kapitel 3 Das Haus
#Info: Du folgst dem Geräusch und landest beim Haus, es gibt Schuppen, Gehäge Schattenhunde, Friedhof
#Zu Tür gehen und versuchen sie zu öffnen, Hexe hört lautes geräusch der türe und bringt dich um
#Friedhof: Untote kommen aus dem Gräbern und penetrieren dich. Nach 10 minutwen macht die hexe mit und du stirbst
#Schuppen: Man findet eine Gartenschere. Du findest einen Zettel mit einem Rezept für ein Ritual: Hexenhaare, Hundeschwanz und eine Rose und Zweigpuppe
#Blödsinn schreiben: Du warst dir unschlüssig und bist an Luft erstickt

#Kapitel 4 Das Haus 2
#Info: Nach dem du die Schere und den Zettel gefunden hast, findest du schon einmal kleine schattenhunde sowie eine rose, doch aus der richtung der rose hörst du ein komisches geräusch. Das Gehäge ist versperrt der Zaun sieht gefärhlich aus.
#Du kletterst über das Gehäge und spießt dich auf
#Du gehst zur Rose doch die Hexe wartete schon im Gebüsch bereit zur paarung. ja das wars
#Findest schlüssel neben dem gehäge sperrst auf und schneidest hunden schwanz ab



