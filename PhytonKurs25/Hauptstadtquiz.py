# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 09:08:38 2025

@author: admin
"""

print("Hauptstadt Quiz")

stadt = input("Wie heißt Österreichs Hauptstadt?: ")
#print("Deine gewählte Stadt ist: ", stadt)
if stadt == "Wien" or stadt == "wien":
    print("Richtig!")
elif stadt == "Klagenfurt" or stadt =="klagenfurt":
    print("Fast, Hauptstadt von Kärnten!")
elif stadt.lower() == "graz":
    print("Das ist die Hauptstadt von der Steiermark.")
elif stadt.lower() == "linz":
    print("Nicht ganz das ist die Hauptstadt von Oberösterreich.")
elif stadt.lower() == "linz":
    print("Das ist die Hauptstadt von Burgenland.")
else:
    print("GANZ FALSCH!!!")