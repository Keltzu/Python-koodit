class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto = Auto("ABC-123", 142)
print(f"Rekisteritunnus: {auto.rekisteritunnus}, Huippunopeus: {auto.huippunopeus} km/h, Nopeus: {auto.nopeus} km/h, Kuljettu matka: {auto.matka} km")