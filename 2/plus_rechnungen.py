import  random

f = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
w = input("Gib einen Wert ein: ")
f = random.randint(1,30)
d = (f + w)
print("Du hast ",f,"+",w,"Gerechnet und bekommst dieses Ergebnis: ")
print(d)
