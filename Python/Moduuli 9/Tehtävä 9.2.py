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

auto1 = Auto("ABC-123", 142)