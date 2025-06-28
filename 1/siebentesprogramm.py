km=input("Wie lang ist die strecke in km?")
vm=input("Zu Fuß (1) oder Fahrrad (2)?")

if vm ==1:
    print("Es dauert",km/5,"Stunden.")
elif vm==2:
    print("Es dauert",km/15,"Stunden.")
else:
    print("Bitte nur 1 oder 2 eingeben!")        