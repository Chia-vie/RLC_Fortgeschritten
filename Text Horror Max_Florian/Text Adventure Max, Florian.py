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

from threading import Timer
#Kapitel 2 Das Lagerfeuer
print(Fore.MAGENTA + 'Du sitzt schon eine Weile am Lagerfeuer, Plötzlich hörst du ein Geräusch....')
time.sleep(2)
print(Fore.MAGENTA + 'Was könnte das bloß sein?')
time.sleep(3)
pfad = input(Fore.BLUE + '''Was tust du jetzt?
Ich suche nach Spitzen Ästen um mich verteidigen zu können, gehe aber auch das Risiko ein zu Sterben [d]
Ich bleibe sitzen und hoffe, dass ich nicht getötet werde [e]
Ich folge dem Geräusch [f]
''')
f2antwort1 = 'd'
f2antwort2 = 'e'
f2antwort3 = 'f'

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
weg3 = input(Fore.BLUE + '''Wohin möchtest du?
Ich gehe zur Tür und schaue mir das Haus genauer an. [g]
Ich gehe gruseligen Friedhof [h]
Ich möchte zum Schuppen, da er sehr abgelegen ist [i]
''')
f3antwort1 = 'g'
f3antwort2 = 'h'
f3antwort3 = 'i'
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
          print(Fore.MAGENTA + '''Du bist zum Schuppen gegangen und hast eine Gartenschere, sowie ein Rezept für ein
          Ritual gefunden''')
          time.sleep(4)
     else:
          print(Fore.RED + 'Du warst dir unschlüssig und bist an Luft erstickt')
          quit()
     if weg3 == 'i':
      break


RZ = random.randrange(1,10)
if RZ == '3':
     quit()
else:
     print(Fore.MAGENTA + 'Du weißt nicht was das Ritual macht aber du glaubst das es eine gute Idee ist es zu befolgen')
     print(Fore.MAGENTA + 'Du errinnerst dich an ein Gehäge voll mit Schattenhunden und schaust dich nach anderen Zutaten um')
     print(Fore.MAGENTA +'Wärend du dich umschaust endeckts du eine Rose die Wichtig aussieht')
     time.sleep(9)
     K4 = input(Fore.BLUE + 'Was wirst du tun?\nIch klettere über den Landminen umgebenen Stachelzaun um an den Hundeschwanz zu Kommen! [a]\nIch werde mir die Rose holen! [b]\nIch schaue nach einem sicheren Eingang ins Hundegehäge! [c]\n')
     #Du kletterst über das Gehäge und spießt dich auf
     while True:
          if K4 == 'a':
               print(Fore.YELLOW + 'Du versuchst über den Zaun zu klettern aber rutschst ab und fällst auf die Stacheln')
               time.sleep(2)
               print(Fore.CYAN + 'Du schafst es aber dich im letzten Moment zu retten')
               time.sleep(2)
               print(Fore.MAGENTA + 'Mit zitternden Händen dankst du Gott das du noch am leben bist')
               time.sleep(1)
               print(Fore.WHITE + 'Das war ein Fehler denn ich, Max, bin der Gott dieser Welt')
               print(Fore.RED + 'Als du dich nach einem sichereren Weg ins Gehäge umschaust steigst du auf eine Landmine und explodierst.\nDas hast du davon einem schlechten Gott zu danken.')
               quit()
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
#    while True
#          K4f1 = input(Fore.BLUE + 'Wie willst du angreifen?\n')

#Du gehst zur Rose doch die Hexe wartete schon im Gebüsch bereit zur paarung. ja das wars
#Findest schlüssel neben dem gehäge sperrst auf und schneidest hunden schwanz ab
#Blödsinn schreiben: Dein Gehirn konnte vor lauter entscheidungen nicht richtig sehen und druckte den selbstzerstörungs Konpft weshalt das Universum explodierte



