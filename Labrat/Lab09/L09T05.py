# Tee ohjelma, joka arpoo lottorivin seitsemän (7) numeroa väliltä 1-40 ja näyttää sen käyttäjälle 
# muodossa '33,5,1,20,10,3,39'. Käytä lukujen arpomiseen pythonin valmista modulia random, kts lisää:
# https://www.w3schools.com/python/gloss_python_random_number.asp
# Lisätehtävä: Jos haluat niin voit tarkistaa, että samaa lukua ei arvota useampaan kertaan.

import random

i = 0
n = 0
luvut = [0,0,0,0,0,0,0]


while i < 7:
    x = random.randrange(1,41)
    currentI = i
    if x in luvut:
        i = currentI
    elif i == 6:
        print(x)
        luvut[i] = x
        i += 1
    else:
        print(x, end = ',')
        luvut[i] = x
        i += 1



