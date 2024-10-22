import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = max(0, min(self.huippunopeus, self.nopeus + muutos))

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<12}{'Huippunopeus':<15}{'Nopeus':<8}{'Matka':<8}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12}{auto.huippunopeus:<15}{auto.nopeus:<8}{auto.matka:<8.1f}")

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)

autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()