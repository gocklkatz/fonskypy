# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 08:43:58 2025

@author: admin
"""

import random

o = random.randint(1,10)
a = int(input("Gib eine zahl zwischen 1 und 10: "))
ver = 1
erraten = False

while erraten == False:
    
    if a == o:
        print("Wir haben die gleiche zahl, ich hab:",o)
        erraten = True
        print("Du hast so viele versuche gebraucht:",ver)
        
    elif a != o and a < 10:
        print("Wir haben unterschidliche zahlen")
        a = int(input("Gib eine zahl zwischen 1 und 10: "))
    else:
        print("Das geht nicht.")
        erraten = True       
        
    ver = ver + 1
    