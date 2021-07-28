# Jatkoa edelliseen. Lajittele nimet aakkosjärjestykseen ennen tulostusta.

filename = "nimet.txt"
women = list()
men = list()
tmplist = list()
switch = True

try:
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
except:
    print('Failed to read file:'+filename)
finally:
    file.close()

for x in lines:
    tmplist.append(x)

for x in tmplist:
    if (x == '[Naiset]'):
        switch = True
    elif x == '[Miehet]':
        switch = False
    if (switch and x is not ''): women.append(x)
    if (not switch and x is not ''): men.append(x)

women.remove('[Naiset]')
women.sort()
men.remove('[Miehet]')
men.sort()
cWomen = list()
cMen = list()

for x in women:
    tmp = x + ' : ' + str(women.count(x))
    cWomen.append(tmp)
cWomen = list(dict.fromkeys(cWomen))
for x in men:
    tmp = x + ' : ' + str(men.count(x))
    cMen.append(tmp)
cMen = list(dict.fromkeys(cMen))

print('Naisten nimiä yhteensä:',len(women))
for x in cWomen:
    print(x)
print()
print('Miesten nimiä yhteensä:',len(men))
for x in cMen:
    print(x)