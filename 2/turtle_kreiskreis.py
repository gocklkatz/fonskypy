from gturtle import *

makeTurtle("indigo")
ecken = input("Wie viele Ecken?")
weite = 600 / ecken
speed(1000)
repeat ecken:
    forward(weite)
    right(360 / ecken)