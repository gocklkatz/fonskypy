from gturtle import * 

farben = ["indigo","black","blue","red","yellow","green","brown","pink","purple","orange"]
makeTurtle("red")
setLineWidth(3)
right(45)
for f in farben:
    setPenColor(f)
    forward(40)
    dot(25)