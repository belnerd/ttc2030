#Tee funktioita varten erillinen tiedosto nimeltä 'utils.py'.
#Lisää tiedostoon funktio show_info ja tulosta sen sisällä konsoliin teksti "I'm Utils.Info".
#Tee toinen Python -ohjelma 'tester.py', josta kutsut funktiota ja varmista, että tulostus näkyy konsolissa.

#Lisää utils.py tiedostoon funktio subtract, jolle viedään 2 parametria.
#subtract funktio palauttaa annettujen parametrien erotuksen.
#Kutsu subtract funktiota ja tulosta sen palauttama arvo konsoliin.

#Lisää utils.py tiedostoon funktio subtract, jolle viedään 2 parametria.
#subtract funktio palauttaa annettujen parametrien erotuksen.
#Kutsu subtract funktiota ja tulosta sen palauttama arvo konsoliin.

#Lisää utils.py tiedostoon funktio calc_consumption. Sinne viedään parametreina:
# -auton kulutus litraa/100km
# -polttoaineen hinta euroa per litra
# -kuljettu matka kilometreinä.

#calc_consumption -funktio tulostaa konsoliin kuinka monta litraa polttoainetta on kulunut matkalla, 
#sekä polttoaineeseen kuluneen rahan määrän.
#Tee tiedosto 'consumption.py', jossa käyttäjältä kysytään: kulutus, polttoaineen hinta ja kuljettu matka. 
#Sen jälkeen kutsu calc_consumption -funktiota ohjelmasta. Tarkista että funktio laskee kulutuksen ja polttoaineen hinnan oikein.

def show_info():
    print("I'm Utils.Info")

def substract(a,b):
    return a-b

def average(a,b,c):
    return (a+b+c)/3

def calc_consumption(kulutus,litrahinta,matka):
    kulutettu = round(((kulutus/100)*matka),2)
    tuhlattu = round((kulutettu * litrahinta),2)
    print("Matkalla on kulunut",kulutettu,"litraa polttoainetta.")
    print("Kulutettu polttoaine on maksanut yhteenä", tuhlattu, "euroa.")