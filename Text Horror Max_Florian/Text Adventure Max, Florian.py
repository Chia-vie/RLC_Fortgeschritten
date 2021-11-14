import random
import colorama
#Farben:
#ROT = TOT
#BLAU = FRAGE
#GELB = DROHENDE GEFAHR
#MAGENTA = GESCHICHTE
#TÜRKIS POSIVITVE AUSWIRKUNG AUF DIE ZUKUNFT
#WEIß NEGATIVE AUSWIRKUNG AUF DIE ZUKUNFT
from threading import Timer
from colorama import Fore, Back, Style
import time
f1antwort1 = 'a'
f1antwort2 = 'b'
f1antwort3 = 'c'
a = 'Ich möchte Jagen!'
b = 'Ich suche mir lieber Holz und versuche mich warmzuhalten'
c = 'Ich renne irgendwo hin'
print(Fore.GREEN + 'Hallo. Mein Name ist Max ich bin einer der Entwickler dieses Spieles.\nDie Regeln dieser welt sind simpel:')
time.sleep(2)
print(Fore.RED + 'Rote Texte sind Todesnachrichten')
time.sleep(1)
print(Fore.BLUE + 'Blaue Texte sind Fragen')
time.sleep(1)
print(Fore.YELLOW + 'Gelbe Texte zeigen drohende Gefahren an')
time.sleep(1)
print(Fore.MAGENTA + 'Magenta farbene Texte zeigen die Gischichte an.Beispielsweise das du pinkeln gehst')
time.sleep(1)
print(Fore.CYAN + 'Türkise texte sind positive auswirkungen auf die Zukunft')
time.sleep(1)
print(Fore.WHITE + 'Weiße Texte zeigen Negative auswirkungen auf die Zukunft an')
time.sleep(1)
print(Fore.GREEN + 'Grüne Texte sind Commentare der Entwickler')
time.sleep(1)
print(Fore.GREEN + '\n\n\nBereit los zu legen?')
time.sleep(1)
print(Fore.GREEN + 'Nein?\nNicht mein Problem')
time.sleep(3)
print(Fore.GREEN + '''─░░░─────────░▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓
░░──────▒█████████████▓▓▓▓▓▒▓▓██▓
░────▒███▓▒▒░──░▒▒░──░░░░░░░────██
░───██░───░░▒░░░░───░─░░▒▒▓▓▒░───██
───▓█───▒░───▒░────▒───────▒▒▒░──░█
───█▒─────────░──────▓████▒───────██
──██────██████─────██▓▓█████▓─░────██
─██▒░───▓███████──░████▓█▓▒█▒─▓▓▓█▒─██▓
▓█─░▓██▓──────█─────▒───▒█▓░▒███▓░██──█
██──▒░▒███▒──██───────────▒▒▒──▒█──██─░█
░█─░──█────██▓─────▓██▒─────▒██▒██▒▓█──█
─██░─██░───██▓───██▓░█──▒████───█░─█░─██
──█──████▓───▒██───░████▓░─██▒███────██
──█▓─█▓█░███████████▒░█──▒███▒██────██
──█▓─███░█▓──█▒─░█───▒███████▓█────██
──██─███████████████████───░██────▓█
──██─██████████████▒───█──██▓────░█
──█▓─░██▓█─█─▒█───█────████─────██▒
──█▒──▒██████▒█▒▒███████▒──░▒▓███
──█░──────▒▒██████▒▒░░──░▒░▓███▒
──█──▒─▒▒──────────░▒▒░──▓██░
──█──░▒▒▒▒▒░░─░─░─░───░██
──██─────────────░▒▒▓███
───██▓░──────▒▓████▓░
──░──█████████████''')
time.sleep(7)
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
print(Fore.MAGENTA + 'Du sitzt schon eine Weile am Lagerfeuer')

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
RZ = random.randrange(1,10)
if RZ == '3':
     quit()
else:
     print(Fore.MAGENTA + 'Du weißt nicht was das Ritual macht aber du glaubst das es eine gute Idee ist es zu befolgen')
     print(Fore.MAGENTA + 'Du errinnerst dich an ein Gehäge voll mit Schattenhunden und schaust dich nach anderen Zutaten um')
     print(Fore.MAGENTA +'Wärend du dich umschaust endeckts du eine Rose die Wichtig aussieht')
     K4 = input(Fore.BLUE + 'Was wirst du tun?\nIch klettere über den Landminen umgebenen Stachelzaun um an den Hundeschwanz zu Kommen! [a]\nIch werde mir die Rose holen! [b]\nIch schaue nach einem sicheren Eingang ins Hundegehäge! [c]\n')
     #Du kletterst über das Gehäge und spießt dich auf
     while True:
          if K4 == 'a':
               print(Fore.YELLOW + 'Du versuchst über den Zaun zu klettern aber rutschst ab und fällst auf die Stacheln')
               time.sleep(2)
               print(Fore.CYAN + 'Du schafst es aber dich im letzten Moment zu retten')
               time.sleep(2)
               print(Fore.MAGENTA + 'Mit zitternden Händen dankst du Got das du noch am leben bist')
               time.sleep(1)
               print(Fore.WHITE + 'Das war ein Fehler denn ich, Max, bin der Got dieser Welt')
               print(Fore.RED + 'Als du dich nach einem sichereren Weg ins Gehäge umschaust steigst du auf eine Landmine und explodierst.\nDas hast du davon einem schlechten Got zu danken.')
          elif K4 == 'b':
               print(Fore.YELLOW + 'Während du zur Rose Läufst bemerkst du das eine Hexe im Gebüsch sitzt und auf dich warten zu scheint.')
               time.sleep(1)
               print(Fore.MAGENTA + 'Voller Tatendrang und Adrinalin errinerst du dich an die Millionen an Animes die du geschaut hast.')
               time.sleep(1)
               print(Fore.MAGENTA + 'Dank der Animes hast du dir selbst gelernt wie man mit einem Speer kämpft und nimmst dadurch eine perfecte Kampfhaltung ein')
               dodge = False
               timeout = 3
               t = Timer(timeout, print, [Fore.RED + 'Dir ist eingefallen das du die Kampfpose eines nutzlosen Charakters eingenommen hast und bist\nvor nutzlosigkeit gestorben.'])
               t.start()
               prompt = f"{Fore.BLUE}Drücke enter um die Hexe anzugreifen.\n"
               answer = input(prompt)
               t.cancel()
               if timeout == "0":
                    print(Fore.RED + "Dir ist eingefallen das du die Kampfpose eines nutzlosen Charakters eingenommen hast und bist\nvor nutzlosigkeit gestorben.")
                    quit()
               else:
                    print(Fore.CYAN + "du rennst mir voller geschwindigkeit auf die hexe zu und attackierst mit maximaler kraft")
                    print('Die Hexe ist gleich stark wie du darum wechselst du instingtiv zu Super Saiyajin')
                    print(Fore.MAGENTA + 'Die Hexe und du fangen an in der Luft fliegent weiter zu kämpfen')
                    dodge = True
                    break
     while True
          K4f1 = input(Fore.BLUE + 'Wie willst du angreifen?\n')

#Du gehst zur Rose doch die Hexe wartete schon im Gebüsch bereit zur paarung. ja das wars
#Findest schlüssel neben dem gehäge sperrst auf und schneidest hunden schwanz ab
#Blödsinn schreiben: Dein Gehirn konnte vor lauter entscheidungen nicht richtig sehen und druckte den selbstzerstörungs Konpft weshalt das Universum explodierte



