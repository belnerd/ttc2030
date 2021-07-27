# Tee kokoelma, jossa on 5 merkkijonoa.
# Kysy käyttäjältä indeksi mihin kohtaan taulukkoa käyttäjä haluaa syöttää uuden tekstin.
# Kysy käyttäjältä uusi teksti ja laita se taulukkoon käyttäjän antamaan indeksiin.
# Tulosta taulukon sisältö.
# Korjaa ohjelma niin ettei se kaadu, jos käyttäjä syöttää indeksin, joka on taulukon ulkopuolella.
# Kerro käyttäjälle mikäli indeksi ei ole kelvollinen ja pyydä syöttämään se uudestaan.

sanat = ['Eka','Toka','Kolkki','Nelkku','Vitska']

def newText():
    i = int(input('Anna uudelle tekstille indeksi:'))
    sanat[i] = str(input('Anna uusi teksti:'))

try:
    newText()
except IndexError:
    print('Virhe: Indeksi taulukon ulkopuolella.')
    newText()
except ValueError:
    print('Virhe: Virheellinen syöte.')
    newText()
except:
    print('Something\'s funny')
    exit()

for x in sanat:
    print(x)
