class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0


audi = Auto("ABC-123", 142)

print(f'Auton rekisteritunnus: {audi.rekisteritunnus}')
print(f'Auton huppunopeus: {audi.huippunopeus}')
print(f'Auton nopeus: {audi.nopeus}')
print(f'Auton kuljettu_matka: {audi.kuljettu_matka} ')