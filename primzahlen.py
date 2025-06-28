x = 2
repeat 999:
    teiler = 2
    primzahl = True
    maximum = x ** 0.5
    while (teiler <= maximum)and(primzahl):
        if (x % teiler) == 0:
            primzahl = False
        else:
            teiler = teiler +1
    if primzahl:
        print(x)
    x = x + 1                