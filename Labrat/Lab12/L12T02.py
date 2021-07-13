# Tee luokka Cat. Tee luokalla on kaksi ominaisuutta name ja color, sekä yksi metodi miau. 
# Luo Cat-luokasta vähintään kaksi erilaista kissa-oliota.
# Näytä kissa-olioiden ominaisuudet konsolille, laita kissat myös naukumaan.

class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __repr__(self):
        return 'Name: % s Color: % s' % (self.name, self.color)
    def miau(self):
        print(self.name,'naukuu!')

cat1 = Cat('Pilkku','Valkoinen')
cat2 = Cat('Piki',"Musta")

print(cat1)
print(cat2)
cat1.miau()
cat2.miau()