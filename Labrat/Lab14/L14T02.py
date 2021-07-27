# Tee ohjelma, jolla yrität lukea Windows-koneella kaikki tiedostot kovalevyn C:n juuresta (macOS/Linux/Unix- koneilla yritä lukea käyttäjän juurihakemisto). 
# Näytä tiedostot konsolilla. Koeta sen jälkeen lisätä tiedosto 'ayho.txt' C:n juureen (macOS/Linux/Unix -koneilla käyttäjän juurihakemistoon).
# Mitä tapahtui? (PermissionError: [Errno 13] Permission denied: 'c:/ayho.txt')
# Korjaa ohjelma niin, ettei se kaadu.
# Bonuskysymys: root

import os

path = "C:/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print(entry)

try:
    print('Writing file c:/ayho.txt')
    f = open('c:/ayho.txt','x')
except PermissionError:
    print('Permission denied!')
except:
    print('Something went wrong!')
