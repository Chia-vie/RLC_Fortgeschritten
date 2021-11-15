from Primpy import is_prim
from Binhex import bintext
from Binhex import textbin

print(ord('1'))
print(ord('2'))
print(ord('3'))
print(ord('A'))
print(ord('B'))
print(ord('C'))

def zufallszahl_finden():
    zufallswort = input('Gib mir viele zufällige Zeichen! ;) \n')
    zufallszahl = 0
    for letter in zufallswort:
        zufallszahl += ord(letter)
    return zufallszahl

zz1 = zufallszahl_finden()
zz2 = zufallszahl_finden()
print(zz1, zz2)

def prim_close(zahl):
    while True:
        if is_prim(zahl):
            return zahl
            break
        else:
            zahl += 1

prim_1 = prim_close(zz1)
prim_2 = prim_close(zz2)
print(prim_1,prim_2)

#publi key
n = prim_1*prim_2
print(n)

#private key
phi_n = ((prim_1-1)*(prim_2-1))
print(phi_n)

def find_e(phi_n):
    e = 0
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

print(find_e(phi_n))

print(phi_n)

d = find_d(e, phi_n)
print(d)

#test:
d = find_d(e, phi_n)
print(d)

d*e

public_key = {'e':e,'n':n}
private_key = {'d':d,'n':n}

def encrypt(message):
     return (message ** public_key['e']) % public_key['n']

def decrypt(message):
     return ((message ** private_key['d']) % public_key['n'])

#text = 0o0000001000100000000110111100000011011100000001110100000000010000000000011000100000001100101000000010000000000011100110000001110101000000111001100000011100000000001101001000000110001100000011010010000001101111000000111010100000011100110000000100001
#text = 0o01000001
text =  ord('a')

enc = encrypt(text)

dec = decrypt(enc)

print(enc)

print(chr(dec))


#binaer = textbin(str)
#klar = bintext(binaer)

#print(binaer)
