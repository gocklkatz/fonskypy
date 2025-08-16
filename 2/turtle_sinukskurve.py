from gturtle import *
from math import sin

makeTurtle()
hideTurtle()
setPenColor("pink")

setPos(-400,0)
moveTo(400,0)
setPos(0,-300)
moveTo(0,300)

speed(10044)
setLineWidth(6)
breite = 50
hoehe = 200
setPos(-400,sin(-400/breite)*hoehe)
for x in range(-400,401):
    moveTo(x,sin(x/breite)*hoehe)