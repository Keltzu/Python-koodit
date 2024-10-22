class Hissi:
    def __init__(self, alin, ylin):
        self.kerros = alin
        self.alin = alin
        self.ylin = ylin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_num, kohde):
        self.hissit[hissi_num].siirry_kerrokseen(kohde)

talo = Talo(1, 10, 3)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(0, 1)