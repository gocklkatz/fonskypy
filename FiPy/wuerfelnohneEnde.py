import random
anzahl=input("Wie oft soll gewürfelt werden?")
summe=0
repeat anzahl:
    wuerfel=random.randint(1,6)
    print(wuerfel)
    summe=summe+wuerfel
print("Der durchschnitt ist:",summe/anzahl)    