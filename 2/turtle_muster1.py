from gturtle import *
from random import randint

makeTurtle()
hideTurtle()
setPenColor("indigo")
#repeat 10000000:
for i in range(0, 10000000):
    x = randint(-400,400)
    y = randint(-300,300)
    setPos(x,y)
    dot(1)
    if(i%1000==0):
        print(i)