# Tee ohjelma, jossa yrität muuttaa listan sellaista arvoa, jota ei ole olemassa. 
# Alusta siis lista, jossa on neljä elementtiä ja sen jälkeen yritä muuttaa viidettä elementtiä. 
# Tarkista millaisen poikkeuksen saat. (IndexError: list assignment index out of range)
# Korjaa ohjelma niin ettei se kaadu.

lista = [1,2,3,4]

try:
    lista[4] = 5
except IndexError:
    print('Index of out range!')
except:
    print('Something went wrong!')
finally:
    print(lista)