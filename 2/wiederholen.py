import random
anzahlen = [0,0,0,0,0,0]
repeat 100000:
    zahl = random.randint(1,6)
    anzahlen[zahl-1] = anzahlen[zahl-1] + 1
for z in range(6):
    print(z+1,":",anzahlen[z])    