'''
Primzahlengenerator
author: Christine Ackerl
date: November 2021
'''
import math

def is_prim(zahl):

    last_digit = int(str(zahl)[-1])
    last_two_digits = int(str(zahl)[-2:])

    if zahl in [2,3,5]:
        primzahl = True

    # Zahlen die mit 5 oder 0 enden sind keine Primzahlen, außer 5
    elif last_digit == 5 or last_digit == 0:
        primzahl = False

    # Gerade Zahlen sind keine Primzahlen, außer die Zahl 2
    elif last_digit % 2 == 0:
        primzahl = False

    # Ist die Ziffernsumme durch 3 teilbar so ist es auch die Zahl selbst
    elif sum(int(x) for x in str(zahl)) % 3 == 0:
        primzahl = False

    else:
        primzahl = True
        z = 7
        while z < math.sqrt(zahl):
            if zahl % z == 0:
                primzahl = False
                break
            z+=2

    return primzahl
