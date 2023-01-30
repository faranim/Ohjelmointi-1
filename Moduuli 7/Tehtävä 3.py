lentoasemat = []
while True:
    print("1. Syötä uusi lentokenttä")
    print("2. Katso lentokentän tiedot")
    print("3. Päätä toiminto")
    valinta = input("Mitä haluaisit tehdä? ")

    if valinta == "1":
        icao = input("Syötä ICAO koodi: ")
        nimi = input("Syötä lentokentän nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "2":
        icao = input("Syötä ICAO koodi: ")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Näillä tiedoilla ei löydy tietoa. ")
    elif valinta == "3":
        break
    else:
        print("Virheellinen valinta")