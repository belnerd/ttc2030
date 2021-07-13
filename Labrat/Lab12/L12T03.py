# Autotallissasi on kolme autoa. Tee luokka Car. Tee luokalla on kolme ominaisuutta brand, model ja price. 
# Luo Car-luokasta vähintään kolme erilaista auto-oliota. Aseta autojen ominaisuudet seuraavasti:

# brand="Skoda" model="Octavia" price=3000
# brand="Audi" model="A4" price=4000
# brand="Volvo" model="V70" price=5000

# Tulosta kaikkien autotallin kolmen auton ominaisuudet konsolille.
# Laske myös autojen yhteishinta, ja näytä se konsolilla.

class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

skoda = Car('Skoda','Octavia',3000)
audi = Car('Audi','A4',4000)
volvo = Car('Volvo','V70',5000)

print(skoda.brand,skoda.model,skoda.price)
print(audi.brand,audi.model,audi.price)
print(volvo.brand,volvo.model,volvo.price)
print('Autojen yhteishinta:',skoda.price+audi.price+volvo.price)