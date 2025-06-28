import random
punkte = 0
fehler = 0
eingabe = 0

while (eingabe != "x"):
    zahl1 = random.randint(3,9)
    zahl2 = random.randint(3,9)
    loesung = zahl1*zahl2
    aufgabe=str(zahl1)+"x"+str(zahl2)+"="
    eingabe=input(aufgabe)
    if eingabe !="x":
        if eingabe==loesung:
            antwort="Richtig! "+aufgabe+str(loesung)
            punkte=punkte+1
        else:
            antwort="Leider falsch! "+aufgabe+str(loesung)
            fehler=fehler+1
        msgDlg(antwort)
auswertung="Ok. "+str(punkte)+" punkte und "+str(fehler)+" Fehler."                
msgDlg(auswertung)    