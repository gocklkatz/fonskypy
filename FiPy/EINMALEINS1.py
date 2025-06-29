import random
zahl1=random.randint(3,9)
zahl2=random.randint(3,9)
loesung=zahl1*zahl2 
print (zahl1,"x",zahl2)
eingabe=input("Wie lautet die Lösung?")
if eingabe==loesung:
    print("Die Lösung ist richtig!")
else:
    print("Leider falsch! Richtig wäre",loesung)    