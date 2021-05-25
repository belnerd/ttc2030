luku1 = int(input("Anna 1. luku: "))
luku2 = int(input("Anna 2. luku: "))
luku3 = int(input("Anna 3. luku: "))

if (luku1 >= luku2) and (luku1 >= luku3): suurin = luku1
elif (luku2 >= luku1) and (luku2 >= luku3): suurin = luku2
else: suurin = luku3

print("Suurin luku on", suurin)