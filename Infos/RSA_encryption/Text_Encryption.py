def encrypt(message, e, n):
    return ((message ** e) % n)


def decrypt(message, d, n):
    return ((message ** d) % n)

text = ord('a')

enc = encrypt(text, 5, 1279151)

print(f'Das ist deine Originaltext : {chr(decrypt(enc, 510749, 1279151))}')


#public_keys:{'e': 5, 'n': 822649}
#private_keys:{'d': 656669, 'n': 822649}

#public_keys:{'e': 7, 'n': 91687}
#private_keys:{'d': 26023, 'n': 91687}

#public_keys:{'e': 5, 'n': 1279151}
#private_keys:{'d': 510749, 'n': 1279151}