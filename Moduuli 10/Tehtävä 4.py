import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, kokonaismatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kokonaismatka = kokonaismatka

    def kiihdytä(self, nopeus_muutos):
        if self.nopeus + nopeus_muutos >= 0 and self.nopeus + nopeus_muutos <= self.huippunopeus:
            self.nopeus = self.nopeus + nopeus_muutos

        elif self.nopeus + nopeus_muutos < 0:
            self.nopeus  = 0

        elif self.nopeus + nopeus_muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def matka_aika(self,tunti):
        self.kokonaismatka = self.kokonaismatka + (self.nopeus * tunti)

class kilpailu:

    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista


    def tunti(self):
        for i in self.autolista:
            i.kiihdytä(random.randint(-10,15))
            i.matka_aika(1)

    def lista(self):
        for x in self.autolista:
            print(f"{x.rekisteritunnus}", f"{x.huippunopeus}km/h", f"{x.nopeus}km/h", f"{x.kokonaismatka}km/h")

    def loput(self):
        for x in self.autolista:
            if x.kokonaismatka >= self.pituus:
                return True

autot = []
for i in range(10):
    autot.append(Auto(f"ABC{i+1}", random.randint(100, 200), 0, 0))

ajo = kilpailu("Suurin romuralli", 800, autot)

eka_kierros = 1
stop = False
while not stop:
    ajo.tunti()
    stop = ajo.loput()
    if eka_kierros% 10 == 0:
        ajo.lista()
        print(f"Kierros {eka_kierros}")
    eka_kierros+= 1

ajo.lista()