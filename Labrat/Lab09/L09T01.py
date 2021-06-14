# Tee ohjelma, joka kysyy käyttäjältä viikon kunkin päivän sademäärän.
# Sademäärä annetaan kokonaislukuna, jollei kyseisenä päivänä ole satanut
# käyttäjä antaa luvuksi 0. Laske ja näytä viikon kokonaissademäärä.

viikonpaivat = ["maanantain", "tiistain", "keskiviikon", "torstain", "perjantain", "lauantain", "sunnuntain"]
sademaara = [0,0,0,0,0,0,0]
yhteismaara = 0
i = 0

print("Anna sademäärät millimetreinä (0 jos ei satanut)")
for x in viikonpaivat:
    sademaara[i] = int(input("Anna " + viikonpaivat[i] + " sademäärä: "))
    yhteismaara = yhteismaara + sademaara[i]
    i = i + 1
print("Koko viikon sademäärä on",yhteismaara)