# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 10:13:00 2025

@author: admin
"""
import random as r 

f1 = "Was ist die Hauptstadt von Tschechien"
f2 = "Was ist irrelevant"
f3 = "Was ist relevant"
f4 = "Wann gibts Jause"
f5 = "Wer ist der beste Lehrer"
b = 1

fragen = [f1, f2, f3, f4, f5, b]

p = 0

while True:
    #print("Du schlägst dich gut")
    print(r.choice(fragen))
    a = input("Deine antwort: ")
    if f1 == "Was ist die Hauptstadt von Tschechien" and a == "Prag":
        print("So was weißt du")
        p += 1 
        fragen.remove(f1)
    elif f2 == "Was ist irrelevant" and a == "unwichtig":
        print("toll gemacht")
        p +=1 
        fragen.remove(f2)
    elif f3 == "Was ist relevant" and a == "wichtig":
        print("Das ist richtig")
        p += 1 
        fragen.remove(f3)
    elif f4 == "Wann gibts Jause" and a == "wenn es halt Jause gibt":
        print("Tzzzzz")
        p += 1 
        fragen.remove(f4)
    elif f5 == "Wer ist der beste Lehrer" and a == "Helene":
        print("Natürlich ist sie das")
        p += 2 
        fragen.remove(f5)
    else:
        print("loser")
        print("Deine Punkte: ", p)
        break
    if len(fragen) == 1:
        print("Das Spiel ist vorbei")
        print("Deine Punkte: ", p)