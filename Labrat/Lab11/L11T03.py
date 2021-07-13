# Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen. 
# Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja näyttää ne yhtenä rivinä pilkulla erotettuna.

nimet = list()

print('Ohjelma kysyy oppilaiden nimiä kunnes annat tyhjän vastauksen.')

while True:
    nimi = str(input('Anna oppilaan nimi: '))
    if nimi == '':
        break
    else:
        nimet.append(nimi)
print('Annoit',len(nimet),'nimeä:')
print(*nimet, sep = ", ")