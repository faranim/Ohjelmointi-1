class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeus_muutos):
        if self.nopeus + nopeus_muutos >= 0 and self.nopeus + nopeus_muutos <= self.huippunopeus:
            self.nopeus = self.nopeus + nopeus_muutos

        elif self.nopeus + nopeus_muutos < 0:
            self.nopeus  = 0

    def kulje(self,tunti):
        self.kuljettu_matka += self.nopeus * tunti

    def tieto(self):
        print(f"Rekkari on {mersu.rekisteritunnus}, huippunopeus on {mersu.huippunopeus} km/h\n"
                f"Hetkellinen nopeus on: {mersu.nopeus} km/h, kuljettumatka on: {mersu.kuljettu_matka} km/h" )


mersu= Auto("moi-123", 200)
mersu.kiihdytä(60)
mersu.kulje(1)
mersu.tieto()

mersu.kiihdytä(50)
mersu.kulje(2)
mersu.tieto()