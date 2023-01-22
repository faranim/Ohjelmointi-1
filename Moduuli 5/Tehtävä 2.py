numerot = []
while True:
    y = input("Syötä luku tai tyhjä merkkijono lopettaaksesi:")
    if y == "":
        break
    else:
        numerot.append(int(y))
numerot.sort(reverse=True)
print("Viisi suurinta lukua:", numerot[:5])