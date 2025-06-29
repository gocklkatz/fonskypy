import random
zufalszahl=random.randint(1,100)
ratezahl=0
zaehler=0
while ratezahl != zufalszahl:
    ratezahl=input("Rate die Zahl:")
    zaehler=zaehler+1
    if ratezahl>zufalszahl:
        print(ratezahl,"ist zu groß.")
    elif ratezahl<zufalszahl:
        print(ratezahl,"ist zu klein.")
print("Glückwunsch,",zufalszahl,"ist die richtige Zahl!")
print("Du hast",zaehler,"versuche gebraucht!")            