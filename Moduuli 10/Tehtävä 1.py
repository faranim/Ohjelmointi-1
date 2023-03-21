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

hissi = Hissi(1,10)
hissi.siirry_kerrokseen(7)
hissi.siirry_kerrokseen(-10)
