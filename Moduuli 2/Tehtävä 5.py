Leiviskä = float(input("Anna leiviskät."))
Naulat = float(input("Anna naulat."))
Luoti = float(input("Anna luodit."))
Leiviskät= float(Leiviskä)*Leiviskä
Naula= float(Naulat)*Naulat
Luoti= float(Luoti)*Luoti
Yhteensä = Leiviskä + Naulat + Luoti
Kilo = Yhteensä / 1000
Gramma  = Kilo - int(Kilo)
Gramma = Gramma * 1000
Gramma = round(Gramma, 2)
print("Massa nykymittoijen mukaan")