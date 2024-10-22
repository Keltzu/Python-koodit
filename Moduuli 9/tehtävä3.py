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

auto = Auto("ABC-123", 142)
auto.matka = 2000
auto.kiihdytä(60)
auto.kulje(1.5)
print(f"Kuljettu matka: {auto.matka} km")