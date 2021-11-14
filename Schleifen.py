while True:
    antwort = input('Gib eine Zahl ein!\n')
    if antwort == 'nein':
        break# / sys.exit  #für letzteres sys importieren

print('Die SChleife wurde beendet.')

zahl = 0

while zahl <= 10: ######bei while schleifen immer ein ende einbauen, sonst kann der Computer abstürzen! Be careful!
    print(zahl)
    zahl+=1  # neue zahl ist sie selbst plus# 1.



zahl = 0
while zahl <= 10:
    if zahl % 2 == 0: #wenn die zahl gerade ist
        zahl +=1
        continue
    print(zahl)
    zahl+=1

for i in range (0,10,2):  #alle zahlen größer 0, kleiner 10, und gerade(in 2er schritten)
    print(var)

for i in range(15)
    print(i)
    if i == 10:
        break#


for i in range(100):
    if i % 5 == 0:
        continue
    print(i)
