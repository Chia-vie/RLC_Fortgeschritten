import random
import colorama
from colorama import Fore, Back, Style
import time
from threading import Timer
#Farben:
#ROT = TOT
#BLAU = FRAGE
#GELB = DROHENDE GEFAHR
#MAGENTA = GESCHICHTE
#TÜRKIS POSIVITVE AUSWIRKUNG AUF DIE ZUKUNFT
#WEIß NEGATIVE AUSWIRKUNG AUF DIE ZUKUNFT
f1antwort1 = 'a'
f1antwort2 = 'b'
f1antwort3 = 'c'
f2antwort1 = 'd'
f2antwort2 = 'e'
f2antwort3 = 'f'
f3antwort1 = 'g'
f3antwort2 = 'h'
f3antwort3 = 'i'
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
          print(Fore.YELLOW)
          time.sleep(3.5)
     elif weg == f1antwort3:
          print(f'{Fore.RED}Du Opfer bist gegen einen Baum gerannt, hingefallen und hast dir das Genick am einem Felsen gebrochen.')
          quit()
     else:
          print(Fore.RED + 'Keine Ahnung was mit deinem Gehirn los ist doch es ist ausgefallen... Die Wölfe haben dich gefressem.')
          quit()
     if weg == 'b':
      break

#Kapitel 2 Das Lagerfeuer
print(Fore.MAGENTA + 'Du sitzt schon eine Weile am Lagerfeuer, Plötzlich hörst du ein Geräusch....')
time.sleep(2)
print(Fore.MAGENTA + 'Was könnte das bloß sein?')
pfad = input(Fore.BLUE + '''Was tust du jetzt?
Ich suche nach Spitzen Ästen um mich verteidigen zu können, gehe aber auch das Risiko ein zu Sterben [d]
Ich bleibe sitzen und hoffe, dass ich nicht getötet werde [e]
Ich folge dem Geräusch [f]
''')
while True:
     if pfad == f2antwort1:
          print(Fore.MAGENTA + 'Du findest ein Stück Holz und gehst zum Lagerfeuer zurück')
          time.sleep(1)
          print(Fore.MAGENTA + '*Speer schnitzen....*')
          time.sleep(2)
          print(Fore.CYAN + 'Jetzt bist du bewaffnet')
          time.sleep(2)
          print(Fore.YELLOW + 'Doch was ist das? Ein Wolf!')
          timeout = 3
          time.sleep(1)
          t = Timer(timeout, print, [Fore.RED + 'Der Wolf hat dich gefressen.'])
          t.start()
          prompt = "Schnell! Besiege den Wolf! Drücke r!!!\n"
          answer = input(prompt)
          t.cancel()
          ssd = 'r'
          if answer == ssd:
               print(Fore.CYAN + 'Du hast den Wolf besiegt und überlebt. Doch das Geräusch hört nicht auf, du folgst ihm')
               time.sleep(5)
          elif timeout == '0':
               quit()
          else:
               quit()
     elif pfad == f2antwort2:
          print(Fore.WHITE + 'Du bleibst sitzen doch das Geräusch kommt näher....')
          time.sleep(1.5)
          print(Fore.WHITE + 'Du versteckst dich hinter einem Baum und bleibst unentdeckt...')
          time.sleep(1)
          print(Fore.WHITE + 'Du weißt beim Lagerfeur ist es nicht sicher und folgst dem Geräusch')
          time.sleep(3)
     elif pfad == f2antwort3:
          print(Fore.RED + 'Du gehst dem Geräusch nacht doch bis du sehen kannst was es ist steigt deine Seele schon gen Himmel')
          quit()
     else:
          print(Fore.RED + 'Du hast das gleichgewicht verloren und bist ins Lagerfeuer gefallen')
          quit()
     if pfad == 'd' or 'e':
      break

#Kapitel 3 Das Haus
print(Fore.MAGENTA + 'Du bist dem Geräusch gefolgt und bei einem Haus gelandet. ')
time.sleep(5)
print(Fore.MAGENTA + '''Du verschaffst dir einen groben Überblick und siehst siehst eine Tür ins Haus, doch dort ist 
das Geräusch am lautesten. Es gibt sowohl auch einen gruseligen Friedhof und einen abgelegenen Schuppen.
''')
time.sleep(5)
weg3 = input(Fore.BLUE + 'Wohin möchtest du?')
time.sleep(0.5)
print('''Ich gehe zur Tür und schaue mir das Haus genauer an. [g]
Ich gehe gruseligen Friedhof [h]
Ich möchte zum Schuppen, da er sehr abgelegen ist [i]
''')
while True:
     if weg3 == f3antwort1:
          print(Fore.YELLOW + 'Du gehst zur tür doch....sie lässt sich nicht öffnen')
          time.sleep(1.5)
          print(Fore.YELLOW + 'Du trittst stark gegen die Tür und verursachst ein lautes Knacksen. Sie öffnet sich')
          time.sleep(2)
          print(Fore.RED + 'Du betrittst das Haus doch die Hexe, die das Geräusch gehört hatte, bringt dich um')
          quit()
     elif weg3 == f3antwort2:
          print(Fore.RED + 'Du bist zum Friedhof gegangen und wurdest von den Untoten penetriert. Nach 10 Minuten bist du gestorben')
          quit()
     elif weg3 == f3antwort3:
          print(Fore.MAGENTA)





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



