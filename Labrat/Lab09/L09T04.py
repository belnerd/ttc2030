# Tee ohjelma, joka kysyy käyttäjältä käyttäjän etu ja sukunimen. 
# Tulosta käyttäjän etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia. 
# Tämän jälkeen tulosta käyttäjän sukunimi käänteisessä järjestyksessä. 
# Siis esimerkiksi jos käyttäjä antaa etunimekseen 'Kirsi' ja sukunimeksi 'Kernell' tuloste olisi:
# 'KKKKK'
# 'llenreK'

etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")
x = etunimi[0]
i = 0

while i < len(etunimi):
    print(x, end = '')
    i += 1

print("\r")

i = len(sukunimi)-1
while i >= 0:
    print(sukunimi[i], end = '')
    i -= 1

