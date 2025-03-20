class Auto:
    def __init__(self, rekisteritunnus, huippunopeus = 200):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto1 = Auto("ABC-123", 142)
print(f"Auton rekisteritunnus on {auto1.rekisteritunnus} ja huippunopeus {auto1.huippunopeus} km/h. "
      f"Tämän hetkinen nopeus on {auto1.nopeus} ja autolla ajettu matka on {auto1.matka}.")