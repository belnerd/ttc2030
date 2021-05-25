saldo = 10
eurot = int(input("Kuinka monta euroa lisätään saldoon: "))
sentit = int(input("Kuinka monta senttiä lisätään saldoon: "))
sentit = sentit / 100;
saldo = saldo + eurot + sentit
print("Saldo on nyt", saldo)
