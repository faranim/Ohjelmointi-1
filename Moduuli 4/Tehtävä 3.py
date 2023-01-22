numero = []
while True:
    annettu_numero = input("Anna luku tai lopeta syöttämällä tyhjä merkkijono:")
    if numero == "":
        break
    else:
        try:
            numero.append(int(annettu_numero))
        except ValueError:
            print("Virheellinen syöte. Syötä numero")

if numero:
    print("Pieni luku: ", min(numero))
    print("Suurin luku: ", max(numero))
else:
    print("Et syöttänyt lukua")