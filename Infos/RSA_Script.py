#Den Primzahlengenerator importieren
from Primpy import is_prim

'''Buchstaben in Zahlen umwandeln

print(ord('1'))
print(ord('2'))
print(ord('3'))
print(ord('A'))
print(ord('B'))
print(ord('C'))'''

def find_zufallszahl():
    zufallswort = input('Gib irgendeine zufällige abfolge von Zeichen ein: \n')
    zufallszahl = 0
    for letter in zufallswort:
        zufallszahl += ord(letter)
    return zufallszahl

zz1 = find_zufallszahl()
zz2 = find_zufallszahl()
print(zz1, zz2)

def close_prim(zahl):
    while True:
        if is_prim(zahl):
            return zahl
            break
        else:
            zahl += 1


prim_1 = close_prim(zz1)
prim_2 = close_prim(zz2)
print(prim_1, prim_2)

# wird veröffentlicht
n = prim_1*prim_2
print(n)

# geheim
phi_n = ((prim_1-1)*(prim_2-1))
print(phi_n)

#Geeignetes (kleines) e finden, co-prim zu phi_n

phi_n % 7

e = 5

#d finden

def find_d(e,phi_n):
    for i in range(2,phi_n):
        if (i*e) % phi_n == 1:
            break
    return i

d = find_d(e, phi_n)
print(d)

# Überprüfen
(d * e) % phi_n

public_key = {'e':e,'n':n}
private_key = {'d':d,'n':n}

def encrypt(message):
     return (message ** public_key['e']) % public_key['n']


def decrypt(message):
     return ((message ** private_key['d']) % public_key['n'])

text = 89

enc = encrypt(text)

enc

decrypt(enc)
