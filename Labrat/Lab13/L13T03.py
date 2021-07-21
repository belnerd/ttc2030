carsObj = {
    "Volvo" : "RPG-768",
    "Ford" : "SEF-423",
    "Opel" : "SMH-739",
    "Skoda" : "LEF-457",
    "Renault" : "EVF-654",
    "BWM" : "NIK-475",
    "Audi" : "HJK-534",
    "Citroen" : "XKA-994",
    "Kia" : "UHV-494",
    "Hyundai" : "YIP-666"
}

brandSorted = sorted(carsObj.items(),key=lambda x: x[0])
regSorted = sorted(carsObj.items(),key=lambda x: x[1])

for brand,reg in brandSorted:
    print(brand,reg)

for brand,reg in regSorted:
    print(reg,brand)
