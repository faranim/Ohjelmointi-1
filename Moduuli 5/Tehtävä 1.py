import random
arpakuutio = int(input("Anna arpakuutioiden lukumäärä:"))
määrä = 0
for i in range(arpakuutio):
    dice_throw = random.randint (1,6)
    määrä += dice_throw
    print("Arpakuution", i+1, "heitto:", dice_throw)
print("Silmälukujen summa:", määrä)