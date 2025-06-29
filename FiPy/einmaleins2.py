import random

punkte = 0
fehler = 0
eingabe = 0

while (eingabe != "x"):
    zahl1 = random.randint(3,9)
    zahl2 = random.randint(3,9)
    loesung = zahl1*zahl2
    print(zahl1,"x",zahl2,"=")
    eingabe = input("Wie lautet die Lösung?")
    if eingabe != "x":
        if eingabe == loesung:
            print("Richtig!",zahl1,"x",zahl2,"=",loesung)
            punkte = punkte + 1
        else:
            print("Leider falsch!",zahl1,"x",zahl2,"=",loesung)
            fehler = fehler + 1
print("Ok.",punkte,"Punkte und",fehler,"Fehler.")