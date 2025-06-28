import random
summe=0
weiter="j"
wuerfel=6
while(weiter=="j")and(wuerfel>1):
    wuerfel=random.randint(1,6)
    if wuerfel>1:
        summe=summe+wuerfel
    else:
        summe=0
    print("Du hast eine",wuerfel,"gewürfelt.")
    print("Deine Punktzahl ist",summe)
    if wuerfel>1:
        weiter=input("Weiterspielen? j/n")