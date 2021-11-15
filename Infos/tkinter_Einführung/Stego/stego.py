from PIL import Image
import bitarray

def file_to_bitarray(filename):
    result = bitarray.bitarray()
    with open(filename, 'rb') as file:
        result.fromfile(file)
    return result

def bitarray_to_file(outfile, bits):
    with open(outfile, 'wb') as file:
        bits.tofile(file)

def set_last_bit(value, integer):
    bits = '{0:b}'.format(integer)
    return int(bits[0:len(bits)-1] + str(value), 2)

def get_last_bit(integer):
    bits = '{0:b}'.format(integer)
    return int(bits[len(bits)-1])

def hide(in_file, out_file):
    im = Image.open(in_file)
    bild = im.load()
    breite, hoehe = im.size
    verschluesseln = file_to_bitarray(in_file)
    k = 0
    l = len(verschluesseln)
    for y in range(hoehe):
        for x in range(breite):
            pixel = bild[x,y]
            r = set_last_bit(verschluesseln[k%l], pixel[0])
            k+=1
            g = set_last_bit(verschluesseln[k%l], pixel[1])
            k+=1
            b = set_last_bit(verschluesseln[k%l], pixel[2])
            k+=1
            bild[x,y] = (r,g,b)
    im.save(out_file)

hide('llama.jpg', 'geheim.txt', 'llama_stego.jpg')

