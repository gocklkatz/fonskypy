from gturtle import * 

makeTurtle("indigo")
setPenColor("black")
setLineWidth(1)
setPos(-100,-200)
figur = [ [100,0],[-100,0],[100,-200],[-100,-200],[-100,0],[0,150],[100,0],[100,-200] ]
for koord in figur:
    moveTo(koord[0],koord[1])
