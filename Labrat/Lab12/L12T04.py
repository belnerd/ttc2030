# Tee seuraava lisäys edelliseen tehtävään. Luo satunnaisesti vähintään viisi erilaista auto-oliota
# seuraavista automerkeistä (brand) 'Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo' ja 'VW'. Autojen
# model ominaisuuden voit jättää halutessasi tyhjäksi. Generoi satunnaisesti niille hinta väliltä 1000-10000.
# Lisää ne sopivaan kokoelmaan, siis esim listaan tai dictionaryyn tms.

# Tulosta kaikkien auton ominaisuudet konsolille.
# Laske myös autojen yhteishinta, ja näytä se konsolilla.

import random

audiModel = ['A3','A4','A6','A7']
bmwModel = ['1 Series','2 Series','3 Series','4 Series','5 Series']
fordModel = ['Focus','Mondeo','Puma','Mach-E','Explorer']
skodaModel = ['Fabia','Octavia','Superb','Kodiaq']
volvoModel = ['V40','V50','V90','XC60','XC90']
vwModel = ['Golf','Polo','Variant','Transporter','Passat']

class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    
def createRandomCar():
    i = random.randint(0,5)
    if i == 0: #Audi
        x = random.randint(0,len(audiModel)-1)
        brand = 'Audi'
        model = audiModel[x]
        price = random.randint(1000,10000)
        return Car(brand,model,price)
    elif i == 1: #BMW
        x = random.randint(0,len(bmwModel)-1)
        brand = 'BWM'
        model = bmwModel[x]
        price = random.randint(1000,10000)
        return Car(brand,model,price)
    elif i == 2: #Ford
        x = random.randint(0,len(fordModel)-1)
        brand = 'Ford'
        model = fordModel[x]
        price = random.randint(1000,10000)
        return Car(brand,model,price)   
    elif i == 3: #Skoda
        x = random.randint(0,len(skodaModel)-1)
        brand = 'Skoda'
        model = skodaModel[x]
        price = random.randint(1000,10000)
        return Car(brand,model,price)
    elif i == 4: #Volvo
        x = random.randint(0,len(volvoModel)-1)
        brand = 'Volvo'
        model = volvoModel[x]
        price = random.randint(1000,10000)
        return Car(brand,model,price)
    elif i == 5: #Volkswagen
        x = random.randint(0,len(vwModel)-1)
        brand = 'Volkswagen'
        model = vwModel[x]
        price = random.randint(1000,10000)
        return Car(brand,model,price)
    else:
        print('Error: Illegal random value.')

cars = list()
counter = 0
summa = 0

for counter in range(5):
    cars.append(createRandomCar())
    summa += cars[counter].price
    print(cars[counter].brand,cars[counter].model,cars[counter].price)

print('Hintojen summa:',summa)