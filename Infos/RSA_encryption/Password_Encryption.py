def encrypt(message, e, n):
    return ((message ** e) % n)


def decrypt(message, d, n):
    return ((message ** d) % n)

def text_to_num():
    pass

password = 'abcd'

encrypted = []
for letter in password:
    encrypted.append(encrypt(ord(letter), 5, 1279151))

decrypted = []
for num in encrypted:
    dec_num = decrypt(num, 510749, 1279151)
    letter = chr(dec_num)
    decrypted.append(letter)

print(decrypted)


#public_keys:{'e': 5, 'n': 822649}
#private_keys:{'d': 656669, 'n': 822649}

#public_keys:{'e': 7, 'n': 91687}
#private_keys:{'d': 26023, 'n': 91687}

#public_keys:{'e': 5, 'n': 1279151}
#private_keys:{'d': 510749, 'n': 1279151}