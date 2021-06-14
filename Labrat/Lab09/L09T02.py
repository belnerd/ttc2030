# Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja. 
# Lukuja kysytään siihen saakka kunnes käyttäjä antaa tyhjän syötteen. 
# Laske kuinka monta lukua käyttäjä antoi, laske myös annettujen lukujen summa. 
# Näytä annettujen lukujen lukumäärä ja summa käyttäjälle.

luku = 0
summa = 0
laskuri = 0

print("Anna kokonaislukuja, lasken niiden summan ja lukumäärän.")
print("Kun et enää halua antaa lukuja paina <ENTER> tyhjään kenttään.")

while True:
    luku = input("Anna kokonaisluku: ")
    if luku:
        summa = summa + int(luku)
        laskuri = laskuri + 1
    else:
        break
        
print("Syötit " + str(laskuri) + " lukua. Lukujen summa on " + str(summa) + ".")