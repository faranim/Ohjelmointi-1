minimi_pituus = 37
kuhan_pituus = input("Kirjoita kuhan pituus")
kuhan_pituus = int(kuhan_pituus)
if kuhan_pituus < minimi_pituus:
    print("Laske kuha takaisin järveen. Se on alimittainen" , minimi_pituus - kuhan_pituus, "cm")
else:
    print("Kuha on oikean pituinen")

