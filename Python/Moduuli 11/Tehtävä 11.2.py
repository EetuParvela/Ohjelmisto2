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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kwh):
        self.akkukapasiteetti_kwh = akkukapasiteetti_kwh
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko_l):
        self.bensatankin_koko_l = bensatankin_koko_l
        super().__init__(rekisteritunnus, huippunopeus)


sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.nopeus = 120
polttomoottoriauto.nopeus = 100

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(sähköauto.matka)
print(polttomoottoriauto.matka)