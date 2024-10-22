class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeus):
        self.nopeus = min(self.huippunopeus, max(0, nopeus))

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(150)
polttomoottoriauto.kiihdytä(120)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauto matka: {sähköauto.matka} km")
print(f"Polttomoottoriauto matka: {polttomoottoriauto.matka} km")