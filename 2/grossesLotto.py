import random
meinTipp = []
anz = input("Wie viele ziehungen möchtest du?")
gewinne= [0,0,0,0,0,0,0]
repeat 6:
    t = input("Gib eine Tippzahl ein:")
    meinTipp.append(t)
meinTipp.sort()
allezahlen = range(1,50)
repeat anz:
    ziehung = random.sample(allezahlen,6)
    ziehung.sort()
    richtige = 0
    for z in meinTipp:
        if z in ziehung:
            richtige = richtige + 1
    if richtige > 2:
        gewinne[richtige] += 1        
print("Auswertung - ",anz,"Ziehungen, Einsatz ",anz,"Euro:")
print("Drei Richtige:",gewinne[3]," Geldgewinn:",gewinne[3]*10,"Euro")
print("Vier Richtige:",gewinne[4]," Geldgewinn:",gewinne[4]*45,"Euro")
print("Fünf Richtige:",gewinne[5]," Geldgewinn:",gewinne[5]*4000,"Euro")
print("Sechs Richtige:",gewinne[6]," Geldgewinn:",gewinne[6]*800000,"Euro")                   