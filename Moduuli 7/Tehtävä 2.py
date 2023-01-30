nimet = []
while True:
    nimi = input("Syötä nimi tai tyhjä merkkijono lopetukseksi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.append(nimi)
print(nimet)
for nimi in nimet:
    print(nimi)