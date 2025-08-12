from gturtle import *
from random import randint

makeTurtle()
hideTurtle()
setPenColor("black")
repeat 1000:
    x = randint(-400,400)
    y = randint(-300,300)
    setPos(x,y)
    dot(3)