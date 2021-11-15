#Den Primzahlengenerator importieren
from Primpy import is_prim

def find_zufallszahl():
    zufallswort = input('Gib irgendeine zufällige abfolge von Zeichen ein: \n')
    zufallszahl = 0
    for letter in zufallswort:
        zufallszahl += ord(letter)
    return zufallszahl

def close_prim(zahl):
    while True:
        if is_prim(zahl):
            return zahl
            break
        else:
            zahl += 1

def find_e(phi_n):
    e = 2
    while True:
        if not phi_n % e == 0:
            return e
        else:
            e+=1

def find_d(e,phi_n):
    for i in range(2,phi_n):
        if (i*e) % phi_n == 1:
            break
    return i


zz1 = find_zufallszahl()
zz2 = find_zufallszahl()

prim_1 = close_prim(zz1)
prim_2 = close_prim(zz2)

# wird veröffentlicht
n = prim_1*prim_2

# geheim
phi_n = ((prim_1-1)*(prim_2-1))

#Geeignetes (kleines) e finden, co-prim zu phi_n
e = find_e(phi_n)

# d finden
d = find_d(e, phi_n)

# Überprüfen
if not (d * e) % phi_n == 1:
    raise(ValueError('Irgendwas stimmt nicht mit '))


public_key = {'e':e,'n':n}
private_key = {'d':d,'n':n}

print(f'public_keys:{public_key}')
print(f'private_keys:{private_key}')