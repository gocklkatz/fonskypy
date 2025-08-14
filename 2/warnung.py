def warnung():
    msgDlg("Achtung hier ist ein falscher Wert eingegeben worden. ")
    
    
x = input("Bitte Zahl unter 10 eingeben")
if x<10:
    print("Danke.")
else:
    warnung()