# Tee ohjelma, joka kysyy käyttäjältä ensin muutetaanko fahrenheitit celsiuksiksi
# vai celsius-asteet fahrenheitiksi. Tämän jälkeen kysytään käyttäjältä asteet ja 
# muutetetaan ne toisiin asteisiin ja näytetään tulos käyttäjälle.

print('Valitse muunnos (1 tai 2):')
print('[1] fahrenheitit celsiuksiksi')
print('[2] celsius-asteet fahrenheitiksi')
valinta = int(input('Valintasi: '))

if valinta == 1:
    asteet = float(input('Anna fahrenheitit: '))
    print(asteet,'fahrenheitia on',((asteet-32)*0.5556),'celcius-astetta.')
elif valinta == 2:
    asteet = float(input('Anna celcius-asteet: '))
    print(asteet,'celcius-astetta on',(asteet*1.8+32),'fahrenheitia.')
else:
    print('Virheellinen valinta!')
