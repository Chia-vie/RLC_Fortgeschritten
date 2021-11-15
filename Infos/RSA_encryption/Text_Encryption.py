def encrypt(message, e, n):
    return ((message ** e) % n)


def decrypt(message, d, n):
    return ((message ** d) % n)

def text_to_num():
    pass

text = ord('1')

enc = encrypt(text, 7, 91687)

print(chr(decrypt(enc, 26023, 91687)))


#public_keys:{'e': 5, 'n': 822649}
#private_keys:{'d': 656669, 'n': 822649}

#public_keys:{'e': 7, 'n': 91687}
#private_keys:{'d': 26023, 'n': 91687}