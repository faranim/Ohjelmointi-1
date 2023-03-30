class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntia):
        self.matkamittari += tuntia * self.huippunopeus


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


if __name__ == '__main__':
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    sähköauto.aja(3)
    print(f"Sähköauton matkamittari: {sähköauto.matkamittari} km")

    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
    polttomoottoriauto.aja(3)
    print(f"Polttomoottoriauton matkamittari: {polttomoottoriauto.matkamittari} km")