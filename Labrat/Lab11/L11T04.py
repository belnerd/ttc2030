# Mäkihypyssä käytetään viittä arvostelutuomaria. Kirjoita ohjelma, 
# joka kysyy arvostelupisteet yhdelle hypylle ja tulostaa tyylipisteiden summan siten,
# että summasta on vähennetty pois pienin ja suurin tyylipiste.

pisteet = list()

for i in range(5):
    x = float(input('Anna {}. tuomarin arvostelupisteet:'.format(i+1)))
    pisteet.append(x)
tyylipisteet = sum(pisteet)
tyylipisteet = tyylipisteet - min(pisteet) - max(pisteet)
print('Arvostelupisteiden summa',sum(pisteet))
print('Lopulliset tyylipisteet:',tyylipisteet)