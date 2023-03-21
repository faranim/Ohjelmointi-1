from prettytable import PrettyTable
import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, kokonaismatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kokoniasmatka = kokonaismatka

    def kiihdytä(self, nopeus_muutos):
        if self.nopeus + nopeus_muutos >= 0 and self.nopeus + nopeus_muutos <= self.huippunopeus:
            self.nopeus = self.nopeus + nopeus_muutos

        elif self.nopeus + nopeus_muutos < 0:
            self.nopeus  = 0

        elif self.nopeus + nopeus_muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def matka_aika(self,tunti):
        self.kokonaismatka = self.kokonaismatka + (self.nopeus * tunti)

    def tieto(self):
        print(f"Rekkari on {mersu.rekisteritunnus}, huippunopeus on {mersu.huippunopeus} km/h\n"
                f"Hetkellinen nopeus on: {mersu.nopeus} km/h, kuljettumatka on: {mersu.kuljettu_matka} km/h" )


def teksti():
    x.field_nimet = ["Rekisterinumero", "Huippunopeus", "Hetkellinen nopeus", "Kokomatka"]
    for i in Autot:
        x.add_row([f"{i.rekisterinumero}", f"{i.huppunopeus}km/h", f"{i.nopeus} km/h" ,f"{i.kokonaismatka}km/h" ])

x= PrettyTable()
Autot = []

for i in range(10):
    Autot.append(Auto(f"moi-{i+1}", random.randint(100, 200), 0, 0))

pysähdys = False

while not pysähdys:
    for i in Autot:
        i.kiihdytä(random.randint(-10, 15))
        i.matka_aika(1)
        if i.kokonaismatka >= 10000:
            pysähdys = True
mersu= Auto("moi-123", 200)

teksti()
print(x)