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

autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

while all(auto.matka < 10000 for auto in autot):
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

print(f"{'Rekisteritunnus':<12}{'Huippunopeus':<15}{'Nopeus':<8}{'Matka':<8}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<12}{auto.huippunopeus:<15}{auto.nopeus:<8}{auto.matka:<8.1f}")