from Primpy import is_prim
import colorama
from colorama import Fore
def randomzahl():
    zufallswort = input(Fore.CYAN + 'Gib eine komplett zufällige Abfolge von Zeichen ein')
    zufallszahl = 0
    for buchstabe in zufallswort:
        zufallszahl += ord(buchstabe)
    return zufallszahl


def primschloss(nummer):
    while True:
        if is_prim(nummer):
            return nummer
            break
        else:
            nummer += 1

def teilerfremd(teiler):
    for i in [3,5,7,11,13,17,23]:
        if not phi_n % i == 0:
            return i

def finde_d(e,phi_n):
    for i in range(2,phi_n):
        if (i*e) % phi_n == 1:
            break
        return i

zahl1 = randomzahl()
zahl2 = randomzahl()
print(zahl1, zahl2)

primzahl1 = primschloss(zahl1)
primzahl2 = primschloss(zahl2)
print(primzahl1, primzahl2)

#veröffentlichte werte
n = primzahl1*primzahl2
print(f'Das ist n: {n}')

#geheime werte
phi_n = ((primzahl1-1)*(primzahl2-1))
print(f'Das ist phi_n: {phi_n}')

e = teilerfremd(phi_n)

d = finde_d(e, phi_n)
print(f'Das ist d: {d}')

(d * e) % phi_n

public_key = {'e':e,'n':n}
private_key= {'d':d,'n':n}

def encrypt(message):
     return (message ** public_key['e']) % public_key['n']

def decrypt(message):
    return((message ** private_key['d']) % public_key['n'])

text = 89
enc = encrypt(text)
print(f'Das ist der verschlüsselte Text: {enc}')


dec = decrypt(enc)
print(f'Das ist der entschlüsselte Text: {dec}')






