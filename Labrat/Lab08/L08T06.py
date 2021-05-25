#Tee ohjelma joka näyttää onko annettu vuosi karkausvuosi. 
#Vuosiluku kysytään käyttäjältä.
#Algoritmi: 4:llä jaolliset on, paitsi täydet vuosisadat. 
#Kuitenkin 400:lla jaolliset vuosisadat ovat karkausvuosia.
#Esim. 1991 -> ei, 1992 -> on, 1900 -> ei, 2000 -> on

vuosi = int(input("Anna vuosiluku: "))

if ((vuosi % 4) == 0):
    if ((vuosi % 100) == 0):
        if ((vuosi % 400) == 0):
            print("{0} on karkausvuosi".format(vuosi))
        else:
            print("{0} ei ole karkausvuosi".format(vuosi))
    else:
        print("{0} on karkausvuosi".format(vuosi))
else:
    print("{0} ei ole karkausvuosi".format(vuosi))