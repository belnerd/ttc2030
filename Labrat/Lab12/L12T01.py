# Tee luokka Human. Luokalla on kaksi ominaisuutta name ja age. 
# Luo Human-luokasta kaksi olioita, joitten arvot asetat. Tulosta olioiden tiedot konsolille

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'Name:% s Age:% s ' % (self.name, self.age)

o1 = Human('Seppo',65)
o2 = Human('Kari',45)

print(o1)
print(o2)