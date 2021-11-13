'''
date:13.11.2021
authors: Bernhard Wolf
         Katharina Melchart
Skizze Our Origins
'''

#inports:
import random as r



#1 Dunkle Höhle
#alles ist schwarz, bis text erscheint:
print('"Where am I?"')
name = input('"Why am I here? Wait... WHO am I? Ah! I start to remember now...My name is \n"')
        ###passt so weit
print('"What should I do now?"')
#Die Knöpfen mit den 2 Entscheidungen erscheinen

#1.1: Rausgehen-Stöcke holen-Waffe (Faustkeil) bauen/zurück in die Höhle gehen

#1.2.: In Höhle umsehen - Steine/Tiefer in die Höhle gehen-tot

#2 Draußen
decision2 = input('"Look! I found some sticks and branches! '
                  '\nShould I pick them up or should I continue walking?"'
                  '\nPress '1' to pick them up or '2' to keep walking.')
if decision2 == '1':
    print('"Okay, I got them... Who knows when they could be helpful!"')
    decision3 = input('"Should I use them to make a weapon?"\n'
          'Yes(1) or No(2)?')
    if decision3 == '1':
        print('"Wow! I will call this... a hand-axe!"')
elif decision2 == '2':
    print('Suddenly some carnivor attacked you and you died a cruelsome death. The End! :)')

#2.1: Fallgrube-Beim Drübergehen draufgehen
#2.2: Sammeln: gute Beeren/tödliche Pilze-tot

