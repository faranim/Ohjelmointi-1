sukupuoli = input("Ilmoita sukupuoli")
hemoglobiini = float(input(("Ilmoita hemogolbiini")))
if sukupuoli.lower() == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")
if sukupuoli.lower() == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")