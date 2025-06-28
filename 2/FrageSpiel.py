import random
frage=input("Was wilst du wissen:")
antwort=random.randint(1,6)
print("Die Antwort lautet:")
if antwort==1:
    print("ja!")
elif antwort==2:
    print("nein!")
elif antwort==3:
    print("vileicht!")
elif antwort==4:
    print("alles")
elif antwort==5:
    print("weiss ich nicht!")
elif antwort==6:
    print("was meinst du?")                            