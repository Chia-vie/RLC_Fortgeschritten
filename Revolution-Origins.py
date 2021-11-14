'''
date:13.11.2021
authors: Bernhard Wolf
         Katharina Melchart
Skizze Our Origins
'''
#inports:
import random as r
import keyboard
import time
death = False
def tools_death():
    print('You kept walking. Suddenly some carnivor attacked you and you died a cruelsome death. The End! :)')
    death = True
def minigame():
    print("This is the Minigame, press a to gather Wood or press d to gather stone, exit with e")
    print("For a weapon you need 3 stone and 2 wood")
    global wood
    global stone
    wood = 0
    stone = 0
    while True:
        if keyboard.is_pressed('a'):
            wood = wood + 1
            print("\rYou got 1 wood!")
            print("You have " + wood + " wood")
            time.sleep(0.5)
        if keyboard.is_pressed('d'):
            stone = stone + 1
            print("\rYou got 1 stone!")
            print("You have " + stone + " stone")
            time.sleep(0.5)
        if keyboard.is_pressed('e'):
            break
print('Where am I?')
name = input('Why am I here? Wait... WHO am I? Ah! I start to remember now...My name is \n')
        ###passt so weit
print('What should I do now?')
print('Should I look around in the Cave or should I go outside?')
Look_or_Outside = input('1: Outside\nor\n2: Cave\n')
if Look_or_Outside == "1":
    death = False
elif Look_or_Outside == '2':
    print('You went further into the cave. Suddenly, you heard a weird sound.\n'
          '"What could that possibly be?" You were getting scared. \nAll of the sudden, a huge bear appeared behind you and bit your head off. Adios, {}!  ;)'.format(name))
    death = True
    exit

#2 Draußen
decision2 = input('"Look! I found some sticks and branches! '
                  '\nShould I pick them up (minigame) or should I continue walking?"'
                  '\nPress 1 to pick them up or 2 to keep walking.')
if decision2 == '1':
    minigame()
    decision3 = input('"Should I use them to make a weapon?"\n'
          'Yes(1) or No(2)?')
    if decision3 == '1':
        if stone < 3
            tools_death()
            exit(0)
        if wood <  2
            tools_death()
            exit(0)
        stone = stone - 3
        wood = wood - 3
        print('"Wow! I will call this... a hand-axe!"')
elif decision2 == '2':
    tools_death()
#2.1: Fallgrube-Beim Drübergehen draufgehen
#2.2: Sammeln: gute Beeren/tödliche Pilze-tot
