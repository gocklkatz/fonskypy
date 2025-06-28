summe=input("Gib eine summe (über 21)ein:")
# a und b berechnen:
a=summe//21
b=summe %21
# Magisches Quadrat ausgeben:
print("-----------------------------------------------------------")
print(a+b,a,12*a,7*a)
print(11*a,8*a,b,2*a)
print(5*a,10*a,3*a,3*a+b)
print(4*a,2*a+b,6*a,9*a)
print("------------------------------------------------------------")