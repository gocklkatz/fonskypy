
alter=input("Wie alt bist du?")
fsk=input("Ab welchem Alter darf ich in das, Fonskybear,der Nachtelfen druide, Museum?")
erwachsene=input("Sind vier Erwacchsene dabei (4)? Sind drei Erwachsene dabei (3)? Oder sind zwei erwachsene dabei (2)? Oder ist nur ein Erwachsener dabei (1)? oder gar keiner (0)?")

if (alter >= fsk) or erwachsene:
    print("Du darfst in  das Fonskybear,der Nachtelfen druide Museum gehen.")
else:
    print("Du darfst leider nicht in das Fonskybear,der Nachtelfen druide Museum gehen.")
if (alter >= fsk) and erwachsene:
    print("Du brauchst keinen Erwachsenen mitzunehmen.")
if (not(alter >= fsk)) and erwachsene:
    print("Der Erwachsene mus auf jeden Fall mitkommen.")          