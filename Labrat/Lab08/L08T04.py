pisteet = int(input("Kuinka monta pistettä sait (0-12): "))
if (pisteet <= 1): arvosana = 0
if (pisteet == 2) or (pisteet == 3): arvosana = 1
if (pisteet == 4) or (pisteet == 5): arvosana = 2
if (pisteet == 6) or (pisteet == 7): arvosana = 3
if (pisteet == 8) or (pisteet == 9): arvosana = 4
if (pisteet >= 10): arvosana = 5
print("Arvosanasi on ", arvosana)