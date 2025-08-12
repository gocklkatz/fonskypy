from gturtle import *
from random import randint

farben = ["indigo","black","blue","red","yellow","green","brown","pink","purple","orange","gray"]
makeTurtle()
hideTurtle()
repeat 3000:
    setPenColor(getRandomX11Color())
    setRandomPos(800, 600)
    dot(20)