import random
repeat 10:
    summe=0
    repeat 1000:
        wuerfel=random.randint(1,6)
        summe=summe+wuerfel
print("Der Durchschnitt ist:",summe/1000)        