# Tee ohjelma, joka arpoo lottorivin ja tallentaa ne tekstitiedostoon 'lotto.txt'.
# Arvottu rivi sisältää seitsemän (7) numeroa väliltä 1-40. Varmista arpoessasi riviä että sama numero ei voi esiintyä kahta kertaa.

import random

def writeFile(filename,data):
    try:
        file = open(filename,'w')
        file.writelines(str(data))
        print('Wrote in file:',filename)
    except Exception as e:
        print('Failed to write file:' + filename)
        print(e)
    finally:
        file.close()

lottofile = 'lotto.txt'
lottorivi = list()

while (len(lottorivi) < 7):
    x = random.randint(1,40)
    if x not in lottorivi:
        lottorivi.append(x)

lottorivi.sort()
writeFile(lottofile,lottorivi)

