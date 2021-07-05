#Lisää utils.py tiedostoon funktio calc_consumption. Sinne viedään parametreina:
# -auton kulutus litraa/100km
# -polttoaineen hinta euroa per litra
# -kuljettu matka kilometreinä.

#calc_consumption -funktio tulostaa konsoliin kuinka monta litraa polttoainetta on kulunut matkalla, 
#sekä polttoaineeseen kuluneen rahan määrän.
#Tee tiedosto 'consumption.py', jossa käyttäjältä kysytään: kulutus, polttoaineen hinta ja kuljettu matka. 
#Sen jälkeen kutsu calc_consumption -funktiota ohjelmasta. Tarkista että funktio laskee kulutuksen ja polttoaineen hinnan oikein.

from utils import calc_consumption

kulutus = float(input("Mikä on auton kulutus l/100 km: "))
hinta = float(input("Kuinka paljon on polttoaineen litrahinta: "))
matka = float(input("Kuinka monta kilometriä on kuljettu: "))

calc_consumption(kulutus,hinta,matka)