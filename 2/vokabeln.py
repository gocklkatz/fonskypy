import random
vokabeln = [["Hallo ","hello "],["Fisch ","fish "],["reptilien ","reptiles "],["Vögel ","birds "],["Heute ","today "]]
random.shuffle(vokabeln)
falsch = 0
richtig = 0
for vok in vokabeln:
    eingabe = input("Wie heist "+vok[0]+"auf English?")
    if eingabe == vok[1]:
        msgDlg ("Richtig!")
        richtig = richtig + 1
    else:
        msgDlg ("Leider Falsch!")
        falsch = falsch + 1
print("Richtige Antworten:",richtig," - falsche Antworten:",falsch)            