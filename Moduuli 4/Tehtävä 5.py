yrityskerrat = 0
while yrityskerrat < 5:
    oikeat = input("Syötä käyttäjätunnus:")
    oikeas = input("Syötä salasana:")
    if oikeat == "nimo" and oikeas == "Rules!":
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjä tunnus tai salasana")
        yrityskerrat += 1
if yrityskerrat ==5:
    print("Pääsy evätty")