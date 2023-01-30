import random
def noppa(yhteismäärä):
    return random.randint(1, yhteismäärä)
yhteismäärä = int(input("Kuinka monta tahkoa nopassa on? "))
maksimi = int(input("MIkä on on nopan maksimisilmäluku? "))
while True:
    heitto = noppa(yhteismäärä)
    print("Silmäluku:", heitto)
    if heitto == maksimi:
        break
