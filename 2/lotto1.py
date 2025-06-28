import random
lottotipp = []
repeat 6:
    zahl = random.randint(1,49)
    while zahl in lottotipp:
        zahl = random.randint(1,49)
    lottotipp.append(zahl)
print(lottotipp)        