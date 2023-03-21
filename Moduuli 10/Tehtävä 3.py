class Hissi:

    def __init__(self,alin,ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerro_ylös(self):
        self.kerros += 1
        if self.kerros > self.ylin:
            self.kerros = self.ylin
        print(f"Hissi on kerroksessa: {self.kerros}")

    def kerros_alas(self):
        self.kerros -=1
        if self.kerros < self.alin:
            self.kerros = self.alin
        print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylin:
            kerros = self.ylin
        if kerros < self.alin:
            kerros = self.alin

        while self.kerros != kerros:
            if self.kerros < kerros:
                self.kerro_ylös()
            if self.kerros > kerros:
                self.kerros_alas()
class Talo:
    def __init__(self, alin, ylin, lkm):
        self.hissit = []
        for i in range(lkm):
            self.hissit.append(Hissi(alin, ylin))

    def liiku_hississä(self, nro, kerros):
        self.hissit[nro].siirry_kerrokseen(kerros)

    def hälytys(self):
        x = 1
        for i in self.hissit:
            print("Hissi numero", x, "liikkuuu...")
            i.kerros_alas(self.alin)
            x+= 1

    def hissi_ajo(self, numero, kerros):
        hissi = self.hissit[numero -1]
        print(f"Hissit {numero} on nyt kerroksessa {hissi.kerros}")

talo = Talo (1, 10, 3)
talo.hissi_ajo(0,3)
talo.hissi_ajo(1,2)
talo.hissi_ajo(2,10)
print("-" * 15)
print("Palohälytys!")
Talo.hälytys()