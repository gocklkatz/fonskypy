import datetime
tage = ["Montag","Dinstag","Mitwoch","Donnerstag","Freitag","Samstag","Sonntag"]
wochentag = datetime.datetime.today().weekday()
print("Heute ist",tage[wochentag])