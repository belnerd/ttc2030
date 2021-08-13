## Harjoitustyö ohjelmoinnin perusteet (TTC2030) -kurssille

* Tapio Ekman
* AB5123
* 13.8.2021

### Ohjelman kuvaus

Perusajatuksena on lukea tiedostoja, tulostaa ne määrätyllä nopeudella ruudulle ja haluttaessa lisätä ko. tiedostoon lokimerkintä.
Määrätyn nopeuden, mikäli asetetaan esim. 0.02, tarkoitus on antaa tulostukseen lukufiilistä.

Ohjelma listaa määrätystä kansiosta yhteensopiviksi määritellyt tiedostot, jonka jälkeen näyttää listan käyttäjälle valintarakenteena.
Käyttäjän valinnan mukaan ohjelma tulostaa ko. tiedoston ruudulle ja kysyy käyttäjältä lisätäänkö tiedostoon loki/lukumerkintä.

### Ohjelman käyttö

* Ohjelma käynnistetään komennolla "python main.py"
* Ohjelma hyväksyy komentoriviltä argumentiksi tulostusviiveeksi määritellyn liukuluvun (esim. python main.py 0.01)
* Mikäli argumenttia ei anneta on tulostus viiveetön (delay = 0)
* Valikossa valinnat suoritetaan numeroin, jotka esitetään tiedostolistauksessa
* Ohjelmasta poistutaan exit -komennolla
* Viiveisen tulostuksen voi keskeyttää painamalla CTRL+C jolloin siirrytään lokimerkintään
* Lokimerkinnän jättämisen voi skipata painamalla ENTER

Oletuksena ohjelma listaa nykyisen työhakemiston alahakemistosta /texts tiedostoja päätteellä *.txt


### Ohjelman rakenne

Jaoin ohjelman kolmeen osaan:
1. main.py
* Pääohjelma, jossa toistorakenne ohjelmalle
* Pääohjelmassa myös valikkorakenne ja lokimerkinnän kysely
* Pääohjelmassa määritellään myös ohjelman perusasetuksen muuttujina
2. outputs.py
* Moduulissa tulostustoimintoja
* Tiedoston sisällön tulostus
* Tiedostolistauksen tulostus
* Käyttöliittymän erottimen tulostus
3. fileops.py
* Moduulissa tiedostojen luku- ja kirjoitustoiminnot
* Myös tiedostolistaus toteutettu tässä moduulissa

Ohjelmassa on pyritty virheensietoon käyttämällä try/except blokkeja käsittelemään mahdolliset virhetilanteet.

#### Käytetyt kirjastot
* os - tarvitaan tiedostolistaukseen/tiedostopolkuihin
* datetime - aika- ja päivämäärätiedot lokia varten
* sys - komentoriviargumenttien luku ja tulostaminen ruudulle (print ei toimi tässä yhteydessä)
* time - viiveen lisääminen merkkien kirjoitukseen

### Oma arvio

Tein suunnitelman ja ohjelman muutamassa tunnissa, koska deadline lähestyi uhkaavasti. Käytin aikaa kokonaisuudessaan n. 5h.
Olen tyytyväinen lopputulokseen ja ohjelman toimintaan, ajan salliessa se olisi toki ollut "nätimpi".

Aika hyvin tuosta arviointilistasta saa mielestäni kohtia ruksata eli pisteitä antaisin itselleni lähes tuon 50.
