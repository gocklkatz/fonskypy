# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 08:33:32 2025

@author: admin
"""


import random

bn = input("Wie lautet dein Benutzername: ")
print("Hallo", bn)
w = input("Wie alt bist du : ")
print("So alt schon?")
r = input ("Gib irgendwas ein: ")
print("interisiert mich nicht.")



o1 = "Du kommst in die Zucherwelt."
o2 = "Du kommst in die 7. Hölle. Hahaha"
o3 = "Du schwimmst in einem undendlichen Ozean, in Neuseeland."
liste = [o1,o2,o3]

www = ["Oh nein du stirbst, Dahm dahm daahm","Du überlebst"]

gh = "Plötzlich fählst du in Uhnmacht."

t = input("""Du stehst in einem Raum, du siehst drei Türen
Eine Pinke
Eine Rote
Eine Blaue
Für welche entscheidest du dich?:  """)

if t.lower()=="pink":
    #a = o3
    a = random.choice(liste)    
elif t == "rot":
    a = random.choice(liste)
elif t == "blau":
    a = random.choice(liste) 
else:
    print("Diese Farbe gibt es nicht hihi! ")

print(a)

#Zuckerwelt
if a == o1:
    print("Du wirst von einem Zuckermonster angegriffen!")
    e = input("Wilst du dagegen kämpfen oder weglaufen: ")
    if e == "kämpfen":
        l = random.choice(www)
        print(l)
        
        if l == "Du hast das Monster besiegst du lebst":
            print(gh)
            out = gh
        else:
            print("Geh nach hause du IDIOT")
            out = "Gestorben"
            
    elif e == "weglaufen":
        print("Du stolperst über einen Stein, das Zuckermonster holt dich ein & frisst dich auf, Hahaha!")
        out = "Gestorben"
    
    else:
        print("Du hast keinen Bock mehr und gehst nach hause.")  
        out = "Gestorben"
        
# Hölle        
elif a == o2:
    print("Plötzlich hörst du eine Stimme, sie sagt: Dein Schicksaal ist besigelt, du wunderst dich, ein Dämon geht auf dich zu und stellt dir eine Frage: ")            

    stadt = input("Wie heißt Österreichs Hauptstadt?: ")
    #print("Deine gewählte Stadt ist: ", stadt)
    if stadt == "Wien" or stadt == "wien":
        ant = "Richtig!"
    elif stadt == "Klagenfurt" or stadt =="klagenfurt":
        ant = "Fast, Hauptstadt von Kärnten!"
    elif stadt.lower() == "graz":
        print("Das ist die Hauptstadt von der Steiermark.")
    elif stadt.lower() == "linz":
        print("Nicht ganz das ist die Hauptstadt von Oberösterreich.")
    elif stadt.lower() == "eisenstadt":
        print("Das ist die Hauptstadt von Burgenland.")
    else:
        print("GANZ FALSCH!!!")
        
    if ant == "Richtig!":
        print("Der Dämon sagt: du kannst weiter gehen.")
        s = input("Was willst du jetzt tun, aufgeben oder weiter gehen: ")
        if s == "weiter gehen":
            sds = input("Du gehst weiter, Plötzlich siehst du eine Cola vor dir liegen, möchtest du sie aufheben und trinken oder liegen lassen: ")
            
            if sds == "trinken":
                o = random.choice(www)
                print(o)
                
                if o == "Du hast das Monster besiegst du lebst":
                    print(gh)
                    out = gh
                else:
                    print("Oh nein")
                    out = "Gestorben"
                    
            else:
                print("Feigling")
                out = "Gestorben"
                
        elif s == "aufgeben":
            print("Mir doch egal dann geh eben nach hause.")
            out = "Gestorben"
            
        else:
            print("Geht nicht.")
            out = "Gestorben"
            
    else:
        print("Der Dämon killt dich Dohm dohm dohm.")
        out = "Gestorben"

#Neuseeland
elif a == o3:
    print("Ein Fisch spricht zu dir er sagt: Du must meine Zahl erraten.")
    ver = 0
    a = random.randint(1,10)
    erraten = False

    while erraten == False:
        eingabe = int(input("Gib eine zahl zwischen 1 und 10 ein: "))
        
        if a == eingabe:
            print("Richtig!")
            print("Deine versuche",ver)
            erraten = True
            print(gh)
            out = gh
        elif a > eingabe:
            print("Die zahl ist größer")
        elif a < eingabe and eingabe < 10:
            print("Diese zahl ist kleiner") 
        else:
            print("DAS GEHT NICHT 1 bis 10 du Idiot!!!!!!!!")
            out = "Gestorben"
            erraten = True
        ver = ver + 1
        
else:
    print("NÄH!!!")

if out == gh:
    print("Du wachst auf ")
    
    
print("Gratulation, du bist beim Endgebiet.")


iij = "Schatz"
print("Du bist beim",iij,"angekommen, du hast gewonnen, Gratulation!!!")
           
