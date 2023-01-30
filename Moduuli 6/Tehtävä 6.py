import math
def pizza_hinta(halkaisija, hinta):
    säde = halkaisija
    pinta_ala = math.pi * säde ** 2
    hinta_per = hinta/pinta_ala
    return hinta_per
halkaisija1 = float(input("Anna ensimmäisen pizzaan halkaisija cm:"))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina:"))
hina_per1 = pizza_hinta(halkaisija1, hinta1)

halaisija2 = float(input("Anna toisen pizzan halkaisija cm: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))
hinta_per2 = pizza_hinta(halaisija2, hinta2)

if hina_per1 < hinta_per2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
else:
    print("Toinen pizza antaa paremman vastineen rahalle")