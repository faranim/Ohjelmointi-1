class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus < 0:
            self.nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = uusi_nopeus

audi1 = Auto("ABC-123", 142)

audi1.kiihdytä(30)
audi1.kiihdytä(70)
audi1.kiihdytä(50)

print('Nopeus', audi1.nopeus)

audi1.kiihdytä(-200)

print('Nopeus', audi1.nopeus)