import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus = 200):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        if nopeuden_muutos + self.nopeus < 0:
            self.nopeus = 0
        elif nopeuden_muutos + self.nopeus > 200:
            self.nopeus = 200
        else:
            self.nopeus += nopeuden_muutos


    def kulje(self, tunti):
        self.matka += tunti * self.nopeus

autot = []
for i in range(10):
    auto = Auto(f"ABC-{i + 1}")
    auto.nopeus = random.randint(100, 200)
    autot.append(auto)

while auto.matka <= 10000:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.matka > 10000:
            print(f"Auto {auto.rekisteritunnus} voitti.\n")
            break

for auto in autot:
    print(f"Auto {auto.rekisteritunnus} tiedot.\n"
          f"Auton nopeus on: {auto.nopeus} km/h.\n"
          f"Auton kulkema matka: {auto.matka} km.\n")