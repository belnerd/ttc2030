# Tee ohjelma, joka kysyy ensin käyttäjältä jonkin luvun väliltä 1-10.
# Tämän jälkeen näytä luvut yhdestä annettuun lukuun ja luvun neliön. 
# Esimerkiksi jos käyttäjä antaa luvun 4, niin tuloste olisi seuraavanlainen:
# luvun 1 neliö on 1
# luvun 2 neliö on 4
# luvun 3 neliö on 9
# luvun 4 neliö on 16

i = 1
luku = int(input("Anna kokonaisluku 1-10 väliltä: "))

if luku <= 10:
    while i <= luku:
        x = i ** 2
        print("luvun " + str(i) + " neliö on " + str(x))
        i += 1
else:
    print("Virheellinen syöte!")



