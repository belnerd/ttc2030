luvut = [0,0,0,0,0]
i = summa = 0
for x in luvut:
    luvut[i] = int(input("Anna luku:"))
    if (luvut[i] <= 0): luvut[i] = 0
    summa = (summa + luvut[i])
    i = i + 1
print("1 tai suurempien lukujen summa on", summa)

    