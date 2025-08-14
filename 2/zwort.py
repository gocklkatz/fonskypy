def zahlwort(zahl):
    
    einer = ["null", "ein", "zwei", "drei", "vier", u"fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", u"zwölf", "dreizehn", "vierzehn", u"fünfzehn", "sechzehn", "siebzehn", "achzehn", "neunzehn"]
    zehner = ["null", "zehn", "zwanzig", u"dreißig", "vierzig", u"fünfzig", "sechzig", "siebzig", "achzig", "neunzig", "hundert"]
    
    if zahl < 20:
        wort = einer[zahl]
        if zahl == 1:
            wort = "eins"
    else:
        z = zahl // 10
        e = zahl % 10
        
        wort = einer[e]+"und"+zehner[z]
        if e == 0:
            wort = zehner[z]
    return wort

x = input("Zahl:")
msgDlg(str(x)+" ist in Worten: "+zahlwort(x))                            