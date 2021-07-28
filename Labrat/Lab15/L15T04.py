# Tee ohjelma joka kysyy käyttäjältä lukuja (joko kokonaisluku tai liukuluku) ja tallenna kokonaisluvut eri tiedostoon kuin liukuluvut.
# Sovellus tulee lopettaa jos käyttäjä ei syötä kokonais- tai liukulukua.
# Tarkista tiedostojen sisältö tekstieditorilla.

intFile = 'integers.txt'
floatFile = 'floats.txt'
integers = list()
floats = list()

def writeFile(filename,data):
    try:
        file = open(filename,'w')
        file.writelines(str(data))
    except Exception as e:
        print('Failed to write file:' + filename)
        print(e)
    finally:
        file.close()

while True:
    try:
        x=eval(input("Anna luku: "))
        if (type(x) is int):
            integers.append(x)
        elif (type(x) is float):
            floats.append(x)
    except Exception:
        break

writeFile(intFile,integers)
writeFile(floatFile,floats)
