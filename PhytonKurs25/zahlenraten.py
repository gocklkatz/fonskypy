# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 12:37:53 2025

@author: admin
"""



import random

print("Zahlenraten")

ver = 0
a = random.randint(1,10)
erraten = False

while erraten == False:

    eingabe = int(input("Gib eine zahl zwischen 1 und 10 ein: "))
    
    if a == eingabe:
        print("Richtig!")
        print("Deine versuche",ver)
        erraten = True
        
    elif a > eingabe:
        print("Die zahl ist größer")
    elif a < eingabe and eingabe < 10:
        print("Diese zahl ist kleiner") 
    else:
        print("DAS GEHT NICHT 1 bis 10 du Idiot!!!!!!!!")
        erraten = True
    ver = ver + 1
    