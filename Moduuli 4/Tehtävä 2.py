while True:
    tuuma = float(input("Anna tuumamäärä:"))
    if tuuma < 0:
        break
    cm = tuuma * 2.54
    print(tuuma, "tuuma on", cm, "senttimetriä")