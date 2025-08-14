from gturtle import *
from random import randint

def vieleck(ecken,laenge):
    winkel = 360/ecken
    repeat ecken:
        forward(laenge)
        right(winkel)
        
        
makeTurtle()
hideTurtle()
penWidth(3)

repeat 100:
    setPenColor(getRandomX11Color()) # Zufallsfarbe setzen
    setRandomHeading() # zufällige Startrichtung setzen
    setRandomPos(800, 600) # zufällige Startposition setzen
    laenge = randint(10,100) # zufällige Kantenlänge setzen
    ecken = randint(3,7) # zufällige Anzahl Ecken
    vieleck(ecken,laenge)        