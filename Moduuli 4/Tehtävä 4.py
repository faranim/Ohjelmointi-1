import random
numero = random.randint(1, 10)
while True:
    arvaa = int(input("Arvaa luku väliltä 1-10"))
    if arvaa == numero:
        print("Oikein!")
        break
    elif arvaa < numero:
        print("Liian pieni arvaus!")
    else:
        print("Liian suuri arvaus")
