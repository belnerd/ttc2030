# Kun x = 0 tulostetaan True, kun muu luku, esim. 1 tulostetaan False. 
# Kun nostetaan merkkijonolla TypeError niin tulostetaan määritetty virheilmoitus ja palautettava arvo on tyhjä/None
# Varsinainen merkkijonon aiheuttama virhehän oli ValueError

# Tutustu TypeError -poikkeukseen tässä dokumentissa:
# https://docs.python.org/3/library/exceptions.html
# Toteuta funktio isthiszero(num). Funktiolla välitetään yksi parametri. Funktio palauttaa true jos parametrin arvo on nolla. 
# Funktio palauttaa false, jos parametri on luku mutta ei nolla. Funktio nostaa TypeError-poikkeuksen, jos parametri ei ole luku. 
# Kokeile kutsua  ohjelmasta funktioita eri arvoilla. Toteuta kutsuvalla ohjelmalle try - except. Mitä havaitset? Vastaukset tehtävän alkuun kommentteina.

def isthiszero(num):
    try:
        if not type(num) is int:
            raise TypeError
        elif (num == 0):
            return True
        elif (int(num)):
            return False
    except TypeError:
        print('Only integers are allowed')

x = 'x'
re = isthiszero(x)
print(re)