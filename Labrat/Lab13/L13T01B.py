deck = list()
counter = 1
counter2 = 1

for counter in range(1,5):
    if (counter == 1): suit = '♦'
    elif (counter == 2): suit = '♣'
    elif (counter == 3): suit = '♥'
    elif (counter == 4): suit = '♠'
    for counter2 in range(1,14):
        deck.append(str(suit)+str(counter2))

counter = 0
for x in deck:
    counter = counter + 1
    print(x,' ',end='')
    if (counter==13): 
        print("\n")
        counter = 0
