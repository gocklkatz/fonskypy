import random

meinTipp = []
repeat 6:
    t = input("Gib eine Tippzahl ein:")
    meinTipp.append(t)
meinTipp.sort()

zaehler = 0
allezahlen = range(1,50)
repeat 100:
    # Ziehung
    ziehung = random.sample(allezahlen, 6)
    ziehung.sort()
    
    # Auswertugn
    richtige = 0
    for z in meinTipp:
        if z in ziehung:
            richtige  = richtige + 1
    
    # Ausgabeblock   
    zaehler = zaehler + 1
    print("Runde: ", zaehler) 
    if richtige > 2:
        print(meinTipp)
        print(ziehung)
        print("Richtig getippte Zahlen:", richtige)
    else:
        print("Eins oder nix erraten!")