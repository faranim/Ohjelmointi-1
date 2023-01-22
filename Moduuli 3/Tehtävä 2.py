hytti_luokka = input("Valitse laivan hytti luokka (LUX, A, B, C)")
if hytti_luokka == "lux":
    print("LUX on hytti, jossa on parveke yläkannella")
elif hytti_luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hytti_luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif hytti_luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")

