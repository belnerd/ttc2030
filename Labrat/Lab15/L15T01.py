lastnames = list()
filename = 'lastnames.txt'

print('Kerätään sukunimiä listaan, tyhjä vastaus päättää nimien keräämisen.')
while True:
    lastname = input(str('Anna sukunimi:'))
    if lastname == "":
        break
    else:
        lastnames.append(lastname+"\n")

try:
    file = open(filename,'w')
    file.writelines(lastnames)
except Exception as e:
    print('Failed to write file:' + filename)
finally:
    file.close()

lines = list()
try:
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
except:
    print('Failed to read file:'+filename)
finally:
    file.close()

print(lines)